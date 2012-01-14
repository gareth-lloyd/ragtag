"""
Test of asset include behaviour
"""

from django.test import TestCase
from blog.models import Post
from models import *

class AssetTest(TestCase):
    def setUp(self):
        self.p = Post(title="title", slug="title", body="body")
        self.p.save()

        self.asset = Asset(asset_location="asset", weight=1)
        self.asset.save()
        self.asset.posts.add(self.p)

    def testReverseLink(self):
        "Check that it is possible to link from a post to assets"
        self.assertTrue(self.p.asset_set)

    def testWeight(self):
        heavyAsset = Asset(asset_location="heavy", weight=2)
        heavyAsset.save()
        heavyAsset.posts.add(self.p)

        self.assertEqual(self.asset, self.p.asset_set.all()[0])
        self.assertEqual(heavyAsset, self.p.asset_set.all()[1])
