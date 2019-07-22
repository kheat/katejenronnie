diffChoice = str(input("Pick a Difficulty (easy, medium, or hard): ")).lower()

if diffChoice == "easy":
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

if diffChoice == "medium":
    print("i x t f y y q p c m p e v s s a p h t z")
    print("f c x k j w m d h p l e h n w d p e a y")
    print("m n o n y a k p y s t a t e m e n t b t")
    print("m a s e w h i l e h f q j h h w q p i r")
    print("g e w t n n r i t u l v t q b r p n l l")
    print("q p u f f z f r q b i q a a t t s g q t")
    print("m n c v o o g z d m y n o h t y p t e v")
    print("k h c v r o q t l p b o t d l y t r u t")
    print("q i x w d w w i u t j r l x t k e x k u")
    print("m q q g j h c n g c j w m g n i r t s v")
    print("j l d s d s b m f t o v e z s r p p e l")
    print("m s f g a x a c v x d n b c p y d v l r")
    print("u p f e t l w t c k w c s e e m i j b k")
    print("q l f i u h o v a d x o m t n i r p a b")
    print("p c m v p n s p h r w y m p r p i b t e")
    print("m z x x l d h a x x r w w q w u w b u o")
    print("h h e m e i n w m d w h w t b d c q m o")
    print("a v t k v b k a n y c z t m d i h t b w")
    print("v s h y n o e x w n y g s k k r h u o h")
    print("r a e y z b b p f s x v w j m p t d i r\n")

if diffChoice == "hard":
    print("k g g t o e h v p l i t f n s h t m d a r s y i s")
    print("t i h r u w n w i r o r b j k s y f q i t s z a p")
    print("p u f r e k t s y c i f t u t y a s t r i n g p r")
    print("a b j y c t t h g l q n w a v s r p b j j z q f j")
    print("m c c h s b c s a k v p t w x y u v i e m b a a w")
    print("i f a e x a j n w l j e f k y b b y j o s u p t s")
    print("f i e s l e x j p u m y y j n w i m z b n n q j e")
    print("d d h z d b g r v e y j d q h q n s x t a d b n o")
    print("g p z f i i a k n i v i n g x c k i r x f q f z u")
    print("q u y v b p y t h o n e u n y z x s z f q n j d c")
    print("q k p p f k r v u g y s z x n m r n c z e y p m o")
    print("n y n d a l s b n m g x c p o f u e y b o n i l n")
    print("v s k l u a g p a j p h s c x k l y l p b q t w s")
    print("t g t c x z q b f l c o b d p z e a c v w x t u t")
    print("k p h f m d d m j f o w h d m i r a v i l e m g r")
    print("w g g w h i l e o x r e o g h c t n m q m x o f u")
    print("z y e l g a l g m w s u h u p u n h q r y y a c c")
    print("x g b a e b z j d j m m w o p t s o u r k i y b t")
    print("x d n i y v m w a j p b j l z e s u d x b n z p o")
    print("a x o w o e h q q l e v e t r n r q q c d l l a r")
    print("t e m f l p n f r v e f m b s i e k o z r w r p a")
    print("r t w u c o e n b t e u t n q l r j e v h c a m r")
    print("x z b o g y h b i h w x d q s o p r p y v b t c g")
    print("x k u m r y i o i d f a b u b q u x f w b x s p z")
    print("y i o r w r c o s d i g v t f w q h z r z i q t b\n")


key = ['constructor', 'string', 'mutable', 'tuple', 'statement', 'elseif', 'while', 'pass', 'python', 'print']
word_list = ['constructor', 'string', 'mutable', 'tuple', 'statement', 'elseif', 'while', 'pass', 'python', 'print']
word_count = 10
user_count = 0

print(user_count, " out of", word_count, "words found.")



while user_count < word_count:
    attempt = input("Enter word: ")
    if attempt == "quit":
        user_count = 10
    else:
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
