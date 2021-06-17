from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Mecab
import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 패스로 지정
import matplotlib.font_manager as fm
import re
import collections

from analysis import TextAnalysis
data = {
        'title' : 'Test',
        'text' : '''
        기분 안 좋아.
        ''',
        'stickers': []
                  }
ta = TextAnalysis(data)

result = ta.text_analysis()

print(result)
words = result['word_count']
word_dict = {i:v for i,v,m in word_count }


spwords = set(STOPWORDS)

wordcloud = WordCloud(max_font_size=200, font_path='/content/drive/My Drive/Colab Notebooks/malgun.ttf',
                     stopwords=spwords,
                     background_color='#FFFFFF',
                     width=1200,height=800).generate_from_frequencies(word_dict)


plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 