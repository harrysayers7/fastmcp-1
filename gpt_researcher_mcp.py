"""
GPT Researcher MCP Server

An MCP server that exposes GPT Researcher's capabilities for conducting
deep web and local document research, generating comprehensive reports with citations.

Based on: https://github.com/assafelovic/gpt-researcher
"""

import asyncio
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Union

from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Create the MCP server
mcp = FastMCP("GPT Researcher MCP Server")


class ResearchConfig(BaseModel):
    """Configuration for GPT Researcher"""
    query: str = Field(..., description="The research query or topic")
    report_type: Literal["research_report", "resource_report", "outline_report"] = Field(
        default="research_report", 
        description="Type of report to generate"
    )
    report_source: Literal["web", "local", "hybrid"] = Field(
        default="web",
        description="Source for research: web search, local documents, or both"
    )
    max_iterations: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Maximum number of research iterations"
    )
    doc_path: Optional[str] = Field(
        default=None,
        description="Path to local documents directory (for local/hybrid research)"
    )
    retriever: str = Field(
        default="tavily",
        description="Retriever to use: tavily, mcp, or comma-separated list"
    )
    mcp_configs: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="MCP configurations for hybrid research"
    )


class ResearchResult(BaseModel):
    """Result of a research operation"""
    query: str
    report: str
    citations: List[str]
    metadata: Dict[str, Any]
    success: bool
    error: Optional[str] = None


