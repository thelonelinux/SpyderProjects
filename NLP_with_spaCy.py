#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:52:06 2020

@author: vicky
"""
import spacy

nlp = spacy.load('en_core_web_sm')

print("------------------------------------Sentence-------------------------------------------\n")
about_text = ('Gus Proto is a Python developer currently'
               ' working for a London-based Fintech'
              ' company. He is interested in learning'
              ' Natural Language Processing.')
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
     print (sentence)
     
print("\n")     
print("-----------Adds support to use `...` as the delimiter for sentence detection---------\n")
def set_custom_boundaries(doc):
     # Adds support to use `...` as the delimiter for sentence detection
     for token in doc[:-1]:
         if token.text == '...':
             doc[token.i+1].is_sent_start = True
     return doc

ellipsis_text = ('Gus, can you, ... never mind, I forgot'
                  ' what I was saying. So, do you think'
                  ' we should ...')
 # Load a new model instance
custom_nlp = spacy.load('en_core_web_sm')
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)

''' Sentence Detection with no customization'''
print("\n")
print("---------------------Sentence Detection with no customization-----------------------\n")
ellipsis_doc = nlp(ellipsis_text)
ellipsis_sentences = list(ellipsis_doc.sents)
for sentence in ellipsis_sentences:
     print(sentence)    
     
     
     
'''Tokenization in spaCy'''
print("\n")
print("--------------------------------Tokenization in spaCy----------------------------\n")
for token in about_doc:
     print (token, token.idx)


'''Stop Words'''
print("\n")
print("-------------------------------Stop Words----------------------------------------\n")
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
#326
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)


'''Lemmatization'''
print("\n")
print("-------------------------------Lemmatization----------------------------------------\n")
conference_help_text = ('Gus is helping organize a developer'
     'conference on Applications of Natural Language'
     ' Processing. He keeps organizing local Python meetups'
     ' and several internal talks at his workplace.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
     print (token, token.lemma_)



'''Word Frequency'''
print("\n")
print("-------------------------------Word Frequency-------------------------------------\n")
from collections import Counter
complete_text = ('Gus Proto is a Python developer currently'
     'working for a London-based Fintech company. He is'
     ' interested in learning Natural Language Processing.'
     ' There is a developer conference happening on 21 July'
     ' 2019 in London. It is titled "Applications of Natural'
     ' Language Processing". There is a helpline number '
     ' available at +1-1234567891. Gus is helping organize it.'
     ' He keeps organizing local Python meetups and several'
     ' internal talks at his workplace. Gus is also presenting'
     ' a talk. The talk will introduce the reader about "Use'
     ' cases of Natural Language Processing in Fintech".'
     ' Apart from his work, he is very passionate about music.'
     ' Gus is learning to play the Piano. He has enrolled '
     ' himself in the weekend batch of Great Piano Academy.'
     ' Great Piano Academy is situated in Mayfair or the City'
     ' of London and has world-class piano instructors.')

complete_doc = nlp(complete_text)
 # Remove stop words and punctuation symbols
words = [token.text for token in complete_doc
         if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
# 5 commonly occurring words with their frequencies
common_words = word_freq.most_common(5)
print (common_words)
#[('Gus', 4), ('London', 3), ('Natural', 3), ('Language', 3), ('Processing', 3)]
 # Unique words
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print (unique_words)