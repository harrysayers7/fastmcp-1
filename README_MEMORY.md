# Memory Operations Makefile

The `Makefile.memory` provides easy commands for saving and managing information in your GitOps + Supabase MCP system using natural language memory operations.

## 🧠 What This Does

This Makefile helps you:
- **Save** important information to memory using Supabase MCP
- **Recall** saved information when needed
- **Search** through your stored memories
- **Manage** your memory system efficiently

## 🚀 Quick Start

### Save Everything at Once
```bash
make -f Makefile.memory quick-save
```
This saves all your important project information to memory in one go.

### Recall Information
```bash
make -f Makefile.memory quick-recall
```
This gives you the commands to recall all your saved information.

### Search Your Memories
```bash
make -f Makefile.memory quick-search
```
This gives you commands to search through your stored memories.

## 📋 Available Commands

### Save Operations
- `make -f Makefile.memory save-config` - Save system configuration
- `make -f Makefile.memory save-project` - Save project details
- `make -f Makefile.memory save-schema` - Save database schema
- `make -f Makefile.memory save-workflow` - Save GitOps workflow
- `make -f Makefile.memory save-commands` - Save useful commands

### Recall Operations
- `make -f Makefile.memory recall-project` - Recall project info
- `make -f Makefile.memory recall-schema` - Recall database schema
- `make -f Makefile.memory recall-workflow` - Recall GitOps workflow
- `make -f Makefile.memory recall-commands` - Recall useful commands

### Search Operations
- `make -f Makefile.memory search-gitops` - Search GitOps memories
- `make -f Makefile.memory search-supabase` - Search Supabase memories
- `make -f Makefile.memory search-project` - Search project memories

### Memory Management
- `make -f Makefile.memory list-memories` - List all saved memories
- `make -f Makefile.memory backup-memories` - Backup memories to file
- `make -f Makefile.memory restore-memories` - Restore from backup
- `make -f Makefile.memory clear-memories` - Clear all memories (DANGEROUS)

## 🎯 How to Use

### Step 1: Save Information
```bash
# Save everything at once
make -f Makefile.memory quick-save

# Or save specific categories
make -f Makefile.memory save-config
make -f Makefile.memory save-project
```

### Step 2: Use Supabase MCP
The Makefile shows you the exact natural language commands to use with Supabase MCP:

```bash
# Example from quick-save output:
"Save complete GitOps + Supabase MCP system information to memory"
```

### Step 3: Recall When Needed
```bash
# Get recall commands
make -f Makefile.memory quick-recall

# Then use the suggested commands with Supabase MCP:
"Recall project information for GitOps + Supabase MCP system"
```

## 🔍 Example Workflow

### Saving Your Project
```bash
# 1. Run the save command
make -f Makefile.memory quick-save

# 2. Copy the suggested command and use it with Supabase MCP:
"Save complete GitOps + Supabase MCP system information to memory"
```

### Recalling Information Later
```bash
# 1. Run the recall command
make -f Makefile.memory quick-recall

# 2. Use the suggested commands with Supabase MCP:
"Recall project information for GitOps + Supabase MCP system"
"What is the current project configuration?"
```

### Searching Your Memories
```bash
# 1. Run the search command
make -f Makefile.memory search-gitops

# 2. Use the suggested commands with Supabase MCP:
"Search for GitOps related information"
"Find memories about GitOps workflow"
```

## 📊 What Gets Saved

The memory system saves:

### System Configuration
- Project name and details
- Supabase project information
- Database connection details
- Environment settings

### Database Schema
- Table structures
- Schema organization
- Relationship information
- Index and constraint details

### GitOps Workflow
- Step-by-step processes
- Migration procedures
- Deployment workflows
- Rollback procedures

### Useful Commands
- Makefile commands
- Common operations
- Troubleshooting steps
- Best practices

## 🛡️ Safety Features

### Backup Before Clearing
```bash
# Always backup before clearing
make -f Makefile.memory backup-memories
make -f Makefile.memory clear-memories  # Only if you're sure!
```

### Confirmation Prompts
The `clear-memories` command asks for confirmation before proceeding.

## 🎉 Benefits

1. **Never Forget**: Important information is always saved
2. **Easy Recall**: Natural language queries to find information
3. **Organized**: Information is categorized and structured
4. **Searchable**: Find specific information quickly
5. **Backup Safe**: Can backup and restore memories
6. **Team Sharing**: Share knowledge across team members

## 🔧 Integration with Supabase MCP

This Makefile works perfectly with your Supabase MCP integration:

1. **Save**: Use the suggested natural language commands
2. **Store**: Information is stored in your Supabase database
3. **Recall**: Query your stored information naturally
4. **Search**: Find information using natural language
5. **Manage**: Organize and maintain your knowledge base

---

**Happy Memory Management! 🧠**

Use `make -f Makefile.memory help` to see all available commands.
