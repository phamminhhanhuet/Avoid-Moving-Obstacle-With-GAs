# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:29:38 2021

@author: Hacha
"""

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()




def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    word_dictionary = {}
    for ch in file_contents:
        if not ch.isalpha():
            file_contents.replace(ch, "")
    word_list = file_contents.split()
    for word in word_list:
        for ch in word:
            if ch in punctuations:
                word.replace(ch, "")
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            if word in uninteresting_words:    
                word_dictionary[word] = 0
            else:
                word_dictionary[word] += 10
    print(word_dictionary)
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dictionary)
    return cloud.to_array()


file_contents = "Liverpool could feel the knock of opportunity. Chelsea’s shock home defeat to West Brom earlier in the day had blown the doors off their security in fourth place and how Liverpool made capital. Jürgen Klopp’s team have enjoyed themselves in London this season and the trend continued with a fifth win in six visits to go with the draw at Fulham. Rather abruptly, they are within touching distance of a Champions League finish via the Premier League. This was not just a victory; it was a controlled detonation of Arsenal, who were unable to show any attacking spark. It was all Mikel Arteta’s team could do to cross halfway and it was difficult to remember them creating a chance. Liverpool called the tune from the first whistle and the only question came to concern whether they could show the needed cutting edge. They gave their answer shortly after Klopp had made a bold substitution just after the hour – sending on the attacker Diogo Jota for the left-back Andy Robertson."

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()