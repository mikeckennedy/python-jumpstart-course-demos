# Working with virtual environments on Windows

Unfortunately, the windows installer doesn't provide full parity with the richer setup on unix-based systems (namely macOS and Linux).

Here are a few tips to help.

## Checking active versions

In the course, you see me using the `which` command. Windows has an equivalent command called `where`. 

This has nothing to do with Python's setup of course, but often you need that command so we start here.

## Activating

Once you've created a virtual environment via

`python -m venv FOLDER_NAME`

(Make sure this is python 3: `python -V` -> 3...)

You activate it differently. It's `activate.bat` is in scripts not bin (why?):

`FOLDER_NAME/scripts/activate.bat`

## Enabling `python3` and `pip3` commands

As noted above, `pip3` and `python3` are commands on unix systems but not windows (why?).

But you can easily create them. Just create two batch files and put them somewhere that is in your path (e.g. the same folder that contains python.exe for v3?).

**pip3.bat**
`pip.exe`

**python3.bat**
`python.exe`

That will run the local python and pip or the one first in your path depending where you locate the files.

This may make following along exactly with my commands easier.



