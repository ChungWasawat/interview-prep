# Unix
<U>What is shell?</U> 

- Bourne-Again SHell or call shortly as shell
- other shell: Zsh of MacOS

<U>Symbols</U>

- `/` = root
- `~` = home
- `.` = current directory
- `..` = parent directory
- `-` = previous working directory (not sure if it works only `cd`)
- `*` = wildcard (can be anything)
- `|` = used after a command to tell computer to do the next command
- `$` = a variable or substitute command
    ```
        1.
        name="Alice"
        echo $name          # Outputs: Alice
        2.
        current_date=$(date)
        echo $current_date  # Outputs the current date and time
    ```
- `$?` = a variable that will return the exit code of the last command you ran

## Environment Variables  
common ones    
- `PATH`: contains a list of directories where systems look for executable files.
- `HOME`: contains the path to the home directory of the current user.
- `PS1`: is the default prompt to control appearances of the command prompt.
### Commands
#### export
sets an environment variable to be passed to child processes in the environment
- example: `export name=student`

## Connectors
- `&&`: first command always executes and the next command will only execute if the one before it succeeds
  - example: `true && echo Hello`
- `||`: first command always executes and the next command will only execute if the one before it fails
  - example: `false || echo Hello`
- `;`: first command and the following commands always execute
  - example: `echo Hello ; ls`
- `|`: Pipes connect multiple commands together by sending the output of the first command to the input of the next command
  - example: `ls -l | head` to print only 10 lines from `ls` 

## Redirection
### >
re-direct the output (standard out) from the command to another place
- example: `ls > files.txt`
- If the file isn't already in your working directory, the file gets created. If the file already exists, then the contents of the command overwrites what is already in the file.
### >>
similar to `>` but it appends to the end of the file instead of overwrite the file
- example: `ls >> files.txt`
### <
take content in the file as input (standard in) for the command
- example: `sort < files.txt` to print sorted content in `files.txt`
  - can save the output with `sort < files.txt > files_sorted.txt`
### Advanced Redirection
Adding a `&` with the `>` symbol results in redirecting both standard out and standard error. For example, the `test.cpp` file prints the string "stdout" with `cout` and the string "stderr" with `cerr`.
```
  $ g++ test.cpp        # execute the file
  $ ./a.out >& test.txt # move the output to test.txt
  $ cat test.txt
  stdout
  stderr
```
- normally, `>` only move standard out but it can use number to move others
  - example: `2` for stderr (standard error), `1` for stdout, `0` for stdin
  ```
  $ g++ test.cpp
  $ ./a.out 2> test.txt
  stdout
  $ cat test.txt
  stderr
  ```

## For Loop and If Else    
```
for i in {1..10}; do
  if [ $i -eq 5 ]; then
    echo "Number is 5"
  else
    echo "Number is $i"
  fi
done
```

## Common Commands
#### pwd
display a current directory
#### ls
show files in current directory
- example: `ls`, `ls directory1`

- `l`: show more details like permission, users, memory used, etc.
- `h`: use with `l` to make a list easier to read 
- `a`: show hidden files
#### cd 
enter to a directory (default is home), work with these symbols `~`, `.`, `..`, `-`
- example: `cd dir1`, `cd parent_dir1/dir1`
#### mkdir and rmdir
create empty directory/ remove empty directory
- example: `mkdir -p folder1`, `rm folder1`
- `p`: to replace existed folders with new one
#### man 
show command manuals
- example: `man cd`
#### echo
show text on terminal, or add text into a file       
- example: `echo test`, `echo test > test.txt`
#### cat
show file's content on terminal or concatenate 2 files into new one
- example: `cat file.txt`, `cat file1.txt file2.txt >> new_file.txt`
#### wc
show a number of words in a file
- example: `wc text.txt`
- `l`: to count lines instead of words
#### head
display the first 10 lines (default) of any passed in text
- example: `head -50 test.txt`
#### tail
display the last 10 lines (default) of any passed in text
- example: `tail -50 test.txt`, `tail -f test.txt`
- `f`: to view in real time any text appended to the file
#### more 
show all file's content
- exmaple `more file.txt`
#### less
similar to more but split content to show on terminal and can move backward to see previous content
- example: `less files.txt`
- `spacebar` to go to the next page
- `enter` followed with below commands    
  + `G`    
  Moves to end of file
  + `g`    
  Moves to beginning of file  
  + `:50`	
  Moves to the 50th line of the file
  + `q`	  
  Exits less
  + `/searchterm`     
  Searches for any string matching 'searchterm' below the current line
  + `/`	      
  Moves you to the next match for your previous 'searchterm' below the current line
  + `?searchterm`	    
  Searches for any string matching 'searchterm' above the current line
  + `?`	      
  Moves you to the next match for your previous 'searchterm' above the current line
  + `up`	      
  Moves up a line
  + `down`	    
  Moves down a line
  + `pageup`	    
  Moves up a page
  + `pagedown`	    
  Moves down a page
