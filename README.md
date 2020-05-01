Journal
=======

## Overview

Journal is a simple Sublime Text plugin that makes it easy to create Journal files for logs, notes, diary, daybooks.... . These files are saved in single location for easy searching and access later.
The files are structured hierachical by date (year\month\day\yyyymmdd.*extension* ). Due to the file naming convention (yyyymmdd) you can - for example - sort the file names by asc and generate a date-ordered summary file.

## Usage
### Basic Usage
1. In Sublime Text Go to ```Open today's Journal File        Ctrl+Shift+Alt+J``` 
2. A new file is opened. The file is named "*yyyymmdd*.*extension*". *yyyymmdd* is evaluated by current date. *extension* is a user-configurable extension. (e.g. ```.md``` for markdown)  

  **Example**  
  ```File > Open today's Journal File        Ctrl+Shift+Alt+J``` to open "[journalroot]\2020\05\20200501.md". Save the file.  

## Configuration
By default the journalroot will points to ```~/Documents/Journal```. The default extension is ```.md```. 
You can change these settings using the following options in your package settings:
```
{
    "save_path": "~/Documents/Journal",
    //"save_path": "~/Foo/Bar/Diary/${file_base_name}",
    //"save_path": "${folder}\\journal",
    //"save_path": "${project_path}\\journal",
    //"save_path": "xyz",
    "extension" : ".md",
    "use_dayfolder" : "false"
}
```
You can set use_dayfolder to "true" to create a folder for each single dayfile. The default setting groups the dayfiles into the matching month directory.


## details about ```save_path```

- The folder structure is created automatically.

- Folders starting with ```~``` are resolved to the user home directory.

- The ```save_path``` can contain variables. See https://www.sublimetext.com/docs/3/api_reference.html#sublime.Window extract_variables() to find the available variable names.
These variable-names has to be enclosed in ```${...}```
Refer https://www.sublimetext.com/docs/3/build_systems.html#variables to find a short description for the listed variable names. 

- A simple string value (e.g. "xyz") set the journal directory to ```~/Documents/xyz``` 
