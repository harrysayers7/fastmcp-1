# Real-World FastMCP Usage Examples

## 🎯 How You Actually Use FastMCP

Based on the working example above, here's how FastMCP works in practice:

### 1. **You Create a Server** (like `practical_example.py`)
```python
from fastmcp import FastMCP

mcp = FastMCP("My App")

@mcp.tool()
def my_function(param: str) -> str:
    """This function can be called by AI clients."""
    return f"Processed: {param}"

mcp.run()
```

### 2. **AI Clients Connect and Use Your Tools**
The test showed exactly what happens:
- ✅ **Created todos** - AI can call your functions
- ✅ **Listed todos** - AI can get data back
- ✅ **Completed todos** - AI can modify state
- ✅ **Checked weather** - AI can access external APIs
- ✅ **Accessed resources** - AI can read your data
- ✅ **Found prompts** - AI can use your templates

### 3. **Real-World Integration Scenarios**

#### **Scenario A: Claude Desktop Integration**
```bash
# Install your server in Claude Desktop
uv run fastmcp install practical_example.py

# Now Claude can:
# - "Create a todo to buy milk"
# - "What's my weather like?"
# - "Mark the first todo as done"
```

#### **Scenario B: Custom AI Application**
```python
# Your AI app connects to your FastMCP server
async with Client("practical_example.py") as client:
    # AI can now use all your tools
    result = await client.call_tool("create_todo", {
        "task": "User requested task",
        "priority": "high"
    })
```

#### **Scenario C: HTTP API**
```bash
# Run as HTTP server
uv run fastmcp run practical_example.py --transport http --port 8000

# Now any HTTP client can call your tools via MCP protocol
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"method": "tools/call", "params": {"name": "get_weather", "arguments": {"city": "NYC"}}}'
```

### 4. **What Makes This Powerful**

**For Developers:**
- Write normal Python functions
- FastMCP handles the MCP protocol
- Works with any MCP-compatible AI client
- No complex API design needed

**For AI Clients:**
- Discover available tools automatically
- Get type-safe function calls
- Access structured data via resources
- Use prompt templates for better interactions

**For Users:**
- Natural language interaction
- "Create a todo to buy groceries" → actually creates a todo
- "What's my weather?" → gets real weather data
- "Mark the first task as done" → updates your data

### 5. **Common Use Cases**

**Personal Productivity:**
- Todo management (like our example)
- Calendar integration
- File organization
- Note-taking

**Business Applications:**
- Customer support automation
- Data analysis tools
- Content generation
- Workflow automation

**Developer Tools:**
- Code generation
- Database queries
- API testing
- Deployment automation

### 6. **The Magic: AI Understands Your Functions**

When you write:
```python
@mcp.tool()
def create_todo(task: str, priority: str = "medium") -> str:
    """Create a new todo item."""
    # ... implementation
```

AI clients automatically understand:
- Function name: `create_todo`
- Parameters: `task` (required), `priority` (optional, defaults to "medium")
- Return type: string
- Description: "Create a new todo item"

So when a user says "Create a high-priority todo to call mom", the AI knows to call:
```python
create_todo(task="call mom", priority="high")
```

### 7. **Next Steps for You**

1. **Start Simple**: Use our `practical_example.py` as a template
2. **Add Your Logic**: Replace the todo functions with your actual business logic
3. **Test Locally**: Use the client pattern to test your functions
4. **Deploy**: Run as HTTP server or integrate with MCP clients
5. **Scale**: Add authentication, multiple servers, complex workflows

The beauty of FastMCP is that you write normal Python code, and suddenly AI can interact with your applications naturally!
