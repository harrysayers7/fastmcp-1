-- Migration: Create GitOps Demo Schema
-- Created: 2024-01-15
-- Author: Harry Sayers
-- 
-- Description: Creates a dedicated demo schema for GitOps + Supabase MCP integration
-- This schema demonstrates a blog system with authors, posts, and comments

-- Create demo schema
CREATE SCHEMA IF NOT EXISTS gitops_demo;

-- Create demo tables for GitOps workflow
CREATE TABLE IF NOT EXISTS gitops_demo.blog_posts (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  content TEXT,
  author_id UUID,
  status VARCHAR(50) DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
  tags TEXT[],
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS gitops_demo.authors (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  bio TEXT,
  avatar_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS gitops_demo.comments (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  post_id UUID NOT NULL REFERENCES gitops_demo.blog_posts(id) ON DELETE CASCADE,
  author_id UUID REFERENCES gitops_demo.authors(id) ON DELETE SET NULL,
  content TEXT NOT NULL,
  approved BOOLEAN DEFAULT false,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Add foreign key constraint
ALTER TABLE gitops_demo.blog_posts 
ADD CONSTRAINT fk_blog_posts_author 
FOREIGN KEY (author_id) REFERENCES gitops_demo.authors(id) ON DELETE SET NULL;

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_blog_posts_status ON gitops_demo.blog_posts(status);
CREATE INDEX IF NOT EXISTS idx_blog_posts_created_at ON gitops_demo.blog_posts(created_at);
CREATE INDEX IF NOT EXISTS idx_comments_post_id ON gitops_demo.comments(post_id);
CREATE INDEX IF NOT EXISTS idx_comments_approved ON gitops_demo.comments(approved);

-- Enable RLS on all tables
ALTER TABLE gitops_demo.blog_posts ENABLE ROW LEVEL SECURITY;
ALTER TABLE gitops_demo.authors ENABLE ROW LEVEL SECURITY;
ALTER TABLE gitops_demo.comments ENABLE ROW LEVEL SECURITY;

-- Create basic RLS policies (demo purposes - very permissive)
CREATE POLICY "Allow all operations on blog_posts" ON gitops_demo.blog_posts FOR ALL USING (true);
CREATE POLICY "Allow all operations on authors" ON gitops_demo.authors FOR ALL USING (true);
CREATE POLICY "Allow all operations on comments" ON gitops_demo.comments FOR ALL USING (true);

-- Create updated_at trigger function
CREATE OR REPLACE FUNCTION gitops_demo.update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for updated_at
CREATE TRIGGER update_blog_posts_updated_at 
    BEFORE UPDATE ON gitops_demo.blog_posts 
    FOR EACH ROW EXECUTE FUNCTION gitops_demo.update_updated_at_column();

CREATE TRIGGER update_authors_updated_at 
    BEFORE UPDATE ON gitops_demo.authors 
    FOR EACH ROW EXECUTE FUNCTION gitops_demo.update_updated_at_column();

CREATE TRIGGER update_comments_updated_at 
    BEFORE UPDATE ON gitops_demo.comments 
    FOR EACH ROW EXECUTE FUNCTION gitops_demo.update_updated_at_column();

-- ROLLBACK: 
-- DROP SCHEMA IF EXISTS gitops_demo CASCADE;
