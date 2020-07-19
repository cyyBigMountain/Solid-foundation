import uuid


# 基本任务对象
class Task:

    def __init__(self, func, *args, **kwargs):
        # 任务的具体逻辑，通过函数引用传递
        self.callable = func
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f"Task id: {self.id}"


if __name__ == '__main__':
    task = Task(func=lambda: print("this is task test."))
    print(task)
