import numpy
import matplotlib.pyplot as plt
from PIL import Image
import time

start = int(round(time.time() * 1000))

img = Image.open("a.png").convert("L")
img.show()

data_final = numpy.array(img)

filter_size=3
temp = []
indexer = filter_size // 2

#print(data_final)

for i in range(512):

    for j in range(512):

        for z in range(filter_size):
            if i + z - indexer < 0 or i + z - indexer > 512 - 1:
                for c in range(filter_size):
                    temp.append(0)
            else:
                if j + z - indexer < 0 or j + indexer > 512 - 1:
                    temp.append(0)
                else:
                    for k in range(filter_size):
                        temp.append(data_final[i + z - indexer][j + k - indexer])

        temp.sort()
        data_final[i][j] = temp[len(temp) // 2]
        temp = []

print("Execution Time --->", (int(round(time.time() * 1000)) - start))

img = Image.fromarray(data_final)
img.show()

