# # Hangman Game

# import random
# HANGMANPICS = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']

# mywords=['word','good','bad']
# random_word=random.choice(mywords)
# display=["-"]*len(random_word)
# # print(display)
# # for i in random_word :
# #     display.append('-')
# print(' '.join(display))
# tries=7
# gussed_list=[]
# while '-' in display and tries!=0:
#         gussed=input('Please Enter your guss letter?')
#         if gussed in random_word and gussed not in gussed_list:
#             for position in range(len(random_word)) :
#                 if random_word[position] ==gussed :
#                     display[position]=gussed
#             print(display)
#         elif gussed in gussed_list :
#             print(f"You gussed this letter before")
#         else :
#             print(f"You gussed wrong letter ")
#             tries-=1
#             print(HANGMANPICS[6-tries])
#         gussed_list.append(gussed)
#         print(f"You have {tries} tries")
        
# if tries==0 :
#     print("****YOU Lose****")
# else :
#     print("****YOU WoN****")    

