template = """
You are a skilled assistant for applying appropriate tools to address user needs.

Tool Definitions
These are the available tools described in JSON Schema format:
<tool_definitions>
{{ TOOL DEFINITIONS IN JSON SCHEMA }}
</tool_definitions>

Instructions for Tool Use:
1. Prioritize Tools: For user queries, use tools unless the query is purely conversational or clearly unrelated to any tool's capabilities.
2. Single Tool Usage: Use only one tool in each response, even if the query implies multiple tasks.
3. Tool Call Format: Respond with tool calls in the exact XML format below, without additional text or code blocks:
<function name="tool_name">
{
  "parameter1": "value1",
  "parameter2": "value2"
}
</function>
   - Ensure parameters are in valid JSON format with strings in quotes.
   - Do not wrap the XML in code blocks or add explanations.

---

User query: {{ USER QUERY }}
Convert this query into a valid tool call using the format above.
"""

grammar = """
root ::= "<function name=" content "</function>"
content ::= ([^`\\n] | "\\n")*
"""

def print_results(response_plain: str, response_constrained: str, time_plain: float, time_constrained: float):
    print("Response without grammar:")
    print(response_plain)
    print("\nResponse with grammar:")
    print(response_constrained)
    print("\nTime taken for LLM queries:")
    print(f"  Without grammar:   {time_plain:.2f} seconds")
    print(f"  With grammar:      {time_constrained:.2f} seconds")
