import time

def calculate_time(func):

    def inner_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken: {end - start} seconds")
        return result
    return inner_func

@calculate_time
def print_word(word):

    print(f"Your word: {word}")

print_word("Amazing")
