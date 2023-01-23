from git import Repo

repo = Repo('myproject')

for tag in repo.tags:  # Iterate over all tags for repo
    print(tag.name)
