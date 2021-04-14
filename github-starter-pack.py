
MOST USED GIT COMMANDS
#######################################

Create new repo from Gitbash cmd line
#####################

#create a mark down description file ('touch' creates files)
$ touch README.md

 #Initialize the repo in the current directory
$ git init

#Stage the changes
$ git add README.md

#Commit it to Git
$ git commit -m "first commit"

#Connect to remote and push
$ git remote add origin git@github.com:joshasgard/<reponame>.git
$ git push -u origin master #push to master branch


Others
###################

#Clone from remote repo into new local directory
git clone git@github.com:username/repo.git
git pull  https://github.com/user-name/repository.git #after creating a local repo

#pull changes from remote repo to existing local directory
git pull origin master

#Force push
git push origin <your_branch_name> --force #for a specific branch
git push https://git.... --force #for the whole repo

#Ignore files that weren't tracked before by git (i.e. before 'git add')
touch .gitignore.
-add files to ignore to .gitignore file

#fetch changes made to a remote repo
git fetch remotename

#merge changes into local branch
git merge origin/branchname
git merge branchname #to master

#Check status
git status

#Remove files from git tracking
git rm -r --cached file/path #remote -r
git rm --cached file/path #local
git rm -r file or folder_name

#hard remove folder from git tracking
'Simply delete the .git folder in the local directory of the folder'

#Create branch
git checkout -b your_branch_name 
git commit --allow-empty -m 'commite_message' #Doing an empty commit into the branch
git push origin your_branch_name #Push branch to remote

#Make forked repo the url you 'commit to' or send 'pull requests to'
git remote set-url origin ...your_forked_repo_url...
#help
git --help
git --help init
