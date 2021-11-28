"""Populate programs into DB

Revision ID: dffa12941a6f
Revises: 6e1f5ea02024
Create Date: 2021-11-28 02:26:40.049996

"""
from datetime import date
import json
from typing import List, Optional, Tuple

from alembic import op
from sqlalchemy import func, MetaData, Table

from program import ProgramType

# revision identifiers, used by Alembic.
revision = 'dffa12941a6f'
down_revision = '6e1f5ea02024'
branch_labels = None
depends_on = None


def upgrade():
    """ Seed program and image data into database. """
    filename = 'titles.json'
    with open(filename) as file:
        mock_data = json.load(file)
    count = mock_data['total']
    entries = mock_data['entries']
    programs, images = programs_and_images(entries)

    connection = op.get_bind()
    meta = MetaData(bind=connection)
    meta.reflect()
    program_table = Table('program', meta)
    image_table = Table('image', meta)
    program_ids = connection.execute(
        program_table.insert().returning(program_table.c.id), programs)

    for image, program in zip(images, program_ids):
        image['program_id'] = program.id

    connection.execute(image_table.insert(), images)
    # Sanity check
    assert connection.execute(
        func.count(program_table.c.id)).scalar() == count, \
        f'Did not insert {count} programs.'
    assert connection.execute(
        func.count(image_table.c.id)).scalar() == count, \
        f'Did not insert {count} images.'


def programs_and_images(entries: List[dict]) -> Tuple[List[dict], List[dict]]:
    """ Extract needed data from JSON. """
    programs = []
    images = []
    for program_image in entries:
        programs.append({
            'title': program_image['title'],
            'program_type': ProgramType[program_image['programType']].value,
            'release_year': _year_to_date(program_image['releaseYear']),
        })
        program_images = program_image['images']
        assert len(program_images) == 1, 'Multiple images found, aborting.'

        image = program_images['Poster Art']
        images.append({
            'url': image['url'],
            'height': image['height'],
            'width': image['width'],
        })

    return programs, images

def _year_to_date(year: int) -> Optional[date]:
    """
    Cast the year integer to a constrained date.
    None if it's zero.
    """
    if year == 0:
        return None

    return date(year=year, month=1, day=1)


def downgrade():
    raise Exception('Cannot reverse seeding database, manually delete data.')
