## Goal
Build a script for generating subjects for a study where the condition can be entered on the commandline.

### feature set
- enter how many subjects you wanna generate
- enter the conditions the subject should be put under
- the entered conditions will be randomly assigned for each subject

The script will generate a csv file for you in the form:
```csv
subjectId|condition 1|condition 2| condition ... | condition n|
subject-1,test,two,meauw,three,one
```