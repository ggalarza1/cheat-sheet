How to create a git repository

1.Download git

----------To start a project in grithub.-----------

1.Make a repository name but make sure it ends with ".md".

2.Pick between public or private.

3.Touch create a repository.


--------
6.Make the folder and text file you are using.

7.The text file should make should end in ".md".

8.Open Windows PowerShell or any other command prompt you have in your computer.

9.When using the command prompt, you want to change the directory to the text file in your computer.

10.Using the universal command "cd", write the path to the folder you are using. 

11. For me, my command path was in my desktop in a folder called python. My text file was called "cheatsheet". ex.".\Desktop\Python\cheatsheet\"
7.Follow the instructions in github to connect to the computer
8.git init  ----  in the prompt.
9.git add README.md --- in the prompt
ls  ---- list directories
git status ---- in the prompt

git config --global user.email "gabrielaasolis@gmail.com"
git config --global user.name "Gabriela Solis"

git commit -m "first commit" ---- mental note
git remote add origin https://github.com/gabrielaasolis/cheat-sheet.git   ---- once. Makes connection from local machine to github repo.
git push -u origin master
git pull

history ---used to see the history of the items made



