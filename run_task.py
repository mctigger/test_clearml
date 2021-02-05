import importlib

from clearml import Task
from time import sleep


def main():
    task = Task.init(project_name="test", task_name="importlib_test")
    printme = importlib.import_module("some_package.file_to_import").printme
    printme()


if __name__ == "__main__":
    main()
