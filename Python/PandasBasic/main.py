import pandas as pd
import matplotlib.pyplot as plt

data_list = []

# Reading data from file
with open('data/impledata.txt', 'r') as data:
    for line in data:
        data_list.append(line.strip().split())

#print(data_list)

# Converting data into data frame, where first row in list is our columns name
data_frame = pd.DataFrame(data_list[1:], columns=data_list[0])

print('-------------1---------------')
print(data_frame)

# If we want to displey specific row
print('-------------2---------------')
print(data_frame.iloc[8])

# If we want to displey specific row with specific column
print('-------------3---------------')
print(data_frame.iloc[8]['name'])

# If we want to displey specific column, we can add [row_number] to see specific row (without .iloc[]])
print('-------------4---------------')
print(data_frame['age'])

# Now lets do a little of data ploting
age = data_frame['age'].astype(int)

# Ploting age to historgram
plt.figure(figsize=(8,6)) # Lets make it little bigger
plt.hist(age, bins=5, edgecolor='black', color='skyblue')

# Adding info
plt.xlabel('Ages')
plt.ylabel('Frequency')
plt.title('Simple data age dist')


# Save the plot to a file (e.g., 'age_distribution.png')
plt.savefig('photo/age_distribution.png')

# Optionally, you can display a message to the user
print("Plot saved as 'age_distribution.png'")

# Show plt if you want without saving it
# plt.show() 