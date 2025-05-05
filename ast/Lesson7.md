# Git

Git is very easy to start using but very hard to master and use to it's full potential

Git is the popular **distributed version control system**. It was create by Linux Torvalds in 2005 to manage the development of Linux. It can be used from the command line or using a UI specific for an IDE (*I.e:* eGit for Eclipse)

## Commit

A commit is a snapshot of your project at a certain point in time. It is a way to save your work and keep track of changes. Some very important commits might be **tagged**.

## Branch

A branch is a separate development stream in a repository. The idea is that you should work on a separate branch when you are developing a new feature and then once you are sure that it works you can **merge** it to the main one.

Branches are the killer feature of Git. It's very efficient and also useful.

## Centralized VCS vs Distributed VCS

In a **centralized VCS** There's a single central repository. This means that if the server crashes or the disk breaks you won't be able to recover your history.

In a **distributed VCS** there can be a central repository, but the point is that each developer has a **complete clone** of the whole repository on it's computer. The main advantage of this approach is that you can work **offline** and you have an automatic kind of **backup** because every single developer basically has one backup.

### More on distributed VCS

In a distributed VCS you can always **connect** your local repository to another one (called **remote**) and the history will become exactly the same between the local and the remote one repository.

In a centralized VCS giving versioning commits it's very easy, you just need to use an incremental number. On a distributed VCS you can't do it so easily but you can still manage to get something equally good: you can use **hashes** of the commit (*I.e:* SHA-1 for git) allowing every commit in every clone to be uniquely identified.

### Main drawback of distributed VCS

Git and distributed VCS in general **are not meant for binary files**, or at least not for binary files that change very often. The main issue is the fact that the size of the history will become very big very fast, this is not an issue if you have a centralized VCS as only the server will have a very big control history and you won't need to have that also on your PC.

## Using Git

To start using Git (offline for the moment) I can just do the following steps:

- Create a folder `mkdir myProject`
- Go into the folder `cd myProject`
- Initialize a git repository `git init`

You can configure a few git settings **globally** like:

- `git config --global user.name "Your Name"`
- `git cofig --global user.email "Your Email"`

*Note:* you should deal with the end of line character by using `git config --global core.autocrlf=input` on Windows and `git config --global core.autocrlf=true` on Unix.

### States of the working tree

Each file of the working tree can be either:

- **Untracked:** not present in the repository
- **Tracked:** present in the repository
- **Staged:** modified and ready to be added to the next commit
- **Dirty:** modified but not staged

### Performing a commit

First you add modified or untracked files to the staging are, `git add`. Then you commit the staged files, `git commit -m "Your message"`.

*Note:* From the command line you can use many different commands, some examples are: `git init`, `git add`, `git commit`, etc. These commands can be executed from every directory in the working tree.

The commit messages should be relevant to be able to revert back the changes at a future time. It's possible to change the history of Git but you should always be careful while doing this.

*Note:* You can specify an empty message in a git commit but **you should never do it**.

If you don't specify a message in the commit command, Git will open a text editor for you to write the message. This way of specifying a message is good as you are allowed to specify a very long message by writing the first line as a **summary** then leaving a blank line and then writing your long message.

By using the command `git diff` you can see the differences between the working tree and the staging area, the format used is the very common `diff` format.

### .gitignore

This file can be specified in any directory of the working tree. This file uses regular expressions in order to declare files and directory that should be ignored even if they are in the working tree directories.

There's a possibility to exclude all the files in a directory by using the `*` character and then specify specific files that should be included by using the `!` character.

You can add comments to the `.gitignore` by using the `#` character.

**Very important note:** for the project remove the `target` Maven directory from the repository by adding it to the `.gitignore` file.

### Git GUIs

Git provides two GUIs: `gitk` and `git gui`. Both are very ugly and not so pleasant to use nowadays but they work on any OS and can be used at first. (*Note:* Those are not preinstalled automatically)

### Git branching

A new branch can be created by using `git branch <name of the branch>`.

You can pick a branch by using `git checkout <name of the branch>`.

You can show all the branches by using `git branch` and you can also remove a branch by using `git branch -d <name of the branch>`. *Note:* this last feature is really powerful and was not present in other older version control systems.

A branch that isn't merged yet cannot be removed by using the `-d` flag, you should use the `-D` flag instead to force the deletion.

### Merging

To merge a branch into the current one you should use `git merge <name of the branch>`.

The merge will succeed if there are no conflicts, if there are conflicts you should resolve them and then commit the changes. *Note:* The merge also produces a commit with a default message.

If two branches don't diverge then we will have a **fast-forward merge**. This is a very simple merge that just moves the pointer of the current branch to the commit of the other branch. This can be avoided by using the command `git merge --no-ff`.

*Note:* you should solve the conflicts before going on with the merge. It's important to take your time.
