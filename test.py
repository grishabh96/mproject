import nltk
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import wordnet
import json
import random
import os
import config
from flask import Flask, render_template, url_for, json



from pprint import pprint
_end='_end'
def make_trie(words):
        root = dict()
        for word in words:
           current_dict = root
           for letter in word:
              current_dict = current_dict.setdefault(letter, {})
           current_dict[_end] = _end
        return root

def add_word(root,word):
         current_dict=root
         for letter in word:
               current_dict = current_dict.setdefault(letter, {})
         current_dict[_end] = _end
         return root
               
    

def in_trie(trie, word):
     current_dict = trie
     for letter in word:
         if letter in current_dict:
             current_dict = current_dict[letter]
         else:
             return False
     else:
         if _end in current_dict:
                return True
         else:
            return False



def nlp(example):
##        print("gtgrgyg")
##        json_decode=json.load('greetings.json','r')
##        print("re")
##        input_file1=open('aboutjaypee.json','r')
       
        nltk.data.path.append('./nltk_data/')

        with open(config.ZOMATO) as json_data:
                d = json.load(json_data)
                json_decode=d
        with open(config.VIDEOS) as json_data1:
                a = json.load(json_data1)
                json_decode1=a
        with open(config.SCORES) as json_data:
                
                d = json.load(json_data)
                json_decode2=d
        with open(config.HOROSCOPE) as json_data:
                d = json.load(json_data)
                json_decode3=d
    
        with open(config.COIN) as json_data:
                d = json.load(json_data)
                json_decode5=d
        with open(config.DICE) as json_data:
                
                d = json.load(json_data)
                json_decode6=d
        with open(config.DICTIONARY) as json_data:
                d = json.load(json_data)
                json_decode7=d
        with open(config.NEWS) as json_data:
                
                d = json.load(json_data)
                json_decode8=d
       
                
        
        my_dict = {}
        my_dict['msg']=json_decode['msg']
        f= [item for sublist in list(my_dict.values()) for item in sublist]
        my_dict1 = {}
        my_dict1['msg']=json_decode1['msg']
        f1= [item for sublist in list(my_dict1.values()) for item in sublist]
        my_dict2 = {}
        my_dict2['msg']=json_decode2['msg']
        f2= [item for sublist in list(my_dict2.values()) for item in sublist]
        my_dict3 = {}
        my_dict3['msg']=json_decode3['msg']
        f3= [item for sublist in list(my_dict3.values()) for item in sublist]
       
        my_dict5 = {}
        my_dict5['msg']=json_decode5['msg']
        f5= [item for sublist in list(my_dict5.values()) for item in sublist]
        my_dict6 = {}
        my_dict6['msg']=json_decode6['msg']
        f6= [item for sublist in list(my_dict6.values()) for item in sublist]
        my_dict7 = {}
        my_dict7['msg']=json_decode7['msg']
        f7= [item for sublist in list(my_dict7.values()) for item in sublist]
        my_dict8 = {}
        my_dict8['msg']=json_decode8['msg']
        f8= [item for sublist in list(my_dict8.values()) for item in sublist]
       
        root=make_trie(f)
        root1=make_trie(f1)
        root2=make_trie(f2)
        root3=make_trie(f3)
        
        root5=make_trie(f5)
        root6=make_trie(f6)
        root7=make_trie(f7)
        root8=make_trie(f8)
        
        print("gsre")
        def process_content():
                try:
                        stop_words=set(stopwords.words("english"))
                        words=word_tokenize(example)
                        filtered_sentence = []
                        for w in words:
                                if w not in stop_words:
                                        filtered_sentence.append(w)
                        

                        tagged = nltk.pos_tag(filtered_sentence)
                        noun=[]
                        vbn=[]
                        pos_a=[]
                        pos_1=[]
                        for word,pos in tagged:
                                pos_a.append(pos)
               
                        count_nn=0
                        count_nnp=0
                        count_vbn=0
                        count_nns=0
                        nnp=[]
                        nn=[]
                        vbn=[]
                        nns=[]
                        all1=[]
                        for f,pos in tagged:
                                all1.append(f)
                        if pos =='NN':
                                count_nn=count_nn+1
                                nn.append(f)
                        if pos=='NNP':
                                 count_nnp=count_nnp+1
                                 nnp.append(f)

                        if pos=='VBN':
                                 count_vbn=count_vbn+1
                                 vbn.append(f)
                        
                        if pos=='NNS':
                                 count_nns=count_nns+1
                                 nns.append(f)
                      
                        flag=0
                        secure_random = random.SystemRandom()
                         
                        for v in all1:
                                if (in_trie(root,v.lower())):
                                        flag=1
                                        my_dict['response']=json_decode['response']
                                        return 1,secure_random.choice(my_dict['response'])
                                elif (in_trie(root1,v.lower())):
                                        flag=1
                                        my_dict1['response']=json_decode1['response']
                                        print("bot responses....")
                                        return 1,secure_random.choice(my_dict1['response'])
                                elif (in_trie(root2,v.lower())):
                                        flag=1
                                        my_dict2['response']=json_decode2['response']
                                        return 1,secure_random.choice(my_dict2['response'])
                                elif (in_trie(root3,v.lower())):
                                        flag=1
                                        my_dict3['response']=json_decode3['response']
                                        print("bot responses....")
                                        return 1,secure_random.choice(my_dict3['response'])
                               
                                elif (in_trie(root5,v.lower())):
                                        flag=1
                                        my_dict5['response']=json_decode5['response']
                                        print("bot responses....")
                                        return 1,secure_random.choice(my_dict5['response'])
                                elif (in_trie(root6,v.lower())):
                                        flag=1
                                        my_dict6['response']=json_decode6['response']
                                        print("bot responses....")
                                        return 1,secure_random.choice(my_dict6['response'])
                                elif (in_trie(root7,v.lower())):
                                        flag=1
                                        my_dict7['response']=json_decode7['response']
                                        print("bot responses....")
                                        return 1,secure_random.choice(my_dict7['response'])
                                elif (in_trie(root8,v.lower())):
                                        flag=1
                                        my_dict8['response']=json_decode8['response']
                                        print("bot responses....")
                                        return 1,secure_random.choice(my_dict8['response'])
                               
                                

                        if(flag==0):
                                return 0,None
                        
                except Exception as e:
                        print(str(e))
        flag,fbye=process_content()
        return flag,fbye

        

nltk.download("averaged_perceptron_tagger", "C:/project/example/venv/Git/Minorproject/nltk_data/")
  
