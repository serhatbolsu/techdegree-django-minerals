from django.core.management.base import BaseCommand

from minerals.models import Mineral

import json


def rename_keys(data):
    new_dict = {}
    for key, value in data.items():
        new_key = key.replace(" ", "_")
        new_dict[new_key] = value
    # change image_filename with element name
    if new_dict['image_filename']:
        new_dict['image_filename'] = new_dict['name'] + '.jpg'
    return new_dict


class Command(BaseCommand):
    help = "Populates mineral db from minerals.json"

    def handle(self, *args, **kwargs):
        with open('data/minerals.json') as file:
            data = json.load(file)
        for mineral in data:
            data_with_underscore = rename_keys(mineral)
            Mineral(**data_with_underscore).save()
            #     name=mineral['name'],
            #     image_filename=mineral['image filename'],
            #     image_caption=mineral['image caption'],
            #     category=mineral['category'],
            #     group=mineral['group'],
            #     formula=mineral.get('formula', ''),
            #     crystal_system=mineral.get('crystal system', ''),
            #     strunz_classification=mineral.get('strunz classification', ''),
            #     unit_cell=mineral.get('unit cell', ''),
            #     crystal_symmetry=mineral.get('crystal symmetry', ''),
            #     cleavage=mineral.get('cleavage', ''),
            #     mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
            #     luster=mineral.get('luster', ''),
            #     streak=mineral.get('streak', ''),
            #     diaphaneity=mineral.get('diaphaneity', ''),
            #     optical_properties=mineral.get('optical properties', ''),
            #     refractive_index=mineral.get('refractive index', '')
            # ).save()
        self.stdout.write(
            self.style.SUCCESS('Successfully saved minerals "%s"' % str(len(data))))
