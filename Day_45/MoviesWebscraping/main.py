from bs4 import BeautifulSoup 
import requests
import lxml

text_file_path=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_45\\MoviesWebscraping\\top100movies.txt")
content=requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

soup=BeautifulSoup(content.text,'lxml')

movies_list=reversed(soup.find_all('h3',class_='listicleItem_listicle-item__title__hW_Kn'))
with open(text_file_path, 'w') as file:
    for movie in movies_list:
        file.write(movie.text+'\n')
print(f"Movies list saved to the txt file.")
        
