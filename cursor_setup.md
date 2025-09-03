# Cursor IDE Setup for GPT Researcher MCP

## Step 1: Install Dependencies
```bash
pip install gpt-researcher
```

## Step 2: Set up Environment Variables
Create a `.env` file in your project directory:
```bash
OPENAI_API_KEY=your-openai-api-key-here
TAVILY_API_KEY=your-tavily-api-key-here
GITHUB_TOKEN=your-github-token-here
```

## Step 3: Configure Cursor MCP

1. Open Cursor IDE
2. Go to **Settings** → **Features** → **Model Context Protocol**
3. Add a new MCP server configuration:

```json
{
  "mcpServers": {
    "gpt-researcher": {
      "command": "python",
      "args": ["/full/path/to/your/gpt_researcher_mcp.py"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key-here",
        "TAVILY_API_KEY": "your-tavily-api-key-here",
        "GITHUB_TOKEN": "your-github-token-here"
      }
    }
  }
}
```

## Step 4: Restart Cursor
After saving the configuration, restart Cursor IDE.

## Step 5: Use in Cursor
You can now use the GPT Researcher tools directly in Cursor:
- Ask Cursor to research topics for your code
- Analyze documentation
- Get insights for your projects
