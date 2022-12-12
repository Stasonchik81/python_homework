import re

def rle_compress(str_):
    list_ = [i for i in str_]
    counter = []
    count = 1
    for i in range(1, len(list_)):
        if i == len(list_)-1:
            counter.append(f"{count}{list_[i-1]}")
        elif list_[i] == list_[i-1]:
            count +=1
        else:
            counter.append(f"{count}{list_[i-1]}")
            count = 1
    return ''.join(counter)

def rle_decompress(str_):
    out_string = ''
    list_d = re.findall(r'\d+', str_)
    list_c = re.findall(r'\D+', str_)
    for i in range(len(list_d)):
        out_string += list_c[i]*int(list_d[i])
    return out_string



with open("in_string.txt", "r") as data_1:
    in_string = data_1.read()
    out_string = rle_compress(in_string)

with open("out_string.txt", "w") as data_2:
    data_2.write(out_string)

with open("out_string.txt", "r") as data_in:
    in_string = data_in.read()
    out_string = rle_decompress(in_string)

with open("in_string.txt", "a") as data:
    data.write('\n')
    data.write(out_string)


