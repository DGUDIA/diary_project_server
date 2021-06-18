def wordcloud_s(sender, diary):    
    from konlpy.tag import Twitter
    from sklearn.feature_extraction.text import TfidfVectorizer
    from collections import defaultdict
    from collections import Counter
    import os
    import stylecloud

    kkma=Twitter()
    speech=kkma.nouns(diary)        
    print(result)

    cnt = Counter(speechW)

    import pytagcloud

    n=cnt.most_common(50) # 상위 50개의 단어
    print(n)
    speech_wc=pytagcloud.make_tags(n,maxsize=80) # 워드 클라우드 생성
    print(speech_wc)
    pytagcloud.create_tag_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), speech_wc, str(sender)+'.png',size=(600,600),
                               fontname='We',rectangular=False
    # #                           ))