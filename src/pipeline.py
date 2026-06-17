import functools, time

def pipeline(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"▶ START {func.__name__}")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"DONE in {end - start:.4f}s")
        return result

    return wrapper