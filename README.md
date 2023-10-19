# Chime In

<!--toc:start-->

- [Build guide](#build-guide)
  - [Environment Setup](#environment-setup)
    - [Python Environment](#python-environment)
    - [Database Variables](#database-variables)
    - [Node Requirements](#node-requirements)
  - [Build Instructions](#build-instructions)

<!--toc:end-->

# Build guide

Please follow these instructions to run the project.

## Environment Setup

### Python Environment

Our project relies on different python libraries in order for it to
function. To make setup easier, we have included an [`environment.yaml`](https://github.com/lucashicks1/lambda-deco3801/blob/main/environment.yaml)
file. This will allow you to create your own miniconda virtual
environment. We recommend you look into [their installation instructions](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html).

You can create and activate this environment with the following:

```sh
conda env create -f environment.yaml
conda activate lambda-env
```

Or you can create your own environment and install the packages with your
preferred python venv manager by installing the following libraries:

```
numpy >= 1.26.0
pillow >= 10.0.1
pytesseract >= 0.3.10
matplotlib >= 3.7.2
pymongo >= 4.5.0
requests >= 2.31.0
fastapi >= 0.103.2
pydantic >= 2.4.2
uvicorn-standard >= 0.23.2
opencv-python-headless >= 4.8.1.78
```

### Database Variables

To then connect to the database you will need to set the environment variables for
the username and password as

```sh
export DB_USER=<database-username>
export DB_PASS=<database-password>
```

> [!NOTE]
> If you need access to the server that we are using please message Lucas Hicks

### Node Requirements

We recommend you install [Node Version Manager(NVM)](https://github.com/nvm-sh/nvm)
to maintain a correct node version. Once NVM is installed we can then run

```sh
nvm install latest
nvm use latest
```

If you don't wish to use NVM then use your chosen package manager to install [Node Latest](https://nodejs.org/en/download).

Then we can install our node packages with:

```
npm install react --save
npm install -g serve
```

This will install all of our node requirements so that you can run the display app.

## Build Instructions

Due to the number of components in this project. It is best to go to the individual
READMEs for each component individual component. For your convenience we have listed
these below:

- [Database Handler](./db-handler/README.md)
- [Image Recognition](./vision/README.md)
- [Display](./ui-display/frontend-app/README.md)
- [Microcontroller](./microcontroller/README.md)
- [Microcontroller Communication](./figurines/README.md)

> [!IMPORTANT]
> If any further details are required, please contact a member of Team \\Lambda
