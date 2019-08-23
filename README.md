# Django REST API

Django REST API concepts.

---

## Vagrant

### Initialization

To initialize vagrant, run:

```commandline
vagrant init ubuntu/bionic64
```

Where `ubuntu/bionic64` is the type (OS) of the created server, there are more options available in the vagrant website.

### Basics

- The box type is `ubunty/bionic64`.
- To install the virtual machine run: `vagrant up`.
- To destroy the virtual machine run: `vagrant destroy`.
- To start the virtual machine run: `vagrant ssh`.
- While inside the virtual machine, the directory that is synchronized with the root folder of this project is the `vagrant` folder.
- While inside the virtual machine, the directory of the synchronized folder will look like `vagrant@ubuntu-bionic:/vagrant$` in the terminal.

### Activation *(inside the virtual machine)*

**1. Installation:**

We need to create a Python virtual environment before creating a Django App. To create and activate a Django environment, run:

```commandline
python -m venv ~/env
```

Note that the directory of this installation is outside the `vagrant` folder, this is to avoid the installed dependencies being synchronized with the root folder.

**2. Activation:**

An active virtual environment is needed so that all of the installed dependencies are pulled from the virtual environment instead of the base operating system. To activate the local environment, run:

```commandline
source ~/env/bin/activate
```

So long as python virtual environment was installed in `~/env`, this command line will run correctly. You will know that you're working on a virtual environment because the name of the virtual environment that is being worked on will appear in brackets as a prefix to the command line input, such as `(env) vagrant@ubuntu-bionic:/vagrant$`.

To deactivate the virtual environment (obviously while it is active) run:

```commandline
deactivate
```

- Useful Python virtual environment cheatsheet: https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/

---

## Dependencies

The required Python packages are located in the `requirements.txt` file as a best practice. This file will include specific packages and versions (pinning them down to specific versions is intended).

For more information about the packages, go to https://pypi.org/.

To install the required dependencies, run inside the virtual machine (while activated):

```commandline
pip install requirements.txt
```

---

## Django

**1. Create a new Django project:**

**While in a git bash command line inside the vagrant machine terminal, and while it is active**, run:

```commandline
django-admin.py startproject profiles_project .
```

What this does is that it will run the `django-admin.py` script that will start a new project by running `startproject` and set a name of `profiles_project` in the specified location `.` (root folder). If a location is not specified, it will create a new sub-folder.

**2. Create a new Django app (within our project):**

A Django project can consist of one or more sub applications within a project that can consist of different functionalities within a project.

To create a sub-application within a project, run (*inside the vagrant machine terminal sync folder, and while it is active*):

```commandline
python manage.py startapp profiles_api
```

Where `startapp` will create a new app, and `profiles_api` is used to set the name (and will appear as a new sub-folder).

**3. Enable an app within our project**:

To install/add new apps to the project, open the `settings.py` file inside the project folder, and add the app's name to the `INSTALLED_APPS` list.

For example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST framework.
    'rest_framework.authtoken',  # Allows usage of authentication tokens out of the box with the REST framework.
    'profiles_api', # Our Django created app.
]
```

**4. Running the Django development server**:

While connected to the vagrant box, working on an environment (`(env)`), run:

```commandline
python manage.py runserver 0.0.0.0:8000
```

This command will start development server available on all network adapters in port 8000 (as set in the `VagrantFile`).

To stop the server, type `CTRL+C`.


--- 

## Django Components

From the components *closest* to the **database tables**, to the components that are *closest* to the **HTTP requests that receive JSON data**:

- **Models**: These describe how we want the structure of our data so that Django can translate Python objects to tables in a database.

- **Serializers**: These translate the data from the HTTP request into a Python object.

- **Views**: These receive the HTTP requests, passes it to a **Serializer** to translate the data from the HTTP request into a Python object, that can then in turn be passed to the **model**, and translated to a row in the database.

For example, the `perform_create()` function in a `ModelViewSet` is the entry point in our hypothetical application. So when we want to create a new user, we make a HTTP POST request which gets received by `perform_create()`, which passes it through the Serializer to convert the raw JSON to a Python object and then passes it to the model to save it in the database.

---

`WIP`