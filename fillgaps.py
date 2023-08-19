import random
import tkinter as tk
from tkinter import messagebox
import re

def load_sentences(file_path):
    sentences = []

    with open(file_path, 'r') as file:
        for line in file:
            # Remove numbers
            line = re.sub(r'\d+', '', line)

            # Remove special characters using regex
            line = re.sub(r'[^\w\sãñõÃÑÕâêîôûÂÊÎÔÛ]', '', line)

            # Replace ã with à
            line = re.sub(r'á', 'a', line)
            line = re.sub(r'í', 'i', line)
            line = re.sub(r'ó', 'o', line)
            line = re.sub(r'ú', 'u', line)
            line = re.sub(r'ñ', 'n', line)
            line = re.sub(r'õ', 'o', line)
            line = re.sub(r'â', 'a', line)
            line = re.sub(r'ã', 'a', line)
            line = re.sub(r'ê', 'e', line)
            line = re.sub(r'î', 'i', line)
            line = re.sub(r'ô', 'o', line)
            line = re.sub(r'û', 'u', line)


            # Split the line into sentences using regex
            sentence_list = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', line.strip())
            sentence_list = [sentence.strip() for sentence in sentence_list if sentence.strip()]
            sentences.extend(sentence_list)

    return sentences


def remove_words(paragraph):
    words = paragraph.split()
    removed_words = random.sample(words, 3)
    removed_words = list(set(removed_words))  # Remove duplicate words
    words = ["___" if word in removed_words else word for word in words]
    gap_paragraph = " ".join(words)
    lower_words =[]
    for word in removed_words:
        lower_words.append(word.lower())
    return gap_paragraph, lower_words

def check_answers(removed_words):
    user_answers = user_input.get().split()
    if len(user_answers) != len(removed_words):
        messagebox.showinfo("Result", "Please enter 5 words.")
    elif all(answer.lower() in [word.lower() for word in removed_words] for answer in user_answers):
        messagebox.showinfo("Result", "Correct!")
        play_next_round()
    else:
        incorrect_words = [word for word, answer in zip(removed_words, user_answers) if word.lower() != answer.lower()]
        messagebox.showinfo("Result", "Incorrect. The correct words were " + ', '.join(incorrect_words))

def play_next_round():
    paragraph = random.choice(paragraphs)
    gap_paragraph, removed_words = remove_words(paragraph)

    random.shuffle(removed_words)
    removed_words_label.config(text="Removed words: " + ', '.join(removed_words))
    paragraph_label.config(text=gap_paragraph)
    user_input.delete(0, tk.END)
    submit_button.config(command=lambda: check_answers(removed_words))

paragraphs = load_sentences('res/paragrafos.txt')

root = tk.Tk()
paragraph = random.choice(paragraphs)
gap_paragraph, removed_words = remove_words(paragraph)

random.shuffle(removed_words)
removed_words_label = tk.Label(root, text="Complete the gaps with these: " + ', '.join(removed_words))
removed_words_label.pack()

paragraph_label = tk.Label(root, text=gap_paragraph)
paragraph_label.pack()

user_input = tk.Entry(root)
user_input.pack()
submit_button = tk.Button(root, text="Submit", command=lambda: check_answers(removed_words))
submit_button.pack()

root.mainloop()
