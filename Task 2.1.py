from pytrie import SortedStringTrie as Trie

s = Trie(cf=0, yz=1)

sentence = "cfyz"


def recoursive(sentence):
    word = ''
    for letter in sentence:
        word += letter
        print(word)
        prefixes = s.keys(prefix=word)
        if len(prefixes) > 0:
            for i in range(0, len(prefixes)):
                if word == prefixes[i]:
                    recoursive(sentence[1:])


recoursive(sentence)
