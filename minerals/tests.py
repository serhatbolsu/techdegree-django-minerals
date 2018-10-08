from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="aDemo Mineral",
            image_filename="Abelsonite",
            image_caption="Beautiful image",
            category="Other",
            formula="not known",
            group="Other",

        )

    def test_mineral_listing(self):
        found = Mineral.objects.get(name = "aDemo Mineral")
        self.assertEqual(self.mineral, found)

    def tearDown(self):
        self.mineral.delete()


class MineralViewTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="aDemo Mineral",
            image_filename="Abelsonite",
            image_caption="Beautiful image",
            category="Other",
            formula="not known",
            group="Other",

        )
        self.mineral2 = Mineral.objects.create(
            name="aDemo Mineral",
            image_filename="Abelsonite",
            image_caption="Beautiful image",
            category="Other",
            formula="not known",
            group="Other",
            specific_gravity="7.20 - 7.22",
            strunz_classification="08.EB.15"
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertEqual(self.mineral, resp.context['mineral'])

    def test_mineral_detail_optional_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral2.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral2, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertContains(resp, self.mineral2.specific_gravity)
        self.assertContains(resp, self.mineral2.strunz_classification)

    def test_mineral_random_view(self):
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertIn(resp.context['mineral'], [self.mineral2, self.mineral])

