# ToDo-app-CLI
A simple and lightweight Python ToDo app accessible from the command line.
A Python CLI program that reads, deletes, and adds tasks to a todo list. Implements typer and datetime libraries for CLI and time logging in todo items.
## Features
- Add new tasks to a numbered list from command line
- Read tasks from list
- Delete tasks when finished
- Each task includes deadline to minute and countdown until deadline
## Installation
Clone this repository:
    git clone https://github.com/nyblotl-mm/ToDo-app-CLI.git
Change directory to cloned repository:
    cd ToDo-app-CLI
Install dependencies (typer):
    pip install datetime
    pip install typer
## Usage
Every available command must be preceded by `python todo_app.py`. 
### Available Commands
`python todo-app.py --help` will display all commands for todo-app.py.
### add
`python todo-app.py add "[TEXT]"` will begin the creation of a new task. The terminal will prompt you to enter a deadline in dd/mm/yyyy format and then a time in the hh:mm format.
Examples:
    python todo_app.py add "CS 243 Final"
    deadline?(dd/mm/yyyy): 13/12/2025
    at?(HH:MM): 23:59
    python todo_app.py add "Order Grandma's Christmas present"
    deadline(dd/mm/yyyy): 24/12/2025
    at?(HH:MM): 23:59
### read
`python todo-app.py read` will display a list of previously added tasks.
Example:
    python todo_app.py read
    1 . 13/12/2025 at 23:59 CS 243 Final

    Time left is: 1:45:01.449881
    2 . 24/12/2025 Order Grandma's Christmas present

    Time left is: 11 days, 1:45:01.4499881
### delete
`python todo-app.py delete [TASK NUMBER]` will remove the specified task from the list.
Example:
    python todo_app.py delete 2
    python todo_app.py read
    1 . 13/12/2025 at 23:59 CS 243 Final

    Time left is: 1:39:41.215254
## Structure
All commands are performed in `todo_app.py` and he task list is stored in `tasks.txt` in `ToDo-app-CLI`.

ToDo-app-CLI
├License
├README.md
├tasks.txt
├todo_app.py