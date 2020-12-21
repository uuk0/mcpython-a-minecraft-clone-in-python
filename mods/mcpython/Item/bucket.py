from .Item import *


class Bucket(Item):
    def getName(self):
        return "minecraft:bucket"

    def getTexturFile(self):
        return "./assets/textures/items/bucket.png"

    def on_destroy_with(self, block):
        if block.getName() == "minecraft:water" and self.slot:
            self.slot.setItem("minecraft:water_bucket")
        elif block.getName() == "minecraft:lava" and self.slot:
            self.slot.setItem("minecraft:lava_bucket")

    def getHoldAbleLiquids(self):
        return ["minecraft:water", "minecraft:lava"]

    def getMaxStackSize(self):
        return 16

    def hasBlock(self):
        return False


handler.register(Bucket)


class WaterBucket(Item):
    def getName(self):
        return "minecraft:water_bucket"

    def getTexturFile(self):
        return "./assets/textures/items/water_bucket.png"

    def getLiquidHoldName(self):
        return "minecraft:water"

    def getMaxStackSize(self):
        return 1

    def on_block_set(self, position):
        self.slot.setItem("minecraft:bucket")

    def getBlockName(self):
        return "minecraft:water"


handler.register(WaterBucket)

liquidhandler.register(WaterBucket, "minecraft:water")


class LavaBucket(Item):
    def getName(self):
        return "minecraft:lava_bucket"

    def getTexturFile(self):
        return "./assets/textures/items/lava_bucket.png"

    def getLiquidHoldName(self):
        return "minecraft:lava"

    def getMaxStackSize(self):
        return 1

    def on_block_set(self, position):
        self.slot.setItem("minecraft:bucket")

    def getBlockName(self):
        return "minecraft:lava"


handler.register(LavaBucket)

liquidhandler.register(LavaBucket, "minecraft:lava")
