import os
from git import Git, Repo

repo_dir = 'myproject'

repo = Repo(repo_dir)

os.chdir(repo_dir)

Repo.clone_from(
    'https://github.com/jstrickler/myproject.git',
    '../TEMP/myprojectcopy'
)  # Clone existing repo to new repo

