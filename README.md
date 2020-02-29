# KorQuAD-embedding
Embedding Model Study

# 소개

일반적인 컴퓨터에서 한글 위키피디아 데이터를 전처리(불필요한 문자 제거, 형태소 분석기를 통한 구분 등)하기엔 사양이 부족하기 마련입니다.
그렇기 때문에, 한국어 질의응답 데이터(KorQuAD)를 바탕으로 데이터를 전처리하고 임베딩 모델을 구축하였습니다.

부족하겠지만 개인 공부 용으로 충분할 것이라고 생각됩니다.

# 코드 실행 방법

1. `pip3 install -r requirements.txt`

이 과정에서 만약 `Konlpy` 관련 설치 에러가 발생한다면 [제 블로그 글](https://judepark96.github.io/blog/mecab/nlp/2020/02/29/Mac-OS-X-%EC%97%90%EC%84%9C-MeCab-%EC%84%A4%EC%B9%98-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0.html)을 참고해주세요.

2. `python3 preprocess_main.py --corpus_path --output_path --mode`

형태소 분석기 통하여 전처리를 하기 전에 우선 데이터를 따로 갖추어놓아야합니다. 그럴 때는 `python3 preprocess_main.py --corpus_path <질의응답_파일.json> --output_path <output_path/filename> --mode preprocess` 를 해주세요.
그 이후에, `python3 preprocess_main.py --corpus_path <전처리.txt> --output_path <output_path/filename> --mode tokenize` 를 하면 형태소 분석기를 통한 전처리를 거친 텍스트 파일이 나옵니다.

> 본 저장소에서는 Mecab 을 사용하였습니다.

3. `python3 embedding.main.py --corpus_path --output_path --size`

`size` 는 임베딩 모델의 차원을 의미합니다. 현재는 Word2Vec 만을 학습할 수 있습니다.
