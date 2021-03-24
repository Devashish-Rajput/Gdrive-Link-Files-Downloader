import os
os.chdir("Your Path to Save File")
import gdown
with open('urls.txt') as f:
      links = [line.rstrip() for line in f]
i=1
for x in links:
  z=''
  if i<10:
    z='0'+str(i)
  else:
    z=str(i)
  url = 'https://drive.google.com/uc?id='+x
  output = 'Your Title'+z
  gdown.download(url, output, quiet=False)
  i=i+1 
