File: moderation_bot/utils/error_handling.py

Contents:
'''
# error_handling.py

import logging

# Set up logging configuration
logging.basicConfig(filename='error.log', level=logging.ERROR)

def log_error(error_message):
    """
    Logs an error message to the error.log file
    :param error_message: The error message to log
    """
    logging.error(error_message)

def handle_error(exception):
    """
    Handles an exception by logging the error and printing a user-friendly message
    :param exception: The exception to handle
    """
    error_message = f"An error occurred: {exception}"
    log_error(error_message)
    print("Oops! Something went wrong. Please try again later.")
'''

Explanation:
- The error_handling.py file contains functions for logging errors and handling exceptions in the moderation bot.
- The log_error function logs an error message to the error.log file.
- The handle_error function logs the error message and prints a user-friendly message to the user when an exception occurs.