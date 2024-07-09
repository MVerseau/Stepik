import multiprocessing

class MinMaxAvr(multiprocessing.Process):
    def __init__(self, args):
        super().__init__()
        self.args=args
        self.result=multiprocessing.Array('l',' '*3)


    def run(self):
        self.target

    def func(self):
