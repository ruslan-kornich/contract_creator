def short_director_name(name: str) -> str:
    split_name = name.split(" ")
    first_name = split_name[1][0]
    last_name = split_name[2][0]
    return f"{split_name[0]} {first_name}. {last_name}."