@mcp.tool
def conduct_research(
    query: str,
    report_type: Literal["research_report", "resource_report", "outline_report"] = "research_report",
    report_source: Literal["web", "local", "hybrid"] = "web",
    max_iterations: int = 3,
    doc_path: Optional[str] = None,
    retriever: str = "tavily",
    mcp_configs: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Conduct comprehensive research on a given query using GPT Researcher.
    
    This tool performs deep research on any topic, gathering information from web sources,
    local documents, or both, and generates a detailed report with citations.
    
    Args:
        query: The research question or topic to investigate
        report_type: Type of report to generate (research_report, resource_report, outline_report)
        report_source: Source for research (web, local documents, or hybrid)
        max_iterations: Maximum number of research iterations (1-10)
        doc_path: Path to local documents directory (required for local/hybrid research)
        retriever: Retriever to use (tavily, mcp, or comma-separated list)
        mcp_configs: MCP configurations for hybrid research with external data sources
    
    Returns:
        Dictionary containing the research report, citations, and metadata
    """
    try:
        # Import GPT Researcher
        from gpt_researcher import GPTResearcher
        
        # Set up environment variables if needed
        if doc_path:
            os.environ["DOC_PATH"] = doc_path
        
        if retriever:
            os.environ["RETRIEVER"] = retriever
        
        # Create researcher instance
        researcher = GPTResearcher(
            query=query,
            report_type=report_type,
            report_source=report_source,
            mcp_configs=mcp_configs or []
        )
        
        # Conduct research
        research_result = asyncio.run(researcher.conduct_research())
        
        # Write report
        report = asyncio.run(researcher.write_report())
        
        # Extract citations and metadata
        citations = getattr(research_result, 'citations', [])
        metadata = {
            "query": query,
            "report_type": report_type,
            "report_source": report_source,
            "max_iterations": max_iterations,
            "retriever": retriever,
            "timestamp": asyncio.run(researcher.get_timestamp()),
            "research_steps": getattr(research_result, 'research_steps', []),
            "total_sources": len(citations)
        }
        
        return {
            "success": True,
            "query": query,
            "report": report,
            "citations": citations,
            "metadata": metadata,
            "error": None
        }
        
    except ImportError:
        return {
            "success": False,
            "query": query,
            "report": "",
            "citations": [],
            "metadata": {},
            "error": "GPT Researcher not installed. Install with: pip install gpt-researcher"
        }
    except Exception as e:
        return {
            "success": False,
            "query": query,
            "report": "",
            "citations": [],
            "metadata": {},
            "error": f"Research failed: {str(e)}"
        }


@mcp.tool
def research_local_documents(
    query: str,
    doc_path: str,
    report_type: Literal["research_report", "resource_report", "outline_report"] = "research_report"
) -> Dict[str, Any]:
    """
    Conduct research using only local documents.
    
    This tool searches through local documents (PDF, TXT, CSV, Excel, Markdown, 
    PowerPoint, Word) to answer research queries.
    
    Args:
        query: The research question or topic
        doc_path: Path to directory containing documents
        report_type: Type of report to generate
    
    Returns:
        Dictionary containing the research report based on local documents
    """
    return conduct_research.fn(
        query=query,
        report_type=report_type,
        report_source="local",
        doc_path=doc_path,
        retriever="local"
    )


@mcp.tool
def deep_research(
    query: str,
    depth: int = 3,
    breadth: int = 5,
    max_iterations: int = 5
) -> Dict[str, Any]:
    """
    Conduct deep recursive research with tree-like exploration.
    
    This tool performs advanced recursive research that explores topics with
    agentic depth and breadth, diving deeper into subtopics while maintaining
    a comprehensive view of the research subject.
    
    Args:
        query: The research question or topic
        depth: Depth of recursive exploration (1-5)
        breadth: Breadth of subtopics to explore (1-10)
        max_iterations: Maximum number of research iterations
    
    Returns:
        Dictionary containing the deep research report with comprehensive analysis
    """
    try:
        from gpt_researcher import GPTResearcher
        
        # Configure for deep research
        researcher = GPTResearcher(
            query=query,
            report_type="research_report",
            report_source="web"
        )
        
        # Set deep research parameters
        researcher.depth = depth
        researcher.breadth = breadth
        researcher.max_iterations = max_iterations
        
        # Conduct deep research
        research_result = asyncio.run(researcher.conduct_deep_research())
        
        # Write comprehensive report
        report = asyncio.run(researcher.write_report())
        
        # Extract comprehensive metadata
        citations = getattr(research_result, 'citations', [])
        metadata = {
            "query": query,
            "research_type": "deep_research",
            "depth": depth,
            "breadth": breadth,
            "max_iterations": max_iterations,
            "timestamp": asyncio.run(researcher.get_timestamp()),
            "research_tree": getattr(research_result, 'research_tree', {}),
            "total_sources": len(citations),
            "subtopics_explored": getattr(research_result, 'subtopics_count', 0)
        }
        
        return {
            "success": True,
            "query": query,
            "report": report,
            "citations": citations,
            "metadata": metadata,
            "error": None
        }
        
    except ImportError:
        return {
            "success": False,
            "query": query,
            "report": "",
            "citations": [],
            "metadata": {},
            "error": "GPT Researcher not installed. Install with: pip install gpt-researcher"
        }
    except Exception as e:
        return {
            "success": False,
            "query": query,
            "report": "",
            "citations": [],
            "metadata": {},
            "error": f"Deep research failed: {str(e)}"
        }


@mcp.tool
def hybrid_research_with_mcp(
    query: str,
    mcp_configs: List[Dict[str, Any]],
    report_type: Literal["research_report", "resource_report", "outline_report"] = "research_report"
) -> Dict[str, Any]:
    """
    Conduct hybrid research using both web search and MCP data sources.
    
    This tool combines web research with specialized data sources like GitHub repositories,
    databases, and custom APIs through MCP integration.
    
    Args:
        query: The research question or topic
        mcp_configs: List of MCP configurations for external data sources
        report_type: Type of report to generate
    
    Returns:
        Dictionary containing the hybrid research report
    """
    return conduct_research.fn(
        query=query,
        report_type=report_type,
        report_source="web",
        retriever="tavily,mcp",
        mcp_configs=mcp_configs
    )


@mcp.tool
def get_research_capabilities() -> Dict[str, Any]:
    """
    Get information about GPT Researcher's capabilities and configuration.
    
    Returns:
        Dictionary containing available features, supported formats, and configuration options
    """
    try:
        from gpt_researcher import GPTResearcher
        
        capabilities = {
            "supported_report_types": ["research_report", "resource_report", "outline_report"],
            "supported_sources": ["web", "local", "hybrid"],
            "supported_document_formats": [
                "PDF", "TXT", "CSV", "Excel", "Markdown", 
                "PowerPoint", "Word documents"
            ],
            "available_retrievers": ["tavily", "mcp", "local"],
            "deep_research_available": True,
            "mcp_integration_available": True,
            "local_document_support": True,
            "citation_support": True,
            "multi_agent_support": True,
            "configuration_options": {
                "max_iterations": "1-10",
                "depth": "1-5 (for deep research)",
                "breadth": "1-10 (for deep research)",
                "report_types": ["research_report", "resource_report", "outline_report"],
                "sources": ["web", "local", "hybrid"]
            }
        }
        
        return {
            "success": True,
            "capabilities": capabilities,
            "error": None
        }
        
    except ImportError:
        return {
            "success": False,
            "capabilities": {},
            "error": "GPT Researcher not installed. Install with: pip install gpt-researcher"
        }


@mcp.tool
def validate_research_setup() -> Dict[str, Any]:
    """
    Validate that GPT Researcher is properly installed and configured.
    
    Returns:
        Dictionary containing validation results and setup instructions
    """
    validation_results = {
        "gpt_researcher_installed": False,
        "required_dependencies": {},
        "api_keys_configured": {},
        "setup_instructions": []
    }
    
    try:
        import gpt_researcher
        validation_results["gpt_researcher_installed"] = True
    except ImportError:
        validation_results["setup_instructions"].append(
            "Install GPT Researcher: pip install gpt-researcher"
        )
    
    # Check for required API keys
    api_keys = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY"),
        "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")  # For MCP GitHub integration
    }
    
    for key, value in api_keys.items():
        validation_results["api_keys_configured"][key] = bool(value)
        if not value:
            validation_results["setup_instructions"].append(
                f"Set {key} environment variable for full functionality"
            )
    
    # Check for optional dependencies
    optional_deps = {
        "phue2": "For smart home integration",
        "requests": "For HTTP requests",
        "beautifulsoup4": "For web scraping"
    }
    
    for dep, description in optional_deps.items():
        try:
            __import__(dep)
            validation_results["required_dependencies"][dep] = True
        except ImportError:
            validation_results["required_dependencies"][dep] = False
    
    return {
        "success": True,
        "validation_results": validation_results,
        "error": None
    }


# Resources for documentation and examples
@mcp.resource("gpt-researcher://docs/installation")
def installation_docs() -> str:
    """Installation and setup documentation for GPT Researcher"""
    return """
# GPT Researcher Installation Guide

## Prerequisites
- Python 3.11 or later
- OpenAI API Key
- Tavily API Key (for web search)

## Installation
```bash
pip install gpt-researcher
```

## Environment Setup
```bash
export OPENAI_API_KEY="your-openai-api-key"
export TAVILY_API_KEY="your-tavily-api-key"
```

## Optional: MCP Integration
For hybrid research with external data sources:
```bash
export GITHUB_TOKEN="your-github-token"  # For GitHub MCP server
```

## Verification
Use the `validate_research_setup` tool to check your installation.
"""


@mcp.resource("gpt-researcher://docs/examples")
def usage_examples() -> str:
    """Usage examples for GPT Researcher MCP tools"""
    return """
# GPT Researcher MCP Usage Examples

## Basic Web Research
```python
# Simple research query
result = conduct_research(
    query="What are the latest trends in AI research?",
    report_type="research_report"
)
```

## Local Document Research
```python
# Research using local documents
result = research_local_documents(
    query="What are the main findings in our quarterly reports?",
    doc_path="/path/to/documents"
)
```

## Deep Research
```python
# Comprehensive recursive research
result = deep_research(
    query="Impact of climate change on agriculture",
    depth=3,
    breadth=5
)
```

## Hybrid Research with MCP
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

## Configuration Options
- report_type: "research_report", "resource_report", "outline_report"
- report_source: "web", "local", "hybrid"
- max_iterations: 1-10
- retriever: "tavily", "mcp", "local", or comma-separated list
"""


@mcp.resource("gpt-researcher://config/template")
def config_template() -> str:
    """Configuration template for GPT Researcher"""
    return json.dumps({
        "research_config": {
            "default_report_type": "research_report",
            "default_source": "web",
            "max_iterations": 3,
            "retriever": "tavily"
        },
        "mcp_configs": [
            {
                "name": "github",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-github"],
                "env": {
                    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
                }
            }
        ],
        "local_documents": {
            "doc_path": "./documents",
            "supported_formats": ["pdf", "txt", "csv", "xlsx", "md", "pptx", "docx"]
        },
        "deep_research": {
            "default_depth": 3,
            "default_breadth": 5,
            "max_iterations": 5
        }
    }, indent=2)


# Prompts for common research tasks
@mcp.prompt("research-outline")
def research_outline_prompt(topic: str) -> str:
    """Generate a research outline for a given topic"""
    return f"""
Create a comprehensive research outline for the topic: "{topic}"

The outline should include:
1. Main research question
2. Key subtopics to explore
3. Potential sources to investigate
4. Expected findings areas
5. Research methodology suggestions

Focus on creating a structured approach that will lead to a thorough understanding of the topic.
"""


@mcp.prompt("research-analysis")
def research_analysis_prompt(query: str, findings: str) -> str:
    """Analyze research findings and provide insights"""
    return f"""
Research Query: {query}

Research Findings:
{findings}

Please provide:
1. Key insights and patterns
2. Contradictions or conflicting information
3. Gaps in the research
4. Recommendations for further investigation
5. Summary of the most important findings

Focus on critical analysis and actionable insights.
"""


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
