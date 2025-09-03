#!/usr/bin/env python3
"""
Demo script showing how to use the GPT Researcher MCP Server

This script demonstrates the different ways to use the MCP server
and shows what you can do with it.
"""

import asyncio
import json
import os
from gpt_researcher_mcp import mcp
from fastmcp.client import Client


async def demo_basic_functionality():
    """Demonstrate basic MCP server functionality"""
    
    print("🚀 GPT Researcher MCP Server Demo")
    print("=" * 50)
    
    async with Client(mcp) as client:
        print("\n📋 Available Tools:")
        tools = await client.list_tools()
        for i, tool in enumerate(tools, 1):
            print(f"  {i}. {tool.name}")
            print(f"     {tool.description[:100]}...")
        
        print("\n📚 Available Resources:")
        resources = await client.list_resources()
        for i, resource in enumerate(resources, 1):
            print(f"  {i}. {resource.uri}")
            print(f"     {resource.name}")
        
        print("\n💡 Available Prompts:")
        prompts = await client.list_prompts()
        for i, prompt in enumerate(prompts, 1):
            print(f"  {i}. {prompt.name}")
            print(f"     {prompt.description}")


async def demo_capabilities_check():
    """Demonstrate capabilities and setup validation"""
    
    print("\n🔍 Checking Capabilities and Setup")
    print("=" * 50)
    
    async with Client(mcp) as client:
        # Check capabilities
        print("\n1. Getting research capabilities...")
        capabilities_result = await client.call_tool("get_research_capabilities", {})
        capabilities_text = capabilities_result.content[0].text if capabilities_result.content else "No content"
        capabilities = json.loads(capabilities_text)
        
        if capabilities.get("success"):
            print("✅ GPT Researcher is available!")
            caps = capabilities.get("capabilities", {})
            print(f"   - Supported report types: {caps.get('supported_report_types', [])}")
            print(f"   - Supported sources: {caps.get('supported_sources', [])}")
            print(f"   - Deep research available: {caps.get('deep_research_available', False)}")
            print(f"   - MCP integration available: {caps.get('mcp_integration_available', False)}")
        else:
            print("❌ GPT Researcher not available")
            print(f"   Error: {capabilities.get('error', 'Unknown error')}")
        
        # Validate setup
        print("\n2. Validating setup...")
        validation_result = await client.call_tool("validate_research_setup", {})
        validation_text = validation_result.content[0].text if validation_result.content else "No content"
        validation = json.loads(validation_text)
        
        if validation.get("success"):
            results = validation.get("validation_results", {})
            print("📊 Setup Status:")
            print(f"   - GPT Researcher installed: {results.get('gpt_researcher_installed', False)}")
            
            api_keys = results.get("api_keys_configured", {})
            print("   - API Keys configured:")
            for key, configured in api_keys.items():
                status = "✅" if configured else "❌"
                print(f"     {status} {key}")
            
            if results.get("setup_instructions"):
                print("\n📝 Setup Instructions:")
                for instruction in results["setup_instructions"]:
                    print(f"   - {instruction}")


async def demo_research_tools():
    """Demonstrate research tools (will show errors if GPT Researcher not installed)"""
    
    print("\n🔬 Research Tools Demo")
    print("=" * 50)
    
    async with Client(mcp) as client:
        # Test basic research
        print("\n1. Testing basic research...")
        try:
            result = await client.call_tool("conduct_research", {
                "query": "What is artificial intelligence?",
                "report_type": "research_report",
                "report_source": "web",
                "max_iterations": 1
            })
            
            result_text = result.content[0].text if result.content else "No content"
            result_data = json.loads(result_text)
            
            if result_data.get("success"):
                print("✅ Research completed successfully!")
                print(f"   Query: {result_data.get('query', 'N/A')}")
                print(f"   Report length: {len(result_data.get('report', ''))} characters")
                print(f"   Citations: {len(result_data.get('citations', []))} sources")
            else:
                print("❌ Research failed")
                print(f"   Error: {result_data.get('error', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Research failed with exception: {e}")
        
        # Test local document research
        print("\n2. Testing local document research...")
        try:
            result = await client.call_tool("research_local_documents", {
                "query": "Test query",
                "doc_path": "/tmp",  # Use a safe path
                "report_type": "research_report"
            })
            
            result_text = result.content[0].text if result.content else "No content"
            result_data = json.loads(result_text)
            
            if result_data.get("success"):
                print("✅ Local document research completed!")
            else:
                print("❌ Local document research failed")
                print(f"   Error: {result_data.get('error', 'Unknown error')}")
                
        except Exception as e:
            print(f"❌ Local document research failed with exception: {e}")


async def demo_resources():
    """Demonstrate accessing resources"""
    
    print("\n📚 Resources Demo")
    print("=" * 50)
    
    async with Client(mcp) as client:
        # Get installation docs
        print("\n1. Getting installation documentation...")
        try:
            docs_result = await client.read_resource("gpt-researcher://docs/installation")
            docs_content = docs_result.contents[0].text if docs_result.contents else "No content"
            print("✅ Installation docs retrieved!")
            print(f"   Content preview: {docs_content[:200]}...")
        except Exception as e:
            print(f"❌ Failed to get installation docs: {e}")
        
        # Get usage examples
        print("\n2. Getting usage examples...")
        try:
            examples_result = await client.read_resource("gpt-researcher://docs/examples")
            examples_content = examples_result.contents[0].text if examples_result.contents else "No content"
            print("✅ Usage examples retrieved!")
            print(f"   Content preview: {examples_content[:200]}...")
        except Exception as e:
            print(f"❌ Failed to get usage examples: {e}")


async def demo_prompts():
    """Demonstrate using prompts"""
    
    print("\n💡 Prompts Demo")
    print("=" * 50)
    
    async with Client(mcp) as client:
        # Test research outline prompt
        print("\n1. Testing research outline prompt...")
        try:
            prompt_result = await client.get_prompt("research-outline", {
                "topic": "Machine Learning in Healthcare"
            })
            
            if prompt_result.messages:
                print("✅ Research outline prompt generated!")
                print(f"   Prompt: {prompt_result.messages[0].content.text[:200]}...")
            else:
                print("❌ No prompt content generated")
                
        except Exception as e:
            print(f"❌ Failed to generate research outline prompt: {e}")


async def main():
    """Run all demos"""
    
    print("🎯 GPT Researcher MCP Server - Complete Demo")
    print("=" * 60)
    
    # Run all demo functions
    await demo_basic_functionality()
    await demo_capabilities_check()
    await demo_research_tools()
    await demo_resources()
    await demo_prompts()
    
    print("\n" + "=" * 60)
    print("🎉 Demo completed!")
    print("\nNext steps:")
    print("1. Install GPT Researcher: pip install gpt-researcher")
    print("2. Set up API keys: OPENAI_API_KEY and TAVILY_API_KEY")
    print("3. Configure Claude Desktop or Cursor with the MCP server")
    print("4. Start conducting research!")
    print("\nFor detailed setup instructions, see:")
    print("- claude_desktop_setup.md")
    print("- cursor_setup.md")
    print("- QUICK_START.md")


if __name__ == "__main__":
    asyncio.run(main())
