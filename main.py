import random
import Hangman_stages
import word_file

lives = 6
chosen_word = random.choice(word_file.word)

display = ["_"] * len(chosen_word)

print("\n🎮 Welcome to Hangman! 🎮")
print("Guess the word before the man is hanged.\n")

game_over = False

while not game_over:

    print("\n" + " ".join(display))
    print(f"❤️ Lives Left: {lives}")

    guessed_letter = input("\n🔤 Guess a letter: ").lower()

    if guessed_letter in display:
        print(f"⚠️ You already guessed '{guessed_letter}'!")
        continue

    for position, letter in enumerate(chosen_word):
        if letter == guessed_letter:
            display[position] = guessed_letter

    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"❌ '{guessed_letter}' is not in the word!")

    print(Hangman_stages.stages[lives])

    if "_" not in display:
        game_over = True
        print("\n🎉 CONGRATULATIONS! YOU WIN! 🎉")
        print(f"🏆 The word was: {chosen_word}")

    if lives == 0:
        game_over = True
        print("\n🎮💀 GAME OVER 💀🎮")
        print(f"📖 The word was: {chosen_word}")