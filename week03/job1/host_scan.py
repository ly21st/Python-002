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


class TcpTread(threading.Thread):
    """
    tcp检测
    """
    def __init__(self, thread_id, deque, ip, timeout):
        super().__init__()
        self.thread_id = thread_id
        self.deque = deque
        self.ip = ip
        self.timtout = timeout

    def run(self):
        while True:
            if self.deque.empty():
                break
            port = self.deque.get()
            cmd = f'nc -z -w {self.timtout} {self.ip} {port}'
            # print('cmd:', cmd)
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ret = p.wait()
            # print(port, ret)
            if ret == 0:
                dataQueue.put(port)



def handle_ping(proc_num, ip, output, timeout):
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
        thread = PingTread("ping_thread" + str(i), ipQueue, timeout)
        thread.start()
        ping_threads.append(thread)

    for t in ping_threads:
        t.join()
    output_list = []
    while True:
        if dataQueue.empty():
            break
        output_list.append(dataQueue.get())
    output_list.sort()
    print('alive hosts:', json.dumps(output_list))

    # 将结果保存到一个json文件中
    file = open(output, 'w', encoding='utf-8')
    json.dump(output_list, fp=file, ensure_ascii=False)


def handle_tcp(proc_num, ip, port, output, timeout):
    portQueue = Queue()
    port_range = port.split('-')
    start = int(port_range[0])
    end = int(port_range[1])
    i = start
    while i <= end:
        portQueue.put(str(i))
        i = i + 1
    tcp_threads = []
    for i in range(proc_num):
        thread = TcpTread("tcp_thread" + str(i), portQueue, ip, timeout)
        thread.start()
        tcp_threads.append(thread)

    for t in tcp_threads:
        t.join()
    output_list = []
    while True:
        if dataQueue.empty():
            break
        output_list.append(dataQueue.get())
        output_list.sort()
    print('open ports:', json.dumps(output_list))

    # 将结果保存到一个json文件中
    file = open(output, 'w', encoding='utf-8')
    json.dump(output_list, fp=file, ensure_ascii=False)


# 存放数据的deque
dataQueue = Queue()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(__file__, description="Fake Afa Trade Log Generator")
    parser.add_argument("--n", "-n", dest='proc_num', help="process or thread num",
                        default=1, type=int)
    parser.add_argument("--f", "-f", dest='type', help="ping测试或者tcp测试",
                        default='ping', type=str)
    parser.add_argument("--ip", "-ip", dest='ip', help="ip地址", type=str)
    parser.add_argument("--port", "-port", dest='port', help="端口范围", type=str, default='1-1024')
    parser.add_argument("--w", "-w", dest='output', help="保存文件名", type=str, default='result.json')


    try:
        args = parser.parse_args()
        proc_num = args.proc_num
        type = args.type
        ip = args.ip
        output = args.output
        port = args.port

        # print('proc_num:', proc_num)
        # print('type:', type)
        # print('ip:', ip)
        # print('output:', output)
        # print('port:', port)

        if type == 'ping':
            handle_ping(proc_num, ip, output, 3)
        elif type == 'tcp':
            handle_tcp(proc_num, ip, port, output, 3)
        else:
            print('arg error')
            exit(-1)
    except Exception:
        print(traceback.format_exc())

