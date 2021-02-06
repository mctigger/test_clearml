import importlib

from clearml import Task
from time import sleep
import os
import platform
import distro


def main():
    task = Task.create(
        project_name="test",
        task_name="importlib_test2",
        task_type="training",
        docker="ubuntu:16.04",
        add_task_init_call=True,
    )
    printme = importlib.import_module("some_package.file_to_import").printme
    printme()
    print(os.name)  # returns os name in simple form

    print(platform.system())  # returns the base system, in your case Linux
    print(platform.release())  # returns release version
    print(distro.linux_distribution())


if __name__ == "__main__":
    main()
