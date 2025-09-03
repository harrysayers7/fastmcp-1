# FastMCP Project Template 📋

> **Template for planning and building your FastMCP server**

Use this template to plan your FastMCP project before you start coding. Fill out each section to clarify your requirements and design.

---

## Project Overview

### Project Name
**Your Server Name:** `_________________`

### Project Description
**What does your server do?**
```
[Describe the main purpose and functionality of your server]
```

### Target Users
**Who will use this server?**
- [ ] Personal use
- [ ] Team/company use  
- [ ] Public API
- [ ] Other: `_________________`

---

## Core Functionality

### Main Features
List the main features your server will provide:

1. **Feature 1:** `_________________`
   - Description: `_________________`
   - Input: `_________________`
   - Output: `_________________`

2. **Feature 2:** `_________________`
   - Description: `_________________`
   - Input: `_________________`
   - Output: `_________________`

3. **Feature 3:** `_________________`
   - Description: `_________________`
   - Input: `_________________`
   - Output: `_________________`

### User Stories
**How will users interact with your server?**

**Example:** "As a user, I want to create a todo item so that I can track my tasks"

1. **Story 1:** `_________________`
2. **Story 2:** `_________________`
3. **Story 3:** `_________________`

---

## Technical Design

### Tools (Functions)
**What functions will AI be able to call?**

| Function Name | Purpose | Parameters | Return Type | Example Usage |
|---------------|---------|------------|-------------|---------------|
| `function1` | `_________________` | `param1: str, param2: int` | `str` | "Call function1 with 'hello' and 42" |
| `function2` | `_________________` | `_________________` | `_________________` | `_________________` |
| `function3` | `_________________` | `_________________` | `_________________` | `_________________` |

### Resources (Data)
**What data will AI be able to access?**

| Resource URI | Purpose | Data Format | Example |
|--------------|---------|-------------|---------|
| `file://config` | `_________________` | `JSON` | `{"version": "1.0"}` |
| `file://{filename}` | `_________________` | `_________________` | `_________________` |
| `api://{endpoint}` | `_________________` | `_________________` | `_________________` |

### Prompts (Templates)
**What prompt templates will you provide?**

| Prompt Name | Purpose | Parameters | Example Output |
|-------------|---------|------------|----------------|
| `summary` | `_________________` | `data: str` | "Summarize this data: ..." |
| `analysis` | `_________________` | `_________________` | `_________________` |
| `report` | `_________________` | `_________________` | `_________________` |

---

## Data Storage

### Data Types
**What data will your server store/manage?**

- [ ] Text files
- [ ] JSON files
- [ ] Database (SQLite/PostgreSQL/etc.)
- [ ] External APIs
- [ ] In-memory only
- [ ] Other: `_________________`

### Data Structure
**Describe your main data structures:**

```json
{
  "example_object": {
    "field1": "description",
    "field2": "description",
    "field3": "description"
  }
}
```

### File Organization
**How will you organize your files?**

```
project/
├── server.py          # Main server file
├── data/              # Data storage
│   ├── config.json
│   └── storage.json
├── utils/             # Helper functions
│   └── helpers.py
└── tests/             # Test files
    └── test_server.py
```

---

## External Dependencies

### Required Libraries
**What Python packages do you need?**

- [ ] `requests` - HTTP API calls
- [ ] `sqlite3` - Database operations
- [ ] `pandas` - Data manipulation
- [ ] `openai` - AI API integration
- [ ] `fastapi` - Web framework
- [ ] Other: `_________________`

### External Services
**What external services will you integrate with?**

- [ ] Weather API
- [ ] Database service
- [ ] File storage (S3, etc.)
- [ ] Email service
- [ ] Other: `_________________`

### API Keys/Configuration
**What configuration will you need?**

```python
# Environment variables needed
API_KEY = "your_api_key"
DATABASE_URL = "your_database_url"
CONFIG_FILE = "config.json"
```

---

## Security & Authentication

### Authentication Method
- [ ] No authentication (public)
- [ ] Bearer token
- [ ] API key
- [ ] OAuth
- [ ] Other: `_________________`

### Security Considerations
**What security measures do you need?**

- [ ] Input validation
- [ ] Rate limiting
- [ ] Data encryption
- [ ] Access control
- [ ] Other: `_________________`

---

## Deployment & Usage

### Deployment Target
- [ ] Local development
- [ ] Personal server
- [ ] Cloud service (AWS, GCP, etc.)
- [ ] Docker container
- [ ] Other: `_________________`

### Transport Method
- [ ] STDIO (for MCP clients)
- [ ] HTTP API
- [ ] Server-Sent Events (SSE)
- [ ] Multiple transports

