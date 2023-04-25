def main():
    x=get_int("what the fuck")
    print(f"x is {x}")#值错误先发生 会报x没被定义
        
def get_int(prompt):
    while 1:
        try:
            return int(input(prompt))
            # x=int(input("?"))
            # print(f"x is {x}")
        except ValueError as n:
            # print("fuck you ")
            # print(n)
            pass
        # else:
            # print(f"x is {x}")
            # return x
        finally:
            print("Hello,word")
    # return x
# print(f"x is {x}")#值错误先发生 会报x没被定义

main()