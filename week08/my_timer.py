from time import time
from time import ctime
from functools import wraps

def timer(func):
    # 结构不变增加wraps
    @wraps(func)
    def inner(*args,**kwargs):
        print("%s called at %s"%(func.__name__,ctime()))
        start_time = time()
        ret = func(*args,**kwargs)
        end_time = time()
        print("%s run time is %d" % (func.__name__, end_time - start_time))
        return ret
    return inner

@timer
def cal():
    sum = 0
    for i in range(10000000):
        sum += i
    print("sum:", sum)

if __name__ == '__main__':
    cal()
