import string
if __name__ == "__main__":
    characters = string.ascii_uppercase
    keys = []
    values = []
    name_keys = []
    name_values = []
    grand_total = 0

    for index in range(0,len(characters)):
        keys.append(characters[index])
        values.append(index+1)
        
    dict_aplha = dict(zip(keys,values))
    f = open("name.txt")
    elements = f.read().split(",")
    sorted_list = sorted(elements)
    
    for range_index in range(0,len(sorted_list)):
        total = 0
        for char in (sorted_list[range_index])[1:-1]:
            total += int(dict_aplha[char])
        grand_total += total * (int(range_index)+1)
print(grand_total)
