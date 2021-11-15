from collections import Counter
from matplotlib import pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
print(histogram)

# Width 10, Move sticks to the right side 5
plt.bar([x + 5 for x in histogram.keys()],
        histogram.values(),
        10,
        edgecolor=(0, 0, 0))

# X label -> -5 ~ 105
# Y label -> 0 ~ 5
plt.axis([-5, 105, 0, 5])

# X Label -> 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")

plt.show()
