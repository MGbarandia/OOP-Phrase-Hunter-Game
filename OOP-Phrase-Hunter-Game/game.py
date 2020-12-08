from phrase import Phrase
import random


Name = input("What is your name?  ")
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("goals are for achievers"),
            Phrase("you can have results or excuses not both"),
            Phrase("no quit in my blood"),
            Phrase("finish the first plan"),
            Phrase("dont be the same as everybody"),
            Phrase("jealousy you have to earn"),
            Phrase("the mind is the limit")
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        return random.choice(self.phrases)


    def start(self):
        self.welcome()
        print("""
           Last Score: {}""".format(self.missed))
        self.missed = 0
        while self.missed != 6 and not self.active_phrase.check_complete(self.guesses):
            print(f"{' '*11}Wrong guesses: {self.missed}\n")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_letters(user_guess):
                print("Try again!!!")
                self.missed += 1
                self.guesses.append(user_guess)
                print("Guesses: {}".format(self.guesses))
            elif self.missed == 6:
                self.game_over()
            self.game_over()


    def welcome(self):
        try:
            enter = input("""
                          >Would you like to enter?>
                          >Phrase Hunter<
                          (Yes/No only)  """.format(Name))
            if enter.lower() == "no":
              print("_Good_Bye_")
              quit()
            rules = input("""
                          >Would you like to hear the rules?
                          >(Yes or No):  """)
            while enter.isnumeric():
                enter = input("Please enter (Yes/No only), {}!  ".format(Name))
            while rules.isnumeric():
                rules = input("Please enter (Yes/No only), {}!  ".format(Name))
        except (ValueError, TypeError):
            print("Please enter (Yes or No only) not {}.".format(enter))
        else:
            while enter.lower() != "yes":
                try:
                    if enter.lower() == "no":
                        print("Maybe you can play next time! Goodbye, {}!!".format(Name))
                        quit()
                    enter = input("Please enter (Yes/No only), {}!  ".format(Name))
                except (ValueError, TypeError):
                    print("Please enter (Yes or No only) not {}.".format(enter))
                else:
                    if enter == "no":
                        print("Maybe you can play next time! Goodbye, {}!!".format(Name))
                        quit()
            while rules.lower() != "no":
                try:
                    if rules.lower() == "yes":
                      rule_1 = ("""
                          -Choose a letter
                          -If incorrect your missed will go higher.
                          -You win by Guessing the Phrase
                          -If your score goes higher than 5 then Game Over!!!
                          -Good Luck!
                          """)
                      print(rule_1)
                      break
                    else:

                      rules = input("Please enter (Yes or No only) not {}.".format(enter))
                except (ValueError, TypeError):
                    print("Please enter (Yes or No only) not {}.".format(enter))
                else:
                    if rules.lower() == "y":
                      rule_1 = ("""
                          -Choose a letter
                          -If incorrect your missed will go higher.
                          -You win by Guessing the Phrase
                          -If your score goes higher than 5 then Game Over!!!
                          -Good Luck!
                          """)
                      print(rule_1)
                      break
        welcome = ("""
                       Hello {}!
                   ->>_Welcome_ _To_<<-
                   ->>_Phrase_ _ _Hunter_<<-""".format(Name))
        print(welcome)


    def get_guess(self):
        while True:
            guess_input = input("\n\n Guess a letter {}:> ".format(Name)).lower()
            try:
                if not guess_input.isalpha():
                    raise ValueError("Try again using only lowercase alphabets. Thank you!")
                    self.missed += 1
                    self.guesses.append(guess_input)
                    print("Guesses: {}".format(self.guesses))
                elif len(guess_input) != 1:
                    raise ValueError("Please enter only one letter. Thank you!")
                    self.missed += 1
                    self.guesses.append(guess_input)
                    print("Guesses: {}".format(self.guesses))
                    print(self.guesses)
            except ValueError as err:
                print("""Value Error: {}, You Have Made an Error!!!!
                \n\n""".format(Name))
                self.missed += 1
                print("missed: {}".format(self.missed))
                print(("*")*30)
                if self.missed == 6:
                  self.game_over()
                else:
                  continue
            else:
                return guess_input

    def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            complete = self.active_phrase.display(self.guesses)
            print(complete)
            print("Congratulation!! You Guessed the Phrase {}!".format(Name))
            self.replay()
        elif self.missed == 6:
            print("\n\n Oh No!! It's Game Over!\n Maybe in the Next Game you'll get it!")
            self.replay()

    def replay(self):
      try:
        enter = input("Would you like to play again (Yes/No only please!):  ")
        while enter.isnumeric():
            enter = input("Please enter (Yes/No only), {}!  ".format(Name))
      except (ValueError, TypeError):
        print("Please enter (Yes or No only) not {}.".format(play))
      else:
        while enter.lower() != "yes":
            try:
                if enter.lower() == "no":
                    print("Maybe you can play again next time! Goodbye, {}!!".format(Name))
                    quit()
                enter = input("Please enter (Yes/No only), {}!  ".format(Name))
            except (ValueError, TypeError):
                print("Please enter (Yes or No only) not {}.".format(play))
            else:
                if enter == "no":
                    print("Maybe you can play again next time! Goodbye, {}!!".format(Name))
                    quit()
      self.restart()

    def restart(self):
        self.guesses = [" "]
        self.active_phrase = self.get_random_phrase()
        self.start()
