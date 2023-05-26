# build-image-v1.0
My attempt at building a custom GitHub action that builds a Docker image

# Pushing to GitHub
```bash
$ git add .
$ git commit -m 'commit-message'
$ git tag -a -m "Description of this release" v1
$ git push --follow-tags
```
- Delete a tag remotely
```bash
$ git push --delete origin v1.0
```

- Delete a tag locally
```bash
$ git tag --delete tagname
```

### Use
```Docker
name: Publish Docker image
 
on: [push]

jobs:
  push_to_registry:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Build and Push Docker Image
        uses: Mbaoma/build-image@v2.0
        with:
          image-name: ${{ github.repository }} 
          github_token: ${{ secrets.GITHUB_TOKEN }}

```

Notes
- Dockerfile has to be in the root directory
