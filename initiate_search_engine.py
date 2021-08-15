import os
from auto_complete import parse
from trie import add
from source import Source


def add_to_trie(file_path, root):
    file = open(file_path, "r", encoding="utf8")
    for position, line in enumerate(file):
        sentence = parse(line)
        for i in range(len(sentence)):
            src = Source(file_path, position, i)
            add(root, sentence[i], src)

    file.close()


def get_popular_sentences(data, root):
    for dir in os.walk(data):
        for d in dir[1]:
            get_popular_sentences(d, root)
        for file in dir[2]:
            add_to_trie(dir[0] + "/" + file, root)
