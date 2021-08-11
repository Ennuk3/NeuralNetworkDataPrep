def folder_name_func(dirpath, name_list):
    for name in name_list:
        
        half_name = dirpath[dirpath.index(r"\\")+2:]
        
        full_name = half_name.split("\\")[0]
        
        if name == full_name:
            return name
