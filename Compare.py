from Sort import *
import time
import random
import tracemalloc
import copy

allsorts = [bubble_sort, insertion_sort, mergeSort, quickSort, countSort, radixSort]



test = random.choices(range(1, 1000), k=50)


def compare_manually(flist, tester):
    for i, f in enumerate(flist):
        t = [i for i in tester]
        start = time.perf_counter()
        #print(t)
        f(t)
        #print(t)
        end = time.perf_counter()
        print(f"{f.__doc__} took: {end - start:.6f}s")




def profile_sorting_algorithm(sort_function, tester):
    temp = copy.deepcopy(tester)

    tracemalloc.start()
    start_time = time.perf_counter()

    sort_function(temp)
    
    end_time = time.perf_counter()
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_ms = (end_time - start_time) * 1000
    peak_memory_kb = peak_memory / 1024
    
    return execution_time_ms, peak_memory_kb


def compare_sorting_algorithms(flist, data_size=1000, value_max=10000):
    tests = [[random.randint(1, value_max) for _ in range(data_size)] for i in range(5)]
    
    print(f"Dataset Size: {data_size} items")
    print(f"{'Algorithm':<20} | {'Time (ms)':<15} | {'Peak Memory (KB)':<15}")
    print("-" * 58)
    
    for func in flist:
        exec_time, peak_mem = 0.0, 0.0
        for test in tests:
            try:
                exec, peak = profile_sorting_algorithm(func, test)
                exec_time += exec
                peak_mem += peak
                
            except Exception as e:
                #print("Failed to execute: {str(e)}")
                a = 0
        exec_time /= len(tests)
        peak_mem /= len(tests)
        print(f"{func.__doc__:<20} | {exec_time:<15.4f} | {peak_mem:<15.4f}")


compare_sorting_algorithms(allsorts, 100, 100)

