import sys

from pathlib import Path
from colorama import Fore


def dir_structure_visualisation(input_path, indent=0) -> None:

    path = Path(input_path)

    if path.exists():
        if path.is_dir():
            items = path.iterdir()
            for item in items:
                if item.is_file():
                    print(f"{Fore.BLUE}{" " * (indent + 4)}📜{item.name}{Fore.RESET}")
                else:
                    print(f"{Fore.YELLOW}{" " * (indent + 4)}📂{item.name}{Fore.RESET}")
                    dir_structure_visualisation(item, indent + 4)
        else:
            print(f"{Fore.RED} \"{path.absolute()}\" is a file!{Fore.RESET}")

    else:
        print(
            f"{Fore.RED} Path \"{path.absolute()}\" "
            f"does not exist, check!{Fore.RESET}"
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        input_path = ''
    else:
        input_path = sys.argv[1]

    print(f"{Fore.YELLOW}📦{Path(input_path).name}{Fore.RESET}")
    dir_structure_visualisation(input_path)
