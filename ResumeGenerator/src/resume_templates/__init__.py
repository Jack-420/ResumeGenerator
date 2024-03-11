from enum import Enum

from .single_column_nophoto import create_document as single_column_nophoto_resume
from .single_column_photo import create_document as single_column_photo_resume


class ResumeTemplate(Enum):
    SINGLE_COLUMN_PHOTO = "single_column_photo"
    SINGLE_COLUMN_NOPHOTO = "single_column_nophoto"
