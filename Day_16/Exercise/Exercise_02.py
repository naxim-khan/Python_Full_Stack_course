from prettytable import PrettyTable # A Package. which makes an ACII table.
table=PrettyTable() # Here we created (table) Object of PrettyTable Class.

# x.field_names=["City Name","Area","Popuation","Annual Rainfal"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
# print(x)

# table ==> object of PrettyTable class 
table.field_names=["Name","Department","Section","Roll No"]
table.add_row(["Nazeem Khan","BS Computer Science","C",160])
table.add_row(["Shakir Khan","BS Computer Science","C",150])
# Accessing object attribute.
table.align="l" # l means left, align item's to left. Similyarly C is used for center and r is used for right.
print(table)
