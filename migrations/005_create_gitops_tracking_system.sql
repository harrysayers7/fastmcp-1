-- Migration: Create GitOps Operations Tracking System
-- Created: 2024-01-15
-- Author: Harry Sayers
-- 
-- Description: Creates comprehensive tracking system for all GitOps operations
-- including migrations, deployments, rollbacks, and system changes

-- Create GitOps operations tracking table
CREATE TABLE IF NOT EXISTS gitops_operations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  operation_type VARCHAR(50) NOT NULL CHECK (operation_type IN (
    'schema_change', 'data_migration', 'rollback', 'deployment', 
    'rollback', 'security_audit', 'documentation_update', 'test_run'
  )),
  description TEXT NOT NULL,
  migration_file VARCHAR(255),
  status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN (
    'pending', 'in_progress', 'success', 'failed', 'rolled_back', 'cancelled'
  )),
  performed_by VARCHAR(100),
  started_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  completed_at TIMESTAMP WITH TIME ZONE,
  rollback_available BOOLEAN DEFAULT false,
  rollback_reason TEXT,
  error_message TEXT,
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create Git commits tracking table
CREATE TABLE IF NOT EXISTS git_commits (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  commit_hash VARCHAR(40) NOT NULL UNIQUE,
  commit_message TEXT NOT NULL,
  author_name VARCHAR(255),
  author_email VARCHAR(255),
  committed_at TIMESTAMP WITH TIME ZONE,
  files_changed TEXT[],
  lines_added INTEGER DEFAULT 0,
  lines_deleted INTEGER DEFAULT 0,
  gitops_operation_id UUID REFERENCES gitops_operations(id),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create deployment tracking table
CREATE TABLE IF NOT EXISTS deployments (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  deployment_name VARCHAR(255) NOT NULL,
  environment VARCHAR(50) NOT NULL CHECK (environment IN ('dev', 'staging', 'production')),
  gitops_operation_id UUID REFERENCES gitops_operations(id),
  status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN (
    'pending', 'deploying', 'success', 'failed', 'rolled_back'
  )),
  deployed_at TIMESTAMP WITH TIME ZONE,
  deployed_by VARCHAR(100),
  deployment_duration_seconds INTEGER,
  rollback_available BOOLEAN DEFAULT false,
  rollback_performed_at TIMESTAMP WITH TIME ZONE,
  deployment_logs TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create system health tracking table
CREATE TABLE IF NOT EXISTS system_health_checks (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  check_type VARCHAR(100) NOT NULL,
  service_name VARCHAR(100) NOT NULL,
  status VARCHAR(20) NOT NULL CHECK (status IN ('healthy', 'warning', 'critical', 'unknown')),
  response_time_ms INTEGER,
  error_message TEXT,
  metadata JSONB DEFAULT '{}',
  checked_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_gitops_operations_type ON gitops_operations(operation_type);
CREATE INDEX IF NOT EXISTS idx_gitops_operations_status ON gitops_operations(status);
CREATE INDEX IF NOT EXISTS idx_gitops_operations_started_at ON gitops_operations(started_at);
CREATE INDEX IF NOT EXISTS idx_git_commits_hash ON git_commits(commit_hash);
CREATE INDEX IF NOT EXISTS idx_git_commits_committed_at ON git_commits(committed_at);
CREATE INDEX IF NOT EXISTS idx_deployments_environment ON deployments(environment);
CREATE INDEX IF NOT EXISTS idx_deployments_status ON deployments(status);
CREATE INDEX IF NOT EXISTS idx_system_health_checked_at ON system_health_checks(checked_at);

-- Enable RLS on all tables
ALTER TABLE gitops_operations ENABLE ROW LEVEL SECURITY;
ALTER TABLE git_commits ENABLE ROW LEVEL SECURITY;
ALTER TABLE deployments ENABLE ROW LEVEL SECURITY;
ALTER TABLE system_health_checks ENABLE ROW LEVEL SECURITY;

-- Create RLS policies (permissive for demo)
CREATE POLICY "Allow all operations on gitops_operations" ON gitops_operations FOR ALL USING (true);
CREATE POLICY "Allow all operations on git_commits" ON git_commits FOR ALL USING (true);
CREATE POLICY "Allow all operations on deployments" ON deployments FOR ALL USING (true);
CREATE POLICY "Allow all operations on system_health_checks" ON system_health_checks FOR ALL USING (true);

-- Create updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for updated_at
CREATE TRIGGER update_gitops_operations_updated_at 
    BEFORE UPDATE ON gitops_operations 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ROLLBACK:
-- DROP TABLE IF EXISTS system_health_checks CASCADE;
-- DROP TABLE IF EXISTS deployments CASCADE;
-- DROP TABLE IF EXISTS git_commits CASCADE;
-- DROP TABLE IF EXISTS gitops_operations CASCADE;
-- DROP FUNCTION IF EXISTS update_updated_at_column() CASCADE;
