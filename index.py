# Author: Colton Sweeney
# Date: August 10, 2017
# Name: TrustRadius Review Scraper
#
# Lang: Python
# Dependencies: BeautifulSoup4
#               Requests
#
# Description: As part of my current workload, I have to create
#              weekly reports gathered from reviews on TrustRadius.
#              In order to expedite this process, I decided to create 
#              simple Python bot that scours the TrustRadius page for
#              all new reviews and then creates detailed reports directly 
#              from the information gathered in those reports.
from bs4 import BeautifulSoup
import requests

# Open up TrustRadius page for Sitefinity
url = "https://www.trustradius.com/products/progress-sitefinity/reviews"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")

# Find all review links from main product page
query = soup.find_all('a', {
    'class' : 'link-to-review-btn'
})

# List that holds URLs of individual reviews
links = []

# Append all the URLs to the list we created
for link in query:
    links.append('https://www.trustradius.com' + link.get('href'))

# Function for returning review sections from review page
# return (dictionary): a key-value list of the headings and review text
# parameters: link (string): the url for the review
def findMaterials(link):
    # Parse the given link into some Beautiful Soup
    req = requests.get(link).text
    review = BeautifulSoup(req, 'html.parser')

    # Set up list string variables.
    sectionHeading = []
    sectionText = []

    # Perform find.contents[] for all of the headings and text
    # and append them to our functions variables
    for find in review.find_all('div', {'class': 'description'}):
        # Recieve review section headings
        sectionHeading.append(find.contents[0].contents[0].contents[1].contents[0].contents[0].contents[0].contents[0].contents[0].text)
        sectionHeading.append(find.contents[0].contents[0].contents[1].contents[1].contents[0].contents[0].contents[0].contents[0].text)
        sectionHeading.append(find.contents[0].contents[0].contents[1].contents[2].contents[0].contents[0].contents[0].contents[0].text)
        sectionHeading.append(find.contents[0].contents[0].contents[1].contents[3].contents[0].contents[0].contents[0].contents[0].text)        
        sectionHeading.append(find.contents[0].contents[0].contents[1].contents[4].contents[0].contents[0].contents[0].contents[0].text)
        sectionHeading.append(find.contents[0].contents[0].contents[1].contents[5].contents[0].contents[0].contents[0].contents[0].text)

        # Recieve review text
        sectionText.append(find.contents[0].contents[0].contents[1].contents[0].contents[1].contents[0].contents[0].contents[0].text)
        sectionText.append(find.contents[0].contents[0].contents[1].contents[1].contents[1].contents[0].contents[0].contents[0].text)
        sectionText.append(find.contents[0].contents[0].contents[1].contents[2].contents[1].contents[0].contents[0].contents[0].text)
        sectionText.append(find.contents[0].contents[0].contents[1].contents[3].contents[1].contents[0].contents[0].contents[0].text)
        sectionText.append(find.contents[0].contents[0].contents[1].contents[4].contents[1].contents[0].contents[0].contents[0].text)
        sectionText.append(find.contents[0].contents[0].contents[1].contents[5].contents[1].contents[0].contents[0].contents[0].text)
    # Return a dictionary object of headings and text
    return(dict(zip(sectionHeading, sectionText)))

dictionary = findMaterials(links[0])

for x, y in dictionary.items():
    print(x,y)

