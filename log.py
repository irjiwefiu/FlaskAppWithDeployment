import logging
import os

# Create logger
def createLogger(fileName:str)->logging.Logger:
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)  # Set minimum log level

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # ======================
    # File Handler
    # ======================
    os.makedirs("logs", exist_ok=True)  # Ensure logs directory exists
    file_handler = logging.FileHandler(f"logs/{fileName}.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # ======================
    # Console Handler
    # ======================
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger