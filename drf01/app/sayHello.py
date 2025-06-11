def my_decorator(func):
    def wrapper():
        print("함수 호출 전")
        func()
        print("호출 후")
    return wrapper()

@my_decorator
def sh():
    print("안녕하세요")

sh()