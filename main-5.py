import random

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
