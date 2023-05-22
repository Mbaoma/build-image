import os
import subprocess
import json
from github import Github
from docker import APIClient

def build_and_push_docker_image(image_name, dockerfile_path, registry, username, password, tags):
    # Build the Docker image
    docker_client = APIClient(base_url='unix://var/run/docker.sock')
    build_logs = docker_client.build(path=os.getcwd(), dockerfile=dockerfile_path, tag=image_name)

    # Print the build logs
    for line in build_logs:
        build_output = json.loads(line.decode('utf-8'))
        if 'stream' in build_output:
            print(build_output['stream'], end='')

    # Push the Docker image to the container registry
    login_command = f'docker login {registry} -u {username} -p {password}'
    subprocess.run(login_command, shell=True, check=True)

    for tag in tags:
        image_with_tag = f'{image_name}:{tag}'
        push_command = f'docker push {registry}/{image_with_tag}'
        subprocess.run(push_command, shell=True, check=True)

def main():
    # Get the inputs from the workflow environment variables
    image_name = os.environ['INPUT_IMAGE_NAME']
    dockerfile_path = os.environ['INPUT_DOCKERFILE_PATH']
    registry = os.environ['INPUT_REGISTRY']
    username = os.environ['INPUT_REGISTRY_USERNAME']
    password = os.environ['INPUT_REGISTRY_PASSWORD']
    tags = os.environ['INPUT_TAGS'].split(',')

    # Authenticate with GitHub to access secrets
    token = os.environ['GITHUB_TOKEN']
    github = Github(token)
    repository = github.get_repo(os.environ['GITHUB_REPOSITORY'])

    # Authenticate with the container registry
    password = repository.get_secret(os.environ['INPUT_REGISTRY_PASSWORD']).value

    # Build and push the Docker image
    build_and_push_docker_image(image_name, dockerfile_path, registry, username, password, tags)

if __name__ == '__main__':
    main()