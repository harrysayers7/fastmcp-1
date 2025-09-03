# Setup Guide: GitOps + Supabase MCP Integration

This guide will walk you through setting up the complete GitOps + Supabase MCP integration for your project.

## 🎯 Overview

By the end of this setup, you'll have:
- ✅ **GitOps Workflow**: Database changes managed through Git
- ✅ **Supabase Integration**: Real-time database operations
- ✅ **Security**: Secure credential management
- ✅ **Automation**: Automated testing and deployment
- ✅ **Documentation**: Auto-generated API docs

## 📋 Prerequisites

Before starting, ensure you have:

- [ ] **Node.js 18+** installed
- [ ] **Python 3.10+** installed
- [ ] **Git** configured with your GitHub account
- [ ] **Supabase account** (free tier is fine)
- [ ] **GitHub account** with repository access

## 🚀 Step 1: Repository Setup

### 1.1 Clone the Repository
```bash
git clone https://github.com/harrysayers7/fastmcp-1.git
cd fastmcp-1
```

### 1.2 Install Dependencies
```bash
# Install Node.js dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt

# Install Supabase CLI
npm install -g @supabase/cli
```

## 🔧 Step 2: Environment Configuration

### 2.1 Create Environment File
```bash
cp .env.example .env
```

### 2.2 Configure Environment Variables
Edit `.env` with your credentials:

```bash
# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key

# GitHub Configuration
GITHUB_TOKEN=your_github_personal_access_token

# MCP Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 2.3 Get Supabase Credentials

1. **Go to your Supabase Dashboard**
   - Visit [supabase.com/dashboard](https://supabase.com/dashboard)
   - Create a new project or select existing one

2. **Get Project URL and Keys**
   - Go to Settings → API
   - Copy the Project URL
   - Copy the anon/public key
   - Copy the service_role key (keep this secret!)

3. **Update your .env file** with these values

## 🗄️ Step 3: Supabase Setup

### 3.1 Initialize Supabase Project
```bash
# Login to Supabase
supabase login

# Link to your project
supabase link --project-ref your_project_ref

# Pull the current schema
supabase db pull
```

### 3.2 Apply Initial Migrations
```bash
# Apply the initial schema
supabase db push

# Verify the schema was applied
supabase db diff
```

### 3.3 Set Up Row Level Security (RLS)
```bash
# Enable RLS on all tables
supabase db push

# Verify RLS is enabled
supabase db diff
```

## 🔐 Step 4: Security Configuration

### 4.1 GitHub Secrets Setup

1. **Go to your GitHub repository**
   - Visit your repository on GitHub
   - Go to Settings → Secrets and variables → Actions

2. **Add the following secrets:**
   ```
   STAGING_SUPABASE_URL=your_staging_supabase_url
   STAGING_SUPABASE_SERVICE_KEY=your_staging_service_key
   PROD_SUPABASE_URL=your_production_supabase_url
   PROD_SUPABASE_SERVICE_KEY=your_production_service_key
   ```

### 4.2 Verify Security Setup
```bash
# Run security audit
npm run security:audit

# Check for hardcoded secrets
npm run security:check
```

## 🤖 Step 5: MCP Configuration

### 5.1 Cursor MCP Setup

Your `.cursor/mcp.json` should already be configured. Verify it contains:

```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": [
        "-y",
        "@supabase/mcp-server-supabase@latest",
        "--read-only",
        "--project-ref=your_project_ref"
      ],
      "env": {
        "SUPABASE_ACCESS_TOKEN": "your_supabase_access_token"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_github_token"
      }
    }
  }
}
```

### 5.2 Test MCP Connections
```bash
# Test Supabase MCP
npm run test:supabase-mcp

# Test GitHub MCP
npm run test:github-mcp
```

## 🔄 Step 6: GitOps Workflow Setup

### 6.1 Create Your First Migration
```bash
# Create a new migration
touch migrations/002_add_sample_data.sql
```

Add content to the migration:
```sql
-- Migration: Add sample data
-- Created: 2024-01-15
-- Author: Your Name

