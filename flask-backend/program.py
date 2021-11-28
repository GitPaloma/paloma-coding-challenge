from enum import Enum

from sqlalchemy import CheckConstraint, Identity
from sqlalchemy.orm import relationship

from db import db
from image import Image

DEFAULT_DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing ' \
    'elit, sed do eiusmod tempor incididunt ut labore et dolore magna ' \
    'aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco ' \
    'laboris nisi ut aliquip ex ea commodo consequat.'

class ProgramType(Enum):
    """ Valid program types. """
    movie = 'movie'
    series = 'series'


class Program(db.Model):
    """ A program, like a movie or TV series. """
    id = db.Column(db.BigInteger, Identity(always=True), primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False, default=DEFAULT_DESCRIPTION)
    program_type = db.Column(db.Enum(ProgramType), nullable=False)
    release_year = db.Column(
        db.Date,
        CheckConstraint("date_trunc('year', release_year) = release_year"))
    images = relationship(Image, back_populates='program')
    poster_art = relationship(
        Image,
        primaryjoin='and_(Program.id == foreign(Image.program_id), '
                    'Image.is_poster_art)',
        back_populates='program',
        viewonly=True)
