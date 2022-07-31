#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from datetime import datetime
import time
import re
import os

options = Options()
options.headless = True

locations = (
    ("Adams Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/1uztB", "E"),
    ("Alcott Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/KvztB", "E"),
    ("Arlington High School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/WvztB", "H"),
    ("Beatty Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/jvztB", "E"),
    ("Bryant Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/RvztB", "E"),
    ("Business Services", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/xvztB", "O"),
    ("Business Services - Purchasing", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/2vztB", "O"),
    ("Castle View Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/CwztB", "E"),
    ("Central Middle School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/EwztB", "M"),
    ("Chemawa Middle School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/KwztB", "M"),
    ("Communications Admin", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/PwztB", "O"),
    ("Earhart Middle School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/gwztB", "M"),
    ("Early Childhood", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/twztB", "O"),
    ("Educational Options", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/DxztB", "O"),
    ("Elementary Education", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/JxztB", "O"),
    ("Emerson Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/QxztB", "E"),
    ("Facilities", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/axztB", "O"),
    ("Family Resource Center", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/ixztB", "O"),
    ("Franklin Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/sxztB", "E"),
    ("Fremont Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/wxztB", "E"),
    ("Gage Middle School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/AyztB", "M"),
    ("Harrison Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/IyztB", "E"),
    ("Hawthorne Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/KyztB", "E"),
    ("Highgrove Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/RyztB", "E"),
    ("Highland Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/YyztB", "E"),
    ("Human Resources", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/cyztB", "O"),
    ("Innovation and Learner Engagement", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/syztB", "O"),
    ("Jackson Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/xyztB", "E"),
    ("Jefferson Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/4yztB", "E"),
    ("Kennedy Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/8yztB", "E"),
    ("Lake Mathews Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/CzztB", "E"),
    ("Liberty Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/FzztB", "E"),
    ("Lincoln Continuation High", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/KzztB", "H"),
    ("Longfellow Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/OzztB", "E"),
    ("Madison Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/PzztB", "E"),
    ("Magnolia Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/gzztB", "E"),
    ("Maintenance and Operations", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/izztB", "O"),
    ("Martin Luther King High School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/pzztB", "H"),
    ("Miller Middle School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/uzztB", "M"),
    ("Monroe Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/j1ztB", "E"),
    ("Mt View Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/p1ztB", "E"),
    ("North High School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/y1ztB", "H"),
    ("Nutrition Services - Administration", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/41ztB", "O"),
    ("Pachappa Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/L2ztB", "E"),
    ("Poly High School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/N2ztB", "H"),
    ("Professional Growth Systems", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/Y2ztB", "O"),
    ("Program Development & Extended Learning", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/j2ztB", "O"),
    ("Program Quality/Academic English Learners", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/n2ztB", "O"),
    ("Project Team", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/u2ztB", "O"),
    ("Psychological Services", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/y2ztB", "O"),
    ("Pupil Services", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/52ztB", "O"),
    ("Raincross Continuation High", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/B3ztB", "H"),
    ("Ramona High School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/L3ztB", "H"),
    ("Research, Assessment and Evaluation", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/P3ztB", "O"),
    ("Risk Management", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/V3ztB", "O"),
    ("Rivera Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/a3ztB", "E"),
    ("Riverside Adult School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/A5ztB", "O"),
    ("Secondary Education", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/c3ztB", "O"),
    ("Sierra Middle School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/p3ztB", "M"),
    ("Special Education", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/t3ztB", "O"),
    ("STEM Academy", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/13ztB", "M"),
    ("Sunshine Early Childhood Center", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/53ztB", "E"),
    ("Superintendent", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/A4ztB", "O"),
    ("Taft Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/D4ztB", "E"),
    ("Technology Services", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/I4ztB", "O"),
    ("Transportation", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/N4ztB", "O"),
    ("Twain Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/T4ztB", "E"),
    ("University Middle School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/g4ztB", "M"),
    ("Victoria Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/h4ztB", "E"),
    ("Washington Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/l4ztB", "E"),
    ("Wellness & Engagement", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/o4ztB", "O"),
    ("Woodcrest Elementary School", "https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/s4ztB", "E")
)

outfilename = "./data/"+datetime.now().strftime("%Y-%m-%d")+".txt"
os.makedirs(os.path.dirname(outfilename), exist_ok = True)
with open(outfilename, "w") as outfile:
    for num, location in enumerate(locations):
        success = False
        while not success:
            browser = webdriver.Chrome(options=options)
            try:
                browser.get(location[1])
                time.sleep(30)  # wait 30 seconds for page to load
                response = browser.page_source

                result = re.search('Total Confirmed Cases.*row block-0.*>(\d+)</div>', response)
                if result:  # There's a good number here; use it
                    count = int(result.group(1))
                    success = True
                else:  # No number found; confirm that it really is "No data":
                    result2 = re.search('Total Confirmed Cases.*<div class="top-dummy" style="height: 0px;"></div><div class="bottom-dummy" style="height: 0px;"></div>', response)
                    if result2:  # Really is "No data"; record a 0:
                        count = 0
                        success = True
                    else:
                        print("ERROR: couldn't find data; try again...")
            except WebDriverException:
                print("ERROR: page unavailable; try again...")
                success = False
            browser.quit()
        print(str(num) + "\t" + location[2] + "\t" + str(count) + "\t" + location[0])
        outfile.write(str(num) + "\t" + location[2] + "\t" + str(count) + "\t" + location[0] + "\n")



