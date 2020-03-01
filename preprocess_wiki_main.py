from corpus_utils import make_wiki_corpus, tokenize

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tool for pre-processing wiki dataset')
    parser.add_argument('--corpus_path', type=str, required=True,
                        help='path of corpus')
    parser.add_argument('--output_path', type=str, required=True,
                        help='path of output')
    parser.add_argument('--mode', type=str, required=True,
                        help='preprocess mode')

    args = parser.parse_args()
    corpus_path = args.corpus_path
    output_path = args.output_path
    mode = args.mode

    if mode == 'preprocess':
        make_wiki_corpus(corpus_path, output_path)
    elif mode == 'tokenize':
        tokenize(corpus_path, output_path)
