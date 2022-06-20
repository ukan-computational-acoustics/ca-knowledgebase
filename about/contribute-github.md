# Getting started with GitHub

This knowledgebase is edited and hosted using GitHub. If you have not used GitHub or git before, you may want to look at
[How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github)
and the [Software Carpentry lesson on version control with git](https://swcarpentry.github.io/git-novice/).

In brief, you should follow the following steps to contribute to the knowledgebase. These steps demonstrate using git from the command line; if you
are using a GUI client, you should have buttons with test similar to the commands given here.

1. Make a fork of the [knowledgebase repo](https://github.com/ca-knowledgebase/ca-knowledgebase.github.io). There is a button in the top right
   corner that allows you to do this.

2. Clone (ie) download your fork of the repo. You can do this by copying the link you see when you click the green 'Code' button on GitHub, then running:
   ```bash
   git clone https://github.com/*THE REST OF THE LINK YOU COPIED*
   ```
   If you have made changes before, you do not need to repeat steps 1 and 2. Instead, you should visit the GitHub page for your fork and click 'Fetch upstream',
   then run the following to pull these changes:
   ```bash
   git pull
   ```

3. Make a new branch. You can do this with:
   ```bash
   git checkout -b *NAME_OF_BRANCH*
   ```
   It's good practice (but not mandatory) to name your branch `YOUR_GIT_USERNAME/NAME_OF_NEW_FEATURE`.

4. Make your changes.

5. Commit your changes:
   ```bash
   git add *
   git commit -m "describe your changes"
   ```

6. Push your changes to your fork on GitHub. You can do this by running:
   ```bash
   git push
   ```

7. Open a pull requst from your branch to the main repository. You can do this by clicking the 'Contribute' button on the GitHub page for your branch.

8. We will then review your pull request. If we suggest changes, you can make these then push again to update the pull request. Once we're happy with your changes,
   we'll merge them and the knowledgebase website will update automatically.
