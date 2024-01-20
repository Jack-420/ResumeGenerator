import argparse
from pathlib import Path

from src import ResumeFormat, create_resume

parser = argparse.ArgumentParser()
parser.add_argument("data_path", type=Path)
parser.add_argument("output_path", type=Path)
parser.add_argument("format", type=ResumeFormat, choices=list(ResumeFormat))

if __name__ == "__main__":
    args = parser.parse_args()
    create_resume(
        args.data_path,
        args.output_path,
        args.format,
    )

    print("Resume generated successfully.")
