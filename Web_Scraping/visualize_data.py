import numpy as np
import matplotlib.pyplot as plt

# Load the data from a .npz file
data = np.load('nouns_data.npz')
nouns = data['nouns']
nouns_count = data['nouns_count']
print(nouns)
print(nouns_count)
# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(nouns, nouns_count, color='skyblue')

# Add title and labels
plt.title('Nouns Frequency', fontsize=16)
plt.xlabel('Nouns', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Rotate the x-axis labels for readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()