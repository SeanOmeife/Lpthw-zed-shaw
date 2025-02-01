## What I learned in this chapter

The formatter variable is called by a function which turns the variable into strings.

What python does is take the formmater string defined on line 1

Calls its format function (which is similar to telling it to do a command named "Format")

It then passes four arguments which match up with the four {}s  in the formatter variable

This results in a new string where the {} is replaced with the four variables

it is written as print(formatter.format()) and not print(format.formatter()) because formatter is a variable that holds the string template, and format is the method being used on the string

Therefore the formate is "print(variable.method()) meaning that you're calling the format method on the formatter variable, and then printing the result.