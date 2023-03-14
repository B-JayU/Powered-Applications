# -*- coding:euc-kr -*-

from func_compute import compute_total_average_word_length, compute_total_unique_words_fraction
from func_compute import count_total_syllables, count_total_words
from func_compute import compute_flesch_reading_ease, get_reading_level_from_flesch
from func_compute import count_word_usage, count_sentence_syllables

import argparse
import nltk

def parse_arguments():
    parser = argparse.ArgumentParser(description="Receive text to be edited")
    parser.add_argument("text", metavar="input text", type=str)
    args = parser.parse_args()
    return args.text


def clean_input(text):
    return str(text.encode().decode("ascii", errors="ignore"))


def preprocess_input(text):
    sentences = nltk.sent_tokenize(text)
    tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return tokens


def get_suggestions(sentence_list):
    
    told_said_usage = sum(
        (count_word_usage(tokens, ["told", "said"]) for tokens in sentence_list)
    )
    but_and_usage = sum(
        (count_word_usage(tokens, ["but", "and"]) for tokens in sentence_list)
    )
    wh_adverbs_usage = sum(
        (
            count_word_usage(
                tokens,
                ["when",
                 "where",
                 "why", 
                 "whence",
                 "whereby",
                 "wherein",
                 "whereupon"
                 ],
            )
            for tokens in sentence_list
        )
    )
    
    result_str = ""
    adverb_usage = "단어 사용량: %s told/said, %s but/and, %s wh- 접속사" % (told_said_usage, but_and_usage, wh_adverbs_usage)
    
    result_str += adverb_usage
    average_word_length = compute_total_average_word_length(sentence_list)
    unique_words_fraction = compute_total_unique_words_fraction(sentence_list)
    
    word_stats = "단어의 평균 길이 %.2f, 고유한 단어의 비율 %.2f" % (average_word_length, unique_words_fraction)
    
    result_str += "\n"
    result_str += word_stats
    
    number_of_syllables = count_total_syllables(sentence_list)
    number_of_words = count_total_words(sentence_list)
    number_of_sentences = len(sentence_list)
    
    syllable_counts = "%d개 음절, %d개 단어, %d개 문장" % (number_of_syllables, number_of_words, number_of_sentences)
    result_str += "\n"
    result_str += syllable_counts
    
    flesch_score = compute_flesch_reading_ease(
        number_of_syllables, number_of_words, number_of_sentences
    )
    
    flesh = "플레시 점수 %.2f: %s" % (
        flesch_score,
        get_reading_level_from_flesch(flesch_score),
    )
    
    result_str += "\n"
    result_str += flesh
    
    return result_str
    
    