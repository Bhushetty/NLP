import re
from collections import Counter

# Step 1: Training data (correct words)
text = "spelling spelling spelling word world work python python language model model"

words = re.findall(r'\w+', text.lower())
word_freq = Counter(words)

# Step 2: Probability of correct word P(S)
def P(word):
    return word_freq[word] / sum(word_freq.values())

# Step 3: Generate possible edits (noise model)
def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
    deletes = [L + R[1:] for L, R in splits if R]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + replaces + inserts)

# Step 4: Choose best correction
def correct(word):
    candidates = edits1(word)
    known = [w for w in candidates if w in word_freq]
    return max(known, key=P) if known else word

# Test
print(correct("speling"))
