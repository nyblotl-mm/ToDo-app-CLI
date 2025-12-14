## What you contributed: Describe your changes and why they're valuable
I rewrote and restructured README.md to include seperate sections on features, installation, usage and structure. Changed the image based instructions to instead be text based for ease of copy and pasting and faster loading of the page. The features section allows for a brief summary of what the program is capable of. The installation section includes two new commands for installing dependencies. The usage section was mostly directly ported from provided images in the original repository. The structure section was added for a quick and clear demonstration of the file path of the program.

In addition to README.md I also added detailed docstrings to each function in todo_app.py. The docstrings include brief and extended descriptions as needed, 
list the arguments inputted into the function, and list at least two usage examples for each function. The module as a whole also has its own docstring with
a brief and extended descriptions. These docstrings should allow users to very quickly be able to preview what each function does if they decide to also
contribute this project.

## Process: How did you approach this work? What tools did you use?
I decided to exclusively use VSCode when doing this program. I started with README.md first since it stuck to me as being in urgent need of adjustment. In
addition to being the first anyone will see of this repository. I used https://markdownlivepreview.com/ to look at my work before committing.

## Challenges: What difficulties did you encounter and how did you solve them?
A challenge I encountered arose from deciding to tackle README.md first. When I got to the usage section of README.md I realized that I hardly had much of
an idea of what each method did. I navigated this challenge by looking at the original README.md of the file, checking todo_app.py, and testing the program
for myself.

## Learning: What did you learn about open source contribution?
From this project I learned about how open source contribution can serve as an opportunity for people to strengthen their skills in a certain element of coding. In addition, open source contribution provides valuable experience in working with other people's code and understanding how read code that isn't just your own. 

## Future work: What else could be improved in this project?

This project could use clearer commenting within functions and a requirements.txt file for easier installation. The current version of this program assumes the user to have typer and datetime installed onto their device/environment. I would also add a sort function that reorders the tasks to be in order of earliest to latest due date.