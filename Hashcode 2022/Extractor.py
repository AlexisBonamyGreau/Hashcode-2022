def extract(name):
    file, i = open("Extractor Input/" + name, "r"), 0
    text = file.readlines()
    back = []

    for element in text:
        line, j = [""], 0
        for k in range(0, len(element)):
            if element[k] == " ":
                line.append("")
                j += 1
            else :
                if element[k] == "\n":
                    back.append(line)
                else :
                    line[j] += element[k]
        i += 1
    back.append(line)

    #print(back)
    file.close()
    return back