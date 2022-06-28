##############################   Datasets of books and authors from Amazon ######################################
import requests
import bs4 

#List For books and authors 
books_and_authors = []

 #Variables
url ='https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg='
page_number = 1
page_still_valid =True


#To grapp name of books and authors
while page_still_valid:
    
    #To get Pages
    pages_url = url+str(page_number)
    get_pages = requests.get(pages_url)
    
    #To get out from pages
    if page_number >= 3:
        break
    
    soup = bs4.BeautifulSoup(get_pages.text , "lxml") #To arrange HTML Document
    
    #To grapping
    for i in soup.select("._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"):
        books_and_authors.append(i.text)
        
    page_number += 1
    books = books_and_authors[::2]
    authors = books_and_authors[1::2]

# Test the application 
books[3] # You can see the number of book you want to garp it and write his number-1
#or 
authors[3] # You can see the number of book you want to garp name of his author it and write his number-1