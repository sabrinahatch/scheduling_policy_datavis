import os
import numpy as np
import matplotlib.pyplot as plt

# Define the parent directory where the data folders are located
parent_directory = "allData"

# Define the folders inside the parent directory where the data files are located
folders = ["FCFS", "PS", "SRPT"]

loads = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Lists to store the average completion times for each folder
avg_completion_times_per_folder = []

for folder in folders:
    folder_path = os.path.join(parent_directory, folder)
    x = np.zeros(len(loads))
    y = np.zeros(len(loads))

    for i, load in enumerate(loads):
        # Modify the file prefix accordingly for each folder type (e.g., "FCFS", "SRPT", "PS")
        file_name = os.path.join(folder_path, f"{folder}_LOAD_{load:.1f}.txt")

        with open(file_name, "r") as my_file:
            # reading the file
            data = my_file.read()

        # replacing and splitting the text when a newline ('\n') is seen.
        data_into_list = data.split("\n")

        # Exclude empty strings from the data
        completion_times = np.array([float(x) for x in data_into_list if x], dtype=float)

        x[i] = load
        y[i] = np.average(completion_times)

    # Store the average completion times for this folder
    avg_completion_times_per_folder.append(y)

# Plotting the data for each folder
for i, folder in enumerate(folders):
    plt.plot(x, avg_completion_times_per_folder[i], label=f"{folder} Scheduler")

plt.xlabel('Load')
plt.ylabel('Average Completion Time')
plt.title('Load vs. Average Completion Time for Different Schedulers')
plt.legend()

plt.ylim(0, 10)  # Set the y-axis limits from 0 to 10
plt.yticks(np.arange(0, 12, 2))  # Set the y-axis tick locations and labels from 0 to 10 with an increment of 2

plt.show()
