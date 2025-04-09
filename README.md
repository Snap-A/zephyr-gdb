# Zephyr-gdb
Python module for user-friendly view Zephyr kernel objects in GDB.

(This code was inspired by https://github.com/espressif/freertos-gdb)

## Requirements

GDB must built with python 3.6+ support

Check your GDB with command:

```bash
gdb -q -ex "python print('OK' if sys.version_info.major==3 and sys.version_info.minor>=6 else 'NOT SUPPORTED')" -ex "quit"
```

## Install
Clone this project to your host. While at the root of the clone tree, run:

```
python setup.py install [--user]
```

## Run
Start GDB and run the command
```
(gdb) python import zephyr_gdb
```

## Commands
The ```zephyr``` command was added, with these subcommands
```
(gdb) zephyr
"zephyr" must be followed by the name of a subcommand.
List of zephyr subcommands:

zephyr thread --  Generate a print out of the current threads and their states.

Type "help zephyr" followed by zephyr subcommand name for full documentation.
Type "apropos word" to search for commands related to "word".
Type "apropos -v word" for full documentation of commands related to "word".
Command name abbreviations are allowed if unambiguous.
```
