# Python Synchronization Script

Usage: 

`python OneWaySync.py <source_folder> <destination_folder> <log_file>` 

Do not wrap the path with quotes or <>.

Pseudocode:

- Setup the MD5 function.
    - Takes two arguments: filename, chunksize

- Setup the synchronization function (wrapped in a try block)
    - Checks directory of destination folder (and creates it if it does not exist)
    - Opens the log file
    - Iterates over the files in source folder and does the following checks:
        - checks if they exist in destination folder.
        - MD5 check.
        - If either are true, file will be added and logged.
    - Check for files present in destination but not in source.
        - Delete files present in destination but not in source (and log the action).
    - Check for error (exception).
    - Check arguments are correct.
    - Call the function.
