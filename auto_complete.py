from string import ascii_lowercase

from trie import find_prefix


def get_five_completions(sources):
    for i in range(min(5, len(sources))):
        f = open(sources[i].src, "r", encoding="utf8")
        line = (f.readlines()[sources[i].line]).replace("\n", "")
        index = sources[i].src.rfind("/")
        src = sources[i].src[index + 1:].replace(".txt", "")
        print(f"{i + 1}. {line} ({src} {sources[i].line})")


def parse(query):
    ignored_chars = [" ", ".", ",", "$", "@", "\t", "\n", ";", ":", "!", "?"]
    parsed_seq = query.lower().split(" ")
    fixed = []
    for word in parsed_seq:
        for char in ignored_chars:
            word = word.replace(char, "")
        if word != "":
            fixed.append(word)
    return fixed


def find_sequences(root, query):
    found_sources = []
    parsed_seq = parse(query)
    for word in parsed_seq:
        found = find_prefix(root, word)
        if found[0]:
            found_sources.append(found[1])

    len_ = len(found_sources)
    if len_ == 0:  # no sequences were found
        return []

    for i in range(len_ - 1):
        temp = []
        j, k = 0, 0
        while j < len(found_sources[i]) and k < len(found_sources[i + 1]):
            if found_sources[i][j] == found_sources[i + 1][k] and found_sources[i][j].offset + 1 == \
                    found_sources[i + 1][k].offset:
                temp.append(found_sources[i + 1][k])
                k += 1
                j += 1
            elif found_sources[i][j] < found_sources[i + 1][k]:
                j += 1
            elif found_sources[i][j] > found_sources[i + 1][k]:
                k += 1
            else:
                k += 1
                j += 1
        found_sources[i + 1] = temp
    return found_sources[len_ - 1]


#
# def get_reg_score(query):
#     return len(query) * 2
#
#
# def get_repl_score(query, index):
#     minus_indexes = {0: 5, 1: 4, 2: 3, 3: 2}
#     minus_score = 1 if index > 4 else minus_indexes[index]
#     return 2 * len(query) - minus_score
#
#
# def get_add_score(query, index):
#     minus_indexes = {0: 10, 1: 8, 2: 6, 3: 4}
#     minus_score = 2 if index > 3 else minus_indexes[index]
#     return 2 * len(query) - minus_score


def manipulate_query(root, query):
    found = 0
    sequences = find_sequences(root, query)
    found += len(sequences)
    if found >= 5:
        get_five_completions(sequences)
        return

    for i in range(len(query) - 1, -1, -1):  # replacements
        for letter in ascii_lowercase:
            if query[i] != "" and query[i] != letter:
                sequences += find_sequences(root, query[:i] + letter + query[i + 1:])
                found = len(sequences)
    if found >= 5:
        get_five_completions(sequences)
        return

    for i in range(len(query) - 1, -1, -1):  # erase
        if query[i] != "":
            sequences += find_sequences(root, query[:i] + query[i + 1:])
            found = len(sequences)
    if found >= 5:
        get_five_completions(sequences)
        return

    for i in range(len(query) - 1, -1, -1):  # add
        for letter in ascii_lowercase:
            if query[i] != "":
                sequences += find_sequences(root, query[:i] + letter + query[i:])
                sequences += find_sequences(root, query + letter)
                sequences += find_sequences(root, letter + query)
                found = len(sequences)
    if found >= 5:
        get_five_completions(sequences)
        return
