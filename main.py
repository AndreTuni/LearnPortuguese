import csv
import random



def load_data(file_path):
    pt_list = []
    ita_list = []

    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            pt, ita = row
            pt_list.append(pt)
            ita_list.append(ita)

    return pt_list, ita_list


def quiz_pt(pt, ita, lives=3):
    score = 0
    used_indices = []

    while lives > 0 and len(used_indices) < len(pt):
        available_indices = [i for i in range(len(pt)) if i not in used_indices]
        question_index = random.choice(available_indices)
        used_indices.append(question_index)
        correct_answer = ita[question_index]

        # Generate indices for wrong answer options
        indices = list(range(len(ita)))
        indices.remove(question_index)
        wrong_answer_indices = random.sample(indices, 4)  # Use 4 indices for four wrong answers
        wrong_answer1 = ita[wrong_answer_indices[0]]
        wrong_answer2 = ita[wrong_answer_indices[1]]
        wrong_answer3 = ita[wrong_answer_indices[2]]
        wrong_answer4 = ita[wrong_answer_indices[3]]

        question = f"Qual è la traduzione in italiano di '{pt[question_index]}'?"
        options = [correct_answer, wrong_answer1, wrong_answer2, wrong_answer3, wrong_answer4]
        random.shuffle(options)

        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_choice = input("Inserisci la tua risposta (1/2/3/4/5): ")
        if user_choice.isdigit() and 1 <= int(user_choice) <= 5:
            chosen_option = options[int(user_choice) - 1]
            if chosen_option == correct_answer:
                print("Corretto!")
                score += 100
            else:
                print("Sbagliato!")
                lives -= 1
                print(f"Vite rimaste: {lives}")
        else:
            print("Input non valido. Inserisci un'opzione valida (1/2/3/4/5).")

        print(f"Punteggio attuale: {score}")

    print("Gioco terminato!")
    print(f"Punteggio finale: {score}")


def quiz_ita(pt, ita, lives=3):
    score = 0
    used_indices = []

    while lives > 0 and len(used_indices) < len(ita) and score < 2000:
        available_indices = [i for i in range(len(ita)) if i not in used_indices]
        question_index = random.choice(available_indices)
        used_indices.append(question_index)
        correct_answer = pt[question_index]

        # Generate indices for wrong answer options
        indices = list(range(len(pt)))
        indices.remove(question_index)
        wrong_answer_indices = random.sample(indices, 4)  # Use 4 indices for four wrong answers
        wrong_answer1 = pt[wrong_answer_indices[0]]
        wrong_answer2 = pt[wrong_answer_indices[1]]
        wrong_answer3 = pt[wrong_answer_indices[2]]
        wrong_answer4 = pt[wrong_answer_indices[3]]

        question = f"Qual è la traduzione in portoghese di '{ita[question_index]}'?"
        options = [correct_answer, wrong_answer1, wrong_answer2, wrong_answer3, wrong_answer4]
        random.shuffle(options)

        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_choice = input("Inserisci la tua risposta (1/2/3/4/5): ")
        if user_choice.isdigit() and 1 <= int(user_choice) <= 5:
            chosen_option = options[int(user_choice) - 1]
            if chosen_option == correct_answer:
                print("Corretto!")
                score += 100
            else:
                print("Sbagliato!")
                lives -= 1
                print(f"Vite rimaste: {lives}")
        else:
            print("Input non valido. Inserisci un'opzione valida (1/2/3/4/5).")

        print(f"Punteggio attuale: {score}")

    print("Gioco terminato!")
    print(f"Punteggio finale: {score}")


if __name__ == '__main__':
    # Example usage
    # file_path = 'res/verbs.csv'  # Replace with the actual path to your CSV file
    # verbs_pt, verbs_ita = load_data('res/verbs.csv')
    # nouns_pt, nouns_ita = load_data('res/nouns.csv')
    # adj_pt, adj_ita = load_data('res/adjectives.csv')
    # adv_pt, adv_ita = load_data('res/adverbs.csv')
    #
    # quiz_ita(verbs_pt, verbs_ita)

    while True:
        print("Welcome to the Language Quiz Game!")
        pos = input("Choose a category you want to train (verbs, nouns, adjectives, adverbs): ").lower()

        if pos not in ['verbs', 'nouns', 'adjectives', 'adverbs']:
            print("Invalid mode. Please choose a valid mode.")
        else:
            break
    data_pt, data_ita = load_data(f'res/{pos}.csv')  # Replace with actual file names

    while True:
        print("Last step")
        mode = input("Choose a mode:   (ita, pt): ").lower()

        if mode not in ['ita', 'pt']:
            print("Invalid mode. Please choose a valid mode.")
        else: break

    if mode == 'ita':
        quiz_ita(data_pt, data_ita)
    if mode == 'pt':
        quiz_pt(data_pt, data_ita)
