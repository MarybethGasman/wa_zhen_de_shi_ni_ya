# i=3
# while i!=0:
#     print("meow")
#     i-=1

for i in [1,2,3]:
    print(":meow")

for i in range(3):
    print("akl")

print("asdas\n"*3, end="")

def get_number():
    while True:
        n=int(input("?"))
        if n>0:
            return n

# for _ in range(n):
#     print("meow")

def main():
    number=get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow:")

if __name__=="__main__":
    main()