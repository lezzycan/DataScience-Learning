import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()  # This will output logs to the console
    ]
)

logger = logging.getLogger("Arithmetic app")


def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result
def subtract(a, b):
    logger.debug(f"Subtract {a} - {b}")
    return a - b
def multiply(a, b):
    logger.debug(f"Multiply {a} * {b}")
    return a * b
def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Divide {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error("Division by zero error", exc_info=True)
        return None
    

add(10,15)
subtract(15,10)
multiply(10,20)
divide(10,0)    