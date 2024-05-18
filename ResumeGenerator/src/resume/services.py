from pathlib import Path

from ..data.models import ResumeData
from .resume_templates import ResumeTemplate


def create_resume(datafile_path: Path, outputdir_path: Path, resume_format: str):

    data_obj = ResumeData.read_from_file(datafile_path)
    latex_data_obj = data_obj.data_for_latex()

    latex_resume = ResumeTemplate.get_template_by_name(resume_format).create_document(
        latex_data_obj
    )

    output_path = (
        outputdir_path
        / f"{data_obj.personal_info.name.replace(' ', '_')}_{resume_format}"
    )

    latex_resume.generate_pdf(str(output_path))
    latex_resume.generate_tex(str(output_path))
