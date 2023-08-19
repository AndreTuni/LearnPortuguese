# Language Quiz Game - Quiz Logic

The provided code is a Python program that implements the quiz logic for the Language Quiz Game. This program allows users to test their knowledge of word translations between Portuguese and Italian. The quiz presents questions in which users need to translate words or phrases from one language to another.

## How to Use

1. Ensure you have Python installed (version 3.6 or higher) on your system.
2. Copy and paste the code into a Python script or file.
3. Replace the example usage section with actual file paths of CSV data for different categories (verbs, nouns, adjectives, adverbs).
4. Run the script.

## Quiz Modes

The quiz supports two modes:
- Italian to Portuguese ('ita'): In this mode, users are presented with Italian words or phrases and must provide their Portuguese translations.
- Portuguese to Italian ('pt'): In this mode, users are shown Portuguese words or phrases and must provide their Italian translations.

## Quiz Process

1. The quiz starts by prompting the user to select a category to practice (verbs, nouns, adjectives, or adverbs).
2. Next, the user chooses a quiz mode: Italian to Portuguese ('ita') or Portuguese to Italian ('pt').
3. The program loads the appropriate data from the selected CSV file (replace file names in the code with actual file names).
4. The quiz begins with questions presented in the chosen mode. For each question:
   - A word or phrase is shown in the source language (Italian or Portuguese).
   - Five translation options are displayed, including the correct translation and four incorrect options.
   - The user selects an option by entering the corresponding number (1 to 5).
   - The program provides feedback on the correctness of the answer and updates the user's score.
   - The user's lives decrease for each incorrect answer.
5. The quiz continues until the user runs out of lives or answers all the questions.
6. At the end of the quiz, the user's final score is displayed.

## Notes

- The program ensures that questions are not repeated within the same quiz session.
- Make sure to have CSV files with word pairs for each category (verbs, nouns, adjectives, adverbs) to replace the example usage.
- You can customize the number of lives or the scoring mechanism according to your preferences.

Feel free to use, modify, and expand upon this code to create your own language quiz game!



Certainly! Here's the provided code formatted as a short Markdown README:

# Sentence Gap-Fill Game

The Sentence Gap-Fill Game is a Python program that provides an interactive quiz experience where users can complete gaps in sentences. It loads sentences from a file, removes random words from them, and prompts users to fill in the gaps with the missing words.

## How to Use

1. Make sure you have Python and the Tkinter library installed.
2. Copy and paste the code into a Python script or file.
3. Replace `'res/paragrafos.txt'` with the path to your text file containing sentences.
4. Run the script.

## Game Process

1. The game starts by displaying a sentence with gaps.
2. The removed words are displayed as options for filling the gaps.
3. Enter your answers in the provided input field, separated by spaces.
4. Click the "Submit" button to check your answers.
5. If correct, you proceed to the next round with a new sentence.
6. If incorrect, the correct words are revealed, and you can try again.

## Notes

- The game ensures the removal of special characters and numbers from sentences.
- The program uses the Tkinter library for the graphical user interface.
- You can customize the behavior of the game by modifying the code according to your preferences.

Enjoy the Sentence Gap-Fill Game and have fun improving your language skills!
```

