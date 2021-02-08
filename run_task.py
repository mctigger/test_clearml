import importlib

from clearml import Task
from time import sleep
import os
import platform
import distro
import torch


def main():
    task = Task.init(project_name="test", task_name="importlib_test2")
    print(torch)


if __name__ == "__main__":
    main()
