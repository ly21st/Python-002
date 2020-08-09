# -* coding: utf-8 -*-

import argparse
import threading
import json
import traceback
from queue import Queue
import subprocess


class PingTread(threading.Thread):
    """
    ping检测
    """
    def __init__(self, thread_id, deque, timeout):
        super().__init__()
        self.thread_id = thread_id
        self.deque = deque
        self.timeout = timeout

    def run(self):
        while True:
            if self.deque.empty():
                break
            ip = self.deque.get()
            cmd = f"ping  -w {self.timeout} {ip}"
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ret = p.wait()
            # print(ip, ret)
            if ret == 0:
                dataQueue.put(ip)

# 存放数据的deque
dataQueue = Queue()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(__file__, description="Fake Afa Trade Log Generator")
    parser.add_argument("--n", "-n", dest='proc_num', help="process or thread num",
                        default=1, type=int)
    parser.add_argument("--f", "-f", dest='type', help="ping测试或者tcp测试",
                        default='ping', type=str)
    parser.add_argument("--ip", "-ip", dest='ip', help="ip地址", type=str)
    parser.add_argument("--w", "-w", dest='output', help="保存文件名", type=str)

    try:
        args = parser.parse_args()
        proc_num = args.proc_num
        type = args.type
        ip = args.ip
        output = args.output

        print('proc_num:', proc_num)
        print('type:', type)
        print('ip:', ip)
        print('output:', output)

        if type == 'ping':
            ipQueue = Queue()
            ip_range = ip.split('-')
            # print('ip_range', ip_range)
            if len(ip_range) == 1:
                ipQueue.put(ip_range[0])
            elif len(ip_range) == 2:
                prefix = ip_range[0][:ip_range[0].rindex('.')]
                start = ip_range[0].split('.')[-1]
                end = ip_range[1].split('.')[-1]
                i = int(start)
                while i <= int(end):
                    ip_str = prefix + '.' + str(i)
                    ipQueue.put(ip_str)
                    i = i + 1

            ping_threads = []
            for i in range(proc_num):
                thread = PingTread("ping_thread" + str(i), ipQueue, 3)
                thread.start()
                ping_threads.append(thread)

            for t in ping_threads:
                t.join()
            output_list = []
            while True:
                if dataQueue.empty():
                    break
                output_list.append(dataQueue.get())
            print('alive hosts:', json.dumps(output_list))

        elif type == 'tcp':
            pass
        else:
            print('arg error')
            exit(-1)
    except Exception:
        print(traceback.format_exc())

