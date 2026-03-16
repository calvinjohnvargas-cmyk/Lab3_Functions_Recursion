# media_engine.py

# Decorator to log processing
def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

# Recursive shutdown (reused)
def signal_shutdown(power):
    if power == 0:
        return 0
    print(f"Current signal strength: {power}")
    return 1 + signal_shutdown(power - 1)

# Generator yielding squared even numbers up to limit
def play_count_stream(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i**2