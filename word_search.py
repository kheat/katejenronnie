print("j k z e c a i h m u l u s l m")
print("e s l t o b j c k g m b k y v")
print("s x t k n n l j s f h r f x z")
print("d i h a s y i t g h t n i r p")
print("s n o h t y p u b o t f r h j")
print("t j y m r e v p g y y i o j f")
print("r b u e u v m l g b e e s u y")
print("i b w i c t k e f g u s e j a")
print("n i b a t l a m n p n l j r w")
print("g i o x o b d b b t p e i h c")
print("k z y f r i p j l m w o i y b")
print("e k a m r u l p k e e l y o q")
print("f t k r g l k d n l e l f c a")
print("x q j j j h z c p k k h d n b")
print("m p a s s l m s k q w t h m d\n")

key = ['constructor', 'string', 'mutable', 'tuple', 'statement', 'elseif', 'while', 'pass', 'python', 'print']
word_list = ['constructor', 'string', 'mutable', 'tuple', 'statement', 'elseif', 'while', 'pass', 'python', 'print']
word_count = 10
user_count = 0

print(user_count, " out of", word_count, "words found.")

while user_count < word_count:
    attempt = input("Enter word: ")
    if attempt in word_list:
        print("\t Word found!")
        word_list.remove(attempt)
        user_count = user_count + 1
        print(user_count, " out of", word_count, "words found.\n")
    else:
        if attempt in key:
            print("\t Word already found, try again.\n")
        else:
            print("\t Word not in puzzle, try again.\n")