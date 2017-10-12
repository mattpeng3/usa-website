# usa-website
Website for the Statistics Undergraduate Student Association at Berkeley.

If this is your first time, clone this repository (git clone https://github.com/usaberkeley/usa-website).  
Otherwise, pull (``git pull origin master``).

If you are changing some code: 

- If a branch for your task does not already exist, create a branch for your job (``git checkout -b BRANCH_NAME``). 

- If a branch does already exist, switch to that branch (``git checkout BRANCH_NAME``). 

You can check what branch you're on by typing ``git branch`` or ``git status``. ``git branch`` will show you a list of all the branches that you can access.

When done updating code, type ``git add -A``, ``git commit -m 'Enter commit message here'``, and ``git push origin BRANCH_NAME``. 

Then visit the repository on your browser, click on "Pull requests" at the top of the page, then click "New pull request". Keep the base-branch as "master", but change the compare-branch to ``BRANCH_NAME``. Then, click "Create pull request". Now wait for someone else to look through the edits to make sure nothing broke! Typos are a scary thing. 

==================

To run a local version of your website, type ``python manage.py runserver`` into the folder that contains the ``manage.py`` file (should be the same one as the current folder!) If this fails, you may have to install Django first. Version 1.9.3 works for our purposes.

``schedule_builder/`` contains all relevant code.
 - HTML files are in ``schedule_builder/templates/schedule_builder/``
 - Static files (images, css, etc) are in ``schedule_builder/static/schedule_builder``

