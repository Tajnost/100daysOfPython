#file = open("my_file.txt")
#contents = file.read()
#print(contents)
#file.close()


#with open("my_file.txt") as file:
#    contents = file.read()
#    print(contents)

with open('my_file.txt', mode="a") as file:
    # mode = a for append , mode w for overwride - def is read only
    file.write("\nNew text.")


