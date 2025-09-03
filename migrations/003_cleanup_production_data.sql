-- Migration: Clean up existing production data to focus on GitOps system
-- Created: 2024-01-15
-- Author: Harry Sayers
-- 
-- Description: Removes existing project management system data from public schema
-- to create a clean database focused on GitOps + Supabase MCP integration
-- 
-- WARNING: This will delete all existing data in the public schema tables

-- Drop existing tables in public schema (in dependency order)
DROP TABLE IF EXISTS public.env_vars_map CASCADE;
DROP TABLE IF EXISTS public.infra_services CASCADE;
DROP TABLE IF EXISTS public.infra_credentials CASCADE;
DROP TABLE IF EXISTS public.inbound_api_keys CASCADE;
DROP TABLE IF EXISTS public.items CASCADE;
DROP TABLE IF EXISTS public.infrastructure_servers CASCADE;
DROP TABLE IF EXISTS public.environments CASCADE;
DROP TABLE IF EXISTS public.project_members CASCADE;
DROP TABLE IF EXISTS public.projects CASCADE;

-- Drop any existing functions that might be related
DROP FUNCTION IF EXISTS public.is_project_member CASCADE;

-- Drop any existing views
DROP VIEW IF EXISTS public.v_project_inventory CASCADE;

-- Clean up any remaining objects
DROP SCHEMA IF EXISTS public CASCADE;

-- Recreate the public schema
CREATE SCHEMA public;

-- Grant permissions
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

-- Add a comment to document the cleanup
COMMENT ON SCHEMA public IS 'Public schema cleaned for GitOps + Supabase MCP integration';

-- ROLLBACK: 
-- This migration cannot be easily rolled back as it deletes production data
-- If rollback is needed, restore from backup
