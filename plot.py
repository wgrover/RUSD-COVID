import os
import matplotlib.pyplot as plt
import numpy

def url():
    plt.gcf().text(0.13, 0.85, "https://wgrover.github.io/RUSD-COVID", fontsize=8)

dates = []
elementarys = []
middles = []
highs = []
others = []

files = os.listdir("./data")
files.sort()
print("\t\tElem\tMidd\tHigh\tOther\tSchools")

for filename in files:
    print(filename[:10], end="\t")
    dates.append(filename[:10])
    infile = open("./data/" + filename, "r")
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
    print(f"{elementary}\t{middle}\t{high}\t{other}\t{elementary+middle+high}")
    elementarys.append(elementary)
    middles.append(middle)
    highs.append(high)
    others.append(other)

schools = numpy.array(elementarys) + numpy.array(middles) + numpy.array(highs)
dates = [date[-2:] for date in dates]  # temporary for January

plt.cla()
plt.bar(dates, schools, color="k")
plt.title("Active cases at all RUSD schools (14-day rolling window)")
plt.xlabel("January 2022")
url()
plt.savefig("all_schools.png")

plt.cla()
plt.bar(dates, elementarys, color="b")
plt.title("Active cases at elementary schools (14-day rolling window)")
plt.xlabel("January 2022")
plt.savefig("elementary_schools.png")

plt.cla()
plt.bar(dates, middles, color="orange")
plt.title("Active cases at middle schools (14-day rolling window)")
plt.xlabel("January 2022")
plt.savefig("middle_schools.png")

plt.cla()
plt.bar(dates, highs, color="r")
plt.title("Active cases at high schools (14-day rolling window)")
plt.xlabel("January 2022")
plt.savefig("high_schools.png")

plt.cla()
plt.bar(dates, others, color="0.80")
plt.title("Active non-school cases (14-day rolling window)")
plt.xlabel("January 2022")
plt.savefig("others.png")