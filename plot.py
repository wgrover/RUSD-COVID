import os
import matplotlib.pyplot as plt
import numpy

dates = []
elementarys = []
middles = []
highs = []
others = []

plt.figure(figsize=(5, 9))
files = os.listdir(".")
files.sort()

for filename in files:
    if filename.endswith(".txt"):
        print(filename, end="\t")
        dates.append(filename[:10])
        infile = open(filename, "r")
        elementary = 0
        middle = 0
        high = 0
        other = 0
        for line in infile:
            # print(line, end="")
            id, cat, count, name = line.strip().split("\t")
            count = int(count)
            if cat == "E":
                elementary += count
            elif cat == "M":
                middle += count
            elif cat == "H":
                high += count
            elif cat == "O":
                other += count
        print(elementary, middle, high, other, elementary+middle+high)
        elementarys.append(elementary)
        middles.append(middle)
        highs.append(high)
        others.append(other)

schools = numpy.array(elementarys) + numpy.array(middles) + numpy.array(highs)

ax1 = plt.subplot(411)
plt.bar(dates, schools)
plt.text(0.01,0.9,'All schools', transform = ax1.transAxes)
plt.tick_params(labelbottom=False)

ax2 = plt.subplot(412)
plt.bar(dates, elementarys)
plt.text(0.01,0.9,'Elementary schools', transform = ax2.transAxes)
plt.tick_params(labelbottom=False)

ax3 = plt.subplot(413)
plt.bar(dates, middles)
plt.text(0.01,0.9,'Middle schools', transform = ax3.transAxes)
plt.tick_params(labelbottom=False)

ax4 = plt.subplot(414)
plt.bar(dates, highs)
plt.text(0.01,0.9,'High schools', transform = ax4.transAxes)


plt.show()