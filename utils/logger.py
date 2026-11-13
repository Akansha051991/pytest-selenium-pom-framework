import logging
import os
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger(logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        # Prevent adding multiple handlers if logger is already initialized
        if not logger.handlers:
            # Create logs directory if it doesn't exist
            log_dir = os.path.join(os.getcwd(), "logs")
            os.makedirs(log_dir, exist_ok=True)

            # Log file path with timestamp or standard name
            log_file = os.path.join(log_dir, "execution.log")

            # File Handler
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(logging.INFO)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Log Format
            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger