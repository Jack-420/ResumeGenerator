from pathlib import Path

from ..src.core.generator import create_resume
from ..src.core.resume_templates import ResumeTemplate

if __name__ == "__main__":
    create_resume(
        Path("ResumeGenerator/example/inputs/example_resume_data.json"),
        Path("ResumeGenerator/example/outputs/example_resume"),
        ResumeTemplate.SINGLE_COLUMN_NOPHOTO,
    )
    print("Resume generated successfully.")
