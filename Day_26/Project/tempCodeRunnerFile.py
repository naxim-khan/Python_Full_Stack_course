import pandas
filepath=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_26\\Project\\NATOphoeneticWords.csv")
word=input("Enter a word: ").upper().split()

data=pandas.read_csv(filepath)
data_f=pandas.DataFrame(data)
dict = {row['key']: row['value'] for _, row in data.iterrows()}
result=[dict[letter] for letter in  word if letter in dict]

print(result)

