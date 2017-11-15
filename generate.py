import random

verbs = ["tunnel through", "login to", "archive", "sync", "download", "overflow", "terminate"]
nouns = ["database cluster", "mainframe", "CSS", "compiler", "VPN", "ARM processor", "socket layer", "hard drive", "ethernet card", "retina kernel"]


verb1_index = random.randint(0, len(verbs)-1)
verb1 = verbs.pop(verb1_index)

verb2_index = random.randint(0, len(verbs)-1)
verb2 = verbs.pop(verb2_index)

noun1_index = random.randint(0, len(nouns)-1)
noun1 = nouns.pop(noun1_index)

noun2_index = random.randint(0, len(nouns)-1)
noun2 = nouns.pop(noun2_index)


# verb1 = verbs.remove("sync")
# print(verb1)
# todo: don't reuse words
print(verb1 + " the " + noun1 + " to " + verb2 + " the " + noun2)
