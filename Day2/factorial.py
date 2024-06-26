
def factorial(n:int):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def list_factorial(list):
    new_list = []
    for item in list:
        new_list.append(factorial(item))
    return new_list