import os
import time

ports = ["8000"]

for port_to_find in ports:
    p = os.popen(f'netstat -ano | findstr :{port_to_find}')

    list_of_pids = []

    for line in p.read().splitlines():
        if "LISTENING" in line:
            list_of_pids.append(line.replace(" ", "").split("LISTENING")[1].strip())
            
    for pid in list_of_pids:
        os.popen(f'taskkill /PID {pid} /F')
