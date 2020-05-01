How to create a git repository

1.Download git

----------To start a project in Github.-----------

1.Make a repository name but make sure it ends with ".md".

2.Pick between public or private.

3.Touch create a repository.


--------
6.Make the folder and text file you are using.

7.The text file should make should end in ".md".

8.Open Windows PowerShell or any other command prompt you have in your computer.

9.When using the command prompt, you want to change the directory to the text file in your computer.

10.Using the universal command "cd", write the path to the folder you are using.

11. For me, my command path was in my desktop in a folder called python. My text file is called "cheatsheet". ex.".\Desktop\Python\cheatsheet\"
7.Follow the instructions in github to connect to the computer
8.git init  ----  in the prompt.
9.git add README.md --- you are adding a file called README.md
ls  ---- list directories
git status ---- in the prompt

git config --global user.email "USE YOUR EMAIL"
git config --global user.name "USE YOUR USERNAME"

git commit -m "first commit" ---- note of what you are doing
git remote add origin https://github.com/USERNAME/FILENAME.git   ---- once. Makes connection from local machine to github repo.
COLAB--!git remote add origin https://<UserName>:<Password>@github.com/<UserName>/<Name-Repository>.git  --- This is what you use in Colab to sign in and post into Github

git push -u origin master ---- the origin can have a different name depending on how everyone organizes their
git pull

----------Cloning a project from Github and adding to it.-----------

git clone https://github.com/<username>/<name-of-repository>.git  --- Note if you use colab you need a ! at the beginning of git

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
