def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a//10000
    y = a%10000//1000
    z = a%1000//100
    m = a%100//10
    n = a%10
    return x>y and y>z and z>m and m>n
print(main(98765))