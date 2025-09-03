# GPT Researcher MCP Server

An MCP (Model Context Protocol) server that exposes GPT Researcher's capabilities for conducting deep web and local document research, generating comprehensive reports with citations.

## Features

- **Web Research**: Conduct comprehensive research using web search
- **Local Document Research**: Search through local documents (PDF, TXT, CSV, Excel, Markdown, PowerPoint, Word)
- **Deep Research**: Advanced recursive research with tree-like exploration
- **Hybrid Research**: Combine web search with MCP data sources (GitHub, databases, APIs)
- **Multiple Report Types**: Research reports, resource reports, and outline reports
- **Citation Support**: All research includes proper citations and source attribution

## Installation

### Prerequisites

- Python 3.11 or later
- OpenAI API Key
- Tavily API Key (for web search)

### Setup

1. Install GPT Researcher:
```bash
pip install gpt-researcher
```

2. Set up environment variables:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export TAVILY_API_KEY="your-tavily-api-key"
```

3. Optional: For MCP integration with external data sources:
```bash
export GITHUB_TOKEN="your-github-token"
```

## Usage

### Basic Web Research

```python
# Simple research query
result = conduct_research(
    query="What are the latest trends in AI research?",
    report_type="research_report"
)
```

### Local Document Research

```python
# Research using local documents
result = research_local_documents(
    query="What are the main findings in our quarterly reports?",
    doc_path="/path/to/documents"
)
```

### Deep Research

```python
# Comprehensive recursive research
result = deep_research(
    query="Impact of climate change on agriculture",
    depth=3,
    breadth=5
)
```

### Hybrid Research with MCP

```python
# Research combining web and GitHub data
result = hybrid_research_with_mcp(
    query="Popular open source AI projects",
    mcp_configs=[{
        "name": "github",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {"GITHUB_TOKEN": "your-token"}
    }]
)
```

## Available Tools

### `conduct_research`
Main research tool that supports all research types and configurations.

**Parameters:**
- `query` (str): The research question or topic
- `report_type` (str): "research_report", "resource_report", or "outline_report"
- `report_source` (str): "web", "local", or "hybrid"
- `max_iterations` (int): Maximum research iterations (1-10)
- `doc_path` (str, optional): Path to local documents
- `retriever` (str): Retriever to use ("tavily", "mcp", "local")
- `mcp_configs` (list, optional): MCP configurations for hybrid research

### `research_local_documents`
Research using only local documents.

**Parameters:**
- `query` (str): The research question
- `doc_path` (str): Path to documents directory
- `report_type` (str): Type of report to generate

### `deep_research`
Advanced recursive research with tree-like exploration.

**Parameters:**
- `query` (str): The research question
- `depth` (int): Depth of exploration (1-5)
- `breadth` (int): Breadth of subtopics (1-10)
- `max_iterations` (int): Maximum iterations

### `hybrid_research_with_mcp`
Research combining web search with MCP data sources.

**Parameters:**
- `query` (str): The research question
- `mcp_configs` (list): MCP configurations
- `report_type` (str): Type of report

### `get_research_capabilities`
Get information about available features and configuration options.

### `validate_research_setup`
Validate installation and configuration.

## Available Resources

- `gpt-researcher://docs/installation`: Installation guide
- `gpt-researcher://docs/examples`: Usage examples
- `gpt-researcher://config/template`: Configuration template

## Available Prompts

- `research-outline`: Generate research outline for a topic
- `research-analysis`: Analyze research findings and provide insights

## Configuration

The server can be configured using the `gpt_researcher.fastmcp.json` file:

```json
{
  "mcpServers": {
    "gpt-researcher": {
      "command": "python",
      "args": ["gpt_researcher_mcp.py"],
      "env": {
        "OPENAI_API_KEY": "${OPENAI_API_KEY}",
        "TAVILY_API_KEY": "${TAVILY_API_KEY}",
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## Supported Document Formats

- PDF files
- Plain text files
- CSV files
- Excel files (.xlsx, .xls)
- Markdown files
- PowerPoint files (.pptx)
- Word documents (.docx)

## Research Types

### Research Report
Comprehensive analysis with detailed findings, insights, and conclusions.

### Resource Report
Focused on available resources, tools, and references for a topic.

### Outline Report
Structured outline of key points and subtopics for a research area.

## Deep Research Features

- **Tree-like Exploration**: Recursive research that dives deeper into subtopics
- **Concurrent Processing**: Faster results through parallel research
- **Smart Context Management**: Maintains context across research branches
- **Configurable Depth/Breadth**: Control the scope of exploration

## MCP Integration

The server supports integration with various MCP data sources:

- GitHub repositories
- Databases
- Custom APIs
- Local file systems

## Error Handling

All tools return structured responses with:
- `success`: Boolean indicating if the operation succeeded
- `query`: The original research query
- `report`: The generated report (if successful)
- `citations`: List of sources and citations
- `metadata`: Additional information about the research
- `error`: Error message (if failed)

## Examples

See `example_usage.py` for comprehensive examples of all available tools and configurations.

## Troubleshooting

### Common Issues

1. **Import Error**: Ensure GPT Researcher is installed: `pip install gpt-researcher`
2. **API Key Issues**: Verify your OpenAI and Tavily API keys are set correctly
3. **Document Path Issues**: Ensure the document path exists and contains supported files
4. **MCP Configuration**: Verify MCP server configurations are correct

### Validation

Use the `validate_research_setup` tool to check your installation and configuration.

## Contributing

This MCP server is built using FastMCP and follows the standard MCP protocol. Contributions are welcome!

## License

This project follows the same license as GPT Researcher (Apache 2.0).

## References

- [GPT Researcher Repository](https://github.com/assafelovic/gpt-researcher)
- [FastMCP Documentation](https://gofastmcp.com)
- [Model Context Protocol](https://modelcontextprotocol.io)
