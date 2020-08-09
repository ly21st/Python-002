# 学习笔记


# scrapy并发参数优化原理
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. Twisted 学习参考文档：
https://pypi.org/project/Twisted/ 
3. asyncio — 异步 I/O 学习文档
https://docs.python.org/zh-cn/3.7/library/asyncio.html 

# scrapy参数优化
![f2e03196803fe221b74fb23f01ec37ef.png](en-resource://database/6362:1)

# 基于twisted的异步io模型
![60e835acdee7df1a90b6f6ad15bfe388.png](en-resource://database/6364:1)

# 2. 多进程：进程的创建

1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. os 模块学习文档：
https://docs.python.org/zh-cn/3.7/tutorial/stdlib.html#operating-system-interface
3. multiprocessing – 基于进程的并行学习文档： https://docs.python.org/zh-cn/3.7/library/multiprocessing.html

# 多进程模型
![76abb5d1184ffeaeb5fb956a45620bd6.png](en-resource://database/6366:1)



# 3. 多进程：多进程程序调试技巧
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. 补充说明：
课程中 18 分 11 秒处，应更改为 进程 0 1 是当前进程的子进程

# 4. 多进程：使用队列实现进程间的通信
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. 进程之间的两种通信通道：
https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#exchanging-objects-between-processes

# 5. 多进程：管道共享内存
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. 进程之间的两种通信通道：
https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#exchanging-objects-between-processes
3. 管道和队列参考文档：
https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#pipes-and-queues

# 6. 多进程：锁机制解决资源抢占
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. 进程间的同步学习文档：
https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#synchronization-between-processes

# 7. 多进程：进程池
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. 进程池学习文档：
https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#module-multiprocessing.pool
3. 迭代器学习文档：
https://docs.python.org/zh-cn/3.7/library/stdtypes.html#iterator-types

# 8. 多线程：创建线程
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. 基于线程的并行学习文档：
https://docs.python.org/zh-cn/3.7/library/threading.html
3. 基于进程的并行学习文档：
https://docs.python.org/zh-cn/3.7/library/multiprocessing.html
4. 底层多线程 API：
https://docs.python.org/zh-cn/3.7/library/_thread.html

# 9. 多线程：线程锁
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. 锁对象学习文档：
https://docs.python.org/zh-cn/3.7/library/threading.html#lock-objects
3. 递归锁对象：
https://docs.python.org/zh-cn/3.7/library/threading.html#rlock-objects

# 10. 多线程：队列
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. queue 学习文档：
https://docs.python.org/zh-cn/3.7/library/queue.html

# 11. 多线程：线程池
1. 获取课程源码操作方法：
切换分支：git checkout 3c
2. concurrent.futures - 线程池执行器： https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#threadpoolexecutor
3. concurrent.futures - 进程池执行器：
https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#processpoolexecutor