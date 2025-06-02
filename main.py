import argparse
import anyio
import json
from time import time

from chuk_mcp.config import load_config
from chuk_mcp.mcp_client.transport.stdio.stdio_client import stdio_client
from chuk_mcp.mcp_client.messages.initialize.send_messages import send_initialize
from chuk_mcp.mcp_client.messages.tools.send_messages import send_tools_list
from utils import template, grammar, print_results
from llm_service import LlamaCppService

llm = LlamaCppService()

async def main(config_file: str, profile: str, user_query: str):
    server_params = await load_config(config_file, profile)

    async with stdio_client(server_params) as (read_stream, write_stream):
        await send_initialize(read_stream, write_stream)
        tools_response = await send_tools_list(read_stream, write_stream)

        prompt = template \
            .replace("{{ TOOL DEFINITIONS IN JSON SCHEMA }}", json.dumps(tools_response, indent=2)) \
            .replace("{{ USER QUERY }}", user_query)
        
        # warm up 
        _ = llm.query(prompt)

        # Unconstrained query
        start_plain = time()
        response_plain = llm.query(prompt)
        end_plain = time()

        # Constrained query with grammar
        start_constrained = time()
        response_constrained = llm.query_with_grammar(prompt, grammar)
        end_constrained = time()
        
        print_results(
            response_plain,
            response_constrained,
            time_plain=end_plain - start_plain,
            time_constrained=end_constrained - start_constrained,
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run MCP tool agent.")
    parser.add_argument("--config", type=str, default="server_config.json", help="Path to server_config.json")
    parser.add_argument("--profile", type=str, default="kubernetes", help="Profile name in config")
    parser.add_argument("--query", type=str, default="List pods in kube namespace.", help="User query to test kubernetes MCPå")
    args = parser.parse_args()

    anyio.run(main, args.config, args.profile, args.query)
