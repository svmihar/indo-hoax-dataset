import os 
import time

os.system('python3 pusher.py')

for _ in range(500):
    time.sleep(1800)
    os.system('python3 pusher.py')
    print(f'hour {_}')