#!/usr/bin/env pypy
import numpy
import matplotlib.pyplot as plt
from PIL import Image
import time
import threading
from multiprocessing import Pool    


start = int(round(time.time() * 1000))

img = Image.open("a.png").convert("L")
img.show()

data_final = numpy.array(img)

filter_size=3
temp = []
indexer = filter_size // 2

# sairam
class Thread1(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        temp = []

        #print ("Starting " + self.name + "\n")

        for i in range(256):

            for j in range(256):

                for z in range(filter_size):
                    if i + z - indexer < 0 or i + z - indexer > 256 - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > 256 - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data_final[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []

        #data[0:0 + data_final.shape[0], 0:0 + data_final.shape[1]] = data_final
        #img = Image.fromarray(data_final)
        #img.show()
       # print ("End " + self.name + "\n")


class Thread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        temp = []

        print ("Starting " + self.name + "\n")

        for i in range(256):

            for j in range(256,512):

                for z in range(filter_size):
                    if i + z - indexer < 0 or i + z - indexer > 256 - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 256 or j + indexer > 512 - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data_final[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []

               # data[0:0 + data_final.shape[0], 256:256 + data_final.shape[1]] = data_final
        #img = Image.fromarray(data_final)
        #img.show()
       # print ("End " + self.name + "\n")


class Thread3(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        temp=[]
        for i in range(256, 512):

            for j in range(256):

                for z in range(filter_size):
                    if i + z - indexer < 256 or i + z - indexer > 512 - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > 256 - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data_final[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []

        #img = Image.fromarray(data_final)
        #img.show()

        #print ("End " + self.name + "\n")


class Thread4(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        temp = []

        print ("Starting " + self.name + "\n")

        for i in range(256,512):

            for j in range(256,512):

                for z in range(filter_size):
                    if i + z - indexer < 256 or i + z - indexer > 512 - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 256 or j + indexer > 512 - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data_final[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []


       # img = Image.fromarray(data_final)
       # img.show()
       # print ("End " + self.name + "\n")




thread1 = Thread1(1, "Thread 1")
thread2 = Thread2(2, "Thread 2")
thread3 = Thread3(3, "Thread 3")
thread4 = Thread4(3, "Thread 4")


thread4.start()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()


print("Execution Time --->", (int(round(time.time() * 1000)) - start))
img = Image.fromarray(data_final)
img.show()
#omsairam
