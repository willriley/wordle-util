import string

DICT_FILE = 'wordle_dict.txt'
NUM_NBORS = 26
WORDLE_LENGTH = 5

class Node:
    def __init__(self):
        self.nbor = [None] * NUM_NBORS

def trie_insert(trie, word):
    curr = trie
    for c in word:
        next = curr.nbor[ord(c) - ord('a')]
        if next is None:
            curr.nbor[ord(c) - ord('a')] = Node()

        curr = curr.nbor[ord(c) - ord('a')]

# words: list of words
# output a trie
def process_words(words):
    root = Node()

    for word in words:
        trie_insert(root, word.strip())

    return root

# trie: a trie holding the dictionary of wordle words
# correct: a dict mapping index -> letter known to be at that index
# omitted: a set of letters that aren't in the word
# TODO: figure out how to work misplaced letters into this
def wordle_find(trie, correct, omitted):

    def helper(i, curr, word, res):
        if curr is None:
            return
        if i == WORDLE_LENGTH:
            print("end", word)
            res.append(''.join(word))
            return

        # only 1 letter at this position
        if i in correct:
            word.append(correct[i])
            curr = curr.nbor[ord(correct[i]) - ord('a')]
            helper(i+1, curr, word, res)
            word.pop()
            return

        for c in string.ascii_lowercase:
            if c in omitted:
                print(c, "is omitted at",i)
                continue

            if curr.nbor[ord(c) - ord('a')]:
                print("expanding at", c, "for idx", i)
                word.append(c)
                nxt = curr.nbor[ord(c) - ord('a')]
                helper(i+1, nxt, word, res)
                word.pop()

    res = []
    helper(0, trie, [], res)
    return res

# import pdb; pdb.set_trace()
with open(DICT_FILE, 'r') as f:
    t = process_words(f.readlines())
    print(wordle_find(t, {0: 's',1:'u',3:'a',4:'r'}, set(['l', 'e', 'o', 'p', 't', 'm'])))
