# Custom Action to push Docker images to GitHub Container Registry
Whenever there's a push event or a release event in the repository, this action automatically pushes the Docker image to ghcr.io. No more manual hassle! 🚀💪

## 💡 Benefits:
✅ Streamlined workflow: Say goodbye to tedious configuration and manual image deployments.

✅ Increased efficiency: Focus on developing and let the CI/CD pipeline handle image distribution.

✅ Seamless integration: GitHub Container Registry simplifies container image management.

## 🛠️ How to Use
Set the following secrets in  your repository:
- ```registry-username```: The username for authentication to the container registry (defaults to the github.actor).
- ```docker_io_token```: Your ```docker.io``` token created via https://hub.docker.com/settings/security.

- Add this step to your workflow as follows:
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

## 🔖 Image Tags
Your image is automatically tagged based on the event behind the image creation.

### Image Tagging Scenario: On Push Event 🚀
Whenever a push event occurs in the repository, this workflow automatically assigns relevant tags to your image. The tags include the ```branch slug```, ```short SHA (commit identifier)```, and ```long SHA```, providing valuable context about the image's origin and version.

For example, let's consider a scenario where you have a GitHub repository for a web application called ```MyWebApp```. Whenever a developer pushes changes to the ```develop``` branch, the workflow automatically tags the image with the following details:

```bash
Branch Slug: develop
Short SHA: abcdefg
Long SHA: abcdefghijklmnopqrstuvwxyz
```

### Image Tagging Scenario: On Release Event 🚀
Whenever a release event occurs in the repository, the action automatically assigns relevant tags to your image. The tags include the ```release version```, ```short SHA (commit identifier)```, and ```long SHA```, providing valuable context about the image's origin and version.

For example, let's consider a scenario where you have a GitHub repository for a web application called ```MyWebApp```. Whenever a developer creates a new release with version ```v1.0```, the action automatically tags the image with the following details:

```bash
Release Version: v1.0
Short SHA: abcdefg
Long SHA: abcdefghijklmnopqrstuvwxyz
```

These automated tagging processes ensures that you can easily track and identify specific versions of your application, streamlining your development and deployment workflows.

## 🏳️ Defaults
- Your ```Dockerfile``` has to be in the root directory.
- Your ```docker image``` is named after your repository.