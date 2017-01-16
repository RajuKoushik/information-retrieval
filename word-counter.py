#words in a string into a dictionary


def word_count(string):
    my_string = string.split()
    my_dict = {}
    for item in my_string:
        my_dict[item] = item.count(item)
    print(my_dict)