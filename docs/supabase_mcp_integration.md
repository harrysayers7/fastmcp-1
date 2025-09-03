# Supabase MCP Integration Guide

This guide shows you how to use your existing Supabase MCP tools with the GitOps workflow we've set up.

## 🎯 What You Already Have

### ✅ **Active Supabase Projects**
- **SSoT1** (`zeopoimfsxdidkyiucsr`) - ACTIVE_HEALTHY
- **SSoT** (`hzttajuyxmjteyvyzlxs`) - ACTIVE_HEALTHY

### ✅ **Rich Database Schema**
Your projects already contain a sophisticated project management system:
- **9 tables** with full RLS (Row Level Security)
- **Multi-environment support** (dev, staging, prod)
- **Infrastructure management** capabilities
- **API key management** with scoping

## 🚀 How to Use Supabase MCP with GitOps

### **1. Direct Database Operations**

You can now perform database operations through natural language:

```bash
# Check project status
"Show me the status of my SSoT1 project"

# List all tables
"List all tables in my active Supabase project"

# Query data
"Show me all projects created in the last month"

# Check security
"Audit the RLS policies on all my tables"
```

### **2. Schema Management**

```bash
# Generate migration from current schema
"Create a migration file from my current database schema"

# Validate migration safety
"Check if this migration is safe to apply"

# Apply migrations
"Apply the latest migration to my staging environment"
```

### **3. Documentation Generation**

```bash
# Auto-generate docs
"Generate documentation for my database schema"

# Update API types
"Generate TypeScript types for my Supabase project"

# Create API documentation
"Create API documentation for my database tables"
```

## 🔄 **GitOps Workflow Integration**

### **Step 1: Schema Changes**
1. Make changes in Supabase Dashboard or via MCP
2. Generate migration file: `"Create migration from current schema"`
3. Review and commit migration to Git
4. Create PR for review

### **Step 2: Automated Testing**
- GitHub Actions validates migration syntax
- Security audit runs automatically
- Schema documentation updates
- TypeScript types regenerate

### **Step 3: Deployment**
- PR approved → Auto-deploy to staging
- Test in staging environment
- Merge to main → Auto-deploy to production

## 🛡️ **Security Best Practices**

### **What's Already Secure**
✅ **RLS Enabled**: All 9 tables have Row Level Security  
✅ **UUID Primary Keys**: Secure, non-sequential IDs  
✅ **Foreign Key Constraints**: Proper referential integrity  
✅ **API Key Management**: Scoped and expiring keys  

### **Additional Recommendations**
- Review RLS policies for each table
- Enable audit logging for sensitive operations
- Regular security audits via MCP
- Monitor API key usage and rotation

## 📊 **Your Current Schema Overview**

### **Core Tables**
- `projects` - Main project entities (3 rows)
- `project_members` - User membership and roles (3 rows)
- `environments` - Environment definitions (9 rows)

### **Infrastructure Tables**
- `infra_servers` - Server configurations (1 row)
- `infra_services` - Service definitions (1 row)
- `infra_credentials` - Credential management (1 row)

### **Data Tables**
- `items` - Generic data items (1 row)
- `env_vars_map` - Environment variable mappings (1 row)
- `inbound_api_keys` - API key management (1 row)

## 🎮 **Try It Now**

### **Quick Commands to Test**

1. **Check Project Status**
   ```
   "What's the status of my SSoT1 Supabase project?"
   ```

2. **List Tables**
   ```
   "Show me all tables in my active Supabase project"
   ```

3. **Generate Migration**
   ```
   "Create a migration file from my current schema"
   ```

4. **Security Audit**
   ```
   "Check the security policies on my database tables"
   ```

5. **Generate Documentation**
   ```
   "Generate documentation for my database schema"
   ```

## 🔧 **Configuration Files**

### **supabase_config.json**
Contains your project configurations and GitOps settings.

### **Migration Files**
Located in `migrations/` directory with versioned SQL files.

### **Documentation**
Auto-generated in `docs/schema/` directory.

## 🚨 **Important Notes**

### **Data Safety**
- ⚠️ **Never sync production data to Git**
- ✅ **Only sync schema and migration files**
- ✅ **Use summaries and metadata only**

### **Secrets Management**
- 🔐 **Store API keys in environment variables**
- 🔐 **Use GitHub Secrets for CI/CD**
- 🔐 **Rotate keys regularly**

### **Migration Safety**
- 📝 **Always test migrations in staging first**
- 📝 **Include rollback procedures**
- 📝 **Keep migrations small and focused**

## 🎉 **What This Enables**

### **For Development**
- Natural language database operations
- Automated schema documentation
- Version-controlled database changes
- Automated testing and validation

### **For Operations**
- Real-time database monitoring
- Automated security audits
- Performance optimization suggestions
- Backup and recovery procedures

### **For Teams**
- Collaborative schema management
- Code review for database changes
- Automated deployment pipelines
- Comprehensive audit trails

## 🚀 **Next Steps**

1. **Test the Integration**
   ```bash
   python scripts/supabase_mcp_demo.py
   ```

2. **Make Your First Change**
   - Use Supabase MCP to modify a table
   - Generate migration file
   - Commit to Git
   - Create PR

3. **Set Up Monitoring**
   - Configure alerts for schema changes
   - Set up performance monitoring
   - Enable audit logging

4. **Expand the Workflow**
   - Add more Supabase projects
   - Create custom MCP tools
   - Integrate with other services

---

**You now have a powerful GitOps + Supabase MCP integration that combines the best of both worlds: the flexibility of natural language database operations with the safety and auditability of Git-based workflows!** 🎉
