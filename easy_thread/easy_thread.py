from threading import Thread


def starts_thread(func):
    def wrapper(*args, **kwargs):
        kwargs['daemon'] = True if 'daemon' not in kwargs else kwargs['daemon']
        t = Thread(target=func, args=args, **kwargs)
        t.start()
        return t
    return wrapper

