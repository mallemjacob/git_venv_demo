# Create a new directory
mkdir my_app

# Change into the directory
cd my_app

# Initialize git
git init

# Check the git status 
git status

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Create a new empty file
touch app.py

# Add the files to staging area
git add app.py

# Save to git repository
git commit -m "Initialized git repository and Create virtual enviroment and created app.py file."

# amend the last commit
git commit --amend

# Add remote origin 
git remote add origin https://github.com/username/git_venv_demo.git

# Push the changes to the remote repository
git push -u origin main

# Create a new branch
git switch -c feature

# Change into a branch
git switch main

# Merge code from feature branch to main branch
git merge feature