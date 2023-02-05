# Import module
import spacy

# Specify the models we want to use.
nlp = spacy.load('en_core_web_md') 
nlp2 = spacy.load('en_core_web_sm')

# Assign a nlp model to three words.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana") 

# Print similarity between words.
print(f"Cat - Monkey: {word1.similarity(word2)}")
print(f"Banana - Monkey: {word3.similarity(word2)}") 
print(f"Banana - Cat: {word3.similarity(word1)}")
print()


# Apply nlp model to a string of words
tokens = nlp('cat apple monkey banana ') 

# Loop through every word to check similarity 
for token1 in tokens:
 for token2 in tokens:
     print(token1.text, token2.text, token1.similarity(token2))

# Leave empty line.
print()

""" My findings regarding the PDF examplese are:
1) apple and banana are more similar than cat and monkey.
2) similarity is higher between monkey eating bananas than cat and apple
3) similarity is quite low between banana and cata and monkey and apple.
"""

# Assign en_core_web_md model to the content of the variable 'tokens'.
tokens = nlp('cat fish dog monkey man banana tractor car ')

# Print relevant message.
print("Similarity check using 'en_core_web_md'\n")

# Loop trhough every token in the string.
for token1 in tokens:

    # Loop through every element again in the string.
    for token2 in tokens:

        # Print tokens in their string representantion and degree of similarity between each other.
        print(token1.text, token2.text, token1.similarity(token2))

# Print an empty line.
print()

# Assign en_core_web_sm model to the content of the variable 'tokens'.
tokens = nlp2('cat fish dog monkey man banana tractor car ')

# Print relevant message.
print("Similarity check using 'en_core_web_sm'\n")

# Loop through every element again in the string.
for token1 in tokens:

    # Loop through every element again in the string.
    for token2 in tokens:

        # Print tokens in their string representantion and degree of similarity between each other.
        print(token1.text, token2.text, token1.similarity(token2))

""" Findings:
nlp = en_core_web_md

1) There is a much greater similarity between cat-dog than
cat-fish (interesting and unexpected.)

2) There is more similarity between cat and monkey (booth) mammals
than cat and fish.

3) There is much less similarity between dog and man, than dog and cat.

4) There is more similarity between dog and monkey (both 4 legged),
than dog and man.

5) There is more similarity between dog and car, than dog and tractor.

6) There is more similarity between dog and car, than cat and car, as dogs
are more likely to jump in the car.

7) There is more similarity between man and car, than man and tractor, as
everyone has a car, but not everyone a tractor.

8) Animals in general have less similarity with car.

nlp = en_core_web_sm

1) Similarities are much similar between animals or man and animals.

2) NOt all findings make sense: cat has a significant similarity with banana
or tractor, but very little with car.

3) Dog has a significant similarity with tractor now, but less with car.

4) All animals seem to have a high similarity with tractors, especially monkeys,
but less with cars.

Overall:

The first language model is more precise as demonstrated from the [W007] 'error'
that appears when running the program with en_core_web_sm model.
"""
