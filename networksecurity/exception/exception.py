import sys
import logging
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details):
        self.error_message = error_message
        
        # execution info se trace-back (tb) nikala
        _, _, exc_tb = error_details.exc_info()
        
        # File name aur line number extract kiya
        self.file_name = exc_tb.tb_frame.f_code.co_filename 
        self.lineno = exc_tb.tb_lineno
    
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )
        
if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block") 
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)``