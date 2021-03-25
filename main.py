import random


def words(file, language):
    for line in file:
        for i in line.split(' '):
            language.append(i)


def transition_matrix(language):
    map_words = {}
    for i in range(0, len(language) - 1):
        first_word = language[i]
        second_word = language[i + 1]
        for j in range(len(language) - 2):
            if (language[j] == first_word) and (language[j + 1] == second_word):
                pair = (first_word, second_word)
                if pair in map_words:
                    after = map_words[pair]
                    after.append(language[i + 2])
                    after = set(after)
                    after = list(after)
                    map_words[pair] = after
                else:
                    map_words[pair] = [language[i + 2]]
    return map_words


def markov_chain(language, map_words, n):
    sentences = []
    for _ in range(n):
        sentence = []
        first_word = random.choice(language)
        second_word = random.choice(language)
        pair = (first_word, second_word)
        sentence.append(first_word)
        sentence.append(second_word)
        if pair in map_words:
            after = map_words[pair]
            if len(after) > 1:
                word = random.choice(after)
            else:
                word = after[0]
            sentence.append(word)
        else:
            sentence.append(random.choice(language))
        sentences.append(sentence)
    return sentences


def snoop_say(f, m):
    language = []
    with open(f, "r", buffering=10, encoding='utf-8') as file:
        words(file, language)
    # print(language)

    map_words = transition_matrix(language)
    # print(map_words)

    sentences = markov_chain(language, map_words, m)
    # print(sentences)
    return sentences


def main():
    m = random.randint(0, 50)
    say = snoop_say("./snoop279.txt", m)
    for s in say:
        print(*s, end='')


if __name__ == '__main__':
    main()
