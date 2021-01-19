#python package index (pypi): https://pypi.org/
#using a package to help us format data in a report
#prettytable - needs to be installed
#-- file -> settings -> Project: Packages -> Python Interpreter -> '+' to install -> search for package then install
#import prettytable

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align="l"
print(table)


