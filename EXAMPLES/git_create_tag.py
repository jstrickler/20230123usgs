import os
from git import Repo

repo_dir = 'myproject'

repo = Repo(repo_dir)

repo.create_tag("v1.0.0", message="First Public Release") # Create tag with descriptive message

