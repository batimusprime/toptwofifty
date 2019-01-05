
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup


#import raw HTML from local file
l = []
soup = BeautifulSoup(open('source.html'), "html.parser")

td = soup.find_all('td')
for t in td:
    t.find_all('titleColumn')
    oname = t.find_all('a')
    for o in oname:
        tex = o.text
        #if len(tex)>1:
        #    l.append(tex.splitlines())
        if len(tex)>2:
            l.append(tex)
f= open("output.txt","w+")
for i in l:
    f.write(i + '\n')

