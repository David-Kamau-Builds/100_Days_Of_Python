# Day 24: Files, Directories, and Paths

## Project: Automated Mail Merge

This project demonstrates how to automate a repetitive task using Python's file I/O capabilities. The script reads a list of names from one text file and a generic letter template from another. It then combines them to create personalized letters for each person, saving each completed letter as a separate `.txt` file in an output directory.

This is a practical example of how programming can be used to handle data and automate document creation.

## Key Concepts Practiced

This project focuses on reading from and writing to files, as well as managing file paths.

### 1. Reading Files

The `open()` function is used with the `with` keyword to safely open and automatically close files.
*   `readlines()`: Reads all lines from a file and returns them as a list of strings. This was used to get the list of names.
*   `read()`: Reads the entire content of a file into a single string. This was used to get the letter template.

### 2. Writing to Files

New files are created by opening a path in write mode (`mode="w"`). The `write()` method is then used to save the content of the newly generated letter into the file.

### 3. String Manipulation

The `strip()` method is used to remove leading/trailing whitespace (like the newline character `\n`) from the names read from the file. The `replace()` method is used to swap a placeholder string (e.g., `[name]`) in the template with an actual name.

### 4. Relative File Paths

The script uses relative paths (e.g., `./Input/Names/invited_names.txt`) to access files located in different subdirectories. This makes the project structure organized and portable, separating input files, output files, and the main script.