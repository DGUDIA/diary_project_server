from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

def wordcloud_s(sender, diary):
    wordcloud = WordCloud(font_path=os.path.join(os.path.dirname(os.path.abspath(__file__)))+'/CookieRun Regular.ttf', background_color='white').generate(diary)

    plt.figure(figsize=(22,22)) #이미지 사이즈 지정
    plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
    plt.axis('off') #x y 축 숫자 제거
    plt.show() 
    plt.savefig(fname = os.path.join(os.path.dirname(os.path.abspath(__file__)))+'/'+sender.replace('@','').replace('.',''))
