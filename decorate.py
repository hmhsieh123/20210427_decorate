def decorate(func):
    def wrapper_func(*args):
        def inner_wrapper_func(*args):
            value = func(*args)
            return "<html>{}</html>".format(value)
        return inner_wrapper_func(*args)
    return wrapper_func

        
@decorate
def myfunction(parameter):
    return parameter

print(myfunction("hello"))