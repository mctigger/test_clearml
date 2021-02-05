from clearml import Task
from time import sleep


def main():
    task = Task.init(project_name="test", task_name="test")
    d = {"a": "1"}
    print("uploading artifact")
    task.upload_artifact("myArtifact", d)
    print("done uploading artifact")
    # not sure if this helps but it won'r hurt to debug
    sleep(3.0)


if __name__ == "__main__":
    main()
