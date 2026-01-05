#!/usr/bin/env python3
"""
Git Synchronization Automation
Automatically syncs repository with GitHub

Usage:
    python git_sync.py
    python git_sync.py --push
    python git_sync.py --auto-commit
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime
import argparse

sys.path.insert(0, str(Path(__file__).parent.parent))
from manifest import PROJECT


class GitSync:
    """Handles Git operations"""
    
    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)
    
    def run_git(self, *args, capture=False):
        """Run git command"""
        cmd = ["git"] + list(args)
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=capture,
                text=True,
                check=True
            )
            return result if capture else True
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e}")
            return None if capture else False
    
    def status(self):
        """Get git status"""
        result = self.run_git("status", "--short", capture=True)
        if result:
            return result.stdout.strip()
        return None
    
    def has_changes(self):
        """Check if there are uncommitted changes"""
        status = self.status()
        return status and len(status) > 0
    
    def pull(self):
        """Pull latest changes"""
        print("📥 Pulling latest changes...")
        return self.run_git("pull", "origin", "main")
    
    def add_all(self):
        """Stage all changes"""
        print("📝 Staging changes...")
        return self.run_git("add", ".")
    
    def commit(self, message):
        """Commit changes"""
        print(f"💾 Committing: {message}")
        return self.run_git("commit", "-m", message)
    
    def push(self):
        """Push to remote"""
        print("📤 Pushing to GitHub...")
        return self.run_git("push", "origin", "main")
    
    def sync(self, auto_commit=False, push=False):
        """Sync repository"""
        print("="*60)
        print(f"  {PROJECT['name']} - Git Sync")
        print("="*60)
        
        # Pull first
        if not self.pull():
            print("⚠️  Pull failed, continuing...")
        
        # Check for changes
        if self.has_changes():
            print(f"\n📝 Changes detected:")
            print(self.status())
            print()
            
            if auto_commit:
                # Auto commit
                self.add_all()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.commit(f"Auto sync {timestamp}")
                
                if push:
                    self.push()
                    print("\n✅ Sync complete!\n")
                else:
                    print("\n✅ Changes committed (not pushed)\n")
            else:
                print("ℹ️  Use --auto-commit to commit changes")
        else:
            print("\n✅ Already up to date\n")


def main():
    """Main sync script"""
    parser = argparse.ArgumentParser(
        description="Sync Android Command Center with GitHub"
    )
    parser.add_argument(
        "--auto-commit",
        action="store_true",
        help="Automatically commit changes"
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push changes to GitHub"
    )
    
    args = parser.parse_args()
    
    syncer = GitSync()
    syncer.sync(auto_commit=args.auto_commit, push=args.push)


if __name__ == "__main__":
    main()
