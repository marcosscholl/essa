# -*- coding: utf-8 -*-

import logging


class Log():
    def __init__(self,arquive=None,name=None, level=None, formatter=None):
        if arquive is None:
            nome = "ESSA.log"
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M:%S',
                            filename='/home/scholl/Dropbox/Spyder/essa/logs/'+nome,
                            filemode='w')
        console = logging.StreamHandler()
        
        
        if level is not None:
            if level == "DEBUG":
                console.setLevel(logging.DEBUG)
            elif level == "INFO":
                console.setLevel(logging.INFO)
            elif level == "WARNING":
                console.setLevel(logging.WARNING)
            elif level == "ERROR":
                console.setLevel(logging.ERROR)
            elif level == "CRITICAL":
                console.setLevel(logging.CRITICAL)
                
        if formatter is not None:
            console.setFormatter(formatter)

        
        logging.getLogger('').addHandler(console) 
        if name is None:
            self.logger = logging.getLogger("Essa")
        else:
            self.logger = logging.getLogger(name)
        
        print self.logger 
        #self.returnLog()
        #return self.logger    
           
    def returnLog(self):
        return self.logger
