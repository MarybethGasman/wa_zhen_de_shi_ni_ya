def convert(a):
    # a = a.replace(":)","🙂")
    # a = a.replace(":(","🙁")
    
    return a.replace(":)","🙂").replace(":(","🙁")
def main():
    print(convert(input()))

main()