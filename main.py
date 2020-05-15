# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:42:14 2020

@author: lssac
"""

import requests
from bs4 import BeautifulSoup
import pickle
from selenium import webdriver
import csv

from korteng import KorTransform2Eng
from keyinput import one_key_input

import pyautogui
import time
import win32clipboard

def get_soup(url, params=None):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    timeout = 2
    while True:
        try:
            if params!=None:
                response = requests.get(url, headers=header, params=params, timeout=timeout)
            else:
                response = requests.get(url, headers=header, timeout=timeout)
            break
        except:
        #except requests.exceptions.Timeout:
            pass

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_longword_namuwiki():

    link = "https://namu.wiki/w/%EB%81%84%ED%88%AC/%ED%95%9C%EA%B5%AD%EC%96%B4/%EA%B8%B4%20%EB%8B%A8%EC%96%B4"
    
    soup = get_soup(link)
    
    trs = soup.find_all("tr")
    
    temp = []
    
    heart = "♥"
    star = "★"
    trs = trs[14:]
    for tr in trs:
        try:
            text = tr.contents[1].text
            text = text.replace(heart,"")
            text = text.replace(star,"")
            temp.append(text)
        except:
            pass
    
    return temp

def get_attack_word_namuwiki():

    link = "https://namu.wiki/w/%EB%81%84%ED%88%AC/%ED%95%9C%EA%B5%AD%EC%96%B4/%EA%B3%B5%EA%B2%A9%20%EB%B0%8F%20%EB%B0%A9%EC%96%B4%20%EB%8B%A8%EC%96%B4"
    
    soup = get_soup(link)
    
    trs = soup.find_all("tr")
    
    temp = []

    heart = "♥"
    star = "★"
    trs = trs[12:]
    for tr in trs:
        try:
            text = tr.text
            text = text.replace(heart,"")
            text = text.replace(star,"")
            
            if text[0] != "[":
                temp.append(text)
        except:
            pass
        
    return temp


def get_logword_kkukowiki():
    links = ["https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%84%B1",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%84%B4",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%84%B7",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%84%B9",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%81",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%82",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%85",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%87",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%88",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%8A",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%8B",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%8C",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%8D",
             "https://kkukowiki.kr/w/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%8E"]

    temp = []
    no_paper = "(없는 문서)"
    for link in links:
        soup = get_soup(link)
        
        trs = soup.find_all("a")

        for tr in trs:
            if "title" not in tr.attrs.keys():
                continue
            text = tr["title"]
            if "부분 편집" in text:
                continue
            
            text = text.replace(no_paper, "")
            text = text.strip()
            temp.append(text)
    return temp

def class_word(list_word, index=0):
    result = {}
    for line in list_word:
        key = line[index]
        if key in result.keys():
            result[key].append(line)
        else:
            result[key] = []
            result[key].append(line)
    return result

def sum_worddict(dicts):
    
    
    keys = []
    for dic in dicts:
        keys += dic.keys()
    keys = list(set(keys))
    
    result = {}
    
    for front in keys:
        words = []
        for dic in dicts:
            if front in dic.keys():
                words += dic[front]
        words = list(set(words))
        
        result[front] = words
    
    return result

def len_worddict(dictt):
    result = 0
    for key in dictt.keys():
        result += len(dictt[key])
    return result

def sort_worddict(dictt):
    for key in dictt.keys():
        dictt[key].sort(key=lambda x:len(x), reverse=True)
    return dictt

def clear_string(string):
    new_string = ""
    for i in string:
        if 65<=ord(i)<=90 or 97<=ord(i)<=122 or 44032<=ord(i)<=55203 or 48 <= ord(i) <= 57:
            new_string += i
    return new_string.strip()

def is_all_korean(string):
    for i in string:
        if not 44032<=ord(i)<=55203:
            return False
    return True

def filter_string(strings):
    words = ["[한방]", "(한방)", "한방"]
    result = []
    for st in strings:
        string = st
        '''
        for word in words:
            string = string.replace(word, "")
            string = string.strip()
        '''
        if any([word in string for word in words]):
            continue
        
        if not is_all_korean(string):
            continue
        
        string = clear_string(string)
        result.append(string)
    
    return result


def load_csv(name):
    with open(name, 'r', encoding='utf-8-sig')as f:
        reader = csv.reader(f)
        result = []
        for line in reader:
            result.append(line)
        
    print("data num :", len(result))
    return result

def save_object(data, name):
    ## Save pickle
    with open(name,"wb") as fw:
        pickle.dump(data, fw)

def load_object(name):
    ## Load pickle
    with open(name,"rb") as fr:
        data = pickle.load(fr)
    return data

class wiki_words:
    filename = "words_wiki.pickle"
    
    def save_words(self):
        longword = get_longword_namuwiki()
        print("get_longword_namuwiki :", len(longword))
        
        longword2 = get_logword_kkukowiki()
        print("get_logword_kkukowiki :", len(longword2))
        
        attackword = get_attack_word_namuwiki()
        print("get_attack_word_namuwiki :", len(attackword))
        
        total = longword + longword2 + attackword
        total = filter_string(total)
        print("total :", len(total))
        words = class_word(total)
        
        save_object(words, self.filename)
        
    def load_words(self):
        words = load_object(self.filename)
        return words

class csv_words:
    filename = "words_kor.pickle"
    
    def save_words(self):
        file = load_csv('kr_korean.csv')
        temp = []
        for line in file:
            if is_all_korean(line[0]) and "동사" not in line[1] and "형용사" not in line[1] and len(line[0]) > 1:
                temp.append(line[0])
        temp = filter_string(temp)
        result = class_word(temp)
        save_object(result, self.filename)
    
    def load_words(self):
        words = load_object(self.filename)
        return words

class word_engine:
    def __init__(self, mode = "attack"):
        self.reset()
        self.mode = mode
        
    def get(self, front, combo=""):
        if self.mode=="attack":
            return self.get_attack(front)
        else:
            return self.get_normal(front, combo)
    
    def get_normal(self, front, combo=""):
        result = ""
        dictt = self.words
        if front in dictt.keys():
            if len(dictt[front]) > 0:
                
                if len(combo) > 0:
                    idx = self.find_most_word(dictt[front], combo)
                else:
                    idx = 0
                    
                result = dictt[front][idx]
                del dictt[front][idx]
        print("get :",result)
        return result
    
    def get_attack(self, front):
        result = ""
        dictt = self.words
        if front in dictt.keys():
            if len(dictt[front]) > 0:
                
                ranks = []
                for i in range(len(dictt[front])):
                    word = dictt[front][i]
                    
                    #후보의 끝으로 시작하는 단어가 없는 경우
                    if word[-1] not in self.words_num.keys():
                        ranks.append([i, -1])
                    #== 있는 경우
                    else:
                        ranks.append([i, self.words_num[word[-1]]])
                
                ranks.sort(key = lambda x:x[1])
                idx, _ = ranks[0]
                
                result = dictt[front][idx]
                del dictt[front][idx]
                self.words_num[front] -= 1

        print("get :",result)
        return result

    
    def find_most_word(self, word_list, combo):
        result = 0
        max_count = 0
        for i in range(len(word_list)):
            cur_count = word_list[i].count(combo)
            if cur_count > max_count:
                max_count = cur_count
                result = i
        return result

    def reset(self):
        self.words = sum_worddict([wiki_words().load_words(), csv_words().load_words()])
        self.words = sort_worddict(self.words)
        
        words_num = {}
        for key in self.words.keys():
            words_num[key] = len(self.words[key])
        self.words_num = words_num
        
        print("reset words")
    
    def save(self):
        wiki_words().save_words()
        csv_words().save_words()

def type_korean(string, interval = 0.02):
    pyautogui.typewrite(KorTransform2Eng(string), interval = interval)

def main(mode, interval = 0.02):
    word_en = word_engine(mode)
    
    while True:
        try:
            key = one_key_input()
        except:
            continue
        
        if key=='0':
            break
        elif key=='1':
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("ctrl", "c")
            pyautogui.press("backspace")
            pyautogui.press("backspace")
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
        
            data = data.replace("1", "")
            data = data.strip()
        
            if len(data) > 1:
                front, combo = data[0], data[1]
                word = word_en.get(front, combo)
            else:
                word = word_en.get(data)
            
            type_korean(word, interval)
            
            pyautogui.press("enter")
        elif key=='9':
            word_en.reset()
        elif key=='2':
            pyautogui.press("backspace")
            pyautogui.press("backspace")
            
            if len(data) > 1:
                front, combo = data[0], data[1]
                word = word_en.get(front, combo)
            else:
                word = word_en.get(data)
            
            type_korean(word, interval)
            
            pyautogui.press("enter")


if __name__=="__main__":
    main("long", 0.0001)
