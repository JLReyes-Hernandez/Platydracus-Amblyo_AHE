import os

def replace_characters_in_file(file_path, old_char, new_char):
    with open(file_path, 'r') as file:
        content = file.read()
    
    content = content.replace(old_char, new_char)
    
    with open(file_path, 'w') as file:
        file.write(content)

def replace_characters_in_folder(folder_path, old_char, new_char):
    for filename in os.listdir(folder_path):
        if filename.endswith('.fas'):
            file_path = os.path.join(folder_path, filename)
            replace_characters_in_file(file_path, old_char, new_char)

if __name__ == "__main__":
    folder_path = '.'  # Current directory
    old_char = '!'
    new_char = 'N'
    
    replace_characters_in_folder(folder_path, old_char, new_char)
    print("Replacement complete.")
