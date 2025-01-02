import time


def search():
    print("performs search")
    time.sleep(4)
    while True:
        text = (yield)
        if "Hello" in text:
            print("It's a greet")
        elif "Bye" in text:
            print("It's a see off")
        else:
            print("Normal conversation")


search = search()
next(search)
search.send("Hey")
search.send("Hello")
search.send("Bye")