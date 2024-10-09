# Bash
* Bash is a script of shell commands, with file extension `.sh` 
* At the beginning of the file, usually has 
    * `#!/usr/bash`
    * `#!/bin/bash`
* basic command `bash scriptname.sh arg1 arg2`
    * `$1` get `arg1`, `$2` get `arg2`
    * `$@` get `arg1` and `arg2` 
    * `$#` get 2 as the amount of arguments
* variables
    * `var1="sam"` assign the value `"sam"` to `var1`. Note that there must be no space between = 
    * `echo "There are $var1 items"`  will print There are 6 items 
* quotation marks
    * 'sometext' interpreted literally
    * "sometext" interpreted literally except $ and ` 
    * \`sometext` interpreted as bash command and return STDOUT into a variable
    * \$(command) is equivalent to \`command`  but the \$(command)  is used more in modern applications
* numerical calculation
    * `expr 1 + 4` get 5
    * `expr 11 + 3.5` get error as expr takes only int into account
    * `echo "11 + 3.5" | bc` get 14.5 as bc (basic calculator) can do more 
    * `echo "11/3" | bc` get 3 since the decimal place has not been defined
    * `echo "scale=3; 11/3" | bc` get 3.666 
    * `$((11+3))`  is `expr 11 + 3` 
* array
    * numerical-indexed
        * `declare -a my_array` to define empty array 
        * or `my_array=(1 2 3)` to provide values while defining array. Note that space is used as separator
        * `echo ${my_array[@]}` get (1 2 3) 
        * `echo ${#my_array[@]}`  get 3 (length of array)
        * `echo array[@]:N:M` where N is the starting idx and M is how many elem to return

## If Else
```
if [ condition ]; then
  # some code
else
  # other code
fi
```
* special flags
    * `-e` if the file exists
    * `-s` if the file exists and has size greater than zero
    * `-r` if the file exists and readable
    * `-w` if the file exists and writable
* combine conditions with `&&` for AND and `||` for OR

## For Loops
```
# print 1,2,3
for x in 1 2 3
do
  echo $x
done

# print a value in {START .. STOP .. INCREMENT} like range(START, STOP, INCREMENT)
for x in {1 .. 10 .. 2}
do
  echo $x
done

for book in $(ls books/ | grep -i 'air') 
# use shell within a shell with $() 
# resulting files with 'air' in their names inside the book directory
do
  echo #book
done

# print 5 or others with if else
for i in {1..10}; do
  if [ $i -eq 5 ]; then
    echo "Number is 5"
  else
    echo "Number is $i"
  fi
done
```

