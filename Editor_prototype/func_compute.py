# -*- coding:euc-kr -*-
import pyphen

def count_word_usage(tokens, word_list):
    return len([word for word in tokens if word.lower() in word_list])

def compute_average_word_length(tokens):
    word_length = [len(word) for word in tokens]
    return sum(word_length) / len(word_length)


def compute_total_average_word_length(sentence_list):
    lengths = [compute_average_word_length(tokens) for tokens in sentence_list]
    return sum(lengths) / len(lengths)    
    
    
def compute_total_unique_words_fraction(sentence_list):
    all_words = [word for word_list in sentence_list for word in word_list]
    unique_word = set(all_words)
    return len(unique_word) / len(all_words)


def count_word_syllables(word):
    dic = pyphen.Pyphen(lang="en_US")
    hyphenated = dic.inserted(word)
    return len(hyphenated.split("-"))


def count_sentence_syllables(tokens):
    punctuation = ".,!?/"
    return sum(
        [
            count_word_syllables(word)
            for word in tokens
            if word not in punctuation
        ]
    )


def count_total_syllables(sentence_list):
    return sum(
        [count_sentence_syllables(sentence) for sentence in sentence_list]
    )


def count_words_per_sentence(sentence_tokens):
    punctuation = ".,!?/"
    return len([word for word in sentence_tokens if word not in punctuation])

    
def count_total_words(sentence_list):
    return sum(
        [count_words_per_sentence(sentence) for sentence in sentence_list]
    )
    

def compute_flesch_reading_ease(total_syllables, total_words, totla_sentences):
    return(
        206.85 - 1.015 * (total_words / totla_sentences) - 84.6 * (total_syllables / total_words)
    )


def get_reading_level_from_flesch(flesch_score):
    if flesch_score < 30:
        return "매우 읽기 어려움"
    elif flesch_score < 50:
        return "읽기 어려움"
    elif flesch_score < 60:
        return "약간 읽기 어려움"
    elif flesch_score < 70:
        return "보통"
    elif flesch_score < 80:
        return "약간 읽기 쉬움"
    elif flesch_score < 90:
        return "읽기 쉬움"
    else:
        return "매우 읽기 쉬움"
        