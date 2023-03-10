import spacy 

nlp = spacy.load("en_core_web_sm")

#5 examples of garden path sentences
"Man loses sight of challenge despite warnings"

"Red tape holds up building of new stadium"

"The dog I love has really lovely bones"

"The boat floated along the canal sank"

"He came and painted the wall with cracks all over"

#sentences stored in list

gardenpathSentences = [
    "Man loses sight of challenge despite warnings",
    "Red tape holds up building of new stadium",
    "The dog I love has really lovely bones",
    "The boat floated along the canal sank",
    "He came and painted the wall with cracks all over"
    ]


# tokenise each sentence

for sample_sentence in gardenpathSentences:
    doc = nlp(sample_sentence)

    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    print([(w.text, w.pos_) for w in doc])
    

# perfom entity recognition
chatgpt_context = """
ChatGPT, an artificial intelligence text generator, is being hailed as the future of work, 
but not everyone is convinced. ChatGPT is an AI tool that can generate human-like text. 
Technologists see this as a disruptor of many jobs. 
Engineers and artists are pushing back against generative AI."""

nlp_chatgpt = nlp(chatgpt_context)
print([(i, i.label_, i.label) for i in nlp_chatgpt.ents])


#----------------------FIRST OUTPUT-----------------------------#
"""
[('this', 'DET'), ('is', 'AUX'), ('a', 'DET'), ('test', 'NOUN'), ('sentence', 'NOUN')]

Man loses sight of challenge despite warnings
['Man', 'loses', 'sight', 'of', 'challenge', 'despite', 'warnings']

Red tape holds up building of new stadium
['Red', 'tape', 'holds', 'up', 'building', 'of', 'new', 'stadium']

The dog I love has really lovely bones
['The', 'dog', 'I', 'love', 'has', 'really', 'lovely', 'bones']

The boat floated along the canal sank
['The', 'boat', 'floated', 'along', 'the', 'canal', 'sank']

He came and painted the wall with cracks all over
['He', 'came', 'and', 'painted', 'the', 'wall', 'with', 'cracks', 'all', 'over']
"""

#----------------------SECOND OUTPUT-----------------------------#


"""
Man loses sight of challenge despite warnings
[('Man', 'NOUN'), ('loses', 'VERB'), ('sight', 'NOUN'), ('of', 'ADP'), ('challenge', 'NOUN'), ('despite', 'SCONJ'), ('warnings', 'NOUN')]


Red tape holds up building of new stadium
[('Red', 'ADJ'), ('tape', 'NOUN'), ('holds', 'VERB'), ('up', 'ADP'), ('building', 'NOUN'), ('of', 'ADP'), ('new', 'PROPN'), ('stadium', 'NOUN')]


The dog I love has really lovely bones
[('The', 'DET'), ('dog', 'NOUN'), ('I', 'PRON'), ('love', 'VERB'), ('has', 'VERB'), ('really', 'ADV'), ('lovely', 'ADJ'), ('bones', 'NOUN')]


The boat floated along the canal sank
[('The', 'DET'), ('boat', 'NOUN'), ('floated', 'VERB'), ('along', 'ADP'), ('the', 'DET'), ('canal', 'NOUN'), ('sank', 'VERB')]


He came and painted the wall with cracks all over
[('He', 'PRON'), ('came', 'VERB'), ('and', 'CCONJ'), ('painted', 'VERB'), ('the', 'DET'), ('wall', 'NOUN'), ('with', 'ADP'), ('cracks', 'NOUN'), ('all', 'ADV'), ('over', 'ADV')]
"""

#perform entity recognition
#----------------------THIRD OUTPUT-----------------------------#
"""
[(AI, 'GPE', 384), (Technologists, 'NORP', 381), (Engineers, 'ORG', 383), (AI, 'ORG', 383)]
This has classified named items'entities in the short chatGPT text and 
put them into pre-determined categories

"""


#how spaCy has categorised each sentence
"""
spaCy has categorised each word in the sentence into various groups.
It is running through the sentence and designating the words to set categories that helps
it decide what the use of the word is and in what context it is being used.


"""
#using spacy.explain to understand entities
"""please see below
"""
entity_det = spacy.explain("DET")
print(f"DET:{entity_det}")

entity_aux = spacy.explain("AUX")
print(f"AUX:{entity_aux}")

entity_cconj = spacy.explain("CCONJ")
print(f"CCONJ:{entity_cconj}")

entity_adp = spacy.explain("ADP")
print(f"ADP:{entity_adp}")

entity_norp = spacy.explain("NORP")
print(f"NORP:{entity_norp}")

entity_gpe = spacy.explain("GPE")
print(f"GPE:{entity_gpe}")



#2 examples of entities looked up for clarity
"""
ENTITY: 
'DET' 

EXPLANATION-  DET: determiner, e.g. a, an, the

DID ENTITIY MAKE SENSE: yes, so the determiner of the object/noun 

*******************************************************

ENTITY: 
'AUX' 

EXPLANATION- AUX: auxiliary, e.g. is, has (done), will (do), should (do)

DID ENTITIY MAKE SENSE: Yes this did. So the aux is the action past, present or future tense
"""


#https://course.spacy.io/en/chapter1
#https://www.machinelearningplus.com/nlp/custom-text-classification-spacy/
#https://en.wikipedia.org/wiki/Garden-path_sentence
#https://www.byrdseed.com/garden-path-sentences/
#https://www.apartmenttherapy.com/garden-sentences-262915
# https://www.context.news/ai/what-is-chatgpt-and-will-it-steal-our-jobs