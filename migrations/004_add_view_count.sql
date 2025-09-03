-- Migration: Add view_count column to blog_posts
-- Created: 2024-01-15
-- Author: Harry Sayers
-- 
-- Description: Adds a view_count column to track how many times each blog post has been viewed

-- Add view_count column to blog_posts table
ALTER TABLE gitops_demo.blog_posts 
ADD COLUMN IF NOT EXISTS view_count INTEGER DEFAULT 0;

-- Create index for performance on view_count queries
CREATE INDEX IF NOT EXISTS idx_blog_posts_view_count 
ON gitops_demo.blog_posts(view_count DESC);

-- Add comment to document the column
COMMENT ON COLUMN gitops_demo.blog_posts.view_count IS 'Number of times this blog post has been viewed';

-- ROLLBACK:
-- ALTER TABLE gitops_demo.blog_posts DROP COLUMN IF EXISTS view_count;
-- DROP INDEX IF EXISTS idx_blog_posts_view_count;
