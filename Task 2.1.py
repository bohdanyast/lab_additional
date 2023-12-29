from pytrie import SortedStringTrie as Trie

s = Trie(al=0, ert=1)

sentence = "alert"


def recoursive(sentence):
    word = ''
    for idx, letter in enumerate(sentence):
        word += letter
        print(word)
        prefixes = s.keys(prefix=word)
        if len(prefixes) > 0:
            for i in range(0, len(prefixes)):
                if word == prefixes[i]:
                    recoursive(sentence[idx + 1:])


recoursive(sentence)