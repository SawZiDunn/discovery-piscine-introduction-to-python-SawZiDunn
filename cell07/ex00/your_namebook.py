#!/usr/bin/env python3

def array_of_names(name_dict):
    result = []
    
    for first_name, last_name in name_dict.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        result.append(full_name)
    
    return result

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))