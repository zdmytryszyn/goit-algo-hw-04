def get_cats_info(path: str) -> list[dict] | str:
    try:
        with open(path, "r", encoding="utf-8") as cat_file:
            cat_info_list = [
                cat.strip().split(",") for cat in cat_file.readlines()
            ]

            return [
                {
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": cat_info[2]
                }
                for cat_info in cat_info_list
            ]

    except FileNotFoundError:
        return f"No such file: '{path}', provide a valid path to file"
    except IOError:
        return f"File '{path}' may be corrupted, cannot be opened"
    except IndexError:
        return ("Not enough information about the cat "
                "or empty field provided, check the file")
