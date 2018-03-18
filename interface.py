from bs4 import BeautifulSoup
import requests

class Interface:

  def __init__(self):
    self.run = True

  def scrapping(self, word):
    url = "https://google.com/search?q=%s" % (word)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup.find_all('cite')

  def start(self):
    while (self.run):
      print("Hello, what are you looking for? (type exit for exit)")
      word = input('> ')
      if (word == 'exit'):
        self.run = False
      else:
        for link in self.scrapping(word):
          print(link)

app = Interface()
app.start()
