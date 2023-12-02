import os

# Set the number of days you want to create folders for
num_days = 25

# Path to your repository
repo_path = 'C:\\Users\\ADMIN\\advent-of-code-2023'

for day in range(1, num_days + 1):
    # Create a formatted folder name, like 'day01', 'day02', ...
    folder_name = f"day{day:02d}"
    folder_path = os.path.join(repo_path, folder_name)

    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Create input.txt and solution.py files
    open(os.path.join(folder_path, 'input.txt'), 'a').close()
    with open(os.path.join(folder_path, 'solution.py'), 'a') as f:
        f.write("# Advent of Code Day {}\n".format(day))

print("Folders and files created successfully.")
