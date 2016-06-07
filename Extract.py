import urllib2, bs4

urlBody = 'file:///C:/Users/User/Desktop/PythonBs4DataExtract/'
urlNum = 1
fileExt = '.html'

for x in range(1,11):
  urlNum = x
  url = urlBody + str(urlNum) + fileExt
  response = urllib2.urlopen(url)
  soup = bs4.BeautifulSoup(response, "html.parser")
  s = str(soup.select('#content > p')[1])
  f = open("ExtractedData.html", "a")
  f.write(s)
  f.write("\n")
  print str(urlNum) + fileExt + " extracted."
  f.close()