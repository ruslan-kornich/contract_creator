def short_director_name(name: str) -> str:
    split_name = name.split(" ")
    if len(split_name) == 3:
        first_name = split_name[1][0]
        last_name = split_name[2][0]
        return f"{first_name}. {last_name}. {split_name[0]}"
    elif len(split_name) == 2:
        return f"{split_name[1][0]}. {split_name[0]}"
    else:
        return name

