from bs4 import BeautifulSoup
import requests

url = "https://www.trustradius.com/products/progress-sitefinity/reviews"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
query = soup.find_all('a', {
    'class' : 'link-to-review-btn'
})

links = []

for link in query:
    links.append('https://www.trustradius.com' + link.get('href'))

def findMaterials(link):
    req = requests.get(link).text
    review = BeautifulSoup(req, 'html.parser')

    sectionHeading = []
    sectionText = []

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

    return(dict(zip(sectionHeading, sectionText)))

dictionary = findMaterials(links[0])

for x, y in dictionary.items():
    print(x,y)

