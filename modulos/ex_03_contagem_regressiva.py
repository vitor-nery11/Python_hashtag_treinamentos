import time 

for numero in range(10, 0, -1):
    time.sleep(1)
    print(numero, end=' \r')

print('o evento começou!!')