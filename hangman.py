import random

def playgame(self):
    wordbank=["awkward","klutz","kate","bagpipes", "banjo", "croquet", "crypt", "fishhook", "flashdrive","ivory","haiku","dwarves","gazebo","gypsy","haphazard","hyphen", "jazzy", "kayak", "kiosk", "jiffy", "jinx", "jukebox", "mystify", "oxygen", "pajama", "phlegm", "pixel", "rhythmic", "rogue", "sphinx", "swivel", "twelfth", "unzip", "hello", "yacht", "zealous", "zombie"]
    word= random.randrange(0, len(wordbank)-1)
    points = 100
    eachlet = points/len(word)
    blankarr=[] #underscore
    for letter in word:
        print("_ ")
        blankarr.append("_ ")
    print("Your starting score is 100")
    while blankarr.find("_ ")>-1:
        let = input("Guess a letter!  ") #letter they guess = let
        let.lower() #makes all input in lower case
        index = word.find(let)  #location of letter they find in the word (-1 if not found)
        if index==-1:
            points=points-eachlet
        else:
            for i in (0:word.length)
                if word[i] == let
                    blankarr[i]=word[i]
    println("Good job! You guessed the word!"
    again = input ("Do you want to play again? Respond \"Y\" for yes or \"N\" for no:    ")
        if again == "Y"
            self.playgame()
        if again == "N"
            println("Thanks for playing!")


