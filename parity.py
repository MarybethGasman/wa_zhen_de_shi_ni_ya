# x=int(input())
# if x%2==0:
#     print("E")
# else:
#     print("o")


def main():
    x=int(input())
    if is_even(x):
        print("E")
    else:
        print("o")
def is_even(n):
    # if n%2==0:
    #     return True
    # else:
    #     return False
    # return True if n%2==0 else False
    return n %2==0
main()