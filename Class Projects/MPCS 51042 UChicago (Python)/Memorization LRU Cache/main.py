class CacheInfo:
    """Attributes:
    hits - number of function calls that was previously calculated
    misses - number of function calls that was not previously calculated
    max_size - maximum number of functions calls and their results that can be stored
    curr_size - current number of functions calls and their results that are stored in"""


    def __init__(self, hits, misses, max_size, curr_size):
        """Initializing hits, misses, max_size, and curr_size attributes"""


        self.hits = hits
        self.misses = misses
        self.max_size = max_size
        self.curr_size = curr_size


    def __repr__(self):
        """Creating a string representation of the CacheInfo class as asked in the exercise"""


        return f"CacheInfo(hits={self.hits}, misses={self.misses}, max_size={self.max_size}, curr_size={self.curr_size})"


def lru_cache(func, maxsize=128):
    """Creating a wrapper function to store each different function calls and their results"""


    stored_function_arguments = []
    def inner(*args, **kwargs):
        """Checking the function call to decide whether to store the function call and its results in the CacheInfo class and update
        the CacheInfo class's attributes"""


        # Extracting function arguments
        function_arguments = []
        for arg in args:
            function_arguments.append(arg)
        for key, value in kwargs.items():
            kwarg_string = f"{key}={value}"
            function_arguments.append(kwarg_string)
        function_arguments_tuple = tuple([function_arguments, func(*args, **kwargs)])
        
        # Checking if the function arguments has been called before
        for arguments_tuple in stored_function_arguments:
            if arguments_tuple == function_arguments_tuple:
                for arg1, arg2 in zip(arguments_tuple, function_arguments_tuple):
                    # Checking each argument in the function call if they have different type than the one previously used e.g. f(3) 
                    # and f(3.0) are different calls
                    if type(arg1) != type(arg2):
                        stored_function_arguments.append(function_arguments_tuple)
                        cache_info.misses += 1
                        cache_info.curr_size = len(stored_function_arguments)
                        return func(*args, **kwargs)
                # for duplicate function calls, using the least recently used replacement policy by removing previous function call
                # from the list and put it back at the end of the list
                stored_function_arguments.remove(arguments_tuple)
                stored_function_arguments.append(function_arguments_tuple)    
                cache_info.hits += 1
                return arguments_tuple[1]                          

        # removing the first function call in the list if the new function call was different from any of the previous ones in the list
        if len(stored_function_arguments) >= maxsize:
            stored_function_arguments.pop(0)
        
        stored_function_arguments.append(function_arguments_tuple)
        cache_info.misses += 1
        cache_info.curr_size = len(stored_function_arguments)
        return func(*args, **kwargs)

    # creating the cache_info variable to hold the current state of the CacheInfo class and the cache_info() function attribute to 
    # return the string representation of the CacheInfo class
    cache_info = CacheInfo(0, 0, maxsize, 0)
    inner.cache_info = cache_info.__repr__
    return inner


if __name__ == "__main__":
    # Checking with examples from the exercise
    def square(num):
        return num * num

    squareC = lru_cache(square, 4)
    print(squareC.cache_info())
    print(squareC(2))
    print(squareC.cache_info())
    print(squareC(4))
    print(squareC.cache_info())
    print(squareC(2))
    print(squareC.cache_info())
    print(squareC(5))
    print(squareC.cache_info())
    print(squareC(6))
    print(squareC.cache_info())
    print(squareC(7))
    print(squareC.cache_info())
    print(squareC(7))
    print(squareC.cache_info())

    def sum(a, b, c):
        return a + b + c

    sumC = lru_cache(sum, 4)
    print(sumC(2, 3, 4))
    print(sumC.cache_info())
    print(sumC(2, 3, 4))
    print(sumC.cache_info())
    print(sumC(2, b=3, c=4))
    print(sumC.cache_info())
    print(sumC(2, b=3, c=4))
    print(sumC.cache_info())
    print(sumC(2, c=4, b=3))
    print(sumC.cache_info())
