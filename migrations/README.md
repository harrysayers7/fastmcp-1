# Database Migrations

This directory contains all database migration files for the GitOps + Supabase MCP project.

## 📁 Structure

```
migrations/
├── README.md              # This file
├── 001_initial_schema.sql # Initial database schema
├── 002_add_users.sql      # Example: Add users table
└── 003_add_posts.sql      # Example: Add posts table
```

## 🔧 Migration Guidelines

### File Naming Convention
- Use sequential numbers: `001_`, `002_`, `003_`, etc.
- Use descriptive names: `add_users_table`, `update_posts_schema`
- Use snake_case: `add_user_authentication.sql`

### Migration Template
```sql
-- Migration: [Brief description of what this migration does]
-- Created: [Date]
-- Author: [Your name]
-- 
-- Description: [Detailed description of the changes]

-- Forward migration
[Your SQL changes here]

-- Rollback (if applicable)
-- ROLLBACK: [SQL to undo the changes]
```

### Best Practices

#### ✅ DO
- **Test migrations locally** before committing
- **Include rollback instructions** in comments
- **Use transactions** for complex changes
- **Add indexes** for performance
- **Update documentation** after schema changes

#### ❌ DON'T
- **Never drop tables** without careful consideration
- **Don't modify existing data** without backup
- **Don't commit sensitive data** (passwords, keys)
- **Don't skip testing** on staging first

### Example Migration

```sql
-- Migration: Add users table with authentication
-- Created: 2024-01-15
-- Author: Harry Sayers
-- 
-- Description: Creates the initial users table with email, password hash, and timestamps

-- Forward migration
CREATE TABLE users (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Add indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);

-- Add RLS (Row Level Security)
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Create policy for users to see only their own data
CREATE POLICY "Users can view own profile" ON users
  FOR SELECT USING (auth.uid() = id);

-- Rollback
-- ROLLBACK: 
-- DROP TABLE users;
```

## 🚀 Applying Migrations

### Local Development
```bash
# Apply all pending migrations
supabase db push

# Apply specific migration
supabase db push --file migrations/001_initial_schema.sql
```

### Staging/Production
Migrations are automatically applied through GitHub Actions when:
- Pull requests are merged to `main`
- Direct pushes to `main` (for hotfixes)

## 🔍 Migration Status

| Migration | Status | Applied | Description |
|-----------|--------|---------|-------------|
| 001_initial_schema.sql | ✅ Ready | - | Initial database schema |
| 002_add_users.sql | 📝 Draft | - | Add users table |
| 003_add_posts.sql | 📝 Draft | - | Add posts table |

## 🛡️ Security Notes

- **Never commit real passwords** or API keys
- **Use environment variables** for sensitive data
- **Test rollbacks** before applying to production
- **Review all migrations** before merging

## 📚 Related Documentation

- [Supabase Migration Guide](https://supabase.com/docs/guides/database/migrations)
- [GitOps Workflow](docs/gitops.md)
- [Security Best Practices](docs/security.md)
