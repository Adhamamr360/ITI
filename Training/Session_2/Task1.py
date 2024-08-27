import nltk

sentence = 'I Love Cat and I Love dog and I Love Elephent'
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(sentence)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

new_sentence = []
for word, pos in nltk.pos_tag(tokenized):
    if is_noun(pos):
        article = "An" if word[0].lower() in "aeiou" else "A"
        new_sentence.append(f'({article}) {word}')
    else:
        new_sentence.append(word)

sentence = ' '.join(new_sentence)
print(sentence)
