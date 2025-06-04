# 📘 mcp-kube-llm

This open-source project demonstrates grammar-constrained LLM interface using [llama.cpp](https://github.com/ggml-org/llama.cpp?tab=readme-ov-file), which converts natural language queries into structured, low-latency AI outputs for a Kubernetes MCP server.

## 🧾 Installation Steps Overview

| Step | Description                       | Action                                                                                   | Notes                                                                                       |
|------|-----------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| 1️⃣   | Install and run `llama-server`   | `brew install llama.cpp`  <br> `llama-server -m path/to/your/model`                             | Replace with your own model path. <br> ([llama-server docs](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)) |
| 2️⃣   | Install MCP Kubernetes server     | `git clone https://github.com/Flux159/mcp-server-kubernetes.git` <br> `cd mcp-server-kubernetes` <br> `bun install` | Builds the Kubernetes MCP server.                                        |
| 3️⃣   | Clone Project and Install Dependencies      | `https://github.com/hanxu12/mcp-kube-llm.git` <br> `pip install -r requirements.txt`                                                                | Run from the root project directory.                                                        |
| 4️⃣   | Set up configuration             | Edit `server_config.json` <br> Replace `/path/to/your/mcp-server-kubernetes/dist/index.js`      | Update the path to the built MCP server entrypoint.                                         |
| 5️⃣   | Run the interface                | `python main.py`                                                                                 | Interactively select or enter query and check structured output.                                          |

## 📤 Example Output

Running the interface with:

```bash
python main.py
```
and selecting: `1. List all pods in the kube-system namespace`

produces output like the following:
```
Response without grammar:
...

Response with grammar:
...

Time taken for LLM queries:
  Without grammar:   5.40 seconds
  With grammar:      0.68 seconds
```