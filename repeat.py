def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                print("Radhe-Radhe")
                func(a)
                print("Jai Shri Krishn")
            return wrapper
        return decorator

@repeat(7)
def say_hello(name):
    print(f"Jai ho mere {a} ki Jai Ho.")
say_hello("Pyaare Gurudev Bhagwan Shri Premanand Ji Maharaj Ji")
