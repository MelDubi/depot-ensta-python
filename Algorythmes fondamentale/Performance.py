import re
from bintrees import FastAVLTree, FastRBTree
from time import process_time
import matplotlib.pyplot as plt


def decode(filename):
    sepwords = re.compile("[^a-zA-Z']+")
    with open(filename) as f:
        for line in f:
            for word in sepwords.split(line.strip()):
                if len(word) > 0:
                    print(word)


def decode_list(filename):
    sepwords = re.compile("[^a-zA-Z']+")
    liste = []
    with open(filename) as f:
        for line in f:
            for word in sepwords.split(line.strip()):
                if len(word) > 0:
                    liste.append(word)
    return liste


def get_first_100_word(voc, n):
    liste = voc[:n]
    return liste


def compare(voc, texte):
    cpt = 0
    start = process_time()
    for word in texte:
        if word in voc:
            cpt = cpt + 1
    stop = process_time()
    time = stop-start
    print("Process time is :", time)
    print("Counter Value is", cpt)

# def compare(voc, texte):
#     cpt = 0
#     start = process_time()
#     for i in range(len(voc)):
#         for j in range(len(texte)):
#             if voc[i] == texte[j]:
#                 cpt = cpt + 1
#     stop = process_time()
#     time = stop-start
#     print("Process time is :", time)
#     print("Counter Value is", cpt)


def struct_set(voc):
    struct_set = set(voc)
    return struct_set


def struct_tree(voc):
    rbt = FastRBTree()
    for word in voc:
        rbt.insert(word, None)
    return rbt

def get_point(x_nb, y_list, y_dico, y_tree, nb, vocab, text_ref):
    vocab_hundred_word_list, vocab_hundred_word_set, vocab_hundred_word_tree = get_first_word(vocab, nb)
    #cnt, time_process_list = count_word(vocab_hundred_word_list, text_ref)
    cnt, time_process_dico = count_word(vocab_hundred_word_set, text_ref)
    cnt, time_process_tree = count_word(vocab_hundred_word_tree, text_ref)

    x_nb.append(nb)
    #y_list.append(time_process_list)
    y_dico.append(time_process_dico)
    y_tree.append(time_process_tree)

    return x_nb, y_list, y_dico, y_tree

if __name__ == '__main__':

    # Create list from vocabulaire and text
    voc = decode_list("W.txt")
    texte = decode_list('Please.txt')

    # Tronque à 100 la liste
    voc_100 = get_first_100_word(voc, 100)
    texte_100 = get_first_100_word(texte, 100)

    print(voc_100)
    print(texte_100)

    # List comparison between 100 words in vocabulaire and texte
    compare(voc_100, texte)

    # # Change liste to set
    # voc_set = struct_set(voc_100)
    # texte_set = struct_set(texte_100)
    #
    # print(voc_set)
    # print(texte_set)
    #
    # # Set comparison
    # compare(voc_set, texte_set)
    #
    # # Change set to tree
    # voc_tree = struct_tree(voc_100)
    # texte_tree = struct_tree(texte_100)
    #
    # print(voc_tree)
    # print(texte_tree)
    #
    # # Tree comparison
    # compare(voc_tree, texte_tree)








    # vocab_hundred_word_list, vocab_hundred_word_set, vocab_hundred_word_tree = get_first_word(vocab_gb, 100)
    #
    # cnt, time_process = count_word(vocab_hundred_word_list, grail)
    # print("cnt: %s, time process: %s" %(cnt, time_process))
    # cnt, time_process = count_word(vocab_hundred_word_set, grail)
    # print("cnt: %s, time process: %s" %(cnt, time_process))
    # cnt, time_process = count_word(vocab_hundred_word_tree, grail)
    # print("cnt: %s, time process: %s" %(cnt, time_process))

x_nb = []
y_list = []
y_dico = []
y_tree = []
nb_words = [100, 300, 1000, 3000, 10000, 30000, 50000, 70000, 100000]

x_nb_full = []
y_list_full = []
y_dico_full = []
y_tree_full = []


for i in range(10):
    for nb_word in nb_words:
        x_nb, y_list, y_dico, y_tree = get_point(x_nb, y_list, y_dico, y_tree, nb_word, vocab_gb, grail)

    x_nb_full.append(x_nb)
    y_list_full.append(y_list)
    y_dico_full.append(y_dico)
    y_tree_full.append(y_tree)


for i in range(len(y_tree_full)):
    plt.plot(x_nb_full[i], y_dico_full[i], label="dico")
    plt.plot(x_nb_full[i], y_tree_full[i], label="tree")

#plt.plot(x_nb, y_list, label="list")
plt.plot(x_nb, y_dico, label="dico")
plt.plot(x_nb, y_tree, label="tree")
plt.legend()
plt.show()








