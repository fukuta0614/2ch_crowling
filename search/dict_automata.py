
import random
import time
import pickle
import re

words = ("東京","東京大学","東大","京都大学","大学","大阪")
words2 = ("東海",)
sentence = "東大とは東京大学のことで東京にあり京都大学とは異なり、タグマ、ましてや大阪大学や名古屋大学ではない、たまに東京大と略される"


class State(object):
    def __init__(self,word,permission = False):
        self.word = word
        self.permission= permission
        self.edge = []

    def add_edge(self,char):
        self.edge.append(char)

    def has_edge(self,char):
        return char in self.edge

    def has_permission(self):
        return self.permission

    @staticmethod
    def create_start():
        node = State(None)
        return node


class StateMachine(object):
    def __init__(self):
        start = State.create_start()
        self.states = {"start":start}
        self.current_key = "start"
        self.discovery = []

    def make_states(self,dictionary):
        for word in dictionary:
            key = ""
            for char in word:
                key += char
                if not key in self.states:
                    self.states[self.current_key].add_edge(char)
                    st = State(key,key == word)
                    self.states[key] = st
                self.current_key = key

            self.current_key = "start"

    def count_document(self,document):

        index = 0
        while index < len(document):
            # print (index)
            if not self.has_edge(sentence[index]):
                # print(sentence[index],self.discovery)
                index += 1
                continue
            # print("ok")
            key = ""
            while self.has_edge(sentence[index]):
                key += sentence[index]
                self.current_key = key
                index += 1
                if index >= len(document) - 1:
                    break

            discovery_word = self.states[self.current_key].word
            if (not discovery_word in self.discovery) and self.states[self.current_key].has_permission():
                self.discovery.append(discovery_word)

            self.current_key = "start"


    def has_edge(self,char):
        return self.states[self.current_key].has_edge(char)

    def printedge(self):
        for key in sorted(self.states)[:300]:
            print(key,self.states[key].edge,self.states[key].permission)
        print(self.discovery)

def remove():

    with open("sorted_word2.txt", "r") as f:
        raw_data = f.read().split('\n')
    remove_words = []
    # p = re.compile(r'^\d{4}年')
    p = re.compile(r'^\d+月\d+日( \(旧暦\))?$')
    for word in raw_data:
        if p.search(word):
            print(word)
            remove_words.append(word)

    for word in remove_words:
        raw_data.remove(word)

    with open('removed_word_list.txt','a') as f:
        for word in remove_words:
            f.write(word + '\n')

    with open('sorted_word1.txt', 'w') as f:
        for word in raw_data:
            f.write(word + '\n')
def main():
    # start = time.time()

    with open("sorted_word1.txt", "r") as f:
        raw_data = f.read().split('\n')


    # with open("AA/sample.txt","r") as f:
    # 	raw_document = f.readlines()
    sm = StateMachine()

    # data = []
    # for i in range(100000):
    # 	data.append(random.choice(raw_data)[:-1])
        # data.append(raw_data[i][:-1])
    # print(raw_data[0])

    sm.make_states(raw_data)
    # sm.make_states(words)
    with open('dict_state_machine.pickle', 'wb') as f:
        pickle.dump(sm, f)
    # sm.count_document(sentence)
    # with open('dict_state_machine.pickle', 'rb') as f:
    #     sm = pickle.load(f)
    # sm.printedge()

    # elapsed_time = time.time() - start
    # print("my_algorithm : {0}".format(elapsed_time))


if __name__ == '__main__':
    main()









