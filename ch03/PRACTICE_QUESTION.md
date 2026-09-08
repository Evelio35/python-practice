# Chapter 3: Functions

## Conceptual Review Questions

### Question 1
Why are functions advantageous to have in your programs?
*ANSWER:*
reusability of functions throughout the program.

### Question 2
When does the code in a function execute: when the function is
defined or when the function is called?
*ANSWER:*
When the function is called

### Question 3
What statement creates a function?
*ANSWER:*
def

### Question 4
What is the difference between a function and a function call?
*ANSWER:*
A function call is the invocation of a function. A function is just a set of instructions.

### Question 5
How many global scopes are there in a Python program? How many
local scopes?
*ANSWER:*
1 global scope, and many local scopes.

### Question 6
What happens to variables in a local scope when the function call returns?
*ANSWER:*
The local scope variable is terminated.

### Question 7
What is a return value? Can a return value be part of an expression?
*ANSWER:*
The value a function call evaluates too. Yes.

### Question 8
If a function does not have a return statement, what is the return value
of a call to that function?
*ANSWER:*
None

### Question 9
How can you force a variable in a function to refer to the global variable?
*ANSWER:*
global keyword

### Question 10
What is the data type of None?
*ANSWER:*
NoneType

### Question 11
What does the import areallyourpetsnamederic statement do?
*ANSWER:*
imports that specific module

### Question 12
If you had a function named bacon() in a module named spam, how
would you call it after importing spam?
*ANSWER:*
spam.bacon()

### Question 13
How can you prevent a program from crashing when it gets an error?
*ANSWER:*
Use try and except clauses

### Question 14
What goes in the try clause? What goes in the except clause?
*ANSWER:*
try: the code that could potentially cause error
except: the code that executes if an error