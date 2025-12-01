def mymap(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def myfilter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

def myreduce(func, iterable, initial = None):
    it = iter(iterable)
    if initial is None:
        value = next(it)
    else:
        value = initial

    for item in it:
        value = func(value, item)
    return value

print(mymap(lambda x: x * 2, [1, 2, 3]))
print(myfilter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(myreduce(lambda a, b: a + b, [1, 2, 3, 4]))