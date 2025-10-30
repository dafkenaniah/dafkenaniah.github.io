# Universal GitHub Setup Prompt

Use this prompt in any workspace to automatically initialize git, create a GitHub repository, and push your code:

---

## Prompt:

```
Create a private GitHub repository for this project and push all files to it. Follow these steps:

1. **Initialize Git Repository:**
   - Run `git init` if not already a git repository
   - Add all files with `git add .`
   - Create initial commit with a descriptive message

2. **Create GitHub Repository Setup Script:**
   - Create a Python script that uses the GitHub API to create a private repository
   - The script should:
     - Use my GitHub username: dafkenaniah
     - Create a private repository with the current directory name
     - Handle cases where repository already exists
     - Set up git remote origin
     - Push the code to GitHub
   - Include error handling for token permissions

3. **Execute the Process:**
   - Run the script to create the repository and push
   - If API fails, provide manual instructions
   - Ensure all files are successfully uploaded

4. **Provide Results:**
   - Confirm repository URL
   - List what files were uploaded
   - Verify the repository is private

The GitHub token should be requested during execution, not hardcoded in files that get committed.
```

---

## Alternative Short Version:

```
Set up this project on GitHub: initialize git if needed, create a private repository under dafkenaniah, and push all files. Create automation scripts to handle the GitHub API calls and provide the final repository URL.
```

---

## What This Accomplishes:

- ✅ Works in any directory/workspace
- ✅ Handles git initialization automatically  
- ✅ Creates private GitHub repositories
- ✅ Pushes all project files
- ✅ Provides automation scripts for future use
- ✅ Includes error handling and fallback options
- ✅ Results in a clean, organized GitHub repository

Save this prompt and use it in any workspace where you want to quickly set up GitHub integration!
