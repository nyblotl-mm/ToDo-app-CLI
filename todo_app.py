import typer
import datetime
from datetime import date
app=typer.Typer()
@app.command()
def add(t: str):
    """
    Adds a task to tasks.txt

    The function takes three rounds of text input with the initial string serving 
    as the name of the task. The second being the deadline in format dd/mm/yyyy. 
    The final string being the deadline in format hh:mm.

    Args:
        t: (str): The inputted strings of the user, the first being
        the name of the task, the second being the deadline in dd/mm/yyyy, the
        final being the deadline in hh:mm.
    
    Examples:
        >>> python todo_app.py add "Task 1"
        deadline?(dd/mm/yyyy): 
        >>> 01/01/2000
        at?(HH:MM):
        >>> 12:00
        >>> python todo_app.py read
        1 . 01/01/2000 at 12:00 Task 1

        Overdue

        >>> python todo_app.py add "Task 2"
        deadline?(dd/mm/yyyy):
        >>> 01/01/2026
        at?(HH:MM):
        >>> 11:59
        >>> python todo_app.py read
        1 . 01/01/2000 at 12:00 Task 1

        Overdue
        2 . 01/01/2026 Task 2

        Time left is: 18 days, 13:05:16.122053
    """
    time=''
    time = typer.prompt("deadline?(dd/mm/yyyy)")
    at=''
    at = typer.prompt("at?(HH:MM)")
    t=time+" at "+at+" "+t+'\n'
    file1=open("tasks.txt",'a')
    file1.write(t)
    file1.close()
@app.command()
def read():
    """
    Displays added tasks to user

    Reads out tasks from .txt in an ordered list, printing deadline and time until
    deadline based on system clock.

    Examples:
        >>> python todo_app.py read
        1 . 01/01/2000 at 12:00 Task 1

        Overdue
        2 . 01/01/2026 Task 2

        Time left is: 18 days, 13:05:16.122053

        >>> python todo_app.py read
        1 . 29/11/2021 at 23:01 Complete CS101 assignment

        Overdue
        2 . 30/11/2021 at 23:02 Complete CS102 assignment

        Overdue
        3 . 01/12/2021 at 23:03 Complete CS103 assignment

        Overdue
    """
    today1 = datetime.datetime.now()
    file1=open("tasks.txt",'r')
    res=file1.readlines()
    file1.close()
    for i in range(0,len(res)):
        u=res[i]
        d=int(u[0]+u[1])
        m=int(u[3]+u[4])
        y=int(u[6]+u[7]+u[8]+u[9])
        h=int(u[14]+u[15])
        min=int(u[17]+u[18])
        now=datetime.datetime(y,m,d,h,min)
        lefttime=str(now-today1)
        print((i+1),". ",res[i])
        if(lefttime[0]=="-"):
            print("Overdue")
        else:
            print("Time left is:",lefttime)
@app.command()
def delete(num: int):
    """
    Deletes a task from tasks.txt

    Args:
        num (int): The index of the task in the list. Assumed to be the read index.

    Examples:
        >>> python todo_app.py read
        1 . 01/01/2000 at 12:00 Task 1

        Overdue
        2 . 01/01/2026 Task 2

        Time left is: 18 days, 13:05:16.122053
        >>> python todo_app.py delete 1
        >>> python todo_app.py read
        1. 01/01/2026 Task 2

        Time left is: 18 days, 13:05:10:122054

        >>> python todo_app.py read
        1 . 29/11/2021 at 23:01 Complete CS101 assignment

        Overdue
        2 . 30/11/2021 at 23:02 Complete CS102 assignment

        Overdue
        3 . 01/12/2021 at 23:03 Complete CS103 assignment

        Overdue
        >>> python todo_app.py delete 2
        >>> python todo_app.py read
        1 . 29/11/2021 at 23:01 Complete CS101 assignment

        Overdue
        2 . 01/12/2021 at 23:03 Complete CS103 assignment

        Overdue
    """
    with open(r"tasks.txt", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        for number, line in enumerate(lines):
            if number not in [num-1]:
                fp.write(line)
if __name__ == "__main__":
    app()
