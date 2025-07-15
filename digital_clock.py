import sys
import time
h=12
m=30
s=0
while True:
    sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
    sys.stdout.flush()
    time.sleep(0.5)
    s+=1
    if s==60:
        m+=1
        s=0
    if m==60:
        h+=1
        m=0
        s=0
    if h==13:
        h=0
        s=0
        m=0
