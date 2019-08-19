# Django REST API

Django REST API concepts.

---

## Vagrant

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

You will know that you're working on a virtual environment because the name of the virtual environment that is being worked on will appear in brackets as a prefix to the command line input, such as `(env) vagrant@ubuntu-bionic:/vagrant$`.

To deactivate the virtual environment (obviously while it is active) run:

```commandline
deactivate
```

---

## API

`WIP`