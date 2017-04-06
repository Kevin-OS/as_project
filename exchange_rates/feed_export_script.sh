#!/bin/bash
# script will run rates_spider and store scraped exchange rates in a csv file called rates.csv
file_name=rates.csv
current_date_time=$(date "+%Y.%m.%d-%H.%M.%S")
new_filename=$current_date_time.$file_name
scrapy crawl rates -s FEED_URI=$new_filename -s FEED_FORMAT=CSV
