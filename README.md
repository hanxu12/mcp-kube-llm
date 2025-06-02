# mcp-kube-llm
This open-source project provides an interface to test natural language queries against Kubernetes MCP server using llama.cpp.

## Prerequisites

### Step 1: Install llama.cpp Server
Install and run a llama.cpp server. On macOs or Linux, you can use:

```
brew install llama.cpp
llama-server -m path/to/your/model
```

For more details, refer to: [https://github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)

### Step 2: Install Kubernetes MCP Server
Clone and build the Kubernetes-compatible MCP server:

```bash
git clone https://github.com/Flux159/mcp-server-kubernetes.git
cd mcp-server-kubernetes
bun install
```

### Step 3: Install Python Dependencies
From the project directory:

```bash
pip install -r requirements.txt
```

### Step 4: Set up Configuration
Replace `/path/to/your/mcp-server-kubernetes/dist/index.js` with the correct path to the MCP server in `server_config.json`.

### Step 5: Run the interface
Run the following command to test a user query:

```bash
python main.py
```
You will see output showing:
- The model's response without grammar constraints
- The model's response with grammar constraints
- Time taken for each query

Depending on the hardware, the sample output will look like:

```
Response without grammar:
...

Response with grammar:
...

Time taken for LLM queries:
  Without grammar:   12.24 seconds
  With grammar:      0.68 seconds
```