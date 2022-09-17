
# class based context manager
from ast import main
import time
from contextlib import contextmanager


class ManagedFile:

    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# example code
# with ManagedFile('hello.txt') as f:
#     f.write('hello, world!')
#     f.write('bye now')

# decorator based context manager


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


# with managed_file('hello_decorator.txt') as f:
#     f.write('hello world')
#     f.write('bye now')


# try implementing a context manager that measures the execution time

class ExecutionTime:
    def __init__(self) -> None:
        self.start_time = time.time()

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed_time = self.end_time-self.start_time
        print("elapsed_time:", elapsed_time)


def func_test_execution():
    time.sleep(10)
    print("func_test_execution")


with ExecutionTime() as e:
    func_test_execution()

