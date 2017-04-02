#!/bin/bash
# script will run rates_spider and store scraped exchange rates in a csv file called rates.csv

scrapy crawl rates -s FEED_URI='rates.csv' -s FEED_FORMAT=CSV
