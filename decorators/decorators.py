from functools import wraps

def fun_decorator(fun_to_be_decorated):
    fun_to_be_decorated.info = "decorated"
    return fun_to_be_decorated

def myfunc():
    print("myfunc")
    print(myfunc.info)

decorated = fun_decorator(myfunc)
myfunc()
# will ouput 
# myfunc
# decorated


def fun_wrapper_decorator(fun_to_be_decorated):
    @wraps(fun_to_be_decorated)
    def wrapper(*args, **kwargs):
        print("before")
        fun_to_be_decorated()
        print("after")
    return wrapper

@fun_wrapper_decorator
def myfunc1():
    print("myfunc")

myfunc1()
# will ouput 
# before
# myfunc
# after

def fun_wrapper_decorator1(fun_to_be_decorated):
    @wraps(fun_to_be_decorated)
    def wrapper(*args, **kwargs):
        print("before1")
        fun_to_be_decorated()
        print("after1")
    return wrapper

@fun_wrapper_decorator1
@fun_wrapper_decorator
def myfunc2():
    print("myfunc2")

myfunc2()
# will ouput 
# before1
# before
# myfunc2
# after
# after1
