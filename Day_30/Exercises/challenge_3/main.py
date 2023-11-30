import pandas
filepath=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_26\\Project\\NATOphoeneticWords.csv")
data=pandas.read_csv(filepath)
dict = {row['key']: row['value'] for _, row in data.iterrows()}

# while True:
#     try:
#         word=input("Enter a word: ").upper()
#         out_list=[dict[letter] for letter in word]
#         out_list=' '.join(out_list)
#         print(out_list)
#         break
#     except KeyError:
#         print("Sorry only letters in the alphabet please.")
    
# ________ ANOTHER WAY OF DOING THIS _________
def generate_phonetic():
    word=input("Enter a word: ").upper()
    word=word.replace(" ","")   
    try:
        out_list=[dict[letter] for letter in word]
        out_list=' '.join(out_list)
    except KeyError:
        print("Sorry only letters in the Alphabet please.")
        generate_phonetic()
    else:
        print(out_list)
    
generate_phonetic()