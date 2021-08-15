from auto_complete import manipulate_query
from initiate_search_engine import get_popular_sentences
from trie import TrieNode

if __name__ == '__main__':
    root = TrieNode("")
    print("Loading the files and preparing the system...")
    get_popular_sentences("2021-archive",root)
    query = input("The system is ready. Please enter your text:")
    while True:
        if query[-1] == "#":
            query = input("Please enter your text:")
        else:
            manipulate_query(root, query)
            query = query + input(query)