### Client Integration
**How will users access your server?**

- [ ] Claude Desktop
- [ ] Cursor IDE
- [ ] Custom web app
- [ ] Command line tool
- [ ] Other: `_________________`

---

## Testing Strategy

### Test Cases
**What will you test?**

1. **Unit Tests:**
   - [ ] Function input validation
   - [ ] Function output correctness
   - [ ] Error handling
   - [ ] Edge cases

2. **Integration Tests:**
   - [ ] Client-server communication
   - [ ] Data persistence
   - [ ] External API calls
   - [ ] End-to-end workflows

3. **User Acceptance Tests:**
   - [ ] Natural language interactions
   - [ ] Real-world usage scenarios
   - [ ] Performance under load

### Test Data
**What test data will you use?**

```python
# Example test data
test_tasks = [
    {"title": "Test task 1", "priority": "high"},
    {"title": "Test task 2", "priority": "medium"}
]
```

---

## Development Plan

### Phase 1: Core Functionality
**What will you build first?**

- [ ] Basic server setup
- [ ] Core tools implementation
- [ ] Data storage
- [ ] Basic testing

**Timeline:** `_________________`

### Phase 2: Enhanced Features
**What comes next?**

- [ ] Advanced tools
- [ ] Resources and prompts
- [ ] Error handling
- [ ] Documentation

**Timeline:** `_________________`

### Phase 3: Production Ready
**Final steps:**

- [ ] Authentication
- [ ] Performance optimization
- [ ] Deployment setup
- [ ] User documentation

**Timeline:** `_________________`

---

## Success Metrics

### Functional Requirements
**How will you know it's working?**

- [ ] All tools respond correctly
- [ ] Data persists between sessions
- [ ] AI can understand and use functions
- [ ] Error handling works properly

### Performance Requirements
**What performance do you need?**

- Response time: `_________________` seconds
- Concurrent users: `_________________`
- Data size limits: `_________________`

### User Experience
**How will you measure success?**

- [ ] Users can complete tasks naturally
- [ ] AI understands user intent
- [ ] Error messages are helpful
- [ ] Documentation is clear

---

## Code Structure Template

### Main Server File (`server.py`)
```python
from fastmcp import FastMCP
# Add your imports here

# Create server
mcp = FastMCP("Your Server Name")

# TOOLS
@mcp.tool()
def your_function(param: str) -> str:
    """Description of what this function does."""
    # Implementation here
    return "result"

# RESOURCES  
@mcp.resource("file://your-resource")
def get_resource() -> str:
    """Description of this resource."""
    # Implementation here
    return "data"

# PROMPTS
@mcp.prompt("your-prompt")
def your_prompt(param: str) -> str:
    """Description of this prompt."""
    # Implementation here
    return "prompt text"

if __name__ == "__main__":
    mcp.run()
```

### Configuration File (`fastmcp.json`)
```json
{
  "name": "Your Server Name",
  "description": "Your server description",
  "tools": ["server.py:your_function"],
  "resources": ["server.py:get_resource"],
  "prompts": ["server.py:your_prompt"],
  "transport": "http",
  "port": 8000
}
```

### Test File (`test_server.py`)
```python
import asyncio
from fastmcp import Client

async def test_your_server():
    async with Client("server.py") as client:
        # Test your functions here
        result = await client.call_tool("your_function", {"param": "test"})
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(test_your_server())
```

---

## Checklist

### Before You Start Coding
- [ ] Project overview is clear
- [ ] Core functionality is defined
- [ ] Technical design is planned
- [ ] Dependencies are identified
- [ ] Security requirements are considered
- [ ] Testing strategy is defined

### During Development
- [ ] Start with basic functionality
- [ ] Test each component as you build
- [ ] Document your functions clearly
- [ ] Handle errors gracefully
- [ ] Keep code simple and readable

### Before Deployment
- [ ] All tests pass
- [ ] Documentation is complete
- [ ] Security measures are in place
- [ ] Performance is acceptable
- [ ] User experience is smooth

---

## Resources

### Documentation
- [FastMCP Official Docs](https://gofastmcp.com)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Python Best Practices](https://docs.python.org/3/tutorial/)

### Examples
- Check the `examples/` directory in FastMCP
- Look at community projects
- Study the test files

### Getting Help
- FastMCP GitHub Issues
- Community Discord/Slack
- Stack Overflow (tag: fastmcp)

---

**Remember:** This template is a starting point. Adapt it to your specific needs and don't feel obligated to fill out every section. The goal is to think through your project before you start coding!

**Happy building! 🚀**
