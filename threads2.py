import concurrent.futures
import time

start = time.perf_counter()
def do_something(seconds):
    print(f'Sleeping {seconds} seconds')
    time.sleep(seconds)
    return f'Done sleeping {seconds} seconds'


with concurrent.futures.ThreadPoolExecutor() as executor:
    f = executor.submit(do_something, 1)
    print(f.result())

    seconds = [5, 4, 3, 2, 1]
    # f = [executor.submit(do_something, second) for second in seconds]
    # for result in concurrent.futures.as_completed(f):
    #     print(result.result())

    f = executor.map(do_something, seconds)
    for result in f:
        print(result)


finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} seconds(s)')