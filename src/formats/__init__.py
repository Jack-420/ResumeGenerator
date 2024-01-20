from enum import Enum

from .single_column_photo import create_document as single_column_photo_resume


class ResumeFormat(Enum):
    SINGLE_COLUMN_PHOTO = 0
