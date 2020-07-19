import uuid
import threading


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


# 异步任务对象
class AsyncTask(Task):
    def __init__(self, func, *args, **kwargs):
        self.result = None
        self.condition = threading.Condition()
        super().__init__(func, *args, **kwargs)

    # 设置运行结果
    def set_result(self, result):
        self.condition.acquire()
        self.result = result
        self.condition.notify()
        self.condition.release()

    # 获取运行结果
    def get_result(self):
        self.condition.acquire()
        if not self.result:
            self.condition.wait()
        result = self.result
        self.condition.release()
        return result


if __name__ == '__main__':
    task = Task(func=lambda: print("this is task test."))
    print(task)
