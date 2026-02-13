import numpy as np

# Create a 5x3 array of random integers between 50 and 100
scores = np.random.randint(50, 101, size=(5, 3))

# Calculate column-wise mean (subject-wise mean)
subject_mean = np.mean(scores, axis=0)

# Center the scores using broadcasting
centered_scores = scores - subject_mean

# Print results
print("Original Scores (5 students × 3 subjects):")
print(scores)

print("\nCentered Scores (after subtracting subject-wise mean):")
print(centered_scores)





import numpy as np

# Step 1: Create a 1D array from 0 to 23
arr = np.arange(24)

# Step 2: Reshape into a 3D array of shape (4, 3, 2)
arr_3d = arr.reshape(4, 3, 2)

# Step 3: Transpose to get shape (4, 2, 3)
final_arr = arr_3d.transpose(0, 2, 1)

# Step 4: Print final shape and array
print("Final Shape:", final_arr.shape)
print("Final Array:")
print(final_arr)