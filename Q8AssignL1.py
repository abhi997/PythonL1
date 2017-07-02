import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    year = book.find('year').text
    price = book.find('price').text
    print(title, author, year, price)