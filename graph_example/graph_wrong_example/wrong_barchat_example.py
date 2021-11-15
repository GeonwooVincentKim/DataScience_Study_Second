from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

plt.ticklabel_format(useOffset=False)

# Can cause to Other people mis-understand the graph
plt.axis([2016.6, 2018.5, 499, 506])
plt.title("Look at the 'Huge' Increase!!")

plt.show()