#list unique tokens from a string


def list_unique_tokens(str):
    word_list = str.split()
    unique_words = set(word_list)
    for word in unique_words:
        print(str(word) + "\n")
    return unique_words

