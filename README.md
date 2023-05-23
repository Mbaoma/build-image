# build-image-v1.0
my attempt at building a custom GitHub action that builds a Docker image

### Setup
- Create a virtual environment and install the requirements stored in the ```requirements.txt``` file.
```python
$ python -m venv venv
$ pip install -r requirements.txt
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
          dockerfile-path: 'Dockerfile'
          registry: ghcr.io
          registry-username: ${{ github.actor }}
          registry-password: ${{ secrets.GITHUB_TOKEN }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          tags: ${{ github.repository_owner }}/${{ github.repository }}:${{ github.sha }}
```

Notes
- Dockerfile has to be in the root directory
