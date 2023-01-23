from git import Repo

repo_dir = 'myproject'

repo = Repo(repo_dir)

print("Untracked files:", repo.untracked_files, '\n')  # Get list of untracked files

print("Branches:")
for branch in repo.branches:  # Iterate over branch objects
    print(branch.name, branch.path)
print()

print(repo.is_dirty(), '\n')  # Are there any changed files?

print(repo.remotes)  # Get list of remotes
