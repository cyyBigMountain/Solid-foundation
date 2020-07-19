from task import Task, AsyncTask
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


class AsyncTestOne:
    @classmethod
    def __async_process(cls):
        num = 0
        for i in range(100):
            num += i
        return num

    def __init__(self):
        # 初始化线程池
        test_pool = ThreadPool()
        test_pool.start()

        # 生成一系列任务
        for i in range(10):
            async_task = AsyncTask(func=self.__async_process)
            # 线程池提交任务
            test_pool.put(async_task)
            result = async_task.get_result()
            print(f"Get Result: {result}")


class AsyncTestTwo:
    @classmethod
    def __async_process(cls):
        num = 0
        for i in range(100):
            num += i
        time.sleep(5)
        return num

    def __init__(self):
        # 初始化线程池
        test_pool = ThreadPool()
        test_pool.start()

        # 生成一系列任务
        for i in range(1):
            async_task = AsyncTask(func=self.__async_process)
            # 线程池提交任务
            test_pool.put(async_task)
            print(f"Get Result in timestamp: {time.time()}")
            result = async_task.get_result()
            print(f"Get Result in timestamp: {time.time()}: {result}")


class AsyncTestThree:
    @classmethod
    def __async_process(cls):
        num = 0
        for i in range(100):
            num += i
        return num

    def __init__(self):
        # 初始化线程池
        test_pool = ThreadPool()
        test_pool.start()

        # 生成一系列任务
        for i in range(1):
            async_task = AsyncTask(func=self.__async_process)
            # 线程池提交任务
            test_pool.put(async_task)
            print(f"Get Result in timestamp: {time.time()}")
            time.sleep(5)
            result = async_task.get_result()
            print(f"Get Result in timestamp: {time.time()}: {result}")


if __name__ == '__main__':
    AsyncTestThree()
