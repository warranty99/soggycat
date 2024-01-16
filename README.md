# .SOGCL
My first programming language, just a learning opportunity for more languages in the future, made in python.
## Syntax
Please note this language is NOT turing complete, thanks :)

The Soggycat Command Line, aka SOGCL is a language made for fun, its a way to execute commands on the soggycat command line with more complexity

The first element are the code bearers ```< >``` these guys hold all the code youll write.
The second element are the ```.start``` and ```.end``` these guys hold 1 command, for example: ```echo Hello World!``` which would be in .sogcl:
````
<.startEchoHello World!.end>
Hello World!
````

Spaces dont matter in .sogcl, in fact, they are discouraged as they can add unnecessary spaces to output due to this being my first interpreter.

If you wanna wait, you can do ```wait``` followed by your number: ```wait5```
Wanna rickroll someone? heres that:
```

<.startopn-whttps://www.youtube.com/watch?v=dQw4w9WgXcQ.end>
```
you can use -opn -w then your website to open something in your browser

### Variables
In .sogcl there are 2 kind of variables, sog variables and usr variables.
sog variables are used for the interpreter, they can be changed though its not reccomended, heres how the change i to something else, crashing the interpreter:
```
<.startsoggycat-change-vari99.end>
```
That code changes the sog variable i to 99.

To make a usr variable (only kind that can be created) you do
```
<.startsoggycat-create-usrvarHello=9.end>
```
To print it to the console, you observe the variable
```
<.startsoggycat-create-usrvarHello=9.end.startsoggycat-usrvarHello.end>
9
```
Those are the most important syntax, all the others either dont work (coming soon) or are useless like ```-info``` (yes, the are no loops)

## Execution
To execute your .sogcl code, put the following into the soggTerminal:
```
soggycat-run-sogcl-body<YOUR CODE>
```
The interpreter will interpret and output through the terminal.
