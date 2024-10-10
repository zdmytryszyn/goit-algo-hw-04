import sys

from pathlib import Path
from colorama import Fore


def main() -> None:
    if len(sys.argv) < 2:
        input_path = ''
    else:
        input_path = sys.argv[1]

    path = Path(input_path)

    if path.exists():

        if path.is_dir():
            items = path.iterdir()
            for item in items:
                if item.is_file():
                    print(f"{Fore.BLUE} {item} {Fore.RESET}")
                else:
                    print(f"{Fore.GREEN} {item} {Fore.RESET}")
        else:
            print(f"{Fore.RED} \"{path.absolute()}\" is a file!{Fore.RESET}")

    else:
        print(
            f"{Fore.RED} Path \"{path.absolute()}\" "
            f"does not exist, check!{Fore.RESET}"
        )


if __name__ == "__main__":
    main()
