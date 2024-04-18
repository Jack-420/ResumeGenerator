from pathlib import Path

from .data import ResumeData
from .resume_templates import (
    ResumeTemplate,
    single_column_nophoto_resume,
    single_column_photo_resume,
)


def create_resume(
    datafile_path: Path, outputdir_path: Path, resume_format: ResumeTemplate
):

    data_obj = ResumeData.read_from_file(datafile_path)
    latex_data_obj = data_obj.data_for_latex()

    print(f"{latex_data_obj.personal_info.name=}")
    print(f"{latex_data_obj.projects[2].technologies=}")

    if resume_format is ResumeTemplate.SINGLE_COLUMN_PHOTO:
        latex_resume = single_column_photo_resume(latex_data_obj)
    elif resume_format is ResumeTemplate.SINGLE_COLUMN_NOPHOTO:
        latex_resume = single_column_nophoto_resume(latex_data_obj)

    output_path = (
        outputdir_path
        / f"{data_obj.personal_info.name.replace(' ', '_')}_{resume_format.name}"
    )

    latex_resume.generate_pdf(str(output_path))
    latex_resume.generate_tex(str(output_path))
