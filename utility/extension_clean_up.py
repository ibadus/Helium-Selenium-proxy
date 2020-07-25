import glob
import os
from utility.config import BASE_DIR

class cleanUp():
    def __init__(self,signal):
        if signal == True:
            self.target = os.path.join(BASE_DIR,'*.zip') 

    def clean_extensions(self,):
        extensionlist = glob.glob(self.target)
        for extension in extensionlist:
            os.remove(extension)