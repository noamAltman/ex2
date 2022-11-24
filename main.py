import math
import nltk
# import spacy
# from datasets import load_dataset
# from collections import defaultdict

def load_corpus(corpus_name):
    corpus = nltk.download(corpus_name)
    return corpus

def filter_corpus_by_tag(tag_name):
    pass

def split_corpus(corpus):
    pass

def find_most_likely_tag_dict(train_set):
    word_tag_dict = dict()

    return word_tag_dict

def compute_error_rate(trained_dict, test_set):
    error_rate = 0
    total_error_rate = 0

    return error_rate, total_error_rate





# def train_unigram_bigram_models(nlp):
#     dataset = load_dataset('wikitext', 'wikitext-2-raw-v1', split="train")
#     unigram_instance_dict = defaultdict(int)
#     bigram_instance_dict = defaultdict(int)
#     text_length = 0
#     num_of_docs = 0
#     for text in dataset['text']:
#         doc = nlp(text)
#         last_token = "0_start"
#         num_of_docs += 1
#         for token in doc:
#             if not token.is_alpha:
#                 continue
#             text_length += 1
#             unigram_instance_dict[token.lemma_] += 1
#             bigram_instance_dict[last_token + " " + token.lemma_] += 1
#             last_token = token.lemma_
#     unigram_model = {word: unigram_instance_dict[word] / text_length for word in unigram_instance_dict}
#     unigram_instance_dict["0_start"] = num_of_docs
#     bigram_model = {pair: (bigram_instance_dict[pair]/(unigram_instance_dict[pair.split()[0]])) for pair in bigram_instance_dict}
#     return unigram_model, bigram_model, text_length
#
# def bigram_model_on_sentence(nlp, model, sentence):
#     sentence_doc = nlp(sentence)
#     bigram_probabilty = 1
#     last_token = "0_start"
#     for token in sentence_doc:
#         pair = last_token + " " + token.lemma_
#         bigram_probabilty *= model.get(pair, 0)
#         last_token = token.lemma_
#     return math.log(bigram_probabilty) if bigram_probabilty else float('-inf')
#
# def smoothed_model_on_sentence(nlp, unigram_model, unigram_l, bigram_model, bigram_l, sentence):
#     sentence_doc = nlp(sentence)
#     smoothed_probabilty = 0
#     last_token = "0_start"
#     for token in sentence_doc:
#         unigram_p = unigram_model.get(token.lemma_, 0)
#         pair = last_token + " " + token.lemma_
#         bigram_p = bigram_model.get(pair, 0)
#         probability = (unigram_l*unigram_p) + (bigram_l*bigram_p)
#         smoothed_probabilty += math.log(probability) if probability else float('-inf')
#         last_token = token.lemma_
#     return smoothed_probabilty
#
# def calculate_perplexity(num_of_tokens, probabilties):
#     sum = 0
#     for p in probabilties:
#         sum += p
#     power = -(sum / num_of_tokens)
#     perplexity = math.exp(power)
#     return perplexity
#
if __name__ == '__main__':
    nlp = spacy.load("en_core_web_sm")
    unigram_model, bigram_model, text_length = train_unigram_bigram_models(nlp)