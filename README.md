# Sitefinity Review Scraper
### via TrustRadius 
##### using Python, python-docx, Requests, and BeautifulSoup

## Dependencies
* `pip install --user python-docx`
* `pip install --user requests`
* `pip install beautifulsoup4`

## Description
As part of my current workload, I have to create weekly reports gathered from reviews on TrustRadius. In order to expedite this process, I decided to create simple Python bot that scours the TrustRadius page for all new reviews and then creates detailed reports directly from the information gathered in those reports.

This bot require a few dependencies listed above. Once those are installed on your local environment and you have `git pull`'d for the index.py file, run `python index.py` to activate the script. The bot will scour the TrustRadius page and create a Word document with information like the reviewer's name, position, company, Sitefinity rating, and there overall review. The Word document is formatted to contain each review on it's own page, so the more reviews that the bot scans, the longer the word document.