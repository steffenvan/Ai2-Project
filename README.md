# Ai2-Project

note : please use the following set up to make sure everything works fine :

- have your Ai2-Project saved in the same directory as the root directory of Semafor
- in src, create path.py, which should contain the absolute path to the Ai2-Project folder.

## Semafor
So far we have managed to run the frame-semantic parser on the output of the dummy
file `src/article.xml`.
### Only new lines
It is important to note that the parser only works for files with no empty new lines;
hence the neccesity for the pre-processing files in the `src` folder.

### Results
To see the result from parsing the `article.xml` file using Semafor, there is
a file located in `results/temp-res.txt` to show the immediate frame-semantic information.

# src files :

pipeline.py :
run this script every time you added new xml files to the data/xml/ folder. It will run the preprocessing steps and create the associated txt and json files.

explore.py : 
this file contains useful data exploration functions

extraction.py : 
contains functions to extract specific sections from text or json files.

preprocess_functions.py :
contains all the functions called by pipeline.py and article.py

