from prettytable import PrettyTable

table = PrettyTable()

pokemons = ["Pikachu", "Squirtle", "Charmander"]
types = ["Electric", "Water", "Fire"]

table.add_column("Pokemon Name", pokemons)
table.add_column("Type", types)

print(table)

table.align = "l"
print(table)
