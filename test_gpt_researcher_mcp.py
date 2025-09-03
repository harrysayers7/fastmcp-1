"""
Test script for GPT Researcher MCP Server

This script tests the basic functionality of the MCP server tools.
"""

# Import the MCP server to access the tools
import gpt_researcher_mcp


def test_get_research_capabilities():
    """Test getting research capabilities"""
    result = gpt_researcher_mcp.get_research_capabilities.fn()
    
    assert isinstance(result, dict)
    assert "success" in result
    assert "capabilities" in result
    
    if result["success"]:
        capabilities = result["capabilities"]
        assert "supported_report_types" in capabilities
        assert "supported_sources" in capabilities
        assert "supported_document_formats" in capabilities


def test_validate_research_setup():
    """Test research setup validation"""
    result = gpt_researcher_mcp.validate_research_setup.fn()
    
    assert isinstance(result, dict)
    assert "success" in result
    assert "validation_results" in result
    
    validation = result["validation_results"]
    assert "gpt_researcher_installed" in validation
    assert "api_keys_configured" in validation
    assert "setup_instructions" in validation


def test_conduct_research_basic():
    """Test basic research functionality"""
    result = gpt_researcher_mcp.conduct_research.fn(
        query="What is artificial intelligence?",
        report_type="research_report",
        report_source="web",
        max_iterations=1
    )
    
    assert isinstance(result, dict)
    assert "success" in result
    assert "query" in result
    assert "report" in result
    assert "citations" in result
    assert "metadata" in result
    assert "error" in result
    
    # Check that the query is preserved
    assert result["query"] == "What is artificial intelligence?"


def test_research_local_documents():
    """Test local document research"""
    result = gpt_researcher_mcp.research_local_documents.fn(
        query="Test query",
        doc_path="/nonexistent/path",
        report_type="research_report"
    )
    
    assert isinstance(result, dict)
    assert "success" in result
    assert "query" in result
    assert result["query"] == "Test query"


def test_deep_research():
    """Test deep research functionality"""
    result = gpt_researcher_mcp.deep_research.fn(
        query="Test deep research query",
        depth=2,
        breadth=3,
        max_iterations=2
    )
    
    assert isinstance(result, dict)
    assert "success" in result
    assert "query" in result
    assert "metadata" in result
    assert result["query"] == "Test deep research query"


def test_hybrid_research_with_mcp():
    """Test hybrid research with MCP"""
    mcp_configs = [
        {
            "name": "test",
            "command": "echo",
            "args": ["test"],
            "env": {}
        }
    ]
    
    result = gpt_researcher_mcp.hybrid_research_with_mcp.fn(
        query="Test hybrid research",
        mcp_configs=mcp_configs,
        report_type="research_report"
    )
    
    assert isinstance(result, dict)
    assert "success" in result
    assert "query" in result
    assert result["query"] == "Test hybrid research"


def test_research_config_validation():
    """Test that research configurations are properly validated"""
    # Test with invalid max_iterations
    result = gpt_researcher_mcp.conduct_research.fn(
        query="Test query",
        max_iterations=15  # Should be capped at 10
    )
    
    assert isinstance(result, dict)
    assert "success" in result


if __name__ == "__main__":
    # Run basic tests
    print("Testing GPT Researcher MCP Server...")
    
    try:
        test_get_research_capabilities()
        print("✓ get_research_capabilities test passed")
    except Exception as e:
        print(f"✗ get_research_capabilities test failed: {e}")
    
    try:
        test_validate_research_setup()
        print("✓ validate_research_setup test passed")
    except Exception as e:
        print(f"✗ validate_research_setup test failed: {e}")
    
    try:
        test_conduct_research_basic()
        print("✓ conduct_research_basic test passed")
    except Exception as e:
        print(f"✗ conduct_research_basic test failed: {e}")
    
    try:
        test_research_local_documents()
        print("✓ research_local_documents test passed")
    except Exception as e:
        print(f"✗ research_local_documents test failed: {e}")
    
    try:
        test_deep_research()
        print("✓ deep_research test passed")
    except Exception as e:
        print(f"✗ deep_research test failed: {e}")
    
    try:
        test_hybrid_research_with_mcp()
        print("✓ hybrid_research_with_mcp test passed")
    except Exception as e:
        print(f"✗ hybrid_research_with_mcp test failed: {e}")
    
    print("\nBasic tests completed!")
