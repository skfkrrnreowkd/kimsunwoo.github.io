import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# 텍스트 데이터
text = "Natural Language Processing (NLP) is a field of study that combines computer science and linguistics to enable computers to understand human language. NLP is used for a wide range of applications, such as chatbots, sentiment analysis, and machine translation."

# 토큰화
tokens = word_tokenize(text)

# 단어 빈도수 계산
freq_dist = nltk.FreqDist(tokens)

# 가장 빈번한 상위 10개 단어 출력
print(freq_dist.most_common(10))
