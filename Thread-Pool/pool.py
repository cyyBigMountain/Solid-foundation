from queue import ThreadSafeQueue
from task import Task

import threading


# 任务处理线程
class ProcessThread(threading.Thread):
    def __init__(self, task_queue: ThreadSafeQueue, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        # 任务线程停止标记
        self.dismiss_flag = threading.Event()
        # 任务队列
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while True:
            # 判断线程是否被要求停止
            if self.dismiss_flag.is_set():
                break

            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            # 执行task实际逻辑
            result = task.callable(*task.args, **task.kwargs)

    def dismiss(self):
        self.dismiss_flag.set()

    def stop(self):
        self.dismiss()