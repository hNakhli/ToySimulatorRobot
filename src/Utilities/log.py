import logging
import sys

'''
Implementing an internal logger class that could easily be modified to enable 
and disable the logging. At the moment it will be logging to console
'''
class Log:
    enabled = True
    logger:logging.Logger = None
    
    
    '''
    Note that in practice, we can inject the logger into this method
    Therefore, it would allow us to mock the logger and test it using
    unit tests to ensure the enabled functionality is working - as this
    is a test project, I have skipped that step.
    '''
    def __init__(self):
        logFormat = '%(asctime)s-%(levelname)s: %(message)s'
        logLevel = logging.DEBUG
        
        logging.basicConfig(format=logFormat, level=logLevel)
        self.logger = logging.getLogger(__name__)
        
        logging.info('started')
    
    # This log level is for anything that is reported as an error
    def Error(self, message:str):
        if not self.enabled:
            return
        self.logger.info(message)
    
    # This log level is mostly for information to provide additional info
    def Info(self, message:str):
        if not self.enabled:
            return
        self.logger.info(message)
        
    # This log level is for programming debug puproses
    def Debug(self, message:str):
        if not self.enabled:
            return
        self.logger.debug(message)