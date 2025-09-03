# Claude Desktop Setup for GPT Researcher MCP

## Step 1: Install GPT Researcher
```bash
pip install gpt-researcher
```

## Step 2: Set up API Keys
Create a `.env` file in your project directory:
```bash
# .env file
OPENAI_API_KEY=your-openai-api-key-here
TAVILY_API_KEY=your-tavily-api-key-here
GITHUB_TOKEN=your-github-token-here  # Optional for MCP integration
```

## Step 3: Configure Claude Desktop

### On macOS:
1. Open Claude Desktop
2. Go to **Claude** → **Settings** → **Developer**
3. Click **Open Config Folder**
4. Edit the `claude_desktop_config.json` file:

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

### On Windows:
1. Open Claude Desktop
2. Go to **File** → **Settings** → **Developer**
3. Click **Open Config Folder**
4. Edit the `claude_desktop_config.json` file with the same content as above

## Step 4: Restart Claude Desktop
After saving the configuration, restart Claude Desktop.

## Step 5: Use the Tools
Once configured, you can ask Claude to:
- "Research the latest trends in AI using the GPT Researcher tools"
- "Analyze my local documents about quarterly reports"
- "Conduct deep research on climate change impacts"

Claude will automatically use the GPT Researcher MCP tools to provide comprehensive research results.
