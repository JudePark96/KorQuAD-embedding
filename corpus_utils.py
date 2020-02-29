from tqdm import tqdm
from konlpy.tag import Mecab


import json


def preprocess_corpus(corpus_path: str, output_path: str) -> None:
    with open(corpus_path) as corpus, open(output_path, 'w', encoding='utf-8') as output:
        dataset_json = json.load(corpus)
        dataset = dataset_json['data']
        for article in tqdm(dataset):
            w_lines = []
            for paragraph in article['paragraphs']:
                w_lines.append(paragraph['context'])
                for qa in paragraph['qas']:
                    q_text = qa['question']
                    for a in qa['answers']:
                        a_text = a['text']
                        # format Question Answer
                        w_lines.append(q_text + ' ' + a_text)
            for line in w_lines:
                output.writelines(line + '\n')

        corpus.close()
        output.close()

def tokenize(corpus_path: str, output_path: str) -> None:
    tokenizer = Mecab()
    with open(corpus_path) as corpus, open(output_path, 'w', encoding='utf-8') as output:
        for line in tqdm(corpus):
            text = ' '.join(tokenizer.morphs(line))
            output.write(text + '\n')

if __name__ == '__main__':
    tokenize('./rsc/data/preprocessed_korquad.txt', './rsc/data/mecab_preprocessed_korquad.txt')
