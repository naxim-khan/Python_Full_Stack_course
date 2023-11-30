from bs4  import BeautifulSoup
import lxml
with open ("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_45\\website.html") as file:
    contents = file.read()

soup=BeautifulSoup(contents, 'lxml')


# print(soup.title) # Reading the title of the html file
# print(soup.title.name) # printing the name of the element
# print(soup)    # Printing all the documents.
# print(soup.prettify()) # printing all the docx in indendent version. 
# print(soup.a)

# Pritning all anchro tags i html
all_anchor_tags=soup.find_all(name='a')

# We can also find things by their attributes like we use loop below.


# print(all_anchor_tags)

# getting text of all anchor tags 

for tag in all_anchor_tags:
    # printing text of all anchor tags 
    # print(tag.getText())
    # Geting all the links
    # print(tag.get('href'))
    pass
    

# Getting ID  the head elements
h3_heading=soup.find(name='h1',id='name')

# print(heading)
# Getting element through class name.
section_heading=soup.find(name='h3', class_="heading")
# print(section_heading.get('class'))

company_url=soup.select_one(selector='#name')

headings=soup.select(".heading")
print(headings)

