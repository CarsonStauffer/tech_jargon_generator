import random

verbs = ["tunnel through", "login to", "archive", "sync", "download", "overflow", "terminate"]
nouns = ["database cluster", "mainframe", "CSS", "compiler", "VPN", "ARM processor", "socket layer", "hard drive", "ethernet card", "retina kernel"]

def pick_word_from(list):
    index = random.randint(0, len(verbs)-1)
    return list.pop(index)

print(pick_word_from(verbs) + " the " + pick_word_from(nouns) + " to " + pick_word_from(verbs) + " the " + pick_word_from(nouns))
