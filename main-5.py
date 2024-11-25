import random
def display_hangman(tries):
  stages = [ 
    """
      --------
      |   |
      |   O
      |  /|\\
      |  / \\
      |
    """,
    """
      --------
      |   |
      |   O
      |  /|\\
      |  / 
      |
    """,
    """
      --------
      |   |
      |   O
      |  /|\\
      |   
      |
    """,
    """
      --------
      |   |
      |   O
      |  /|
      |   
      |
    """,
    """
      --------
      |   |
      |   O
      |   |
      |   
      |
    """,
    """
      --------
      |   |
      |   O
      |   
      |   
      |
    """,
    """
      --------
      |   |
      |   
      |   
      |   
      |
    """
  ]
  return stages[tries]

def hangman():
  words = ["python", "javasscript", "programming", "computer", "science",
       "linux", "games", "array", "algorithm", "variable", "function", "data", 
       "information", "encoding", "memory", "file", "directory", "folder", "monitor",
       "keyboard", "system", "loop"]
  word = random.choice(words)
  letters_in_word = set(word)
  alphabet = set(chr(i) for i in range(ord('a'), ord('z') + 1))
  guessed_letters = set()
  lives = 6
  
  while len(letters_in_word) > 0 and lives > 0:
    print(display_hangman(lives))
    print("Осталось жизней:", lives)
    print(' '.join([letter if letter in guessed_letters else '_' for letter in word]))

    guess = input("Введите букву: ").lower()
    if len(guess) != 1 or not guess.isalpha():
      print("Неверный ввод. Введите одну букву.")
      continue

    if guess in alphabet - guessed_letters:
      guessed_letters.add(guess)
      if guess in letters_in_word:
        letters_in_word.remove(guess)
        print("")
      else:
        lives -= 1
        print("Эта буква не входит в слово.")
    elif guess in guessed_letters:
      print("Вы уже угадали эту букву. Попробуйте другую.")
    else:
      print("Неверный ввод. Введите букву.")

  if lives == 0:
    print(display_hangman(lives))
    print("Вы проиграли! Слово было:", word)
  else:
    print("Поздравляем! Вы угадали слово:", word)


hangman()
