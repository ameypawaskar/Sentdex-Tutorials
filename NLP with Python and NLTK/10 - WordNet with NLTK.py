#WordNet is a lexical database for the English language, which was created by Princeton,
#and is part of the NLTK corpus.

from nltk.corpus import wordnet

syns = wordnet.synsets("program")

# synsets of word program
print(syns[0].name())

#example of a synset
print(syns[0].lemmas()[0].name())

#Just the word
print(syns[0].definition())

#Examples of the word in use
print(syns[0].examples())

#synonyms and antonyms to a word
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))


#Similarity of two words, by incorporating the Wu and Palmer method 
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))
