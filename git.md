How to create a git repository

Download git if you do not have it in your computer

----------To start a project in Github -----------

1.Make a repository name but make sure it ends with ".md".

2.Pick between public or private.

3.Touch create a repository.


-------- Using PowerShell or another command prompt --------
Make the folder and text file you are using.

The text file should make should end in ".md".

Open Windows PowerShell or any other command prompt you have in your computer.

When using the command prompt, you want to change the directory to the text file in your computer.

Using the universal command "cd", write the path to the folder you are using.

For me, my command path was in my desktop in a folder called python. My text file is called "cheatsheet". ex.".\Desktop\Python\cheatsheet\"
Follow the instructions in github to connect to the computer
git init  ----  in the prompt.
git add README.md --- you are adding a file called README.md
ls  ---- list directories
git status ---- in the prompt

git config --global user.email "USE YOUR EMAIL"
git config --global user.name "USE YOUR USERNAME"

git commit -m "first commit" ---- note of what you are doing
git remote add origin https://github.com/USERNAME/FILENAME.git   ---- once. Makes connection from local machine to github repo.
For COLAB use this one--!git remote add origin https://<UserName>:<Password>@github.com/<UserName>/<Name-Repository>.git  --- This is what you use in Colab to sign in and post into Github

git push -u origin master ---- the origin can have a different name depending on how everyone organizes their
git pull

----------Cloning a project from Github and adding to it.-----------

git clone https://github.com/<username>/<name-of-repository>.git  --- Note if you use colab you need a ! at the beginning of git

First you must find the file. Use "ls" to list the file. The command "cat <filename>" would let you go inside the file.
Other commands include pwd- this is the present working directory.
cd - the change directory command
cd .. brings you back one directory
cd <nameofthedirectory> If you add cd followed by the directory name it will bring you there.

%%writefile <FileName> --- to write on the repository

git add .
git init
git config --global user.email "USE YOUR EMAIL"
git config --global user.name "USE YOUR USERNAME"
git add .
git commit -m "WRITE A COMMENT TO REMEMBER WHAT YOU DID"
git remote add origin https://<UserName>:<Password>@github.com/<UserName>/<Name-Repository>.git
git push -u origin master
git remote rm origin --- use this to clear what you have written before


#history ---used to see the history of the items made
