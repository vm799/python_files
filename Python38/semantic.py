import spacy 

nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2)) 
# 0.6770565478895127

print(word3.similarity(word2))
# 0.7276309976205778

print(word3.similarity(word1))
# 0.6806929391210822

"""
The closest similarity is 0.7276309976205778 for banana and monkey
"""

word1 = nlp("dog")
word2 = nlp("bone")
word3 = nlp("woof")

print(word1.similarity(word2)) 
# 0.7336331449269807

print(word3.similarity(word2))
# 0.5742562766858373

print(word3.similarity(word1))
# 0.6728868271935052

"""
The closest similarity is 0.7336331449269807 for dog and bone which I expected
but the similarity was close in 0.6728868271935052 for dog and woof too

"""



tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
"""
with "en_core_web_sm"
cat cat 1.0
cat monkey 0.6012927293777466
cat banana 0.1981828361749649
apple cat 0.6963739395141602
apple apple 1.0
apple monkey 0.7503186464309692
apple banana 0.2811802327632904
monkey cat 0.6012927293777466
monkey apple 0.7503186464309692
monkey monkey 1.0
monkey banana 0.35610878467559814
banana cat 0.1981828361749649
banana apple 0.2811802327632904
banana monkey 0.35610878467559814
banana banana 1.0

"en_core_web_md"
cat cat 1.0
cat apple 0.2036806046962738
cat monkey 0.5929930210113525
cat banana 0.2235882580280304
apple cat 0.2036806046962738
apple apple 1.0
apple monkey 0.2342509925365448
apple banana 0.6646699905395508
monkey cat 0.5929930210113525
monkey apple 0.2342509925365448
monkey monkey 1.0
banana cat 0.2235882580280304
banana apple 0.6646699905395508
banana monkey 0.4041501581668854
banana banana 1.0
"""

sentence_to_compare = "Why is my cat on the car"

sentences = [
    
]


"""
The 'en_core_web_md' is for a larger sized model than sm
and seems to be more accurate
e.g
sm model
monkey banana 0.35610878467559814
monkey cat 0.6012927293777466


md model
monkey banana 0.4041501581668854
monkey cat 0.5929930210113525

However it doesn't follow for all use cases in the examples given 

------https://spacy.io/models/en#en_core_web_sm-----
This mentions that sm package is trained on written web text such as blogs, news and comments.
"""

# https://spacy.io/models/#model-versioning