# What is this? #

You can use this repo to create new python projects.  Whether it's a new docker image that you intend to have run in google cloud run / fargate, or a google cloud function / aws lambda, this can help you spin it up!

This has been tested in gcp with circleci.  In the future, we can make it cloud agnostic and also set up the deployment process with github actions instead.  These can be substituted via an arg.  For now, you might need to customize your deployment process.  Essentially this assumes that you have a dev/stg/prd type of setup with docker artifact registries in each and that you push locally to the dev one and have some automation bring it to the stg one and then approve that before it goes to prd.

# Usage #

## To begin with a new project: ##

```
./bin/create_project.py --name <project_name> --username <your gh username>
```

This will create a new directory called `projects` in your home directory (usually /Users/<login_name>) with the name of your project. 
You can create the `projects` folder in a different root directory if you want by passing a valid directory with argument `--root`. The directory you specify must exist. See example below:
```
./bin/create_project.py --name <project_name> --username <your gh username> --root /Users/loginname/repos/
```

The resulting directory will contain a skeleton of several files:
- A Makefile to help you build and deploy.  Make options are available with `make help`.
- A `Dockerfile`.  The `Dockerfile` will contain the base image (which can be changed according to your requirements). You can also add additional dependencies to the `Dockerfile` if needed. 
- A poetry `pyproject.toml` that will contain the python packages that will be installed in the image.  You can add additional python packages to this file.  
- A script, `init_git.sh`, that you can run from within your project's directory to publish the package to a new GitHub repo.

Once your skeleton project is created, `cd` into the project folder and run the `init_git.sh` script to create a corresponding repository in GitHub. 
You can delete the `init.git.sh` script once this step has been completed successfully. You will need to enter permissions for team collaborators to the repository in GitHub.
For example:
```
cd /Users/<login_name>/project/my_project
./init_git.sh
```
Note: If you didn't provide a username arg when creating the project, you will need to replace `user` in the script with your username before running this.

## To modify a project: ##

Code should go in `src`.  This code can be called from a dag which references the resulting image, or from inside of a cloud function.
Tests should go in `tests`.  These tests can be run using `make test`.
If you have trouble with this, you might not have the correct packages installed: Use:
```
pip install pytest
pip install pytest-cov
pip install python-dotenv
```

## To build a project: ##

```
cd docker/projects/<project_name> # Go to the project directory
make install  # This will use poetry to install the python packages and output a requirements.txt file
make docker-build  # This will build the docker image
```

## To deploy a project: ##

In progress!
```
