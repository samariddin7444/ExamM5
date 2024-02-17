def prime_generator(N):
    """
    Bu funksiya dastlabki N ta tub sonni chiqaradi.

    Args:
    - N (int): chiqariladigan tub sonlar soni.

    Yields:
    - int: Tub sonlar.
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            yield num
            count += 1
        num += 1


# Dastlabki 10 ta tub sonni chiqaramiz
N = 10
for prime in prime_generator(N):
    print(prime)
