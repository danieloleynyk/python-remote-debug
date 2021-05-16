python-seed template
=====================

What's it?
----------
This is an opinionated template that contains all the needed tools to develop production ready 
python apps, some features that can be found in this template: <br/> 
- remote container debug using pycharm-professional (tested on 2021.1 version)
- linting, using flake8 with some useful plugins
- formatting, using black
- testing, coverage, using pytest & coverage
- type safety

Sadly there is no way to make remote container debugging work on
the community edition since I'm using some features that are only available on the 
professional version (ssh interpreter)

Motivation
----------
My goal was to achieve a fully containerized batteries included development environment,
getting the option to remote debug (similarly to vscode's dev containers) 
my python code was my mail goal, unfortunately I've encountered numerous issues 
during my attempts which brought me to issues that were opened 5-7 years ago on jetbrain's 
youtrack issues platform... <br/>
Side note, this is kind of sad the amount of workarounds that I had to make in order
to make it work, there is no reason that such a simple feature would be that hard to achieve
especially in a paid product... <br/>
During the process I've decided to take it a step further and also add all the needed tools to
make it a batteries included template`(testing, linting, formatting)`

How does it work?
-----------------

- the idea is to have a container that we can access it using ssh,
  the venv should be created on the container, and not on the host machine since the 
  command `python -m venv venv` creates symbolic links.
  
- `.remote` folder that contains the needed docker configurations:
    - `Dockerfile` contains an opinionated dev environment, the most important part
      of it is the *ssh-configuration* which will be later used to connect to the container with ssh.
    - `docker-compose.yml` contains a simple compose file that expose our `Dockerfile`
      please keep the `dev` service as is, you can add other services for your needs.
      
- `.idea` folder that contains pycharm's configuration, normally you wouldn't push this
  folder to your vcs but to make the template batteries included I've decided to also upload it.
    - `deployment.xml` represents the component that takes care of deploying your code to the
      dev container `remoteFilesAllowedToDisappearOnAutoupload` attribute must be set to false,
      otherwise your code will strangely disappear... <br/>
      `<paths name="root@localhost:9922 password">` "root" & "password" are the username and 
      password that were set for our ssh during the `Dockerfile` build process(replace if needed)
      <br/>`<mapping deploy="/workspace" local="$PROJECT_DIR$" />` maps our host project directory
      to the containers `/workspace`
    - `modules.xml & remote-debug.iml` are used for linking the venv inside our dev container to 
      our pycharm.
  
- change the `Dockerfile` and the `docker-compose.yml` to your needs this is a flexable setup
- testing are achieved using pytest
- coverage using `coverage & pytest`
- linting, using `flake8` and some additional plugins, take a note this is definitely an opinionated
setup, you can change `.flake8` to your needs
- formatting, using `black` yet another opinionated tool, if you don't like it go ahead and remove it :)
- type safety, using `mypy` currently seems kind of redundant since pycharm already make all
the heavy lifting for typing anyways, might be useful later within a ci pipe...
- docstrings, configured to use the Google format
- dependency management, using `pipenv` you can also try `poetry` instead.

- there are a few simple `make` commands that will make your life a bit easier
    - `make init` will spin up the `docker-compose.yml`
    - `make venv` will spin up a remote ssh terminal with venv activated, 
      use all your `pip & pipenv` inside this remote terminal.
    - `make clean` will clean pycharm cache (a workaround one of the issues with pycharm...)
    - `make test` runs all the tests
    - `make coverage` spins up all the tests and generate a `coverage report`
    - `make lint` run `flake8` and `black`

Setting up pycharm
------------------
- spin up your dev container using `make init venv`
- set up a remote ssh python interpreter: <br/>
_1. `ctrl + alt + s` or `File/Settings`_ <br/>
_2. `Project/Python Interpreter`_ <br/>
_3. press the `cog wheel` and then press `add`_ <br/>
_4. select the `SSH interpreter` and fill in your container's credentials_ <br/>
_5. now the most important part, choose your python interpreter, 
  `by default /.venvs/venv/bin/python`_ <br/>
_6. map the sync folder to `$PORJECT_ROOT -> /workspace` and uncheck the auto upload_ <br/>

That's it you can use your brand-new python interpreter in your run configurations :D

Known Issues
------------
- project files are empty after spinning up the dev container:
    - happens because of the auto file transfer, in order to disable it go to
      `Tools/Deployment` and uncheck to `Automatic Upload`
- a package is still usable in your code even though you uninstalled 
  it already, and the code doesn't run with it.
    - this is a yet another pycharm bug that JetBrains never fixed...<br/>
      https://intellij-support.jetbrains.com/hc/en-us/community/posts/205813579-Any-way-to-force-a-refresh-of-external-libraries-on-a-remote-interpreter-
    - this happens because of the cache that pycharm saves on your host machine
    - I've solved it using `make clean` which goes to your pycharm's cache directory and removes it. <br/>
        * be careful it removes all the cached packages in all the projects that are saved on your 
          host machine.

Roadmap
-------
- add documentation generation e.g: `sphinx`
- add a basic ci pipeline which will run: `linting, formatting, tests, type checks...`
- add support for vscode

Help
----
If you need any help, or want to add to the template something, don't hesitate just open an issue
I'll make sure to check it out as soon as possible.
