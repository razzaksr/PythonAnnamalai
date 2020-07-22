# decimal to binary

def convert(num):
    if num>=1:
        print(num%2,end="")
        convert(num//2)

convert(int(input("Enter the number to convert: ")))
