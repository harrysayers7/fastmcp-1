# FastMCP CLI Usage for GPT Researcher MCP

## Running the Server with FastMCP CLI

### Method 1: Direct Run
```bash
# Make sure you're in the directory with gpt_researcher_mcp.py
uv run fastmcp run gpt_researcher_mcp.py
```

### Method 2: Using the Configuration File
```bash
# Use the fastmcp.json configuration
uv run fastmcp run --config gpt_researcher.fastmcp.json
```

### Method 3: Inspect the Server
```bash
# Inspect what tools, resources, and prompts are available
uv run fastmcp inspect gpt_researcher_mcp.py
```

## Environment Setup
Make sure your environment variables are set:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export TAVILY_API_KEY="your-tavily-api-key"
export GITHUB_TOKEN="your-github-token"  # Optional
```

## Testing the Server
```bash
# Run the test suite
uv run python test_gpt_researcher_mcp.py

# Run the direct usage example
uv run python direct_usage_example.py
```

## Server Output
When you run the server, you'll see output like:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

The server will be available at `http://127.0.0.1:8000` for HTTP-based MCP clients.
