import questionary
from src.chapters import get_chapters
from src.download import get_input
from src.search import search_book
from os import system, name
import argparse

cls = lambda: system('cls' if name == 'nt' else 'clear')

def main():
    parser = argparse.ArgumentParser(description="Audio book downloader")
    parser.add_argument("-S", "--source", choices=["toky", "freeaudiobooks"], default="toky", help="Source website")
    args = parser.parse_args()

    choices = [
        'Search book',
        'Download from URL',
        'Exit'
    ]

    selected_action = questionary.select(
        "Choose action:",
        choices=choices
    ).ask()

    options = [
        lambda: search_book(args.source),
        lambda: get_input(args.source),
        exit
    ]
    res = options[choices.index(selected_action)]()

    if res:
        cls()
        get_chapters(res, args.source)

if __name__ == "__main__":
    main()
