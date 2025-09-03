# FastMCP Beginner's Guide 🚀

> **Complete step-by-step guide to building your first FastMCP server**

## What is FastMCP?

FastMCP lets you create AI-powered applications by writing simple Python functions. When you create a FastMCP server, AI assistants (like Claude) can automatically understand and use your functions through natural language.

**Example:** You write a function to create todos, and then you can tell Claude "Create a todo to buy groceries" and it actually creates the todo!

---

## Prerequisites

Before you start, make sure you have:

- **Python 3.10+** installed
- **uv** package manager (we'll install this)
- Basic Python knowledge (functions, decorators)

---

## Step 1: Install FastMCP

### Install uv (if you don't have it)
```bash
# On macOS
brew install uv

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install FastMCP
```bash
# Clone the repository
git clone https://github.com/jlowin/fastmcp.git
cd fastmcp

# Install dependencies
uv sync
```

---

## Step 2: Your First Server

Create a file called `my_server.py`:

```python
from fastmcp import FastMCP

# Create your server
mcp = FastMCP("My First Server")

# Add a simple tool (function that AI can call)
@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}! Nice to meet you!"

# Add another tool
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

# Run the server
if __name__ == "__main__":
    mcp.run()
```

### Test Your Server
```bash
# Run your server
uv run fastmcp run my_server.py

# In another terminal, inspect what you built
uv run fastmcp inspect my_server.py
```

You should see:
```
Server
  Name:         My First Server
  Generation:   2

Components
  Tools:        2
  Prompts:      0
  Resources:    0
  Templates:    0
```

---

## Step 3: Understanding the Components

FastMCP has 4 main components:

### 1. Tools (Functions AI can call)
```python
@mcp.tool()
def my_function(param: str) -> str:
    """Description of what this function does."""
    return f"Processed: {param}"
```

### 2. Resources (Data AI can access)
```python
@mcp.resource("file://config")
def get_config() -> str:
    """Get configuration data."""
    return '{"version": "1.0", "status": "running"}'
```

### 3. Prompts (Templates for AI interactions)
```python
@mcp.prompt("greeting")
def greeting_prompt(name: str) -> str:
    """Generate a greeting prompt."""
    return f"Say hello to {name} in a friendly way."
```

### 4. Resource Templates (Dynamic resources)
```python
@mcp.resource("file://{filename}")
def read_file(filename: str) -> str:
    """Read a file by name."""
    with open(filename, 'r') as f:
        return f.read()
```

---

## Step 4: Building a Real Application

Let's build a **Personal Task Manager**:

```python
from fastmcp import FastMCP
import json
import os
from datetime import datetime

# Create the server
mcp = FastMCP("Task Manager")

# Storage file
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# TOOLS
@mcp.tool()
def create_task(title: str, description: str = "", priority: str = "medium") -> str:
    """Create a new task."""
    tasks = load_tasks()
    
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "completed": False,
        "created": datetime.now().isoformat()
    }
    
    tasks.append(task)
    save_tasks(tasks)
    
    return f"Created task: '{title}' (Priority: {priority})"

@mcp.tool()
def list_tasks() -> str:
    """List all tasks."""
    tasks = load_tasks()
    
    if not tasks:
        return "No tasks found. Create one with create_task!"
    
    result = "📋 Your Tasks:\n"
    for task in tasks:
        status = "✅" if task["completed"] else "⏳"
        result += f"{task['id']}. {status} {task['title']} ({task['priority']})\n"
        if task["description"]:
            result += f"   📝 {task['description']}\n"
    
    return result

@mcp.tool()
def complete_task(task_id: int) -> str:
    """Mark a task as completed."""
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            return f"✅ Completed task: '{task['title']}'"
    
    return f"❌ Task {task_id} not found"

@mcp.tool()
def delete_task(task_id: int) -> str:
    """Delete a task."""
    tasks = load_tasks()
    
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_title = task["title"]
            tasks.pop(i)
            save_tasks(tasks)
            return f"🗑️ Deleted task: '{deleted_title}'"
    
    return f"❌ Task {task_id} not found"

# RESOURCES
@mcp.resource("file://tasks")
def get_tasks_data() -> str:
    """Get raw tasks data as JSON."""
    tasks = load_tasks()
    return json.dumps(tasks, indent=2)

# PROMPTS
@mcp.prompt("task_summary")
def task_summary_prompt() -> str:
    """Generate a prompt for task analysis."""
    return """Please analyze my current tasks and provide:
1. Summary of pending tasks
2. Priority recommendations  
3. Suggested next actions
Use the list_tasks tool to get current data."""

