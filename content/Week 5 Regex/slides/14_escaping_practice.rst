Escaping practice
=================

.. quizdown:: 

    ## Which definitions of ```s``` will cause ```re.findall(r"\don't", s)``` to return a non-empty list?

    - [ ] ```s = "don't"```
    - [x] ```s = "1on't"```
    - [ ] ```s = "do not"```
    - [x] ```s = "0on't"```

.. free-r:: 
    :answer: ['-', ']', '^']

    # Question 2

    What is the result of ```re.findall("[]^-]", "we're learning about hy-phens and [square brackets] and circumflex^caret")```



.. quizdown:: 

    ## Which of the following match the regular expression ```\d.\d\d```?

    - [x] ```3.14```
    - [ ] ```1.5```
    - [x] ```2e23```
    - [ ] ```10x5```

    ## Which of the filenames is given by regular expression "task.\.py"
    
    - [x] ```task1.py```
    - [x] ```task2.py``` 
    - [ ] ```task3_py```
    - [ ] ```task_3_py.zip```