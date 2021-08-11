def pred_comp_func(src_file, ref_file, path):
    i = 0
    
    while i < len(ref_file):
        
        src_file.at[5] = ref_file.loc[i][1]
        src_file.at[6] = ref_file.loc[i][2]
        src_file.at[7] = ref_file.loc[i][3]
        src_file.at[8] = ref_file.loc[i][4]
        src_file.to_csv(path + str(ref_file.loc[i][0]), index = False, header = None)
        
        i += 1
