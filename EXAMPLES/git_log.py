import os
from git import Git, Repo

repo_dir = 'myproject'

repo = Repo(repo_dir)

os.chdir(repo_dir)

g = Git(repo)
print(g.log())  # get log for entire repo
print('-' * 60)
print(g.log('unicode.py'))  # get log for specific file
print('-' * 60)
print(g.log('fizzbuzz1.py'))  # get log for specific file
