# functions.py

import time
from decorators import time_logger

@time_logger
def slow_function(seconds):
    """
    Simulates a slow function by sleeping for a specified number of seconds.

    :param seconds: Number of seconds to sleep.
    :return: A completion message.
    """
    time.sleep(seconds)
    return "Function complete!"

@time_logger
def add(a, b):
    """
    Adds two numbers.

    :param a: First number.
    :param b: Second number.
    :return: Sum of a and b.
    """
    return a + b

@time_logger
def greet(name, greeting="Hello"):
    """
    Greets a person with a specified greeting.

    :param name: Name of the person.
    :param greeting: Greeting message.
    :return: A personalized greeting message.
    """
    return f"{greeting}, {name}!"
