# 📘 mcp-kube-llm

This open-source project provides an interface to test natural language queries against a Kubernetes MCP server using [llama.cpp](https://github.com/ggml-org/llama.cpp?tab=readme-ov-file).

## 🧾 Installation Steps Overview

| Step | Description                       | Command/Action                                                                                   | Notes                                                                                       |
|------|-----------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| 1️⃣   | Install and run `llama-server`   | `brew install llama.cpp`  <br> `llama-server -m path/to/your/model`                             | For macOS/Linux. Replace with your own model path. <br> [Docs](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) |
| 2️⃣   | Install MCP Kubernetes server     | `git clone https://github.com/Flux159/mcp-server-kubernetes.git` <br> `cd mcp-server-kubernetes` <br> `bun install` | Builds the MCP server with Kubernetes compatibility.                                        |
| 3️⃣   | Install Python dependencies      | `pip install -r requirements.txt`                                                                | Run from the root project directory.                                                        |
| 4️⃣   | Set up configuration             | Edit `server_config.json` <br> Replace `/path/to/your/mcp-server-kubernetes/dist/index.js`      | Update the path to the built MCP server entrypoint.                                         |
| 5️⃣   | Run the interface                | `python main.py`                                                                                 | Executes a sample query and shows model responses.                                          |

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
  Without grammar:   12.24 seconds
  With grammar:      0.68 seconds
```