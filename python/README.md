# Keep this in mind
## Coding Pattern
### 1. Functional design
Principles for "writing functional code"
- Atomicity: A function should only do one task.
- Idempotency: If you run the code multiple times with the same input, the output should be the same. In the case of storing the output in an external data store, the output should not be duplicated.
- No side effects: A function should not affect any external data (variable or other) besides its output.
- Additional:
    - [higher order functions](https://www.geeksforgeeks.org/higher-order-functions-in-python/)
    - [functional composition](https://en.wikipedia.org/wiki/Function_composition_%28computer_science%29)
    - [referential transparency](https://blog.rockthejvm.com/referential-transparency/)
### 2. Factory pattern
how the factory pattern works:
- Use a factory pattern when multiple pipelines follow a similar pattern.
- A factory will be responsible for creating the appropriate (Reddit, Twitter, or mastodon) etl object
- Prevents complex `if..else` statements that are hard to manage and provides a standard interface to interact with multiple similar pipelines.
- You can define a standard set of methods that all the ETL classes must implement. The common method’s names and signatures (inputs, & outputs) are called abstract interfaces since that defines how we interact with any ETL implementing the standard. The actual implementation is called the concrete implementation

pros 
+ If you have multiple similar etls, a factory can significantly improve code consistency and make it much easier to evolve your pipelines. 
+ Using factory patterns to establish connections to external systems will enable easier testing. E.g., a db factory allows you to use sqllite3 for dev testing and pg for prod easily. You can also put your spark session behind a factory to use less executor in dev and higher mem setting in prod, etc.

cons 
+ If you use the factory method to define data pipelines that are inherently different (e.g., ETL v ELT or API data pulls vs. S3 -> S3 data transfer, etc.), it will make the code highly complex and brittle. Only use a factory if the underlying data pipelines have a similar structure.
+ Using the factory method when there are only one or two data pipelines (without any signs of more data pipelines) is premature optimization and can potentially slow down development due to abstract interface limiting development velocity.
### 3. Strategy pattern
Strategy Pattern, which allows our code to choose one way of transformation among multiple methods of transformations (aka chose one strategy among various strategies - e.g. choose mean over mode, avg).
### 4. Singleton, & Object pool patterns
- Use a singleton pattern when your program should only have one object of a class for the entirety of its run. The singleton pattern is commonly used in database connections, logs,
- In Object pool pattern, instead of being able to use only one single object, you can use an object from a pool of objects. The pool size is set depending on the use cases. Object pool pattern is commonly seen in applications that have multiple incoming requests and need to communicate with the database quickly(e.g., backend apps, stream processing).
- [example of connection pool](https://www.psycopg.org/psycopg3/docs/advanced/pool.html)
- [more details about singleton](https://stackoverflow.com/questions/12755539/why-is-singleton-considered-an-anti-pattern)

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

## Miscellaneous
1. Project Structure    
A well-organized [project structure](https://docs.python-guide.org/writing/structure/) ensures logical imports and allows for easier navigation of the codebase.
2. Naming    
check more on [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
3. Automated formatting, lint checks, & type checks     
- do automation with these packages `black`, `isort`, `flake8`, and `mypy`
- `Makefile` can help combine commands of those packages in a single command [Makefile example](https://github.com/josephmachado/socialetl/blob/main/Makefile)
4. CI/CD with `Githooks`    
- [CI/CD example](https://www.startdataengineering.com/post/ci-data-test/#2-ci)
- [Github flow](https://docs.github.com/en/get-started/using-github/github-flow) 
- [Git action](https://github.com/features/actions)

## learn more about these concepts in Python
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
