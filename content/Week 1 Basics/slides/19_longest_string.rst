Longest String
==============

Consider the function len

``len(s)``

Takes a string s and returns the number of characters in the string.

In this challenge, the input is two strings, one on each line. You should define a variable ``longer_length`` that stores a number that's the length of the longer string.

The first string is stored in the variable ``str1``, and the second in the variable ``str2``.

**Sample Input:**

.. code-block::

    longer
    short

**Sample Output:**

.. code-block::

    6

.. challenge::
    :tester: /_static/cs515_challenges/Week1/Challenge8/longest_test.py

    # define longer_length
    #   it's the longer of the two lengths of the inputs
    #     str1 and str2