# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_item_generic(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_item_generic_quality_zero(self):
        items = [Item("+5 Dexterity Vest", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_item_generic_sell_in_zero(self):
        items = [Item("+5 Dexterity Vest", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_item_aged(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_item_aged_sell_in_zero(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_item_aged_quality_fifty(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_item_legendary(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_item_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_item_backstage_passes_quality_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_item_backstage_passes_sell_in_ten_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_item_backstage_passes_sell_in_five_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_item_backstage_passes_sell_in_zero_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_item_conjured(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_item_conjured_sell_in_zero(self):
        items = [Item("Conjured +5 Dexterity Vest", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured +5 Dexterity Vest", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

if __name__ == '__main__':
    unittest.main()
