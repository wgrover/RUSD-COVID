#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy
from datetime import datetime, timedelta

def url():
    plt.gcf().text(0.085, 0.82, "https://wgrover.github.io/RUSD-COVID", fontsize=7)
    plt.gcf().text(0.94, 0.05, "2022")

dates = []
elementarys = []
middles = []
highs = []
others = []
missed_dates = []

files = os.listdir("./data")
files.sort()

checked_dates = []

for filename in files:
    if ".DS_Store" in filename:
        continue
    checked_dates.append(datetime.strptime(filename[:10], "%Y-%m-%d"))

print("\t\tElem\tMidd\tHigh\tOther\tSchools")

first_day = checked_dates[0]
print("\t\tFIRSTDAY ", first_day.strftime("%m/%d/%Y"))

last_day = checked_dates[-1]
print("\t\tLASTDAY ", last_day.strftime("%m/%d/%Y"))

num_days = (last_day - first_day).days + 1

all_dates = [first_day + timedelta(days=x) for x in range(num_days)]

for date in all_dates:
    print(date.strftime("%m/%d/%Y"), end="\t")
    if date in checked_dates:
        dates.append(date)
        infile = open("./data/" + date.strftime("%Y-%m-%d") + ".txt", "r")
        elementary = 0
        middle = 0
        high = 0
        other = 0
        for line in infile:
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
    else:
        print("MISSED")
        missed_dates.append(date)


schools = numpy.array(elementarys) + numpy.array(middles) + numpy.array(highs)

plt.figure(figsize=(6, 3), dpi=300)

plt.cla()
plt.bar(dates, schools, color="k")
span = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
plt.plot(missed_dates, [0.02*span] * len(missed_dates), "ro", markersize=2)
plt.title("Active cases at all RUSD schools (14-day rolling window)")
url()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %e"))
for label in plt.gca().get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
plt.tight_layout()
plt.savefig("all_schools.png")

plt.cla()
plt.bar(dates, elementarys, color="b")
span = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
plt.plot(missed_dates, [0.02*span] * len(missed_dates), "ro", markersize=2)
plt.title("Active cases at elementary schools (14-day rolling window)")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %e"))
for label in plt.gca().get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
plt.savefig("elementary_schools.png")

plt.cla()
plt.bar(dates, middles, color="green")
span = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
plt.plot(missed_dates, [0.02*span] * len(missed_dates), "ro", markersize=2)
plt.title("Active cases at middle schools (14-day rolling window)")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %e"))
for label in plt.gca().get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
plt.savefig("middle_schools.png")

plt.cla()
plt.bar(dates, highs, color="orange")
span = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
plt.plot(missed_dates, [0.02*span] * len(missed_dates), "ro", markersize=2)
plt.title("Active cases at high schools (14-day rolling window)")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %e"))
for label in plt.gca().get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
plt.savefig("high_schools.png")

plt.cla()
plt.bar(dates, others, color="0.80")
span = plt.gca().get_ylim()[1] - plt.gca().get_ylim()[0]
plt.plot(missed_dates, [0.02*span] * len(missed_dates), "ro", markersize=2)
plt.title("Active non-school cases (14-day rolling window)")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %e"))
for label in plt.gca().get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
plt.savefig("others.png")
