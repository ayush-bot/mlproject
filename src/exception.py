#handling if exception arises . This is only one time making 
import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):# error and details of it present in sys library
    _,_,exc_tb=error_detail.exc_info()#all error info will be stored in exc_tb and first 2 variable just ignore it we dont need it
    file_name=exc_tb.tb_frame.f_code.co_filename#from here we will the file name check the documentation of exception handling
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))#here we are replacing the 0 1 2 as parameter inside we are choosing the custom formatting of error handling 

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


        