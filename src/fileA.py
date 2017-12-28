f = open("E:\qwerty.kl","r")
# content = f.read()
content = f.readline()
print(content)
f.close()
# raise NameError('HiThere')


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")
    finally:
        print("最后")

