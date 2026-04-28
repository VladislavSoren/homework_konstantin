def inner_fun():
    print("inner_fun")


def fun(any_fun):
    any_fun()

fun(inner_fun)