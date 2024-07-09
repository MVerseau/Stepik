import multiprocessing
import ctypes


class Encrypter(multiprocessing.Process):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.result = multiprocessing.Array('u',8)

    def run(self):
        result = crypto_utils(self.text)
        self.result[:] = result



def crypto_utils(text: str) -> str:
    if text.startswith("a"):
        return "aaa45678"
    if text.startswith("b"):
        return "bbb45678"


text_blocks = ("allocation", "bombshell")


def main():
    result = dict()
    processes = [Encrypter(text=item) for item in text_blocks]
    for pr in processes:
        pr.start()
    for pr in processes:
        pr.join()
    for pr in processes:
        result[pr.result[:]] = pr.text
    print(result)


if __name__ == '__main__':
    main()
