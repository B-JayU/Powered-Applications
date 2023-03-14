# -*- coding:utf-8 -*-
import logging
import sys

from preprocessing import parse_arguments, clean_input, preprocess_input, get_suggestions

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_out = logging.StreamHandler(sys.stdout)
console_out.setLevel(logging.DEBUG)
logger.addHandler(console_out)

def main():
    input_text = parse_arguments()
    processed = clean_input(input_text)
    tokenized_sentences = preprocess_input(processed)
    suggestions = get_suggestions(tokenized_sentences)
    print(suggestions)


main()


    