# Sample Python service

This repo includes all the boiler plate code in order to create a Python restuful API service that runs on flask.

## Requirements
### For developing
In order to develop and run in dev mode, all that is needed is `Python3.7` together with the [pipenv](https://github.com/pypa/pipenv) module.

Besides that, programming in Visual Studio Code is heavily recommended in order to automate testing and linting.

### Deploying
For deploying, having an updated version of [Docker CE](https://docs.docker.com/install/) is required.

## Setup

1. Install `Python3.7`
2. Clone or download the contents of this repo into a folder and `cd` into it
3. Run `pipenv install` to create a virtual environment and install the current dependencies.

If you are developing on Visual Studio Code (as you should to get maximum benefits of this boilerplate) continue with the following:

4. Open the command palette (`cmd + shift + P` in mac or `ctrl + shift + P` in windows and linux).
5. Select _Python: Select Interpreter_
6. Select the Python version that corresponds to the virual environment just created by `pipenv`. (_help_: That version should say _virtualenv_ somewhere in its name and by a version of `Python3.7`)

Now you are ready to develop and deploy!

## Development

### Working

In order to add functionality, simply work within the `src` folder. The structure within `src` has no importance. The only requiremente is that the main app object is defined within the `main.py` file at the first level and that it is named `app`.

That is, the only required structure is the following
```
src
|-possibly
| `-other
|   |-files
|   |-and
|   `-folders
`-main.py # obligatory file
```
and the contents of `main.py` must include
```python
app = Flask("my app name")
```
somewhere.

### Installing dependencies

Whenever you install a new Python module, it is of utmost importance that you declare it on the `Pipfile`. A simple way of doing this is installing dependencies _through_ pipenv. 

Lets say you wish you install numpy, simply run:
```
$ pipenv install numpy
```
That will both, install the module on the virutal environment and declare the dependency on the `Pipfile`.

### Running
In order to run locally on can simply execute `main.py`. Just remember to activate the virtual environment, or you will probably have dependency issues. Here are a few examples:

1. Run through pipenv:
    ```
    $ pipenv run python src/main.py
    ```
2. Activate the virtual environmente
    ```
    $ pipenv shell
    (my-virtualenv)$ python src/main.py
    ```

### Testing
In order to write tests for your service, just write your tests on the `test` folder.
This version writes is tests using Python's [unittest](https://docs.python.org/3/library/unittest.html) module. 

As with the `src` folder, the structure within `test` is of no importance, with only two restrictions:
1. All test files must start with the word `test`. (eg: `test_front_page.py`)
2. Every new folder within `test` must declare an empty `__init__.py` file. (this allows the `test` folder to be interpreted as a module by the Python interpreter)

Example tree structure:
```
test
|-messages
| |-__init__.py
| |-test_message_actions.py
| `-test_reactions.py
|-users
| |-__init__.py
| `-test_users.py
`__init__.py
```

#### Test Running
If you are using Visual Studio Code, simply open the command palette (`cmd + shift + P` in mac or `ctrl + shift + P` in windows and linux) and run _Python: Run All Unit Tests_. Results will be shown on the editor.

If you are not using Visual Studio Code, simply run the following code on the root directory (make sure you are within the virtual environment):
```
$ python -m unittest
```
## Deployment
In order to deply, first you must lock all the python dependencies. In order to do so, just run
```
$ pipenv lock
```
Sometimes this raises a dependency error, in which case running the following command may solve the issue.
```
$ pipenv lock --pre
```
Once the dependencies have been locked, you must build the docker image:
```
$ docker build -t python-service .
```
And finally, you can run the service with the following command
```
$ docker run -p <PORT>:5000 python-service
```
which will setup your service on port `<PORT>` on localhost.

Additionally you may choose to run in detached mode by adding the `-d` flag.

```
$ docker run -d -p <PORT>:5000 python-service
```

If you do this, you may check for the container status by running `docker ps`. This container can be forcefully killed by running `docker kill <container id>`.