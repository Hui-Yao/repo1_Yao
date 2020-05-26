#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''Queue：实现进程间的数据通信。不像通过硬盘来实现数据互通，这里的数据是放在内存中的，而不是放在硬盘上。
q = Queue（max）   max：允许放入的最大数据量
queue.put()：向队列中放数据。如果超过了允许放的最大数据量，那么程序会卡死
queue.get():从队列中取数据。如果队列空了还在取，那么程序会卡死。


'''






