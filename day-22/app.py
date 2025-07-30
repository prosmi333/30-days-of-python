
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/dataset/45/heart+disease'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
content = response.content  # we get all the content from the website
# beautiful soup will give a chance to parse
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)  # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text())  # UCI Machine Learning Repository: Data Sets
print(soup.body)  # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table')
print('TABLES', tables)
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0]  # the result is a list, we are taking out data from it

# print('TABLE', table.find_all('td')[0].text)
for td in table.find_all('td')[0].text:
    print(td)
