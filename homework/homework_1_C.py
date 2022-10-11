def summation(*args):
    _list = []
    for idx, arg in enumerate(args):
        if arg < 0:
            _list.append(abs(arg) * 2)
    _list.sort()
    x = 0
    for idx, arg in enumerate(args):
        if arg < 0:
            arg = (abs(arg) * 2) / _list[-1]
        else:
            arg = arg / _list[-1]
        x += arg
    print(x)
summation(-10, 2, 3, 15, -4)