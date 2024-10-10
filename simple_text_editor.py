import os

filename = input('Enter the filename to open or create: ')

full_filename_path = os.path.join(os.getcwd(), filename)

if os.path.exists(full_filename_path):
    with open(full_filename_path, 'r') as file:
        content = file.read()
        print(content)
else:
    with open(full_filename_path, 'w') as file:
        file.write('')


lines = []
print("Enter text (type 'SAVE' on a new line to save and exist):\n")
while True:
    line = input()
    if line == 'SAVE':
        print(f'{filename} saved !')
        break
    lines.append(line)


with open(full_filename_path, 'a') as file:
    file.write("\n".join(lines))


with open(full_filename_path, 'r') as file:
    updated_content = file.read()
    print(updated_content)
