# Auto-Complete
## google-project

In this project we implemented a feature of Google's search engines - AutoComplete.

Autocomplete, or word completion, is a feature in which an application predicts the rest of a word a user is typing.

The purpose of the completion action is to make it easier for the user to find the most appropriate sentence.

Once inserting some text the user will get the five closest completions to the input.

If there are five sentences that the text is their sub-string, they will be returned. Otherwise will be returned sentences containing the sub-string with one of the changes - a missing letter, additional letter, or a replaced letter.

If the user inserts #, then we start a new word to search.

The results will be from sentences within given input text files.

You can upload your own files. in main.py, line 8, by changing it to your path of folder wanted.
