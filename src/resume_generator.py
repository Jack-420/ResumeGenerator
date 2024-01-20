from pathlib import Path

from .data import load_data
from .formats import ResumeFormat, single_column_photo_resume


def create_resume(data_path: Path, output_path: Path, resume_format: ResumeFormat):
    data_obj = load_data(data_path)

    match resume_format:
        case ResumeFormat.SINGLE_COLUMN_PHOTO:
            latex_resume = single_column_photo_resume(data_obj)

    latex_resume.generate_pdf(str(output_path))
    latex_resume.generate_tex(str(output_path))
