# 📘 mcp-kube-llm

This open-source project demonstrates grammar-constrained decoding using [llama.cpp](https://github.com/ggml-org/llama.cpp?tab=readme-ov-file) to convert natural language queries into structured tool calls against Kubernetes MCP server.

## 🧾 Installation Steps Overview

| Step | Description                       | Action                                                                                   | Notes                                                                                       |
|------|-----------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| 1️⃣   | Install and run `llama-server`   | `brew install llama.cpp`  <br> `llama-server -m path/to/your/model`                             | Replace with your own model path. <br> ([llama-server docs](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)) |
| 2️⃣   | Install MCP Kubernetes server     | `git clone https://github.com/Flux159/mcp-server-kubernetes.git` <br> `cd mcp-server-kubernetes` <br> `bun install` | Builds the Kubernetes MCP server.                                        |
| 3️⃣   | Clone Project and Install Dependencies      | `https://github.com/hanxu12/mcp-kube-llm.git` <br> `pip install -r requirements.txt`                                                                | Run from the root project directory.                                                        |
| 4️⃣   | Set up configuration             | Edit `server_config.json` <br> Replace `/path/to/your/mcp-server-kubernetes/dist/index.js`      | Update the path to the built MCP server entrypoint.                                         |
| 5️⃣   | Run the interface                | `python main.py`                                                                                 | Executes a sample query and see outputs.                                          |

## 📤 Example Output

When you run:

```bash
python main.py
```

You will see output similar to:
```
Response without grammar:
...

Response with grammar:
...

Time taken for LLM queries:
  Without grammar:   5.40 seconds
  With grammar:      0.68 seconds
```