# importing pyshortner to get Shortner class
from pyshorteners import Shortener

# asking for url to create short url
url: str = input("Enter a url to create shorter url : ")

# Creating variable of Shortner class
s: Shortener = Shortener()
# printing url after shortning it
print("your shortened url is : ", s.tinyurl.short(url))
