from gensim.models import Word2Vec

import argparse
import logging
import multiprocessing


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tool for embedding')
    parser.add_argument('--corpus_path', type=str, required=True,
                        help='path of corpus')
    parser.add_argument('--output_path', type=str, required=True,
                        help='path of output')

    parser.add_argument('--size', type=int, required=True,
                        help='dimension size')

    args = parser.parse_args()
    corpus_path = args.corpus_path
    output_path = args.output_path
    dim_size = args.size

    worker = multiprocessing.cpu_count()

    corpus = [sent.strip().split(' ') for sent in open(corpus_path, 'r').readlines()]
    model = Word2Vec(corpus, size=dim_size, workers=worker, sg=1)
    model.save(output_path)