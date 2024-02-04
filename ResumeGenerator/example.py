from pathlib import Path

from src import ResumeTemplate, create_resume

if __name__ == "__main__":
    create_resume(
        Path("ResumeGenerator/example/inputs/example_resume_data.json"),
        Path("ResumeGenerator/example/outputs/example_resume"),
        ResumeTemplate.SINGLE_COLUMN_NOPHOTO,
    )
    print("Resume generated successfully.")
