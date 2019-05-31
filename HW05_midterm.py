## Home work 6, midterm test


## 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("algae.csv")
print(data)

result = data.groupby('genus').mean()
print(result)

sns.set(style="ticks")

met = list(result)
fig, axs = plt.subplots(ncols=5)
for i in range(len(met)):
    sns.catplot(x="genus", y=met[i], kind="bar", data=data, ax=axs[i])
plt.show(block=True)


## 2
my_iter = map(lambda x: True if x%3 == 0 else False, [1,2,3,4,5,6])
print(list(my_iter))

print("______________________________")

x = my_iter
while True:
    try:
        print(next(x))
    except StopIteration:
        break
# Error here is "StopIteration". I have fixed it with try-except block

# Iterators vs lists: you can create any pattern of iterators
# (iterator objects). Also you can use it in infinite mode
# while the answer will not be found. Also it can be called
# exactly in the moment and doesnt full the memory.


## 3
print("\nThird part of the test.")
import requests

BASE = 'http://numbersapi.com/'
KB_ENDPOINT = [17, 45, 999, 1883]
MATH = 'math'
words_uninteresting = ['uninteresting', 'boring', 'unremarkable', 'missing']


print("Checking for MATH sense:")
for x in KB_ENDPOINT:
    result = requests.get(BASE + str(x) + '/' + MATH)
    if result.ok:
        uninterest = False
        for w in words_uninteresting:
            if result.text.find(w) != -1:
                print("no|||", result.text)
                uninterest = True
                break
        if not uninterest:
            print("math|||", result.text)
    else:
        print('Smth went wrong ', result.status_code)

print("\nChecking for HISTORICAL sense:")
for x in KB_ENDPOINT:
    result = requests.get(BASE + str(x))
    if result.ok:
        uninterest = False
        for w in words_uninteresting:
            if result.text.find(w) != -1:
                print("no|||", result.text)
                uninterest = True
                break
        if not uninterest:
            print("hist|||", result.text)
    else:
        print('Smth went wrong ', result.status_code)
