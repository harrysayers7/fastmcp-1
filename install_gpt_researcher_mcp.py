#!/usr/bin/env python3
"""
Installation script for GPT Researcher MCP Server

This script helps set up the GPT Researcher MCP server with proper dependencies
and configuration.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is 3.11 or later"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print(f"✗ Python 3.11+ required, found {version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor} is compatible")
    return True


def install_dependencies():
    """Install required dependencies"""
    dependencies = [
        "gpt-researcher",
        "fastmcp",
        "pydantic",
        "httpx",
        "uvicorn"
    ]
    
    print("Installing dependencies...")
    for dep in dependencies:
        if not run_command(f"pip install {dep}", f"Installing {dep}"):
            return False
    return True


def create_env_file():
    """Create .env file template"""
    env_file = Path(".env")
    if env_file.exists():
        print("✓ .env file already exists")
        return True
    
    env_content = """# GPT Researcher MCP Server Environment Variables
# Copy this file and fill in your API keys

# Required for GPT Researcher
OPENAI_API_KEY=your-openai-api-key-here
TAVILY_API_KEY=your-tavily-api-key-here

# Optional: For MCP integration with external data sources
GITHUB_TOKEN=your-github-token-here

# Optional: For other MCP servers
# Add other API keys as needed
"""
    
    try:
        with open(env_file, "w") as f:
            f.write(env_content)
        print("✓ Created .env template file")
        print("  Please edit .env and add your API keys")
        return True
    except Exception as e:
        print(f"✗ Failed to create .env file: {e}")
        return False


def create_documents_directory():
    """Create documents directory for local research"""
    docs_dir = Path("documents")
    if docs_dir.exists():
        print("✓ Documents directory already exists")
        return True
    
    try:
        docs_dir.mkdir(exist_ok=True)
        print("✓ Created documents directory")
        print("  Add your documents here for local research")
        return True
    except Exception as e:
        print(f"✗ Failed to create documents directory: {e}")
        return False


def test_installation():
    """Test the installation"""
    print("Testing installation...")
    
    try:
        # Test imports
        import gpt_researcher
        print("✓ GPT Researcher import successful")
    except ImportError:
        print("✗ GPT Researcher import failed")
        return False
    
    try:
        import fastmcp
        print("✓ FastMCP import successful")
    except ImportError:
        print("✗ FastMCP import failed")
        return False
    
    # Test MCP server
    try:
        from gpt_researcher_mcp import get_research_capabilities
        result = get_research_capabilities()
        if result["success"]:
            print("✓ MCP server tools working")
        else:
            print("✗ MCP server tools not working properly")
            return False
    except Exception as e:
        print(f"✗ MCP server test failed: {e}")
        return False
    
    return True


def main():
    """Main installation process"""
    print("GPT Researcher MCP Server Installation")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        print("Please upgrade to Python 3.11 or later")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("Failed to install dependencies")
        sys.exit(1)
    
    # Create configuration files
    if not create_env_file():
        print("Failed to create environment file")
        sys.exit(1)
    
    if not create_documents_directory():
        print("Failed to create documents directory")
        sys.exit(1)
    
    # Test installation
    if not test_installation():
        print("Installation test failed")
        sys.exit(1)
    
    print("\n" + "=" * 40)
    print("Installation completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file and add your API keys")
    print("2. Add documents to the 'documents' directory (optional)")
    print("3. Run the MCP server: python gpt_researcher_mcp.py")
    print("4. Or use with FastMCP: fastmcp run gpt_researcher_mcp.py")
    print("\nFor more information, see README_GPT_Researcher_MCP.md")


if __name__ == "__main__":
    main()
