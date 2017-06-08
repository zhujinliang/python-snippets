# -*- coding: utf-8 -*-
"""
Run this on python3.5
"""

import asyncio
import threading
import time

async def speak_async():
    print('Hello world! ({})'.format(threading.current_thread()))
    await asyncio.sleep(3)
    print('Hello again! ({})'.format(threading.current_thread()))

loop = asyncio.get_event_loop()
tasks = [speak_async(), speak_async(), speak_async(), speak_async(), speak_async()]

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('complete time {}'.format(end - start))
loop.close()



