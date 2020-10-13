def dict_concat(dictionary):
    result_dictionary = {}
    for d in dictionary:
        for k, v in d.items():
            result_dictionary[str(k)] = v
    return result_dictionary


def dict_concat_in_lists(dictionary):
    result_dictionary = {}
    for d in dictionary:
        for k, v in d.items():
            result_dictionary.setdefault(k, []).append(v)
    return result_dictionary
