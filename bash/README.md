# Unix
<U>What is shell?</U> 

- Bourne-Again SHell or call shortly as shell
- other shell: Zsh of MacOS

<U>Symbols</U>

- `/` = root
- `~` = home
- `.` = current directory
- `..` = parent directory
- `*` = wildcard (can be anything)
- `|` = used after a command to tell computer to do the next command
- `$` = refer variable or substitute command
    ```
        1.
        name="Alice"
        echo $name          # Outputs: Alice
        2.
        current_date=$(date)
        echo $current_date  # Outputs the current date and time
    ```

## for loop and if else
```
for i in {1..10}; do
  if [ $i -eq 5 ]; then
    echo "Number is 5"
  else
    echo "Number is $i"
  fi
done
```

## common commands
### pwd
show a current directory
### whoami
show a current user
### ls
show files in current directory
- example: `ls`, `ls directory1`

- `l`: show more details like users, memory used, etc.
- `h`: use with `l` to make a list easier to read 
- `a`: show hidden files
### echo
show text on terminal, or add text into a file       
- example: `echo test`, `echo test > test.txt`
### wc
show a number of words in a file
- example: `wc text.txt`
- `l`: to count lines instead of words
### cat
show file's content on terminal or concatenate 2 files into new one
- example: `cat file.txt`, `cat file1.txt file2.txt >> new_file.txt`
### more 
show all file's content
- exmaple `more file.txt`
### less
similar to more but split content to show on terminal 
- `enter`+`q` to exit and `spacebar` to go to the next page
### grep
find a phrase in text or files
### mkdir and rmdir
create blank directory/ remove blank directory
- example: `mkdir -p folder1`, `rm folder1`
- `p`: to replace existed folders with new one
### cp
copy a file/ files into other folder
- example: `cp file1.txt folder2` `cp -r folder1 folder2`
- `r`: to copy all files in the folder to new one
### mv 
move a file/ files or file's content
- example: `mv file.txt folder`, `mv file1.txt file2.txt`
### rm
remove files to bin
- example: `rm file1.txt`
- `r`: delete process includes all files in a directory
- `f`: ignore error to delete files
### touch 
create a blank file
- example: `touch text.txt`
### vim
create file if not exist and edit text there 
- example: `vim text.txt`
- `esc` >> write `:q` to exit
### nano
create file if not exist and edit text there 
- example: `nano text.txt`
- `ctrl + x` >> write `y` >> `enter` to exit and save 
### wget and curl
extract data from URL 
- example: `wget https://source.com/123.txt` `wget -O new_name.txt https://source.com/123.txt`
- `O`: save a downloaded file as new name
- example: `curl https://source.com/123.txt` `curl -o new_name.text https://source.com/123.txt`
- `o`: save a downloaded file as new name
### zip and unzip
`zip` compress folder into zip files
`unzip` extract content in zip file
- example: `zip name.zip folder1`, `zip name.zip file1 file2`
- example: `unzip name.zip`, `unzip -l name.zip`
- `l`: to see the content of a zip file without extracting
### tar
- example: `tar -xf dir1.tar`, `tar -cf dir1.tar foo bar`
- `c`: create a tar file
- `x`: extract a tar file
- `v`, `verbose`: list processed files
- `z`: extract only gzip
- `f`: extract chosen files  
### chmod
change a file's permission
- example: `chmod 444 file.txt`
- `111` = `rwx` means it has a <U>read</U>, <U>write</U> and <U>execute</U> permission
- first three for who owns the file, middle three for group's member, last three for anyone not in the first two categories
### source
execute bash files
- example: `source dir1/test.sh`
update changes like change paths, set new path to a machine profile
- example: `source ~/.bashrc` after `export JAVA_HOME="/lib/java-11-openjdk"`
### pip 
package manager for python
- `freeze`: show all installed packages
### ln
create shortcut for file, so when there are changes in shortcut files, the changes also happen in original file
- example: `ln -s file.txt linked_file.txt`
