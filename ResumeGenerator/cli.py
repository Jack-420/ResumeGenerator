import argparse
from pathlib import Path

from src import ResumeFormat, create_resume

parser = argparse.ArgumentParser()

# group = parser.add_mutually_exclusive_group()
parser.add_argument("data_path", nargs="?", type=Path)
parser.add_argument("output_path", nargs="?", type=Path)
parser.add_argument("format", nargs="?", type=ResumeFormat, choices=list(ResumeFormat))

format_group = parser.add_mutually_exclusive_group()
format_group.add_argument("-f", "--formats", action="store_true")

if __name__ == "__main__":
    args = parser.parse_args()

    if args.formats:
        print("The available resume formats are:-")
        for i, format in enumerate(ResumeFormat, start=1):
            print(f"\t{i}.", format.value)
    else:
        create_resume(
            args.data_path,
            args.output_path,
            args.format,
        )

        print("Resume generated successfully.")
