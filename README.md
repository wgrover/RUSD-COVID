# RUSD-COVID

Code for tracking active COVID-19 cases in the [Riverside Unified School District](https://www.riversideunified.org).  The resulting plots are available at [https://wgrover.github.io/RUSD-COVID](https://wgrover.github.io/RUSD-COVID).

## Prerequisites

To run the code on a Raspberry Pi:

- selenium via `pip3 install selenium`
- chromedriver via `sudo apt install chromium-chromedriver`
- numpy via `pip3 install numpy`
- matplotlib via `pip3 install matplotlib`

## Usage

`python3 scrape.py` to scrape the [RUSD COVID case dashboard](https://datastudio.google.com/u/0/reporting/768d990d-b5cc-459f-9d31-a8b68e950ae1/page/1uztB) and create a new file in the `data` directory with today's data (or replace today's file if it already exists).

`python3 plot.py` to generate plots summarizing all the locally saved data.

`make` executes a makefile that scrapes the dashboard, generates plots, and pushes the results to the GitHub repository.  This is performed automatically every night at 8:00 PM using the `crontab` line `0 20 * * * cd /home/wgrover/RUSD-COVID && make -k > debug.log 2>&1` running on a Raspberry Pi 4B sitting on my desk at home.

