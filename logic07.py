def main(a):
    if a%3==0 and a%5==0:
        return "yes"
    if a%3!=0 and a%5!=0:
        return "no"
print(main(15))