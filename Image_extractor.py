#importing modules 
import ipywidgets as widgets
import urllib.request
from skimage import io
import cv2
textarea=widgets.Text(description='link:',disabled=False,placeholder='EX:https://www.uncannyvision.com/',value=input())
url=textarea.value
display(textarea)
text=urllib.request.urlopen(url)
file=text.read()
decoded=file.decode()
corpus=set()
filter=''
index=0
#All links are stored in corpus
end=0
l=decoded.count("img")
leng=len(decoded)
for i in range(l):
    index=decoded.find(r"img",end,leng)
    src=decoded.find(r"src=",index,leng)
    end=decoded.find('\"',src+5,leng)
    filter+=decoded[src+5:end:]
    corpus.add(filter)
    filter=''
print(l)
try:
    for i in list(corpus):
        image=io.imread(i)
        
        k=cv2.resize(image,(400,400))
        cv2.imshow("Images",cv2.cvtColor(k,cv2.COLOR_BGR2RGB))
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    
except:
    pass