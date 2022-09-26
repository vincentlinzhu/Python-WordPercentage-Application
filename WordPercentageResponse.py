import os
import re
import sys
import urllib


def dictionary_of_key(InputKey):
    Htable = {}
    Key = open(InputKey, 'rU')
    KeyList = Key.read()
    for KeyWords in KeyList:
        KeyWords = KeyList.split()
        for KeyWord in KeyWords:
            KeyWord = KeyWord.lower()
            if KeyWord not in Htable:
                Htable[KeyWord] = 1
    return sorted(Htable.keys())

def dictionary_of_text(filename):
    Dict = {}
    file_text = open(filename, 'rU')
    lines = file_text.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in Dict:
                Dict[word] = 1
    return sorted(Dict.keys())

def regex(text_file):
    real_dict_of_text = []
    for element in dictionary_of_text(text_file):
        match = re.search(r'(\w+)', element)
        new_element = match.group()
        real_dict_of_text.append(new_element)
    return real_dict_of_text
   
def compare(percent, key_file, text_file):
    keyfoundintext = []
    dK = dictionary_of_key(key_file)
    #print dK
    dT = regex(text_file)
    #print dT
    for WordOfKey in dK:
        #print 'Here Here'
        #print WordOfKey
        if WordOfKey in dT:
            #print WordOfKey
            #print 'HERE HERE'
            keyfoundintext.append(WordOfKey)
    print keyfoundintext
    
    x = len(keyfoundintext)
    y = len(dK)*percent
    if x >= y:
        print 'True'
        return True
    else:
        print 'False'
        return False


def main():
    args = sys.argv[0:]
    per = int(args[1])
    percentage = per/100.00
    compare(percentage, args[2], args[3])
    
if __name__ == '__main__':
    main() 
