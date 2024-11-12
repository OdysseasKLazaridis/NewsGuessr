import numpy as np
import matplotlib.pyplot as plt
file_name = "all_words"+".npz"
# Load the data from a .npz file
data = np.load(file_name)
words = data['words']
count = data['words_count']


# Get indices for sorting in descending order of counts
sorted_indices = np.argsort(count)[::-1]

# Sort words and counts based on those indices
sorted_words = words[sorted_indices]
sorted_counts = count[sorted_indices]

# Print the sorted results
print("Sorted words:", sorted_words)
print("Sorted counts:", sorted_counts)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_words[:50], sorted_counts[:50], color='skyblue')

# Add title and labels
plt.title('Nouns Frequency', fontsize=16)
plt.xlabel('words', fontsize=12)
plt.ylabel('words_count', fontsize=12)

# Rotate the x-axis labels for readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()