import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    print(dump)

    for ip in dump:
        print(ip)
        os.system('ping -n 2 {}'.format(ip))
        time.sleep(5)

import time