from corpus_utils import preprocess_corpus

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tool for pre-processing korquad dataset')
    parser.add_argument('--corpus_path', type=str, required=True,
                        help='path of corpus')
    parser.add_argument('--output_path', type=str, required=True,
                        help='path of output')

    args = parser.parse_args()
    corpus_path = args.corpus_path
    output_path = args.output_path

    preprocess_corpus(corpus_path, output_path)
