"""
Direct usage example of GPT Researcher MCP Server

This shows how to use the MCP server directly in Python code
without needing Claude Desktop or Cursor.
"""

import asyncio
import json
from gpt_researcher_mcp import mcp
from fastmcp.client import Client


async def direct_usage_example():
    """Example of using the MCP server directly"""
    
    # Create a client that connects to our MCP server
    async with Client(mcp) as client:
        print("🔍 Testing GPT Researcher MCP Server")
        print("=" * 50)
        
        # Test 1: Get capabilities
        print("\n1. Getting research capabilities...")
        capabilities_result = await client.call_tool("get_research_capabilities", {})
        capabilities = capabilities_result.content[0].text if capabilities_result.content else "No content"
        print(f"✓ Capabilities: {capabilities}")
        
        # Test 2: Validate setup
        print("\n2. Validating setup...")
        validation_result = await client.call_tool("validate_research_setup", {})
        validation = validation_result.content[0].text if validation_result.content else "No content"
        print(f"✓ Setup validation: {validation}")
        
        # Test 3: Conduct basic research (if GPT Researcher is installed)
        print("\n3. Conducting basic research...")
        try:
            research_result = await client.call_tool("conduct_research", {
                "query": "What is artificial intelligence?",
                "report_type": "research_report",
                "report_source": "web",
                "max_iterations": 1
            })
            research_text = research_result.content[0].text if research_result.content else "No content"
            print(f"✓ Research result: {research_text[:200]}...")
        except Exception as e:
            print(f"⚠️  Research failed (likely due to missing GPT Researcher): {e}")
        
        # Test 4: List available tools
        print("\n4. Available tools:")
        tools = await client.list_tools()
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        
        # Test 5: List available resources
        print("\n5. Available resources:")
        resources = await client.list_resources()
        for resource in resources:
            print(f"  - {resource.uri}: {resource.name}")
        
        # Test 6: List available prompts
        print("\n6. Available prompts:")
        prompts = await client.list_prompts()
        for prompt in prompts:
            print(f"  - {prompt.name}: {prompt.description}")


async def research_example():
    """Example of conducting actual research"""
    
    async with Client(mcp) as client:
        print("\n🔬 Conducting Research Example")
        print("=" * 50)
        
        # This will only work if GPT Researcher is properly installed
        # and API keys are configured
        try:
            result = await client.call_tool("conduct_research", {
                "query": "Latest trends in machine learning",
                "report_type": "research_report",
                "report_source": "web",
                "max_iterations": 2
            })
            
            print("Research completed!")
            result_text = result.content[0].text if result.content else "No content"
            print(f"Result: {result_text[:300]}...")
                
        except Exception as e:
            print(f"Research failed: {e}")
            print("Make sure GPT Researcher is installed and API keys are configured")


if __name__ == "__main__":
    print("GPT Researcher MCP Server - Direct Usage Example")
    print("=" * 60)
    
    # Run the basic example
    asyncio.run(direct_usage_example())
    
    # Uncomment the line below to run the research example
    # (requires GPT Researcher to be installed and configured)
    # asyncio.run(research_example())
