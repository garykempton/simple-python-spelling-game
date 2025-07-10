# simple-python-spelling-game
A simple spelling game in Python using `random.choice`, `input`, and basic string methods.

I'm currently learning Python and revisiting some of my earlier JavaScript knowledge from before the pandemic.

The idea for this project came from watching my son play a spelling game. I wanted to build a similar project for an ESL program I'm working on.

To begin, I asked ChatGPT to generate some initial code based on a basic prompt. I then studied the code, line by line, to understand how it worked. After that, I began modifying and expanding it myself.

Python has an extensive library but each module needs to be imported for anything that is required of it for the project.
So import random.

Next... since I wanted the spelling test to be generating random words for the student, I needed a list first ('array' in Javascript) so I could take the words from it.

I placed the score at '0'.

In the function, I needed the program to loop through the list so that all the words could be selected as far as the range would allow.

The rest of the code went as supposed, with corrections made mostly with ':' and proper indentation.
I ran the code, calling the function and it worked.

Then, I modified the code so that each correct answer would add to the score incrementally and display the score after each correct answer given.  Initally it didn't work as I wrongly coded the same variable locally as was globally - the 'score' variable'.  'score' was then changed to 'score += 1'.

Newly improved program.
For a new improvement, ideally the word is spoken on the page, not written. 
This program allowed me to use import random(), the module from python, run a loop, increment a variable, set global and local variables, call a function, use an f string, use linux via the terminal in vsc, and an if/else statement.

What I Practiced

- Importing a module (`random`)
- Creating and using lists
- Looping with `for`
- Using global and local variables
- Taking user input
- Comparing strings with `==`
- Using `f-strings` for dynamic text
- Debugging logic and variable scope
