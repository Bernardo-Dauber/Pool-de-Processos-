# Pool of Process 

This project implements a process management system in Python that allows creating, executing, and managing different types of processes, such as computing, writing, reading, and printing processes.


### ⚠️ Work in Progress

This project is still a work in progress and is not fully functional. There are known bugs and unfinished features, so it may not behave as expected in all scenarios. Use with caution and feel free to contribute to its development.

### Known Issues

- Some processes may not execute correctly or produce the expected output.
- The `CarregarFile` method does not fully support all process types.
- The system may not handle certain edge cases properly.

**If you encounter any issues, feel free to report them or contribute fixes.**

## 💡 Project Structure

The system consists of several classes, each representing a specific type of process:

- **Process**: The base class for all processes, containing common attributes like `pid` (process identifier) and `tipo`.
- **ComputingProcess**: Processes arithmetic expressions (addition, subtraction, multiplication, division) and displays the result.
- **WritingProcess**: Writes expressions to a text file.
- **ReadingProcess**: Reads expressions from a text file, creates instances of `ComputingProcess` from the expressions read, and adds them to the process list.
- **PrintingProcess**: Displays the details of all processes in the process list.

## 🔨 Features

### Main Menu

The system offers a main menu with the following options:

1. **Create Processes**: Allows creating new processes of different types.
2. **Execute Next Process**: Executes the next process in the queue.
3. **Execute Specific Process**: Allows selecting a specific process to execute based on its `pid`.
4. **Save Process Queue**: Saves the current list of processes to a text file.
5. **Load Processes**: Loads processes from a text file into the process list.
0. **Exit**: Exits the system.

### Process Creation

In the process creation menu, you can choose from the following process types:

- **ComputingProcess**: Prompts for an arithmetic expression and adds it to the process list.
- **WritingProcess**: Prompts for an expression to be written to a text file.
- **ReadingProcess**: Reads expressions from a text file and creates instances of `ComputingProcess` from them.
- **PrintingProcess**: Prints the details of all processes in the list.

### Process Execution

- **Execute Next Process**: Removes and executes the first process from the process list.
- **Execute Specific Process**: Allows selecting and executing a specific process by its `pid`.

### Process Persistence

- **Save Process Queue**: Saves the process list to a text file (`computation_2.txt`).
- **Loads processes** from the text file and adds them to the process list.

## Final Considerations
This system is a simple example of how to manage different types of processes and how to maintain data persistence using files. It can be expanded with new functionalities as needed.


## How to Run

To run the system, simply execute the main script:
    
```bash
python3 sistema_processos.py
