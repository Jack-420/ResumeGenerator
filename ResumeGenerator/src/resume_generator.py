from pathlib import Path

from .data import ResumeData
from .formats import (
    ResumeTemplate,
    single_column_nophoto_resume,
    single_column_photo_resume,
)


def create_resume(data_path: Path, output_path: Path, resume_format: ResumeTemplate):
    data_obj = ResumeData.load_data(data_path)
    latex_data_obj = data_obj.data_for_latex()

    if resume_format is ResumeTemplate.SINGLE_COLUMN_PHOTO:
        latex_resume = single_column_photo_resume(latex_data_obj)
    elif resume_format is ResumeTemplate.SINGLE_COLUMN_NOPHOTO:
        latex_resume = single_column_nophoto_resume(latex_data_obj)

    latex_resume.generate_pdf(str(output_path))
    latex_resume.generate_tex(str(output_path))
