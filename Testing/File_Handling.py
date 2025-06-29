# File Objects

with open("File_Handling.txt", "r") as f:
    # print(f.read())
    # print(f.readline())
    # print(f.readlines())

    # for line in f:
    #     print(line, end="")

    # print(f.read(100), end="")

    size_to_read = 100
    f_content = f.read(size_to_read)

    print(f.tell())

    # while len(f_content) > 0:
    #     print(f_content, end="")
    #     f_content = f.read(size_to_read)

# f = open("File_Handling.txt", "r")
# print(f.mode)
# f.close()