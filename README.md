# RUSD-COVID

Code for tracking active COVID-19 cases in the [Riverside Unified School District](https://www.riversideunified.org)

## Prerequisites

- python3 via [https://www.python.org](https://www.python.org)
- selenium via `pip3 install selenium`
- numpy via `pip3 install numpy`
- matplotlib via `pip3 install matplotlib`

Additionally, `scrape.py` is configured to use Safari on MacOS, but this could be changed to use other browsers if needed.

Note that this code is "quick and dirty" and has some bad design decisions (like using fixed character offsets to locate data in the Google Data Studio page source, using `time.sleep()` to wait for the page to load, etc.).

## Usage

`python3 scrape.py` to scrape the [RUSD COVID case dashboard](https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/1uztB) and create a new file with today's data (or replace today's file if it already exists).

`python3 plot.py` to generate plots summarizing all the locally saved data.

