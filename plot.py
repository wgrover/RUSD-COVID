import os
import matplotlib.pyplot as plt
import numpy

dates = []
elementarys = []
middles = []
highs = []
others = []

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
dates = [date[-2:] for date in dates]

plt.cla()
plt.bar(dates, schools)
plt.title("Total cases at RUSD schools (14-day rolling window)")
plt.xlabel("January 2021")
plt.savefig("all_schools.png")

plt.cla()
plt.bar(dates, elementarys)
plt.title("Elementary schools (14-day rolling window)")
plt.xlabel("January 2021")
plt.savefig("elementary_schools.png")

plt.cla()
plt.bar(dates, middles)
plt.title("Middle schools (14-day rolling window)")
plt.xlabel("January 2021")
plt.savefig("middle_schools.png")

plt.cla()
plt.bar(dates, highs)
plt.title("High schools (14-day rolling window)")
plt.xlabel("January 2021")
plt.savefig("high_schools.png")

