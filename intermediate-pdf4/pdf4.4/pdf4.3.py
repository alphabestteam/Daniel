def main():

    f = open("example.txt", 'w')
    f.write("This is the txt before changed.")
    f = open("example.txt",'r')
    contenta = f.read()
    print(contenta)

    f = open("example.txt","w")
    user_input = input("enter new txt\n")
    f.write(user_input)
    f = open("example.txt", 'r')
    content = f.read()
    print(f"text after change - {content} ")


if __name__ == '__main__':
    main()
