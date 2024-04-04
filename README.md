# BUMPR
The BUMPR Project is a website development project for Wellesley students to efficiently find other students to carpool with to a certain destination. It acts as a scheduler that uses the matching algorithm to schedule two or more students together. 

# Goal: 
Create a matching algorithm that will consider certain parameters to choose a group of people to carpool to their destination. The parameters include the distance, time at which students request/need to reach a destination, the price of the trip, the starting location & destination.

# UI/UX: 
A wonderful group of Wellesley students designed the website's wireframes and high-fidelity prototype in Figma after conducting user interviews, competitive analysis and a heuristic evaluation.

# Frontend: 
React

# Backend: 
Python

# Database: 
Firebase

# Communication via Slack: 
Email dc103@wellesley.edu if you'd like to join our team!

# Launching
Steps to run everything:
1. Run the command `pip install python-dot`, if not previously done
2. Run the command `npm start` in bumpr directory
3. Open a new terminal
4. Run the command `npm run start-backend` in the backend directory

# Dependency Management
Currently, we are using `pipenv` to manage packages. 

If you are a first-time user, make sure you have `pipenv` installed in the right version of python locally.

Instructions for installing `pipenv`:
1. Run the command `pip3 --version` or `pip --version`.
    * Make sure this is `running on (python 3.11)`
    * If these commands give you differing versions, pick the one that runs on python 3.11, to install `pipenv`.
    * Run PIPENV_DEFAULT_PYTHON_VERSION to python3.11 if the above does not work.
2. Run the command `pip3 install pipenv` or `pip install pipenv` in your home directory.

If you are adding dependencies to the project:
1. Activate the `pipenv` shell, run `pipenv shell`.
2. If you want to add a package for prod code, use `pipenv install <package>`. Use the `--dev` flag if you are adding packages for test code.

If you are installing dependencies from pipenv after an update:
1. Run the command `pipenv install`. This will update your project dependencies to use the packages found in Pipfile.

FYI about `pipenv`:
* `pipenv` is a package that manages dependencies for us. It creates a virtual environment for us, so that we may share the same versions of package dependencies across the entire dev team. 
* Here's a [cheatsheet of available commands](https://gist.github.com/bradtraversy/c70a93d6536ed63786c434707b898d55).
* Any issues, ask Ashley!