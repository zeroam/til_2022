import logging
from functools import wraps

# Example from: https://www.geeksforgeeks.org/create-an-exception-logging-decorator-in-python/


def create_logger():
    # create a logger object
    logger = logging.getLogger("exc_logger")
    logger.setLevel(logging.INFO)

    # create a file to store all the logged exceptions
    logfile = logging.FileHandler("exc_logger.log")

    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)

    logfile.setFormatter(formatter)
    logger.addHandler(logfile)

    return logger


def exception(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                issue = "exception in " + func.__name__ + "\n"
                issue = issue + "===============\n"
                logger.exception(issue)
                raise

        return wrapper

    return decorator


if __name__ == "__main__":
    logger = create_logger()

    # you will file a log file
    # created in a given path
    print(logger)

    @exception(logger)
    def divide_by_zero():
        return 12 / 0

    divide_by_zero()
