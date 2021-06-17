import pandas
import random

def sentence_picker(senti):
    sad = ["그랬군요 ㅠㅠㅠ 다이아리도 슬퍼요... 좋은 글 읽고 조금이라도 힘내세요!"]
    neutral = ["오늘 일기에서는 감정이 느껴지지는 않아요! 좋은 의미겠죠?", "중립적인 일기예요!"]
    happy = ["꺄아!!! 당신이 행복하다면, 다이아리도 행복헤요!!!"]
    anxious = ["불안해하지말고, 우선 한숨자고 생각하는건 어때요? ㅠㅠㅠ 다 잘될거예요!"]
    angry = ["일단 일기로도 더 적어서 풀고, 잠도 더 자고 일어나서 생각해봐요! 화난 감정 이해하지만 너무 당신을 괴롭히진 말아요!"]
    exceptp = ["뭔지 모르겠네요!", "무슨 뜻인지 모르겠어요."]
    list_matrix = [sad, neutral, happy, anxious, angry, exceptp]
    n = random.randint(1,3)
    return list_matrix[senti][len(list_matrix[senti])%n - 1]

sentence_picker(0)


