#! /usr/bin/python3

from argparse import ArgumentParser
import os
import pathlib

template_path = '/'.join(pathlib.Path(__file__).parent.resolve().__str__().split('/')[0:-1]) + '/templates/'

FILES_AND_TEMPLATES = {
    "init_git.sh": template_path + 'init_git.sh',
    "README.md": template_path + 'README.md',
    "Dockerfile": template_path + 'python/Dockerfile',
    "Makefile": template_path + 'python/Makefile',
    "poetry.toml": template_path + 'python/poetry.toml',
    "pyproject.toml": template_path + 'python/pyproject.toml',
    "src/__init__.py": template_path + 'python/empty.py',
    "tests/__init__.py": template_path + 'python/empty.py',
    "tests/test_sample.py": template_path + 'python/test_sample.py',
    "bin/placeholder.py": template_path + 'python/empty.py',
    ".env/env": template_path + 'python/env',
    ".env/test": template_path + 'python/env',
    ".gitignore": template_path + 'python/gitignore',
    ".circleci/config.yml": template_path + 'python/circleci_config.yml',
}


def create_docker_image(docker_image_name, root_directory="", username="user"):
    docker_image_directory = f"{root_directory}projects/{docker_image_name}"
    os.mkdir(docker_image_directory)
    os.mkdir(f"{docker_image_directory}/src")
    os.mkdir(f"{docker_image_directory}/tests")
    os.mkdir(f"{docker_image_directory}/bin")
    os.mkdir(f"{docker_image_directory}/.env")
    os.mkdir(f"{docker_image_directory}/.circleci")

    for file_path, template_file in FILES_AND_TEMPLATES.items():
        with open(template_file, "r") as temp:
            file_contents = temp.read()
        replaced_file_contents = file_contents.replace("docker_image_name", docker_image_name).replace("username", username)

        docker_image_file_path = f"{docker_image_directory}/{file_path}"
        print(f"Creating {docker_image_file_path}...")
        with open(docker_image_file_path, "w+") as f:
            f.write(replaced_file_contents)

        if ".sh" in file_path:
            os.chmod(docker_image_file_path, 0o755)


def create_docker_image_if_nonexistent(docker_image_name, root_directory="", username="user"):
    project_directory = root_directory + "projects/"

    if not os.path.exists(project_directory):
        os.mkdir(project_directory)
    if not os.path.exists(project_directory + docker_image_name):
        print(f"Creating {docker_image_name} docker_image...")
        create_docker_image(docker_image_name, root_directory, username)
    else:
        print(f"The {docker_image_name} docker_image already exists at {project_directory}. Not creating...")


if __name__ == "__main__":
    parser = ArgumentParser(prog="Docker-ater")
    parser.add_argument(
        "--name",
        "-n",
        dest="name",
        required=True,
        help="The name of the docker project to create.",
    )
    parser.add_argument(
        "--root",
        "-r",
        dest="root_path",
        required=False,
        default="",
        help="Optional: Root path where your new docker project will be created.",
    )
    parser.add_argument(
        "--user",
        "-u",
        dest="username",
        required=False,
        default="",
        help="Optional: Username of the github repo owner / organization.",
    )
    args = parser.parse_args()
    if args.root_path:
        if args.root_path[-1] != "/":
            root_path = args.root_path + "/"
    else:
        root_path = pathlib.Path.home().__str__() + "/"

    create_docker_image_if_nonexistent(args.name, root_path, args.username)
