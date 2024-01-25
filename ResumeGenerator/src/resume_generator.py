from pathlib import Path

from .data import load_data
from .formats import (
    ResumeTemplate,
    single_column_nophoto_resume,
    single_column_photo_resume,
)


def create_resume(data_path: Path, output_path: Path, resume_format: ResumeTemplate):
    data_obj = load_data(data_path)

    if resume_format is ResumeTemplate.SINGLE_COLUMN_PHOTO:
        latex_resume = single_column_photo_resume(data_obj)
    elif resume_format is ResumeTemplate.SINGLE_COLUMN_NOPHOTO:
        latex_resume = single_column_nophoto_resume(data_obj)

    latex_resume.generate_pdf(str(output_path))
    latex_resume.generate_tex(str(output_path))
