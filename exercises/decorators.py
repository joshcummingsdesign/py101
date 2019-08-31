def auth(fn):
    def auth_wrapper(*args, **kwars):
        print('this gets called by the decorator')
        return fn()
    return auth_wrapper

@auth
def hello():
    print('this gets called by the hello function')

hello()