-- Add sample users
INSERT INTO users (email, password_hash, first_name, last_name) VALUES
  ('admin@example.com', crypt('password123', gen_salt('bf')), 'Admin', 'User'),
  ('user@example.com', crypt('password123', gen_salt('bf')), 'Regular', 'User');

-- Add sample posts
INSERT INTO posts (user_id, title, content, slug, status) VALUES
  ((SELECT id FROM users WHERE email = 'admin@example.com'), 
   'Welcome to FastMCP', 
   'This is a sample post created during setup.', 
   'welcome-to-fastmcp', 
   'published');

-- Rollback
-- ROLLBACK: 
-- DELETE FROM posts WHERE slug = 'welcome-to-fastmcp';
-- DELETE FROM users WHERE email IN ('admin@example.com', 'user@example.com');
```

### 6.2 Test the Migration
```bash
# Apply the migration locally
supabase db push

# Verify the data was added
supabase db diff
```

### 6.3 Commit and Push
```bash
git add migrations/002_add_sample_data.sql
git commit -m "Add sample data migration"
git push origin main
```

## 🧪 Step 7: Testing the Setup

### 7.1 Test Database Operations
```bash
# Test database connection
npm run test:db-connection

# Test migration system
npm run test:migrations

# Test RLS policies
npm run test:rls
```

### 7.2 Test MCP Integration
```bash
# Test Supabase MCP tools
npm run test:supabase-tools

# Test GitHub MCP tools
npm run test:github-tools
```

### 7.3 Test GitOps Workflow
```bash
# Create a test migration
npm run create:migration "test_migration"

# Test the CI/CD pipeline
git add .
git commit -m "Test GitOps workflow"
git push origin main
```

## 📚 Step 8: Documentation Generation

### 8.1 Generate API Documentation
```bash
# Generate TypeScript types
npm run generate:types

# Generate API documentation
npm run generate:docs

# Update README
npm run update:readme
```

### 8.2 Verify Documentation
```bash
# Check generated files
ls -la docs/
ls -la src/types/

# Verify documentation is up-to-date
npm run docs:verify
```

## ✅ Step 9: Verification Checklist

Before considering your setup complete, verify:

- [ ] **Repository cloned** and dependencies installed
- [ ] **Environment variables** configured correctly
- [ ] **Supabase project** linked and accessible
- [ ] **Initial migrations** applied successfully
- [ ] **GitHub secrets** configured
- [ ] **MCP servers** responding correctly
- [ ] **GitOps workflow** tested
- [ ] **Documentation** generated and up-to-date
- [ ] **Security audit** passed
- [ ] **All tests** passing

## 🚨 Troubleshooting

### Common Issues

#### 1. Supabase Connection Issues
```bash
# Check your project URL and keys
supabase status

# Re-link your project
supabase link --project-ref your_project_ref
```

#### 2. MCP Server Issues
```bash
# Check MCP server logs
npm run logs:mcp

# Restart MCP servers
npm run restart:mcp
```

#### 3. Migration Issues
```bash
# Check migration status
supabase db diff

# Reset and reapply migrations
supabase db reset
supabase db push
```

#### 4. GitHub Actions Issues
- Check repository secrets are set correctly
- Verify GitHub token has necessary permissions
- Check Actions logs for specific error messages

## 🎉 Next Steps

Once your setup is complete, you can:

1. **Start developing** with the GitOps workflow
2. **Create new migrations** for database changes
3. **Use MCP tools** for database operations
4. **Automate documentation** updates
5. **Set up monitoring** and alerts

## 📖 Additional Resources

- [GitOps Workflow Guide](gitops.md)
- [Supabase Integration Guide](supabase.md)
- [Security Best Practices](security.md)
- [API Documentation](api.md)

## 🆘 Getting Help

If you encounter issues:

1. **Check the logs** for specific error messages
2. **Review the troubleshooting** section above
3. **Create an issue** on GitHub
4. **Join the discussion** in GitHub Discussions

---

**Congratulations!** 🎉 You now have a fully functional GitOps + Supabase MCP integration set up and ready for development!
