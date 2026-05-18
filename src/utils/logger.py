"""Logger for the application."""
import logging
import sys
from datetime import datetime


class LogColors:
    """ANSI escape codes for beautiful console coloring."""
    RESET = "\033[0m"
    INFO = "\033[94m"     # Blue
    WARNING = "\033[93m"  # Yellow
    ERROR = "\033[91m"    # Red
    SUCCESS = "\033[92m"  # Green


class CustomFormatter(logging.Formatter):
    """Custom formatter for logging with colors."""
    format_str = "[%(asctime)s] [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s"

    def __init__(self):
        super().__init__()
        self.formats = {
            logging.INFO: LogColors.INFO + self.format_str + LogColors.RESET,
            logging.WARNING: LogColors.WARNING + self.format_str + LogColors.RESET,
            logging.ERROR: LogColors.ERROR + self.format_str + LogColors.RESET,
        }

    def format(self, record):
        # Trick to add a custom "SUCCESS" visual indicator using INFO level if needed
        # or just format based on standard levels
        log_fmt = self.formats.get(record.levelno, self.format_str)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


def setup_logger(name: str = "LegalMoveAI") -> logging.Logger:
    """Configures and returns a production-ready logger instance."""
    # Cambiamos el nombre de la variable interna para evitar el warning de scope
    logger_instance = logging.getLogger(name)

    # Verificamos los handlers en la instancia interna
    if logger_instance.hasHandlers():
        return logger_instance

    logger_instance.setLevel(logging.INFO)

    # 1. Console Handler (Outputs to terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(CustomFormatter())
    logger_instance.addHandler(console_handler)

    # 2. File Handler (Outputs to a permanent audit file for Compliance)
    file_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler = logging.FileHandler(
        "app_audit.log", mode="a", encoding="utf-8")
    file_handler.setFormatter(file_formatter)
    logger_instance.addHandler(file_handler)

    return logger_instance


# Ahora la variable global 'logger' no colisiona con nada interno
logger = setup_logger()
