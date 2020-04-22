#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:52:06 2020

@author: vicky
"""


import spacy

nlp = spacy.load('en_core_web_sm')


about_text = ('Gus Proto is a Python developer currently'
               ' working for a London-based Fintech'
              ' company. He is interested in learning'
              ' Natural Language Processing.')
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
     print (sentence)
     
     

#part 2

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


# Sentence Detection with no customization
ellipsis_doc = nlp(ellipsis_text)
ellipsis_sentences = list(ellipsis_doc.sents)
for sentence in ellipsis_sentences:
     print(sentence)     