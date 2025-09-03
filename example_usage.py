"""
Example usage of the GPT Researcher MCP Server

This script demonstrates how to use the GPT Researcher MCP server
for various research tasks.
"""

import asyncio
import json
from gpt_researcher_mcp import mcp


async def example_basic_research():
    """Example of basic web research"""
    print("=== Basic Web Research Example ===")
    
    # This would be called through the MCP protocol in practice
    # Here we're showing the tool function directly
    from gpt_researcher_mcp import conduct_research
    
    result = conduct_research(
        query="What are the latest trends in artificial intelligence research?",
        report_type="research_report",
        report_source="web",
        max_iterations=3
    )
    
    print(f"Research Query: {result['query']}")
    print(f"Success: {result['success']}")
    if result['success']:
        print(f"Report Length: {len(result['report'])} characters")
        print(f"Citations: {len(result['citations'])} sources")
        print(f"Metadata: {json.dumps(result['metadata'], indent=2)}")
    else:
        print(f"Error: {result['error']}")


async def example_local_document_research():
    """Example of local document research"""
    print("\n=== Local Document Research Example ===")
    
    from gpt_researcher_mcp import research_local_documents
    
    result = research_local_documents(
        query="What are the main findings in our quarterly reports?",
        doc_path="./documents",  # Path to your documents
        report_type="research_report"
    )
    
    print(f"Research Query: {result['query']}")
    print(f"Success: {result['success']}")
    if result['success']:
        print(f"Report Length: {len(result['report'])} characters")
        print(f"Sources: {len(result['citations'])} documents")
    else:
        print(f"Error: {result['error']}")


async def example_deep_research():
    """Example of deep recursive research"""
    print("\n=== Deep Research Example ===")
    
    from gpt_researcher_mcp import deep_research
    
    result = deep_research(
        query="Impact of climate change on global agriculture",
        depth=3,
        breadth=5,
        max_iterations=5
    )
    
    print(f"Research Query: {result['query']}")
    print(f"Success: {result['success']}")
    if result['success']:
        print(f"Report Length: {len(result['report'])} characters")
        print(f"Sources: {len(result['citations'])} sources")
        print(f"Subtopics Explored: {result['metadata'].get('subtopics_explored', 0)}")
    else:
        print(f"Error: {result['error']}")


async def example_hybrid_research():
    """Example of hybrid research with MCP integration"""
    print("\n=== Hybrid Research with MCP Example ===")
    
    from gpt_researcher_mcp import hybrid_research_with_mcp
    
    mcp_configs = [
        {
            "name": "github",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {"GITHUB_TOKEN": "your-github-token"}
        }
    ]
    
    result = hybrid_research_with_mcp(
        query="Popular open source AI research projects",
        mcp_configs=mcp_configs,
        report_type="research_report"
    )
    
    print(f"Research Query: {result['query']}")
    print(f"Success: {result['success']}")
    if result['success']:
        print(f"Report Length: {len(result['report'])} characters")
        print(f"Sources: {len(result['citations'])} sources")
    else:
        print(f"Error: {result['error']}")


async def example_capabilities_check():
    """Example of checking capabilities and setup"""
    print("\n=== Capabilities and Setup Check ===")
    
    from gpt_researcher_mcp import get_research_capabilities, validate_research_setup
    
    # Check capabilities
    capabilities = get_research_capabilities()
    print("Capabilities:")
    print(json.dumps(capabilities, indent=2))
    
    # Validate setup
    validation = validate_research_setup()
    print("\nSetup Validation:")
    print(json.dumps(validation, indent=2))


async def main():
    """Run all examples"""
    print("GPT Researcher MCP Server Examples")
    print("=" * 50)
    
    # Run examples
    await example_capabilities_check()
    await example_basic_research()
    await example_local_document_research()
    await example_deep_research()
    await example_hybrid_research()
    
    print("\n" + "=" * 50)
    print("Examples completed!")


if __name__ == "__main__":
    asyncio.run(main())
