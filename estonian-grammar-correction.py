# Õigekirjakontroll
from estnltk import Text
import collections

def insert_text():
    text = Text(input("Palun, kirjutage teksti: "))
    analysed_sentences = collections.OrderedDict()
    for sentence in text.split_by("sentences"):
        analysed_sentences[sentence.text] = sentence.get.word_texts.spelling.spelling_suggestions.as_dataframe
    return analysed_sentences

def correct_sentence(sentence, analyse):
    bad_words = analyse[analyse.spelling == False]
    for _, row in bad_words.iterrows():
        print("Vale sõna on: ", row.word_texts)
        if len(row.spelling_suggestions) == 1:
            fixed_word = row.spelling_suggestions[0]
            sentence = sentence.replace(row.word_texts, fixed_word)
            print("Meie soovitus on(rohkem soovitusi meil ei ole): ", fixed_word)
        elif len(row.spelling_suggestions) == 0:
            user_word = input("Mul ei ole soovitusi, kirjuta midagi muud: ")
            sentence = sentence.replace(row.word_texts, user_word)
        else:
            print("Meie soovitused: ")
            for i in range(len(row.spelling_suggestions)):
                print(i+1, row.spelling_suggestions[i])
            word_position = int(input("Vali number sobiva sõnaga: "))
            sentence = sentence.replace(row.word_texts, row.spelling_suggestions[word_position-1])
    return sentence


def sentence_processing(analysed_sentences):
    correct_sentences = []
    for sentence, dataframe in analysed_sentences.items():
        if all(dataframe.spelling):
            correct_sentences.append(sentence)
            print("Lause ilma veata on: ", sentence)
        else:
            print("Lause veaga on: ", sentence)
            correct_sentences.append(correct_sentence(sentence, dataframe))
    return correct_sentences



def main():
    text = insert_text()
    result = sentence_processing(text)
    final_result = " ".join(result)
    print("Parandatud tekst: ", final_result)

main()
