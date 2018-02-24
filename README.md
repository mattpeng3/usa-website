# usa-website
Website for the Statistics Undergraduate Student Association at Berkeley.

## macOS
1. [Install Homebrew](https://brew.sh/)
2. Type commands in `Terminal`

## Windows
1. [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
2. Type commands in `Bash on Ubuntu on Windows`

## Setup
1. Install `python3`
    * **macOS:** `brew install python3`
    * **Windows/Linux:** `sudo apt-get install python3`
2. Install `git`
    * **macOS:** `brew install git`
    * **Windows/Linux:** `sudo apt-get install git`
3. `git clone https://github.com/SUSA-org/usa-website` to clone the repo
4. `pip install -r requirements.txt` (or `pip3 install -r requirements.txt`) to install requirements
5. `git checkout -b my_name` to create your own branch (replace `my_name` with your name)
6. `git pull origin master` to bring in latest changes
7. To run a local version of your website, type `python manage.py runserver` (or `python3 manage.py runserver`) into the folder that contains the `manage.py` file (should be the same one as the current folder)
8. Visit the local URL in your browser (should look like `http://127.0.0.1:8000/`)
9. If you are able to see the website, pat yourself on the back!

## General Tips
* You can check what branch you're on by typing `git branch` or `git status`
* `git branch` will show you a list of all the branches that you can access

## Workflow
1. Start local test environment: `python manage.py runserver` (or `python3 manage.py runserver`)
2. Make changes, refresh test site
3. If everything looks good:
    1. `git add -A`
    2. `git commit -m 'Enter commit message here'`
    3. `git push origin BRANCH_NAME`
4. Then visit the repository on your browser, click on "Pull requests" at the top of the page, then click "New pull request". Keep the base-branch as `master`, but change the compare-branch to `BRANCH_NAME`. Then, click "Create pull request". Now wait for someone else to look through the edits to make sure nothing broke! Typos are a scary thing.

## Layout
* ``usa_website/`` contains all relevant code.
* HTML files are in ``usa_website/templates/usa_website/``
* Static files (images, css, etc) are in ``usa_website/static/usa_website``

## Useful References
* [git](https://git-scm.com/)
* [python](https://www.python.org/)
* [django](https://www.djangoproject.com/)
