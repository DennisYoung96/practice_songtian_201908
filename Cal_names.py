
#e10.4Cal《冰与火之歌》全集（1-5卷）.py
import jieba
excludes = {"他们","我们","自己","一个","什么","没有","知道","不是","一样","可以","还有","不会","起来","就是","这里","这些","你们","还是","这个","不能","这样","怎么","只有","只是"}
txt = open("《冰与火之歌》全集（1-5卷）.txt", "r").read()
jieba.add_word("丹妮斯")
jieba.add_word("兰尼斯特")
jieba.add_word("史塔克")
jieba.add_word("史坦尼斯")
jieba.add_word("史塔克")
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:  #排除单个字符的分词结果
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
words = ''
for i in range(50):
    word, count = items[i]
    words += str(word)+' '
    print ("{0:<10}{1:>5}".format(word, count))
'''
#e10.2Cal A Game of Thrones.py
excludes = {"the","and","of","you","a","i","my","in",'”', 'to', 'his', 'he',\
    'was', 'her', 'it', 'had', 'she', 'as', 'him', 'with', 'that', 'said', 'not',\
    'at', 'for', 'on', 'but', 'they', 'is', 'from', 'them', 'have', 'see',\
    'be', 'were', 'would', 'no', 'all', 'me', 'ser', 'when', '“i', 'will',\
    'your', 'if', 'so', 'could', 'one', 'their', 'ned', 'out', 'up', 'now',\
    'man', 'back', 'are', '…', 'been', 'there', 'down', 'what', 'did', 'know',\
    'do', 'this', 'like', 'men', 'by', 'or', '“the', '“you', 'than', 'who',\
    'only', 'we', 'more', 'off', 'over', 'even', 'an', 'here', 'old', 'into'}
def getText():
    txt = open("A Game of Thrones.txt", "r", encoding = 'utf-8').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:			
    counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])    
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
words = ''
for i in range(20):
    word, count = items[i]
    words += str(word) + ' '
    print ("{0:<10}{1:>5}".format(word, count))
# print(words)
'''
from wordcloud import WordCloud

w = WordCloud(font_path = "simkai.ttf",background_color = "skyblue",width = 800, height = 600, margin = 2).generate(words)
import matplotlib.pyplot as plt 
plt.imshow(w)
plt.axis("off")
plt.show()

w.to_file('test.png')