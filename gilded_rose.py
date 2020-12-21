# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    AGED = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    LEGENDARY = "Sulfuras, Hand of Ragnaros"

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        self.compute_quality()
        self.fix_quality()
        self.compute_sell_in()

    def compute_quality(self):
        if Item.AGED == self.name:
            self.quality += 1
            if self.sell_in <= 0:
                self.quality += 1
            return
        if Item.BACKSTAGE_PASSES == self.name:
            self.quality += 1
            if self.sell_in <= 10:
                self.quality += 1
            if self.sell_in <= 5:
                self.quality += 1
            if self.sell_in <= 0:
                self.quality = 0
            return
        if Item.LEGENDARY == self.name:
            return

        self.quality -= 1
        if self.sell_in <= 0:
            self.quality -= 1

    def fix_quality(self):
        if Item.LEGENDARY == self.name:
            return
        if self.quality >= 50:
            self.quality = 50
        if self.quality <= 0:
            self.quality = 0

    def compute_sell_in(self):
        if Item.LEGENDARY == self.name:
            return
        self.sell_in -= 1
