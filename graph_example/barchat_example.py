from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# X coordinate -> [0, 1, 2, 3, 4]
# Y coordinate -> [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# Of Academy Awards")
plt.xticks(range(len(movies)), movies)

plt.show()
