# GPT Researcher MCP - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install GPT Researcher
```bash
pip install gpt-researcher
```

### Step 2: Set up API Keys
```bash
# Create a .env file
echo "OPENAI_API_KEY=your-openai-api-key-here" > .env
echo "TAVILY_API_KEY=your-tavily-api-key-here" >> .env
```

### Step 3: Test the Installation
```bash
# Run the test suite
uv run python test_gpt_researcher_mcp.py
```

### Step 4: Choose Your Integration Method

#### Option A: Claude Desktop (Recommended)
1. Open Claude Desktop
2. Go to **Claude** → **Settings** → **Developer**
3. Click **Open Config Folder**
4. Edit `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "gpt-researcher": {
      "command": "python",
      "args": ["/full/path/to/gpt_researcher_mcp.py"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key-here",
        "TAVILY_API_KEY": "your-tavily-api-key-here"
      }
    }
  }
}
```
5. Restart Claude Desktop

#### Option B: Cursor IDE
1. Open Cursor
2. Go to **Settings** → **Features** → **Model Context Protocol**
3. Add the same configuration as above
4. Restart Cursor

#### Option C: Direct Python Usage
```bash
# Run the direct usage example
uv run python direct_usage_example.py
```

#### Option D: FastMCP CLI
```bash
# Run the server directly
uv run fastmcp run gpt_researcher_mcp.py
```

### Step 5: Start Researching!

Once configured, you can ask your AI assistant to:
- "Research the latest trends in AI using GPT Researcher"
- "Analyze my local documents about [topic]"
- "Conduct deep research on [subject]"
- "Get a comprehensive report on [topic] with citations"

## 🛠️ Available Tools

- **`conduct_research`** - Main research tool
- **`research_local_documents`** - Local document analysis
- **`deep_research`** - Advanced recursive research
- **`hybrid_research_with_mcp`** - Web + external data sources
- **`get_research_capabilities`** - Feature information
- **`validate_research_setup`** - Installation check

## 📚 Resources Available

- **Installation guide** - `gpt-researcher://docs/installation`
- **Usage examples** - `gpt-researcher://docs/examples`
- **Configuration template** - `gpt-researcher://config/template`

## 🆘 Troubleshooting

### Common Issues:
1. **"GPT Researcher not installed"** - Run `pip install gpt-researcher`
2. **"API key not found"** - Check your environment variables
3. **"Tool not found"** - Restart your AI application after configuration

### Get Help:
- Check the full documentation in `README_GPT_Researcher_MCP.md`
- Run `uv run python test_gpt_researcher_mcp.py` to test your setup
- Use `validate_research_setup` tool to check configuration

## 🎯 Example Usage

Once set up, try these commands in your AI assistant:

```
"Use GPT Researcher to research the latest developments in quantum computing"
"Analyze my local documents about project requirements"
"Conduct deep research on climate change solutions"
"Get a comprehensive report on AI ethics with citations"
```

The AI will automatically use the appropriate GPT Researcher tools to provide comprehensive, cited research results!
