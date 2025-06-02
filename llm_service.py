from typing import Optional
import requests
from abc import ABC, abstractmethod

LLAMA_CPP_ENDPOINT = "http://localhost:8080/completion"
    
class LLMService(ABC):
    """Abstract base class to query LLM services."""
    
    @abstractmethod
    def query(self, prompt: str) -> Optional[str]:
        """Send a query to the service and return the generated SQL."""
        pass

    @abstractmethod
    def query_with_grammar(self, prompt: str, grammar: str) -> Optional[str]:
        """Send a query to the service with grammar and return the generated SQL."""
        pass
    
class LlamaCppService(LLMService):
    """Implementation of LLMService for Llama.cpp API."""
    def __init__(self):
        """Initialize the Llama.cpp model."""
        
    def query(self, prompt: str) -> Optional[str]:
        """Send a query to Llama.cpp server and return the response."""
        payload = {
            "prompt": prompt,
            "n_predict": 1024,
            "temperature": 0,
            "stop": ["</s>"]
        }
        try:
            response = requests.post(LLAMA_CPP_ENDPOINT, json=payload)
            if response.status_code == 200:
                result = response.json()
                return result.get("content", "").strip()
        except Exception as e:
            print(f"Error querying Llama.cpp: {e}")
            return None
            
    def query_with_grammar(self, prompt: str, grammar: str) -> Optional[str]:
        """Send a query along with query to Llama.cpp server and return the response."""
        payload = {
            "prompt": prompt,
            "n_predict": 1024,
            "temperature": 0,
            "stop": ["</s>", "</function>"],
            "grammar": grammar
        }
        try:
            response = requests.post(LLAMA_CPP_ENDPOINT, json=payload)
            if response.status_code == 200:
                result = response.json()
                return result.get("content", "").strip()
        except Exception as e:
            print(f"Error querying Llama.cpp: {e}")
            return None