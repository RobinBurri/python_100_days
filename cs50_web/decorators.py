def announce(f):
    def wrapper():
        print("About to run the funtion")
        f()
        print("Done running the function")

    return wrapper


@announce
def hello():
    print("Hello World!")


hello()
