import time

start = 0
end = 0

def start():
    start = time.time()

def end():
    end = time.time()
    takes = end - start
    print('program takes ' + takes + ' s.')