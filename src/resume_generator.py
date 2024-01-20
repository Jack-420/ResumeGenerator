from pathlib import Path

from .data import load_data
from .latex import create_document


def create_resume(data_path: Path, output_path: Path):
    data_obj = load_data(data_path)
    latex_resume = create_document(data_obj)

    latex_resume.generate_tex(str(output_path))
    latex_resume.generate_pdf("output")
