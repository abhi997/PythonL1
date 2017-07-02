import os

class filesize:
    def __init__(self,size = 0):
        self.size = size
        
    def zerosize(self, path):
        self.path = path
        os.chdir(path)
        for file in os.listdir(self.path):
            if os.stat(file).st_size == 0:
                print(file)

c1 = filesize()
c1.zerosize('E:\\holi image')  

