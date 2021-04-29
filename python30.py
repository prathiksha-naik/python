#closures
def outer(msg):
    message=msg
    def inner():
        print(message)
    return inner
var=outer('hi')
value=outer('hllo')

var()
value()
