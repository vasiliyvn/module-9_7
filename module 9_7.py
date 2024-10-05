
def is_prime(d):
    def wrapper(*args):
        result1 = d(*args)
        summa = sum(args)
        if summa<2:
            return False
        for i in range(2, int(summa**0.5)+1):
            if summa % i ==0:
                print('Составное')
        else:
            print('Простое')
        return result1
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_

result = sum_three(2, 3, 6)
print(result)