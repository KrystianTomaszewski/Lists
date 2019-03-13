code1 = "79-900"
code2 = "80-155"

def generator(arg1,arg2):

    generator = []
    first_part = arg1[0:2]
    first_part +=arg1[3:7]
    first_part = int(first_part)
    first_part += 1
    second_part = arg2[0:2]
    second_part +=arg2[3:7]
    second_part = int(second_part)

    for elem in range(first_part,second_part,1):
        elem = str(elem)
        code = elem[0:2] + "-" + elem[2:5]
        generator.append(code)
    print (generator)

generator(code1,code2)