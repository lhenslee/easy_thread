from easy_thread import starts_thread
import time


@starts_thread
def hi(text, daemon=False):
    # do some asyncrynous code
    time.sleep(1)
    print(text)


t = hi('hello')
print('fuck')
t.join()
