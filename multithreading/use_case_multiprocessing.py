import time, multiprocessing, sys, math



sys.set_int_max_str_digits(100000)


def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 700, 8000]
    
    start_time = time.time()
    
    
    # create a pool of workers processses
    
    with multiprocessing.Pool as pool:
        results = pool,map(compute_factorial, numbers)
        
    end_time = time.time()
    
    print(f"Result: {results}")
    print("Time taken: {end_time - start_time} seconds")