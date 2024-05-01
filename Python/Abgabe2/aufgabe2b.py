def generate_outputs(text):
    words_list = text.split()

    words_tuple = tuple(words_list)

    sorted_words = sorted(words_list)

    line_length = len(text)

    min_value = min(text)
    max_value = max(text)

    character_info = [(char, ord(char), ascii(char), bytes(char, encoding='utf-8')) for char in text]

    return words_list, words_tuple, sorted_words, line_length, min_value, max_value, character_info

text = input("Geben Sie eine Textzeile ein: ")

outputs = generate_outputs(text)

print("Die Wörter der Zeile als Liste:", outputs[0])
print("Die Wörter der Liste als Tupel:", outputs[1])
print("Die Wörter Zeile als sortierte Liste:", outputs[2])
print("Die Länge der Zeile:", outputs[3])
print("Der Minimalwert der Zeile:", outputs[4])
print("Der Maximalwert der Zeile:", outputs[5])
print("Jedes Zeichen in besonderer Schreibweise:")
for info in outputs[6]:
    print(info[0], info[1], info[2], info[3])
