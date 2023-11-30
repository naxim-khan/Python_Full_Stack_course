import pandas
filepath=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_26\\Project\\NATOphoeneticWords.csv")
data=pandas.read_csv(filepath)
dict = {row['key']: row['value'] for _, row in data.iterrows()}

word=input("Enter a word: ").upper()
result=[dict[letter] for letter in  word if letter in dict]
result=' '.join(result)
print(result) # f"{word.capitalize()}="

