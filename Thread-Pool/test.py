from task import Task
from ThreadPool import ThreadPool

import time


class SimpleTask(Task):
    def __init__(self):
        super(SimpleTask, self).__init__(self.__process)

    @classmethod
    def __process(cls):
        time.sleep(1)
        print("This is a SimpleTask callable function 1.")
        time.sleep(1)
        print("This is a SimpleTask callable function 2.")


class Test:
    def __init__(self):
        # 初始化线程池
        test_pool = ThreadPool()
        test_pool.start()

        # 生成一系列任务
        for i in range(10):
            simple_task = SimpleTask()
            # 线程池提交任务
            test_pool.put(simple_task)

        # 线程池提交任务执行


if __name__ == '__main__':
    Test()
