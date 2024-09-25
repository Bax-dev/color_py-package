import colorama
from colorama import Fore, Style
import logging

# Initialize colorama (for Windows support)
colorama.init(autoreset=True)

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Default color scheme
DEFAULT_COLORS = {
    'string': Fore.BLUE,
    'int': Fore.RED,
    'float': Fore.CYAN,
    'array': Fore.GREEN,
    'function': Fore.MAGENTA,
    'variable_name': Fore.YELLOW,
    'type': Fore.WHITE,
    'class': Fore.LIGHTMAGENTA_EX
}

def display_variable(variable_name, value, colors=DEFAULT_COLORS):
    """
    Displays a variable name and its value in different colors.
    
    Parameters:
        variable_name (str): The name of the variable.
        value (any): The value of the variable to display.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_variable('age', 25)
    """
    logger.info(f"Displaying variable: {variable_name} = {value}")
    print(f"{colors['variable_name']}{variable_name}: {colors['type']}{value}")

def display_array(array, colors=DEFAULT_COLORS):
    """
    Displays an array in a specified color.
    
    Parameters:
        array (list): The array to display.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_array([1, 2, 3])
    """
    logger.info(f"Displaying array: {array}")
    print(f"{colors['array']}Array: {array}")

def display_function(function_name, colors=DEFAULT_COLORS):
    """
    Displays a function name in a specified color.
    
    Parameters:
        function_name (str): The name of the function.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_function('my_func')
    """
    logger.info(f"Displaying function: {function_name}")
    print(f"{colors['function']}Function: {function_name}")

def display_class(class_name, colors=DEFAULT_COLORS):
   
    logger.info(f"Displaying class: {class_name}")
    print(f"{colors['class']}Class: {class_name}")

def display_string(string, colors=DEFAULT_COLORS):
    """
    Displays a string in a specified color.
    
    Parameters:
        string (str): The string to display.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_string('Hello, World!')
    """
    logger.info(f"Displaying string: {string}")
    print(f"{colors['string']}String: '{string}'")

def display_int(integer, colors=DEFAULT_COLORS):
    """
    Displays an integer in a specified color.
    
    Parameters:
        integer (int): The integer to display.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_int(42)
    """
    logger.info(f"Displaying integer: {integer}")
    print(f"{colors['int']}Integer: {integer}")

def display_float(floating_point, colors=DEFAULT_COLORS):
    """
    Displays a float in a specified color.
    
    Parameters:
        floating_point (float): The float to display.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_float(3.14)
    """
    logger.info(f"Displaying float: {floating_point}")
    print(f"{colors['float']}Float: {floating_point}")

def display_type(variable, colors=DEFAULT_COLORS):
    """
    Displays the type of a variable in a specified color.
    
    Parameters:
        variable (any): The variable whose type needs to be displayed.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_type('Hello')
    """
    logger.info(f"Displaying type of variable: {variable}")
    print(f"{colors['type']}Type of variable: {Fore.YELLOW}{type(variable).__name__}")

def display_any(variable_name, value, colors=DEFAULT_COLORS):
    """
    Dynamically detects the type of a variable and displays it with appropriate colors.
    
    Parameters:
        variable_name (str): The name of the variable.
        value (any): The value of the variable.
        colors (dict): Customizable color scheme. Default is DEFAULT_COLORS.
    
    Example:
        display_any('age', 25)
    """
    logger.info(f"Displaying any type of variable: {variable_name} = {value}")
    display_type(value, colors=colors)
    if isinstance(value, str):
        display_string(value, colors=colors)
    elif isinstance(value, int):
        display_int(value, colors=colors)
    elif isinstance(value, float):
        display_float(value, colors=colors)
    elif isinstance(value, list):
        display_array(value, colors=colors)
    elif isinstance(value):
        display_class(variable_name, colors=colors)
    elif callable(value):
        display_function(variable_name, colors=colors)
    else:
        raise TypeError(f"Unsupported type for: {variable_name}")
