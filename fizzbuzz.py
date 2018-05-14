
import doctest


def fizzbuzz(n):
    """
    Return 'fizz' if n divisible by three.
    Return 'buzz' if n divisible by five.
    Return 'fizzbuzz' if n divisible by three and five.
    In other cases return n as string.

    >>> fizzbuzz(1)
    '1'
    >>> fizzbuzz(2)
    '2'
    >>> fizzbuzz(3)
    'fizz'
    >>> fizzbuzz(4)
    '4'
    >>> fizzbuzz(5)
    'buzz'
    >>> fizzbuzz(6)
    'fizz'
    >>> fizzbuzz(14)
    '14'
    >>> fizzbuzz(15)
    'fizzbuzz'
    >>> fizzbuzz(16)
    '16'
    """

    # Implements your code.
    return str(n)


if __name__ == '__main__':
    doctest.testmod()
    for n in range(100):
        print(fizzbuzz(n))
