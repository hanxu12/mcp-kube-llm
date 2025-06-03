import argparse
import anyio
import json
import re
from time import time

from chuk_mcp.config import load_config
from chuk_mcp.mcp_client.transport.stdio.stdio_client import stdio_client
from chuk_mcp.mcp_client.messages.initialize.send_messages import send_initialize
from chuk_mcp.mcp_client.messages.tools.send_messages import send_tools_list, send_tools_call
from utils import template, grammar, print_results
from llm_service import LlamaCppService

llm = LlamaCppService()

PREDEFINED_QUERIES = [
    "List all pods in the kube-system namespace.",
    "Get the clusterIP for the Kubernetes service.",
    "Show details of all nodes in the cluster.",
    "Is the kube-proxy pod running?",
    "What is the status of the etcd cluster?",
    "Custom query"
]

def select_user_query():
    print("Select a query to test:")
    for i, q in enumerate(PREDEFINED_QUERIES, start=1):
        print(f"{i}. {q}")
    
    choice = input("Enter choice number: ").strip()
    try:
        idx = int(choice) - 1
        if idx == len(PREDEFINED_QUERIES) - 1:
            return input("Enter your custom query: ").strip()
        return PREDEFINED_QUERIES[idx]
    except (ValueError, IndexError):
        print("Invalid choice. Falling back to default query.")
        return PREDEFINED_QUERIES[0]

def build_prompt(tools_response, user_query):
    return template \
        .replace("{{ TOOL DEFINITIONS IN JSON SCHEMA }}", json.dumps(tools_response, indent=2)) \
        .replace("{{ USER QUERY }}", user_query)

def extract_function_and_args(response: str):
    name_match = re.search(r'<function name="([^"]+)">', response)
    function_name = name_match.group(1) if name_match else None

    json_match = re.search(r'({.*})', response, re.DOTALL)
    json_str = json_match.group(1) if json_match else None
    json_obj = json.loads(json_str) if json_str else None

    return function_name, json_obj

async def main(config_file: str, profile: str):
    user_query = select_user_query()
    server_params = await load_config(config_file, profile)

    async with stdio_client(server_params) as (read_stream, write_stream):
        await send_initialize(read_stream, write_stream)
        tools_response = await send_tools_list(read_stream, write_stream)

        prompt = build_prompt(tools_response, user_query)

        # Warm-up
        _ = llm.query(prompt)

        # Unconstrained
        start_plain = time()
        response_plain = llm.query(prompt)
        end_plain = time()

        # Constrained
        start_constrained = time()
        response_constrained = llm.query_with_grammar(prompt, grammar)
        end_constrained = time()

        print_results(
            response_plain,
            response_constrained,
            time_plain=end_plain - start_plain,
            time_constrained=end_constrained - start_constrained,
        )

        function_name, arguments = extract_function_and_args(response_constrained)

        confirm = input("\nDo you want to call this tool? (y/n): ").strip().lower()
        if confirm in ["y", "yes"]:
            result = await send_tools_call(read_stream, write_stream, name=function_name, arguments=arguments)
            print("Tool call result:", result)
        else:
            print("Tool call skipped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run interactive MCP tool agent.")
    parser.add_argument("--config", type=str, default="server_config.json", help="Path to server_config.json")
    parser.add_argument("--profile", type=str, default="kubernetes", help="Profile name in config")
    parser.add_argument("--query", type=str, default="List all pods in the kube-system namespace.", help="User query to test kubernetes MCP")
    args = parser.parse_args()

    anyio.run(main, args.config, args.profile)
