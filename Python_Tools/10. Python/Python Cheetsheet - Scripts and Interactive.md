Python Cheet Sheet

SCRIPTS - PLAIN TEXT FILE CONTAINING PYTHON CODE 

PS> python script_name.py

PYTHON INTERACTIVE - INTERPRIVE LANAGUAGES CAN BE RUN INTACTIVELY

PS> python
>>> print('Hello World!')

Hello World!

>>> 2 + 5
7

>>> quit()
or
>>> exit()

REDIRECTING THE OUTPUT

PS> python3 hello.py > output.txt

CONCATINATE AND REDIRECTING THE OUTPUT

PS> python3 hello.py >> output.txt

SEARCHING SYS.PATH FOR A MODULE, RUNS ITS CONTENT AS __MAIN__

PS> python3 -m hello
Hello World!

WINDOWS SUPPORTS FILE SCRIPTS FROM FILE SPACES

C:\devspace> hello.py
Hello World!

RUN PYTHON SCRIPTS INTERACTIVELY WITH IMPORT

When the module contains only classes, functions, variables, 
and constants definitions, you probably won’t be aware that 
the code was actually run, but when the module includes 
calls to functions, methods, or other statements that 
generate visible results, then you’ll witness its execution.

>>> import hello
Hello World!

>>> import sys
>>> for path in sys.path:
