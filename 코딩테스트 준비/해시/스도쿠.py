from collections import Counter

name = ['Kim', 'Kim', 'Lee', 'Kim', 'Park', 'Kown', 'Lee']
counter = Counter(name)
print(counter['Kim'])

names = ['James', 'Judy', 'Jin']
dic = {v:i for i, v in enumerate(names)}
print(dic)