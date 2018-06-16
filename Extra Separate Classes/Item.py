from getData import *
# from PIL import Image, ImageTk

# print("1")


class Item:
    ItemData = loadSettings("data/items.json")
    itemSprites = []
    itemSpriteHighlights = []
    for i in range(len(ItemData)):
        itemSprites.append(loadImage(ItemData[str(i + 1)]["icon"]))
        itemSpriteHighlights.append(loadImage(ItemData[str(i + 1)]["iconHighlight"]))
    def __init__(self, id, durability):
        self.id = id
        self.name = Item.ItemData[str(id)]["name"]
        self.type = Item.ItemData[str(id)]["type"]
        self.cost = Item.ItemData[str(id)]["cost"]
        self.needTable = Item.ItemData[str(id)]["tableRequired"]
        self.sprite = Item.itemSprites[id - 1]
        self.spriteHighlight = Item.itemSpriteHighlights[id - 1]
        self.durability = durability
        self.screenObj = -1

        if id in [9,10,11]:
            self.furnitureId = Item.ItemData[str(id)]["furnitureID"]