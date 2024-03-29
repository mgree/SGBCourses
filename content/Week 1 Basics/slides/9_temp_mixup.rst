Temperature Conversion Mixup
============================

Below is a short program to convert temperature from Fahrenheit to Celsius. In the input box, a floating point number is given as the Fahrenheit value. We've set up this code challenge so that the input number will be stored in a variable named ``fahrenheit``---we'll learn more about how input in Python works later in the lesson.

The code below tries to convert the ``fahrenheit`` input value into a ``celsius`` value. *However, the output is incorrect if you run the code as it is!*

Identify why the following piece of code does not produce the correct output and fix the expression so that it evaluates appropriately. Do *NOT* change the variable names.

The math formula for converting temperature from fahrenheit to celsius is shown below.

.. image:: /assets/images/cs515/Week1/temp_conv.png

.. challenge::
    :tester: /_static/cs515_challenges/Week1/Challenge3/test_temperature.py

    # Correct the following expression so as convert fahrenheit to celsius appropriately
    celsius = fahrenheit - 32 * 5 / 9
