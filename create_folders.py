import os


num_days = 25

repo_path = 'repo-path'

for day in range(1, num_days + 1):
   
    folder_name = f"day{day:02d}"
    folder_path = os.path.join(repo_path, folder_name)

    
    os.makedirs(folder_path, exist_ok=True)

   
    open(os.path.join(folder_path, 'input.txt'), 'a').close()
    with open(os.path.join(folder_path, 'solution.py'), 'a') as f:
        f.write("# Advent of Code Day {}\n".format(day))

print("Folders and files created successfully.")
