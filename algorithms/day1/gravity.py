import random

def build_data(data):
    for i in range(0, 10):
        data.append(random.randint(0, 10))
    return data

data = []
data = build_data(data)
print(data)
count = 0
for num in range(1, len(data)):
    if data[0] <= data[num]:
        count += 1
print(len(data)-1-count)


