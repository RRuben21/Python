import time

def teletype_print(text, delay=0.1):
    for ch in text:
        print(ch, end='')
        time.sleep(delay)
    
teletype_print('Hello world my name is Phase 10')
