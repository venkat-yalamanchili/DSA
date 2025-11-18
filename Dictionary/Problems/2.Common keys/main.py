def merge_dicts(dict1, dict2):
    final_dict = dict1.copy()
    for key, value in dict2.items():
        final_dict[key] = final_dict.get(key,0) + value
    return final_dict