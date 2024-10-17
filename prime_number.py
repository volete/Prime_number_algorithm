numr: int = int(input("enter number: "))

for i in range(2, numr):
    if numr % i != 0:
        divisible_from_one_to_num = False


def prime_or_not():
    if numr > 1:
        if not divisible_from_one_to_num:
            print("you've got yourself a prime number")
    elif numr == 1:
        print("1 is not valid")
    else:
        print(f"Either {numr} is a prime number or sum went wrong, idk")


if prime_or_not():
    prime_or_not()
