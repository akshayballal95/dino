import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

labels = []


dir = 'captures'  # directory to get the captured images from

# get the labels for each image in the directory

for f in os.listdir(dir):
    key = f.rsplit('.', 1)[0].rsplit(" ", 1)[1]

    if key == "n":
        labels.append({'file_name': f, 'class': 0})
    elif key == "space":
        labels.append({'file_name': f, 'class': 1})


field_names = ['file_name', 'class']


# write the labels to a csv file
with open('labels_dino.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(labels)

# #  read the csv file and plot the histogram of the classes
# df = pd.read_csv("labels_dino.csv")
# df.hist(column=["class"])

# # balancing the dataset by sampling the non-action class to the same number of samples as the action class
# action = df[df['class'] != 0]
# non_action = df[df['class'] == 0]

# num = action['class'].value_counts().max()
# non_action = non_action.sample(n=num)

# df_sample = pd.concat([action, non_action], axis=0).sample(frac=1)

# df_sample.hist(column=['class'])

# #write the balanced dataset to a csv file
# df_sample.to_csv("labels.csv", index=False)
# print(len(df_sample))
