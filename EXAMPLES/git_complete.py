import os
import shutil
from git import Git, Repo

repo_dir = 'newproject'

r = Repo.init(repo_dir)  # Create new empty repo
os.chdir(repo_dir)

file_to_add = 'creating_dicts.py'
g = Git(r)  # Create Git() object from repo
shutil.copy('../' + file_to_add, ".")  # Copy file to add (typically created with IDE, so no need to copy)

g.add(file_to_add)  # Stage file for commit
g.commit(file_to_add, message="initial commit")  # Commit file
print(g.log())  # Show repo log
