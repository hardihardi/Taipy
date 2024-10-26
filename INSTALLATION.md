
# Installation:-

Welcome to the installation section of the Taipy web application builder! This section will
guide you through the seamless and straightforward process of setting up and deploying your
own powerful web applications.


!!! note "Installation for Contributing to Taipy"


If your goal is to look into the code, modify and improve it, go straight
to the [source installation] (#installing-for-development) section.

    If you aim to modify the Taipy source code or contribute to its development, please refer
    to the contributing page to get more information.


# Installing Taipy library:-

## Installing from PyPI:-

## Prerequisite:-


Before installing Taipy, ensure you have Python (**version 3.9 or later**) and
[pip](https://pip.pypa.io) installed on your system. If you don't have pip installed, you can
follow these steps to install it:


Run the command:-
```bash
pip install taipy
```

If you are running in a virtual environment, you will have to issue the command:-
```bash
pipenv install taipy
```

Alternatively, you can use `venv` to create a virtual environment:-
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

1. **[Python Installation Guide](http://docs.python-guide.org/en/latest/starting/installation/)**:
    Follow the installation guide to set up Python on your system.
    After the installation, you can open the Command Prompt and type `python --version` to check
    the installed Python version.

2. **[Installing pip](https://pip.pypa.io/en/latest/installation/)**: Pip is included by default
    if you use Python 3.4 or later. Otherwise, you can follow the official
    installation page of pip to install it. To verify the installation, type `pip --version` or
    `pip3 --version`.

Alternatively, if you are using a Conda environment, you can install pip using the following
command:
```console
conda install pip
```

## The latest stable release from Pypi:-

### Pip:-

The preferred method to install Taipy is by using **pip**. After downloading Taipy package
from **[PyPI repository](https://pypi.org/project/taipy/)** the following commands install
it in the Python environment with all its dependencies. Open your terminal or command prompt
and run the following command:
```console
pip install taipy
```

### Pipenv:-

If you are using a virtual environment with **[Pipenv](https://pipenv.pypa.io/en/latest/)**,
use the following command:
```console
pipenv install taipy
```

### Venv:-

Alternatively, you can use `venv` to create a virtual environment. Please run the following
commands replacing `<myenv>` (twice) with your desired environment name:
```console
python -m venv <myenv>
source myenv/bin/activate  # On Windows use `<myenv>\Scripts\activate`

pip install taipy
```

### Conda:-

If you prefer to work within a [Conda](https://docs.conda.io/projects/conda/en/latest/index.html)
environment, you can install Taipy using the following commands replacing `<myenv>` with your
desired environment name:
```console
conda create -n <myenv>
conda activate <myenv>
pip install taipy
```


## Installing a Specific Version from PyPI:-

To install a specific version of Taipy, use the following command:-
```bash
pip install taipy==<version>
```
Replace `<version>` with a specific version number of Taipy.
The list of all released Taipy versions can be found [here](https://pypi.org/project/taipy/#history).

## Installing from GitHub:-

The development version of Taipy is updated daily with changes from the Taipy R&D and external
contributors whom we praise for their input.

The development version of Taipy can be installed using *pip* and *git*:-

## A specific version from PyPI:-

### Pip:-

To install a specific version of Taipy, use the following command replacing `<version>` with a
specific version number of Taipy among the
**[list of all released Taipy versions](https://pypi.org/project/taipy/#history)**:
```console
pip install taipy==<version>
```


### Pipenv:-

If you are using a virtual environment with **[Pipenv](https://pipenv.pypa.io/en/latest/)**,
use the following command:
```console
pipenv install taipy==<version>
```


## Installing for development:-

If you need the source code for Taipy on your system so you can see how things are done or maybe
participate in the improvement of the packages, you can clone the GitHub repository:-

### Venv:-

Alternatively, you can use `venv` to create a virtual environment:
```console
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
pip install taipy==<version>
```


### Conda:-

If you prefer to work within a [Conda](https://docs.conda.io/projects/conda/en/latest/index.html)
environment, you can install Taipy using the following commands replacing `<myenv>` with your
desired environment name:
```console
conda create -n <myenv>
conda activate <myenv>
pip install taipy==<version>
```

## A development version from GitHub:-

### Building the JavaScript bundles:-

### Pip:-

The development version of Taipy is hosted on
**[GitHub repository](https://git@github.com/Avaiga/taipy)** using the `develop` branch. This
branch is updated daily with changes from the Taipy R&D team and external contributors whom we
praise for their input.


The development version of Taipy can be installed using **pip**. After downloading Taipy source
code from the **[GitHub repository](https://git@github.com/Avaiga/taipy)** the following commands
build the package, and install it in the Python environment with all its dependencies.


**There are two main JavaScript bundles that can be built:-**

- **Taipy GUI:-** All the graphical interfaces that Taipy GUI can generate are based on a set of
  generated files, including the web application and all the predefined visual elements.

- **Taipy:-** A set of visual elements dedicated to Scenario Management.

**Prerequisites:-** If you need to build the JavaScript bundle, you need to make sure that the
[Node.js](https://nodejs.org/) JavaScript runtime version 18 or above is installed on your
machine.<br/>
Note that Node.js comes with the [`npm` package manager](https://www.npmjs.com/) as part
of the standard installation.

Open your terminal or command prompt and run the following command:

```bash
pip install git+https://git@github.com/Avaiga/taipy
```


### Pipenv:-

If you are using a virtual environment with **[Pipenv](https://pipenv.pypa.io/en/latest/)**,
use the following command:
```console
pipenv install git+https://git@github.com/Avaiga/taipy
```


Here is the sequence of commands that can be issued to build both sets of files:-

### Venv:-

Alternatively, you can use `venv` to create a virtual environment:
```console
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
pip install git+https://git@github.com/Avaiga/taipy
```


### Conda:-

If you prefer to work within a [Conda](https://docs.conda.io/projects/conda/en/latest/index.html)
environment, you can install Taipy using the following commands replacing `<myenv>` with your
desired environment name:
```console
conda create -n <myenv>
conda activate <myenv>
pip install git+https://git@github.com/Avaiga/taipy
```

# Installing Taipy with Colab:-

### Debugging the JavaScript bundles:-

If you plan to modify the front-end code and need to debug the TypeScript
code, you must use the following:-
```bash
npm run build:dev
```

instead of the *standard* build option.

This will preserve the debugging symbols, and you will be able to navigate in the
TypeScript code from your debugger.

> **Note:-** Web application location
>
> When you are developing front-end code for the Taipy GUI package, it may
> be cumbersome to have to install the package over and over when you know
> that all that has changed is the JavaScript bundle that makes the Taipy
> web app.
>
> By default, the Taipy GUI application searches for the front-end code
> in the `[taipy-gui-package-dir]/taipy/gui/webapp` directory.<br/>
> You can, however, set the environment variable `TAIPY_GUI_WEBAPP_PATH`
> to the location of your choice, and Taipy GUI will look for the web
> app in that directory.<br/>
> If you set this variable to the location where you build the web app
> repeatedly, you will no longer have to reinstall Taipy GUI before you
> try your code again.

## Running the tests:-

To run the tests on the package, you need to install the required development packages.
We recommend using [Pipenv](https://pipenv.pypa.io/en/latest/) to create a virtual environment
and install the development packages.

Google Colab is a popular and free Jupyter notebook environment that requires no setup
and runs entirely in the cloud. To install Taipy in Google Colab, follow these simple
steps:

1. **Open a new Colab notebook:-** Visit [Google Colab](https://colab.research.google.com)
    and start a new notebook.

2. **Run the installation command:-** In a new cell, enter the following command and run
    the cell to install the latest stable release of Taipy in your Colab environment:


    ```python
    !pip install --ignore-installed taipy
    ```


Then you can run the tests with the following command:-

3. **Start building your app:-** Follow this
    [tutorial](https://docs.taipy.io/en/latest/tutorials/articles/colab_with_ngrok/) to build
    and run your Taipy web application directly within the Colab notebook.


!!! tip
    Remember that Google Colab environments are ephemeral. If you disconnect or restart
    your Colab session, you will need to reinstall Taipy.
