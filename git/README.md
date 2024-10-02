# Git
### Things that must not be pushed into git repository 
- code part of username/password, ip address
- config file (should be done as environment)
- service account file or private key file ( `json`, `pem` )
- personal information
- use [.gitignore](https://github.com/github/gitignore)
    - how to write in `.gitignore`
    ``` 
        password.josn   #only this file
        .cache   #specific files
        config/  #folder
        .vscode/* #config of vscode
        .idea/*   #config of pycharm
    ```
### when to split branch
- master/main:  main branch for production (one in a project)
- feature:      for new features, splitting from develop branch
- release:      a branch to check everything's okay including features from develop and bug fixing from hotfix before merging to master
- develop:      to merge features into one (one in a project)
- hotfix:       to fix bugs in release

### clone with ssh key
1. create public and private ssh-key
```
ssh-keygen
```
2. copy keys
```
cat ~/.ssh/id_rsa.pub (to see and copy them, in case choose default folder to save keys when creating keys)
```
- on github gui
    - go to settings on the website
    - go to ssh and gpg keys
    - paste copied keys there
3. `git clone` like https but using ssh this time

### how to write a markdown file
[markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
#### what to write in README.md
should have 4-5 of these  
- Project title
- Description
- Technologies Used
- Folder Structure
- Getting Started, Installation
- FAQ
- Future Scope

[see more here](https://github.com/mundimark/awesome-markdown)

### Github action
#### Continuous Integration (CI)
- helps in building software and testing it automatically after pushing new commits
- work with pull request and code review
#### Continuous Delivery/ Deployment (CD)
- deliver latest software after going through CI process? 
- deploy the software for users (testers before deploy in production)
#### main components
- workflow
    - yaml file in `.github` directory
        - name
        - on (trigger)
        - jobs (action)
    - [starter workflow](https://github.com/actions/starter-workflows)
- trigger
- action
    - [find more in Actions Marketplace](https://github.com/marketplace?type=actions)
    - [Javascript with Action Toolkit](https://github.com/actions/toolkit)
    - can save action secrets to use every new push
        - sometimes credentials need to be in base64
        - `cat ~/key.json|base64 -w 0 > ~/base64_key.txt`
            - `...|base64` base64 encoding
            - `-w 0` make a result in a single line

[code to try CI/CD](https://github.com/fonylew/simple-cloud-functions-to-bigquery)

## Commands
#### Clone
```
1.  git clone git@github.com:xxxx/xxx.git
```
Status: check if there is changes in the repository, used before add files
```
1. git status
```
#### Add
```
1.  git add <file1> (<file2>)
2.  git add . (all files in the current directory)
```
#### Commit
```
1.  git commit -m "commit msg: edit xxxx"
2.  git commit -am "commit msg" (git add + commit in one line)
```
#### Push
```
1.  git push 
2.  git push <origin> <branch_name> (<remote-name> <branch-name>)
3.  git push -f origin <feature_branch>
```
* `-f` force
    - ignore everything and push (e.g. used after rebase)
Pull
```
1.  git pull <remote-name> <branch-name>
```
#### Create branch
```
1.  git branch <branch_name>
2.  git checkout -b <branch_name> (switch to this branch after creating)
```
#### Switch branch
```
1.  git checkout <branch_name>
```
#### Merge
```
1.  git checkout <destination_branch>
    git merge --no-ff <branch_that_is_wanted_to_merge_with_dest> (e.g. origin/main or feature/branch1)
```
* `--no-ff` (fastforward)
    * will combine every commit in a source branch into a single commit 
    * meanwhile without no-ff will concatenate the source branch at the end of the destination branch     

#### Rebase 
- want to use new features in main but still not want to merge a current branch     
- caution
    - only use with local commit which hasn't pushed into remote
    - update data on local before rebase so switch to the target branch and pull latest commit then switch back
    - careful about branch when checkout
    - not the best when there are many people using the same branch
```
1.  git rebase <target branch>
2.  git rebase --continue (continue rebase after resolving conflict)
```
#### Pull-Request or Merge-Request
- `create a merge commit`:  keep all commits and show them in the base branch
- `squash and merge`:       make the commits as a single commit in the base branch
- `rebase and merge`:       rebase with conflict resolving of each commit in feature branch and merge as a single commit in the base branch
#### Reset
```
1.  git reset --hard
2.  git reset HEAD~2 (undo changes and move to the second previous commit)
```
* `--soft` move to specific commit but leave every change still
* `--hard` undo and delete the changes to match specific commit
#### Revert
```
1.  git revert <commit-id> (remove changes on a specific commit in a new commit)
```
#### Cherry-pick
```
1.  git cherry-pick <commit-id> (move a specific commmit to another branch's latest commit)
```
#### Stash (first in, last out)
```
1.  git stash (keep all changes away from current work dir so the dir can pull from main branch)
2.  git stash pop (apply the changes to cur dir and remove them from stash list)
```