if __name__ == "__main__":
    print("🚀 Starting Task Manager MCP Server...")
    print("📋 Available tools: create_task, list_tasks, complete_task, delete_task")
    print("📁 Available resources: file://tasks")
    print("💬 Available prompts: task_summary")
    mcp.run()
```

### Test Your Task Manager
```bash
# Run the server
uv run fastmcp run my_server.py

# In another terminal, test it
uv run fastmcp inspect my_server.py
```

---

## Step 5: Running Your Server

### Option 1: Standard Mode (for MCP clients)
```bash
uv run fastmcp run my_server.py
```

### Option 2: HTTP Mode (for web APIs)
```bash
uv run fastmcp run my_server.py --transport http --port 8000
```

### Option 3: Development Mode (with inspector)
```bash
uv run fastmcp dev my_server.py
```

---

## Step 6: Connecting to AI Clients

### Claude Desktop
1. Create a config file `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "task-manager": {
      "command": "uv",
      "args": ["run", "fastmcp", "run", "/path/to/my_server.py"]
    }
  }
}
```

2. Add this to your Claude Desktop MCP configuration

### Cursor IDE
1. Install the MCP extension
2. Add your server to the configuration
3. Use natural language to interact with your tools

---

## Step 7: Advanced Features

### Authentication
```python
from fastmcp.server.auth import BearerAuth

mcp = FastMCP("Secure Server", auth=BearerAuth("your-secret-token"))
```

### Multiple Servers
```python
# Mount other servers
mcp.mount("api", other_server)
```

### Configuration Files
Create `fastmcp.json`:
```json
{
  "name": "My Server",
  "tools": ["my_server.py:my_tool"],
  "transport": "http",
  "port": 8000
}
```

---

## Step 8: Testing Your Server

Create a test file `test_my_server.py`:

```python
import asyncio
from fastmcp import Client

async def test_server():
    async with Client("my_server.py") as client:
        # Test creating a task
        result = await client.call_tool("create_task", {
            "title": "Test task",
            "description": "This is a test",
            "priority": "high"
        })
        print(f"Created: {result}")
        
        # Test listing tasks
        tasks = await client.call_tool("list_tasks", {})
        print(f"Tasks: {tasks}")

if __name__ == "__main__":
    asyncio.run(test_server())
```

Run the test:
```bash
uv run python test_my_server.py
```

---

## Common Patterns

### File Operations
```python
@mcp.tool()
def read_file(filename: str) -> str:
    """Read a file."""
    with open(filename, 'r') as f:
        return f.read()

@mcp.tool()
def write_file(filename: str, content: str) -> str:
    """Write content to a file."""
    with open(filename, 'w') as f:
        f.write(content)
    return f"Wrote {len(content)} characters to {filename}"
```

### API Calls
```python
import requests

@mcp.tool()
def get_weather(city: str) -> str:
    """Get weather for a city."""
    # Replace with real API call
    return f"Weather in {city}: Sunny, 72°F"
```

### Database Operations
```python
import sqlite3

@mcp.tool()
def add_user(name: str, email: str) -> str:
    """Add a user to the database."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return f"Added user: {name}"
```

---

## Troubleshooting

### Common Issues

**1. "No server object found"**
- Make sure your server variable is named `mcp`, `server`, or `app`
- Or use `file.py:object_name` syntax

**2. "Module not found"**
- Make sure you're in the right directory
- Check your Python path

**3. "Port already in use"**
- Use a different port: `--port 8001`
- Or kill the process using that port

### Getting Help
- Check the [FastMCP documentation](https://gofastmcp.com)
- Look at examples in the `examples/` directory
- Join the community discussions

---

## Next Steps

1. **Build your own server** using this guide
2. **Explore the examples** in the `examples/` directory
3. **Read the full documentation** at https://gofastmcp.com
4. **Join the community** for help and inspiration

**Remember:** Start simple, test often, and build incrementally. FastMCP makes it easy to create powerful AI-powered applications with just Python functions!

---

## Quick Reference

### Essential Commands
```bash
# Run server
uv run fastmcp run server.py

# Inspect server
uv run fastmcp inspect server.py

# Run with HTTP
uv run fastmcp run server.py --transport http --port 8000

# Development mode
uv run fastmcp dev server.py

# Install in MCP client
uv run fastmcp install server.py
```

### Essential Decorators
```python
@mcp.tool()                    # Function AI can call
@mcp.resource("uri://path")    # Data AI can access
@mcp.prompt("name")            # Template for AI interactions
```

### Essential Patterns
```python
# Simple tool
@mcp.tool()
def my_function(param: str) -> str:
    """Description for AI."""
    return f"Result: {param}"

# Resource with parameters
@mcp.resource("file://{filename}")
def read_file(filename: str) -> str:
    """Read file by name."""
    return open(filename).read()
```

**Happy coding! 🎉**
