from collections import defaultdict
from operator import itemgetter

def best_sender(messages, senders):
    best = defaultdict(int)
    for i in range (len(messages)):
        best[senders[i]]+=len(messages[i].split())
    sorted_best = dict(sorted(best.items(), reverse=True))
    return max(sorted_best, key=sorted_best.get)
messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))