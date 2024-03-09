# -*- coding: utf-8 -*-
# /usr/bin/env python3
import argparse
from src.crawler import Crawler
from apscheduler.schedulers.blocking import BlockingScheduler


parser = argparse.ArgumentParser(
    prog="LeetCode-submissions-crawler", description="Get all your submissions!"
)

parser.add_argument("-c", "--cookie", type=str, help="Your cookie for login")
parser.add_argument("-o", "--output", type=str, help="Output path")
parser.add_argument("-d", "--day", type=int, help="Fetching codes in 'day'")
parser.add_argument(
    "-O",
    "--overwrite",
    action="store_true",
    help="Flag to enable overwrite",
    default=False,
)

if __name__ == "__main__":
    args = parser.parse_args()
    scheduler = BlockingScheduler()
    scheduler.add_job(Crawler(args).execute, 'interval', hours=24) 
    scheduler.start()