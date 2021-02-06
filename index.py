import time
from functools import wraps;

def speed_test(fun):
    @wraps(fun)
    def wraper(*args, **kwargs):

        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()

        print(f'Speed test function : {round(end_time - start_time,5)}')
        return result

    return wraper

@speed_test
def sun_func():
    return sum(number for number in range(3000000))


print(sun_func())


# 2.73135 2.71833 2.71953
#