from tqdm import tqdm
from konlpy.tag import Mecab
from gensim.corpora import WikiCorpus, Dictionary
from gensim.utils import to_unicode


import json
import re, json, glob, argparse


WIKI_REMOVE_CHARS = re.compile("'+|(=+.{2,30}=+)|__TOC__|(ファイル:).+|:(en|de|it|fr|es|kr|zh|no|fi):|\n", re.UNICODE)
WIKI_SPACE_CHARS = re.compile("(\\s|゙|゚|　)+", re.UNICODE)
EMAIL_PATTERN = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.UNICODE)
URL_PATTERN = re.compile("(ftp|http|https)?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", re.UNICODE)
WIKI_REMOVE_TOKEN_CHARS = re.compile("(\\*$|:$|^파일:.+|^;)", re.UNICODE)
MULTIPLE_SPACES = re.compile(' +', re.UNICODE)


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

def exec_wiki_regex(content, token_min_len=2, token_max_len=100, lower=True):
    content = re.sub(EMAIL_PATTERN, ' ', content)  # remove email pattern
    content = re.sub(URL_PATTERN, ' ', content)  # remove url pattern
    content = re.sub(WIKI_REMOVE_CHARS, ' ', content)  # remove unnecessary chars
    content = re.sub(WIKI_SPACE_CHARS, ' ', content)
    content = re.sub(MULTIPLE_SPACES, ' ', content)
    tokens = content.replace(", )", "").split(" ")
    result = []
    for token in tokens:
        if not token.startswith('_'):
            token_candidate = to_unicode(re.sub(WIKI_REMOVE_TOKEN_CHARS, '', token))
        else:
            token_candidate = ""
        if len(token_candidate) > 0:
            result.append(token_candidate)
    return result


def make_wiki_corpus(in_f, out_f):
    output = open(out_f, 'w')
    wiki = WikiCorpus(in_f, tokenizer_func=exec_wiki_regex, dictionary=Dictionary())
    i = 0
    for text in tqdm(wiki.get_texts()):
        output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
        i = i + 1
        if (i % 10000 == 0):
            print('Processed ' + str(i) + ' articles')
    output.close()
    print('Processing complete!')

def tokenize(corpus_path: str, output_path: str) -> None:
    tokenizer = Mecab()
    with open(corpus_path) as corpus, open(output_path, 'w', encoding='utf-8') as output:
        for line in tqdm(corpus):
            text = ' '.join(tokenizer.morphs(line))
            output.write(text + '\n')

if __name__ == '__main__':
    tokenize('./rsc/data/preprocessed_korquad.txt', './rsc/data/mecab_preprocessed_korquad.txt')