#### grep
find a phrase in text or files
- `i`:	remove case sensitivity
- `r`:	search recursively through directories
- `w`:	search only whole words
- `c`:	prints number of times found
- `n`:	prints line found on with phrase
- `v`:	prints invert match
- [regex tutorial](https://github.com/mikeizbicki/ucr-cs100/tree/2015winter/textbook/using-bash/regex)
#### history
prints out an incremented command line history
- It is common to use the `grep` command with the `history` command to search for a particular command
- example: `  $ history | grep g++`
#### sed
a stream editor that performs text transformations on an input.
- Common use of this command is to replace expressions which takes the form `s/regexp/replacement/g` 
- example: `sed 's/Hello/Hi/g' test.txt` to replace "Hello" in `test.txt` with "Hi"    
[more sed tutorial](https://github.com/mikeizbicki/ucr-cs100/tree/2015winter/textbook/using-bash/sed)
#### awk
finds and replaces text by searching through files for lines that have a pattern
- example: `awk 'pattern {action}' test.txt`
#### cp
copy a file/ files into other folder
- example: `cp file1.txt folder2` `cp -r folder1 folder2`
- `r`: to copy all files in the folder to new one
#### mv 
move a file/ files or file's content
- example: `mv file.txt folder`, `mv file1.txt file2.txt`
#### rm
remove files to bin
- example: `rm file1.txt`
- `r`: delete process includes all files in a directory
- `f`: ignore error to delete files
#### ln
create shortcut for file, so when there are changes in shortcut files, the changes also happen in original file
- example: `ln -s file.txt linked_file.txt`
#### touch 
create a blank file
- example: `touch text.txt`
#### vim
create file if not exist and edit text there 
- example: `vim text.txt`
- `esc` >> write `:q` to exit
#### nano
create file if not exist and edit text there 
- example: `nano text.txt`
- `ctrl + x` >> write `y` >> `enter` to exit and save 
#### source
execute bash files
- example: `source dir1/test.sh`
update changes like change paths, set new path to a machine profile
- example: `source ~/.bashrc` after `export JAVA_HOME="/lib/java-11-openjdk"`
#### wget and curl
extract data from URL 
- example: `wget https://source.com/123.txt` `wget -O new_name.txt https://source.com/123.txt`
- `O`: save a downloaded file as new name
- example: `curl https://source.com/123.txt` `curl -o new_name.text https://source.com/123.txt`
- `o`: save a downloaded file as new name
#### zip and unzip
`zip` compress folder into zip files
`unzip` extract content in zip file
- example: `zip name.zip folder1`, `zip name.zip file1 file2`
- example: `unzip name.zip`, `unzip -l name.zip`
- `l`: to see the content of a zip file without extracting
#### tar
- example: `tar -xf dir1.tar`, `tar -cf dir1.tar foo bar`
- `c`: create a tar file
- `x`: extract a tar file
- `v`, `verbose`: list processed files
- `z`: extract only gzip
- `f`: extract chosen files  
#### ping
tests a network connection
- example: `ping google.com`
#### git
a version control system that is commonly used in the industry and in open source projects    
[more git tutorial](https://github.com/mikeizbicki/ucr-cs100/tree/2015winter/assignments/lab/lab1-git)
#### nc
short for netcat, a utility used to debug and investigate the network    
[more netcat tutorial](https://github.com/mikeizbicki/ucr-cs100/tree/2015winter/textbook/using-bash/nctutorial)
#### pip 
package manager for python
- `freeze`: show all installed packages
#### true
always returns the exit status zero to indicate success
- example: 
  ```
  true
  echo $?   # return 0
  ```
#### false
always returns the exit status non-zero to indicate failure
- example: 
  ```
  true
  echo $?   # return 0
  ```
#### ps
short for process status, prints out information about the processes running
- example : `-ps`
  - process identification number (PID)
  - terminal type (TTY),
  - how long process has been running (TIME)
  - name of command that launched the process (CMD)

## Permission
use `ls -l` to print out permission of each file and other information
### Commands
#### whoami
show a current user
#### chmod
change a file's permission
- example: `chmod 444 file.txt`, `chmod ug+rw test.txt`
- `444` = `100100100` = `r--r--r--` or read only
  - first three for who owns the file or `u`
  - middle three for group's member or `g`
  - last three for anyone not in the first two categories or `o`
  - `a` for all users
- `7` = `111` = `rwx` 
  - means it has a <U>read</U>, <U>write</U> and <U>execute</U> permission
- `+`: give following permission
- `-`: deny following permission


## Keyboard Shortcuts
| Shortcut	| Description                       |
|-----------|-----------------------------------|
| CTRL-A	  | Move cursor to beginning of line  |
| CTRL-E	  | Move cursor to end of line        |
| CTRL-R	  | Search bash history               |
| CTRL-W	  | Cut the last word                 |
| CTRL-U	  | Cut everything before the cursor  |
| CTRL-K	  | Cut everything after the cursor   |
| CTRL-Y	  | Paste the last thing to be cut    |
| CTRL-_	  | Undo                              |
| CTRL-L	  | Clears terminal screen            |