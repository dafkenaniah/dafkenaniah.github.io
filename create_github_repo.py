#!/usr/bin/env python3
"""
GitHub Repository Creation and Push Script
This script creates a private GitHub repository and pushes local git content to it.
"""

import os
import subprocess
import requests
import json
import getpass
from typing import Optional

class GitHubRepoCreator:
    def __init__(self):
        self.github_api_base = "https://api.github.com"
        self.username = "dafkenaniah"
        self.repo_name = "money"
        
    def get_github_token(self) -> str:
        """Get GitHub personal access token from user input."""
        print("To create a GitHub repository, you need a Personal Access Token.")
        print("Create one at: https://github.com/settings/tokens")
        print("Required scopes: 'repo' (for private repositories)")
        print()
        token = getpass.getpass("Enter your GitHub Personal Access Token: ")
        return token.strip()
    
    def create_repository(self, token: str) -> bool:
        """Create a private repository on GitHub."""
        url = f"{self.github_api_base}/user/repos"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        data = {
            "name": self.repo_name,
            "private": True,
            "description": "Money project with automation strategy documents",
            "auto_init": False  # Don't initialize with README since we have local content
        }
        
        print(f"Creating private repository '{self.repo_name}'...")
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print("✅ Repository created successfully!")
            return True
        elif response.status_code == 422:
            error_data = response.json()
            if "name already exists" in str(error_data):
                print(f"⚠️  Repository '{self.repo_name}' already exists.")
                return True  # Continue with push anyway
            else:
                print(f"❌ Error creating repository: {error_data}")
                return False
        else:
            print(f"❌ Error creating repository: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    
    def run_git_command(self, command: list) -> tuple[bool, str]:
        """Run a git command and return success status and output."""
        try:
            result = subprocess.run(command, 
                                  capture_output=True, 
                                  text=True, 
                                  check=True)
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            return False, f"Error: {e.stderr}"
    
    def check_git_status(self) -> bool:
        """Check if we're in a git repository and have commits."""
        success, output = self.run_git_command(["git", "status", "--porcelain"])
        if not success:
            print("❌ Not in a git repository or git not available")
            return False
        
        # Check if we have commits
        success, output = self.run_git_command(["git", "log", "--oneline", "-1"])
        if not success:
            print("❌ No commits found in repository")
            return False
        
        print("✅ Git repository ready with commits")
        return True
    
    def setup_remote_and_push(self) -> bool:
        """Set up remote origin and push to GitHub."""
        repo_url = f"https://github.com/{self.username}/{self.repo_name}.git"
        
        # Check if origin already exists
        success, output = self.run_git_command(["git", "remote", "get-url", "origin"])
        if success:
            print(f"✅ Remote 'origin' already set to: {output.strip()}")
        else:
            # Add remote origin
            print(f"Adding remote origin: {repo_url}")
            success, output = self.run_git_command(["git", "remote", "add", "origin", repo_url])
            if not success:
                print(f"❌ Failed to add remote: {output}")
                return False
            print("✅ Remote origin added")
        
        # Push to GitHub
        print("Pushing to GitHub...")
        success, output = self.run_git_command(["git", "push", "-u", "origin", "master"])
        if success:
            print("✅ Successfully pushed to GitHub!")
            print(f"🌐 Repository URL: https://github.com/{self.username}/{self.repo_name}")
            return True
        else:
            # Try with 'main' branch if 'master' fails
            print("Trying with 'main' branch...")
            success, output = self.run_git_command(["git", "push", "-u", "origin", "main"])
            if success:
                print("✅ Successfully pushed to GitHub!")
                print(f"🌐 Repository URL: https://github.com/{self.username}/{self.repo_name}")
                return True
            else:
                print(f"❌ Failed to push: {output}")
                return False
    
    def run(self):
        """Main execution flow."""
        print("🚀 GitHub Repository Creator")
        print("=" * 50)
        
        # Check git status
        if not self.check_git_status():
            return False
        
        # Get GitHub token
        token = self.get_github_token()
        if not token:
            print("❌ No token provided")
            return False
        
        # Create repository
        if not self.create_repository(token):
            return False
        
        # Push to GitHub
        if not self.setup_remote_and_push():
            return False
        
        print("\n🎉 All done! Your repository is now on GitHub.")
        return True

def main():
    creator = GitHubRepoCreator()
    success = creator.run()
    
    if success:
        print("\n✅ SUCCESS: Repository created and pushed to GitHub!")
    else:
        print("\n❌ FAILED: Could not complete the GitHub setup.")
        print("\nTroubleshooting:")
        print("1. Make sure you have a GitHub Personal Access Token with 'repo' scope")
        print("2. Ensure you're in the correct git repository directory")
        print("3. Check your internet connection")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
