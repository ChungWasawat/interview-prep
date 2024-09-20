# Keep this in mind
## try to follow these concepts in Python
* Multithreading and concurrency
    - Running and handling multiple threads in parallel and making sure they run without deadlocks or race conditions is a skill every programmer should develop.
    - Learn: multithreading, race conditions, live locks, deadlocks, mutexes, semaphores
* Immutability
    - The amount of robustness immutability provides to a program in spite of being such a simple concept is often overlooked by new programmers and not taught in tutorials or university classes.
    - Learn: [more](https://www.freecodecamp.org/news/write-safer-and-cleaner-code-by-leveraging-the-power-of-immutability-7862df04b7b6/)
* Debugging techniques
    - Debugging is a fundamental part of the programming process, yet it's often an area where students struggle.
    - Learn: Debuggers, logging, profiling, rubber duck debugging
* Performance optimization
    - Performance optimization is an important aspect of programming, but it's often not taught until later in a computer science curriculum. 
    - Learn: Caching, Parallel processing, algorithm optimization, memory optimization
* Testing and quality assurance
    - Testing and quality assurance are crucial for ensuring that software is reliable and meets the needs of its users.
    - Learn: Unit tests, integration tests, testing frameworks, tools

## Writing memory efficient data pipelines in Python
1. Using generators to not store values in memory
    - use `(tuple)` instead of `[list]` or use `yield` instead of `return`    

**When pulling a large dataset (either from a DB or an external service) into your python process, you will need to make a tradeoff between Memory and Speed**
- Memory: Pulling the entire data will cause out of memory errors.
- Speed: Fetching one row at a time from the database will incur expensive network calls.   
see example [here](https://www.startdataengineering.com/post/writing-memory-efficient-dps-in-python/)    


|       pros                                       |        cons                                      |
|:-------------------------------------------------|:-------------------------------------------------|
|No need to install or maintain external libraries |Parallelizing data processing is an involved process.                           |
|Native python modules have good documentation.    |Sorting and aggregating will require you to keep the data in memory.            |
|Easy to use                                       |Joining multiple datasets will require complex patterns and handling edge cases.|
|Since most of the distributed data processing frameworks support python, it’s relatively easy to port this code over if needed.|   |

2. Using distributed frameworks
- If you think that your data will grow significantly in size, complexity or that the requirements for speed of data processing will be high     

|           pros                              | cons                                                      |
|:--------------------------------------------|:----------------------------------------------------------|
|Most data processing functions are in-built. |Can be hard to install, setup clusters, and upgrade.       |
|Can easily scale to large data sets.         |If cluster resources are not allocated appropriately, the processing may fail.                 |
|If you are in a python ecosystem, it’s very easy to use any of these frameworks.|They have their own quirks and gotchas of which to be aware.|


