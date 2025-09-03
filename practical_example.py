#!/usr/bin/env python3
"""
A practical FastMCP server example - Personal Assistant
This demonstrates real-world usage patterns for FastMCP
"""
import os
import json
import requests
from datetime import datetime
from typing import List, Dict, Any
from fastmcp import FastMCP

# Create a personal assistant MCP server
mcp = FastMCP("Personal Assistant")

# 1. TOOLS - Functions that can be called by AI clients
@mcp.tool()
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    # In a real app, you'd use a weather API
    return f"The weather in {city} is sunny and 72°F"

@mcp.tool()
def create_todo(task: str, priority: str = "medium") -> str:
    """Create a new todo item."""
    todo = {
        "task": task,
        "priority": priority,
        "created": datetime.now().isoformat(),
        "completed": False
    }
    
    # Save to a simple JSON file
    todos_file = "todos.json"
    todos = []
    if os.path.exists(todos_file):
        with open(todos_file, 'r') as f:
            todos = json.load(f)
    
    todos.append(todo)
    
    with open(todos_file, 'w') as f:
        json.dump(todos, f, indent=2)
    
    return f"Created todo: '{task}' with priority '{priority}'"

@mcp.tool()
def list_todos() -> str:
    """List all current todos."""
    todos_file = "todos.json"
    if not os.path.exists(todos_file):
        return "No todos found. Create one with create_todo!"
    
    with open(todos_file, 'r') as f:
        todos = json.load(f)
    
    if not todos:
        return "No todos found. Create one with create_todo!"
    
    result = "Current todos:\n"
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo["completed"] else "⏳"
        result += f"{i}. {status} {todo['task']} (Priority: {todo['priority']})\n"
    
    return result

@mcp.tool()
def complete_todo(todo_number: int) -> str:
    """Mark a todo as completed."""
    todos_file = "todos.json"
    if not os.path.exists(todos_file):
        return "No todos found."
    
    with open(todos_file, 'r') as f:
        todos = json.load(f)
    
    if todo_number < 1 or todo_number > len(todos):
        return f"Invalid todo number. Please choose 1-{len(todos)}"
    
    todos[todo_number - 1]["completed"] = True
    
    with open(todos_file, 'w') as f:
        json.dump(todos, f, indent=2)
    
    return f"Completed todo: '{todos[todo_number - 1]['task']}'"

# 2. RESOURCES - Data that can be accessed
@mcp.resource("file://todos")
def get_todos_data() -> str:
    """Get raw todos data as JSON."""
    todos_file = "todos.json"
    if not os.path.exists(todos_file):
        return json.dumps([])
    
    with open(todos_file, 'r') as f:
        return json.dumps(json.load(f), indent=2)

@mcp.resource("file://config")
def get_assistant_config() -> str:
    """Get assistant configuration."""
    config = {
        "name": "Personal Assistant",
        "version": "1.0",
        "features": ["weather", "todos", "notes"],
        "last_updated": datetime.now().isoformat()
    }
    return json.dumps(config, indent=2)

# 3. PROMPTS - Templates for AI interactions
@mcp.prompt("todo_summary")
def todo_summary_prompt() -> str:
    """Generate a prompt for summarizing todos."""
    return """Please analyze the current todos and provide:
1. A summary of pending tasks
2. Priority recommendations
3. Suggested next actions
Use the list_todos tool to get current data."""

@mcp.prompt("weather_planning")
def weather_planning_prompt(city: str) -> str:
    """Generate a prompt for weather-based planning."""
    return f"""Based on the weather in {city}, help me plan my day:
1. What activities would be good for this weather?
2. Any clothing recommendations?
3. Should I plan indoor or outdoor activities?
Use the get_weather tool to get current conditions."""

if __name__ == "__main__":
    print("🚀 Starting Personal Assistant MCP Server...")
    print("📋 Available tools: get_weather, create_todo, list_todos, complete_todo")
    print("📁 Available resources: file://todos, file://config")
    print("💬 Available prompts: todo_summary, weather_planning")
    print("\n" + "="*50)
    
    # Run the server
    mcp.run()
