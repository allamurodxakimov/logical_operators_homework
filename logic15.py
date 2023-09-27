def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a//100
    y = a%10//10
    z = a%10
    return (x+y+z)%2!=0
print(main(346))