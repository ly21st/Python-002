
def my_map(func, it):
    return [func(x) for x in it]

def my_map2(func, it):
    return (func(x) for x in it)

def my_map3(func, it):
    for x in it:
        yield func(x)


def power(x):
    return x * 2

if __name__ == '__main__':
    it = [10, 20, 30, 40, 50]
    print(list(my_map(power, it)))
    print(list(my_map2(power, it)))
    print(list(my_map3(power, it)))


