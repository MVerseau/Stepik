import multiprocessing


# импортируйте необходимое, если нужно что-то еще

class MyProcess(multiprocessing.Process):
    def __init__(self, target=None, args=('Hi'), name='my_process', daemon=True):
        super().__init__()
        #self._parent_pid = multiprocessing.parent_process().pid
        #self._parent_name = multiprocessing.parent_process().name
        self.name = name
        self.target = target
        self.args = args

    def run(self):
        self.target(self.args)
        #print(super().pid)
        #print(multiprocessing.current_process().pid)

    @property
    def parent_name(self):
        return self._parent_name

    @property
    def parent_pid(self):
        return self._parent_pid

    @parent_name.setter
    def parent_name(self):
        self._parent_name = multiprocessing.parent_process().name

    @parent_pid.setter
    def parent_pid(self):
        self._parent_pid = multiprocessing.parent_process().pid


# @pid.setter
# def pid(self):
#   # return super().pid, super().name
#    self._parent_pid = super().pid
#    self._parent_name = super().name
#


if __name__ == '__main__':
    pr = MyProcess(target=print)

    pr.start()
    print(pr.parent_name)
