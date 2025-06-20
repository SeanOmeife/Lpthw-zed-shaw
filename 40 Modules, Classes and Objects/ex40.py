# mystuff = {'apple': 'I AM APPLES'}
# print(mystuff['apple'])


# # Example 2 This goes in mystuff.py
# def apple():
#     print("I AM APPLES!")
# #  this is just a variable
# tangerine = "Living reflection of a dream"


# # Example 3
# class MyStuff(object):
#     def __init__(self):
#         self.tangerine = "and now a thousand years between"
        
#     def apple(self):
#         print("I AM CLASSY APPLES")
    

# # dict style
# mystuff['apples']

# # module style
# mystuff.apple()
# print(mystuff.tangerine)

# # class style
# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song (["""Happy Birthday to you
I don\'t want to get sued
So I\'ll stop right there
                    """])

bulls_on_parade = Song(["""They rally around tha family
With pockets full of shells
                        """])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()