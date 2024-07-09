import multiprocessing
import time


# импортируйте необходимое, если нужно что-то еще

class MyProcess(multiprocessing.Process):
    def __init__(self, target=None, name='my_process', daemon=True):
        super().__init__()
        self.target = target


    def run(self):
        self.target()

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

if __name__ == '__main__':
    pr = MyProcess(target=time.sleep)
    pr.start()
    pr.join()
    print(f"pr' process name: {pr.name:.>30}")
    print(f"pr' pid: {pr.pid:.>33}")
    print(f"pr's parent process' name: {pr.parent_name:.>21}")
    print(f"pr's parent process' pid: {pr.parent_pid:.>16}")
    print(f"current process' name: {multiprocessing.current_process().name:.>25}")
    print(f"current process' pid: {multiprocessing.current_process().pid:.>20}")

