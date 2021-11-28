from sqlalchemy import CheckConstraint, ForeignKey, Identity, Index
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from db import db
POSTER_ART_DESCRIPTION = 'Poster Art'


class Image(db.Model):
    """ Images to be used with the programs. """
    id = db.Column(db.BigInteger, Identity(always=True), primary_key=True)
    program_id = db.Column(
        db.BigInteger, ForeignKey('program.id'), nullable=False)
    program = relationship('Program')
    description = db.Column(
        db.Text, nullable=False, default=POSTER_ART_DESCRIPTION)
    height = db.Column(
        db.Integer, CheckConstraint('height > 0'), nullable=False)
    width = db.Column(
        db.Integer, CheckConstraint('width > 0'), nullable=False)
    url = db.Column(db.Text)
    __table_args__ = (
        Index(
            'one_poster_art_per_program',
            program_id,
            unique=True,
            postgresql_where=(description == POSTER_ART_DESCRIPTION)),
    )

    @hybrid_property
    def is_poster_art(self):
        """ Convenience method for determining if this is the poster art. """
        return self.description == POSTER_ART_DESCRIPTION
