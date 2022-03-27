from Extractor import extract

def write(input):
    file = open("output.txt", "w")
    space = False

    for line in input:
        for word in line:
            if space: file.write(" ")
            file.write(word)
            space = True
        space = False
        file.write("\n")
    file.close

#write(input)