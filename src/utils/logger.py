import logging


def setup_logger():
    logger = logging.getLogger("LibraryLogger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("library.log")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
