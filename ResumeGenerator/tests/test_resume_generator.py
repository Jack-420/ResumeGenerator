from pathlib import Path

import pytest

from ResumeGenerator.src.resume_generator import ResumeTemplate, create_resume


def test_create_resume_single_column_photo():
    # Set the paths
    data_path = Path("ResumeGenerator/example/inputs/example_resume_data.json")
    output_path = Path("ResumeGenerator/example/outputs/single_column_photo")
    resume_format = ResumeTemplate.SINGLE_COLUMN_PHOTO

    # Create the resume
    create_resume(data_path, output_path, resume_format)

    # Check that the output file exists
    output_path = output_path.with_suffix(".pdf")
    assert output_path.exists()

    # Clean up the output file
    output_path.unlink()


def test_create_resume_single_column_nophoto():
    # Set the paths
    data_path = Path("ResumeGenerator/example/inputs/example_resume_data.json")
    output_path = Path("ResumeGenerator/example/outputs/single_column_nophoto")
    resume_format = ResumeTemplate.SINGLE_COLUMN_NOPHOTO

    # Create the resume
    create_resume(data_path, output_path, resume_format)
    output_path = output_path.with_suffix(".pdf")

    # Check that the output file exists
    assert output_path.exists()

    # Clean up the output file
    output_path.unlink()


def test_create_resume_empty_json():
    # Set the paths
    data_path = Path("ResumeGenerator/example/inputs/empty.json")
    output_path = Path("outputs/single_column_photo")
    resume_format = ResumeTemplate.SINGLE_COLUMN_PHOTO

    # Create the resume
    with pytest.raises(Exception):
        create_resume(data_path, output_path, resume_format)


def test_create_resume_invalid_path():
    # Set the paths
    data_path = Path("ResumeGenerator/example/inputs/non_existent_file.json")
    output_path = Path("outputs/single_column_photo")
    resume_format = ResumeTemplate.SINGLE_COLUMN_PHOTO

    # Create the resume
    with pytest.raises(Exception):
        create_resume(data_path, output_path, resume_format)
