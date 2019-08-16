# Clash-RC-Round-2
# Update 03

--Guys, It's time to start working vigorously on this project.

I NEED CONTRIBUTION FOR ALL OF YOU!

please, don't fear to commit in git repo, if something goes wrong seniors and teammates are there to help us. And be active on whatsapp group, you can text me or senior anytime if you face any error in code

I will be distributing work and adding new members in each teams. These are the following points that were disscussed in today's meet. 

-> Updating and adding new fields in UserProfile, Questions and Submission
-> add functions compile, runTestCase and compare in views.py
-> adding load buffer button(using AJAX for refreshing page) in the coding page
-> working on leaderboard's logic.
-> saving, Compiling and testing code.

So, As discussed in our team meet, we have to work on our logic for connecting Models.py and views.py so that it can work properly.

As compilation,compare and runTestCases function needed for every submitted code, we are going to create judge folder in data directory which will contain a python file that will do compilation, compare and testcases verification.
We can run this python file using subprocess after submission of each code.

As discussed we are creating a new team who will work on views.py and try to connect and implement the logic of the compilation, testing, load buffer.The members are of the teams with there work are:

1) Views.py      (implement the logic of various functions)
    
   - Gaurav  (Adding load buffer button and logic of it using AJAX)
   - Sanchit (Build logic to save submission whenever the user click submit)
   - Rutuja  (to add compile function in views.py)
   - Yash    (to add compile function in views.py)
   
2) Models.py     (Will work on data storing and compliation of the cpp files)
   
   - Gaurav  (connecting userProfile and Submission using foreign keys)
   - Abhishek(add needed fields into Questions and makemigrations of all)
   - pranav  (add needed fields into UserProfile)
   - Nikhil  (add needed fields into UserProfile)

3) Os and Subprocess modules (Will work on data storing and compliation of the cpp files)
   
   - Sanket  (compare output with std_output and update score)
   - Prerna  (compilation of program)
   - Murtuza (input output redirection using subprocess.PIPE)
   - Shreya  (use of subprocess.Popen)
   - Ram     (making standard input/output directories after signup)

Working with views.py and os/subprocess modules are interconnected to each other so we all have to work together and stay connected for understanding whole code of the project! it's important to understand all Code!!

KEEP PUSHING YOUR CODE IN GITHUB REPO.!

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Update 02

Since, All of us are now comfortable with git's command, I want you guys to start contributing your work on "clash-rc-round-2" repository..

before pushing any changes into the "clash-rc-round-2" repo, please make sure that you have added correct code in the commit.. If you not sure that your code which you added is correct or not, you can push it in your own repo and ask me to check whether it is correct or not, then push it into "clash-rc-round-2" repo.

In last meet we discussed and divide our work into teams. these are the teams:

I) Model (will work on creating Models and the key relations between them)
   - Gaurav Ghati
   - Sanchit Raina
   - Nikhil Kulkarni
   - Abhishek
 
  These people will study and Data Relations, Foreign Key, ManyTomany fields and try to implement them and create Questions, UserProfile and Submission models

II) Compilation Team (Will work on data extraction and compliation of the cpp files)
   - Sanket 
   - Prerna
   - Murtuza
   - Rutuja
   - Shreya
  
  This team will read about "Subprocess" and "os" module and how to create user's folder in "user_code" folder.

Remaining members are requested to join whichever team they want, please append the team list further.

All of us have to work on same Project now it's important to understand all project. so, whenever anyone added or push some code into the repo you all are suppose to pull and understand the code so that you will be able to work with it.


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Update 01

Hey, This is to make sure you all have cloned the repo and set git for working with it..
Refer StepsForGit.png in repo to see screenshot of commands of git on terminal

--> These are the steps you need to follow for setting your git with this project's repository..

1) Create a empty folder in environment folder("myenv" in my case) and name it as "round2".

2) go in that folder by terminal and follow below git commands

3) $ git init
   this will create empty repositry in round2 folder
   
4) $ git remote add origin https://github.com/clash-rc-round-2/Clash-RC-Round-2.git
   - Sets the new remote
 
   $ git remote -v
   - Verifies the new remote URL
   
5) $ git pull origin master
   Then pull the all code into the round2 folder from the GitHub
   
Bofore making commit append the list below which you can find in round2 folder as a readme.md, So that I can understand you have completed and set the git by following all 9 steps correctly.
         
         --> Gaurav Ghati 
         --> Nikhil Kulkarni
         --> Sanchit Raina  
         --> Murtuza Husain
         --> Sanket Landge
         --> Prerna Bhardwaj
         --> Abhishek Velankar
	 --> Ram Borade
         -->Pranav Doshi
         --> Rutuja Dhanawade
	 --> Shreya Rani
6) $ git add .
   - Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
   
7) $ git commit -m "Initial commit"
   Then Commit into it by this above command
   
8) $ git push origin master
   Then push the all changes into the GitHub by this command
   
9) give your username and password to it
   then it will push all your changes into GitHub
   
