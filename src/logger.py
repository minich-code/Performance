# Import the `logging` module for logging messages.
import logging
import logging
# Import the `os` module for file system operations.
import os
# Import the `datetime` module for working with dates and times.
from datetime import datetime

# Define the name of the log file. The current date and time are included in the file name to make it unique.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the log file in the current working directory.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directory for the log file if it doesn't already exist.
os.makedirs(logs_path, exist_ok = True)

# Define the full path to the log file.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module with a basic configuration.
logging.basicConfig(
    filename=LOG_FILE_PATH,                # Specify the log file path.
    level=logging.INFO,                       # Set the logging level to INFO.
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"  # Define the format of the log messages.
)


# if __name__ == "__main__":
#     # Create a logger object and log an informational message.
#     logging.basicConfig(level=logging.INFO)  # Set up basic configuration for logging
#     logger = logging.getLogger(__name__)  # Create a logger object
#     logger.info("Logging has started")  # Log an informational message