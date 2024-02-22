# Import the `sys` module for accessing system-related information.
import sys

# Define a function called `error_message_detail` that takes two arguments:
# `error`, which is the error message, and `error_detail`, which is an object containing detailed information about the error.
def error_message_detail(error, error_detail: sys):
    
    # Unpack the `error_detail` object into three variables: `_, _, exc_tb`.`_` is used to ignore the first two values, which are not needed.
    # `exc_tb` contains information about the traceback.
    _,_,exc_tb = error_detail.exc_info()
    # Extract the name of the file where the error occurred from the traceback.
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Create an error message string containing information about the exception, such as the filename, line number, and error message.
    error_message = "Error occured in python script name [{0}] line number[{1}] error_message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    # Return the error message.
    return error_message

# Define a custom exception class called CustomException, which inherits from the built-in Exception class.
class CustomException(Exception):
    # Define the constructor for the `CustomException` class.
    # It takes two arguments: `error_message`, which is the error message, and `error_message_detail`,
    # which is an object containing detailed information about the error.
    def __init__(self, error_message, error_message_detail:sys):
        # Call the constructor of the parent class (`Exception`) with the `error_message` argument.
        super().__init__(error_message)
        # Store the detailed error message in the `error_message` attribute of the exception object.
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    # Define the `__str__` method for the `CustomException` class.
    # This method is called when the exception is converted to a string.
    def __str__(self):
        # Return the detailed error message when the exception is converted to a string.
        return self.error_message


