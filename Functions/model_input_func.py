def model_input_func(path):
    i = 1
    folder_path_list = []
    folder_list = []
    folder_nr = int(input("How many folders? "))
    while i <= folder_nr:
        folder = input("Folder name? ")
        folder_list.append(folder)
        folder_path = path + str(folder) + r"\files\c\\"
        folder_path_list.append(folder_path)
        i += 1
    return folder_list, folder_path_list
