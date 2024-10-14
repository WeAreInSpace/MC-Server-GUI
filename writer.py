from m import *

fixed = "&cFixed"
shaped = "&6Shaped"
shapeless = "&eShapeless"

resu_str = """panels:\n"""
resu_dict = """panels:\n"""

dt = "&0&l>> &r"

ss = [
    {
        "title": "C:Granite",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STONE, "id": "3", "link": "C:Diorite"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": QUARTZ, "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE, "id": "1", "am": "1"}
    },
    {
        "title": "C:Polished Granite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STONE, "id": "1", "link": "C:Granite"}, "5": {"m": STONE, "id": "1", "link": "C:Granite"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STONE, "id": "1", "link": "C:Granite"}, "8": {"m": STONE, "id": "1", "link": "C:Granite"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE, "id": "2", "am": "4"}
    },
    {
        "title": "C:Diorite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": QUARTZ, "id": "", "link": "C:"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": QUARTZ, "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE, "id": "3", "am": "2"}
    },
    {
        "title": "C:Polished Diorite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STONE, "id": "3", "link": "C:Diorite"}, "5": {"m": STONE, "id": "3", "link": "C:Diorite"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STONE, "id": "3", "link": "C:Diorite"}, "8": {"m": STONE, "id": "3", "link": "C:Diorite"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE, "id": "4", "am": "4"}
    },
    {
        "title": "C:Andesite",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STONE, "id": "3", "link": "C:Diorite"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE, "id": "5", "am": "2"}
    },
    {
        "title": "C:Polished Andesite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STONE, "id": "5", "link": "C:Andesite"}, "5": {"m": STONE, "id": "5", "link": "C:Andesite"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STONE, "id": "5", "link": "C:Andesite"}, "8": {"m": STONE, "id": "5", "link": "C:Andesite"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE, "id": "6", "am": "4"}
    },
    {
        "title": "C:Oak Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": LOG, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD, "id": "", "am": "1"}
    },
   {
        "title": "C:Spruce Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": LOG, "id": "1", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD, "id": "1", "am": "1"}
    },
    {
        "title": "C:Birch Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": LOG, "id": "2", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD, "id": "2", "am": "1"}
    },
    {
        "title": "C:Jungle Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": LOG, "id": "3", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD, "id": "3", "am": "1"}
    },
    {
        "title": "C:Acacia Wood Planks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": LOG_2, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD, "id": "4", "am": "1"}
    },
    {
        "title": "C:Dark Oak Wood Planks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": LOG_2, "id": "1", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD, "id": "5", "am": "1"}
    },
    {
        "title": "C:Lapis Lazuli Block",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"},

        "res": {"m": LAPIS_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Dispenser",
        "type": fixed,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": BOW, "id": "", "link": "C:Bow"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": DISPENSER, "id": "", "am": "1"}
    },
    {
        "title": "C:Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SAND, "id": "", "link": "G:Ore"}, "5": {"m": SAND, "id": "", "link": "G:Ore"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SAND, "id": "", "link": "G:Ore"}, "8": {"m": SAND, "id": "", "link": "G:Ore"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SANDSTONE, "id": "", "am": "1"}
    },
    {
        "title": "C:Chiseled Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STONE_SLAB2, "id": '', "link": "C:SandstoneSlab"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STONE_SLAB2, "id": "", "link": "C:SandstoneSlab"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SANDSTONE, "id": "1", "am": "1"}
    },
    {
        "title": "C:Smooth Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "5": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "8": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SANDSTONE, "id": "2", "am": "4"}
    },
    {
        "title": "C:Note Block",
        "type": fixed,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": NOTE_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Powered Rail",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": POWERED_RAIL, "id": "", "am": "1"}
    },
    {
        "title": "C:Detector Rail",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": STONE_PLATE, "id": "", "link": "S:StonePressurePlate"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": DETECTOR_RAIL, "id": "", "am": "1"}
    },
    {
        "title": "C:Sticky Piston",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": PISTON_BASE, "id": "", "link": "C:Piston"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": PISTON_STICKY_BASE, "id": "", "am": "1"}
    },
    {
        "title": "C:Piston",
        "type": fixed,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": PISTON_BASE, "id": "", "am": "1"}
    },
    {
        "title": "C:Wool",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STRING, "id": "", "link": "C:"}, "5": {"m": STRING, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STRING, "id": "", "link": "C:"}, "8": {"m": STRING, "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "", "am": "1"}
    },
    {
        "title": "C:Orange Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "14", "link": "C:OrangeDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "1", "am": "1"}
    },
    {
        "title": "C:Magenta Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "13", "link": "C:MagentaDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "2", "am": "1"}
    },
    {
        "title": "C:Light Blue Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "12", "link": "C:LightBlueDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "3", "am": "1"}
    },
    {
        "title": "C:Yellow Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "4", "am": "1"}
    },
    {
        "title": "C:Lime Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "10", "link": "C:LimeDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "5", "am": "1"}
    },
    {
        "title": "C:Pink Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "6", "am": "1"}
    },
    {
        "title": "C:Gray Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "7", "am": "1"}
    },
    {
        "title": "C:Light Gray Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "7", "link": "C:LightGrayDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "8", "am": "1"}
    },
    {
        "title": "C:Cyan Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "6", "link": "C:CyanDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "9", "am": "1"}
    },
    {
        "title": "C:Purple Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "10", "am": "1"}
    },
    {
        "title": "C:Blue Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "11", "am": "1"}
    },
    {
        "title": "C:Brown Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "3", "link": "C:CocoaBeans"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "12", "am": "1"}
    },
    {
        "title": "C:Green Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "2", "link": "C:GreenDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "13", "am": "1"}
    },
    {
        "title": "C:Red Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "14", "am": "1"}
    },
    {
        "title": "C:Black Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOL, "id": "15", "am": "1"}
    },
    {
        "title": "C:Block Of Gold",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:"},

        "res": {"m": GOLD_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Block Of Iron",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:"},

        "res": {"m": IRON_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": STONE, "id": "", "link": "S:Stone"},

        "res": {"m": STEP, "id": "", "am": "6"}
    },
    {
        "title": "C:Sandstone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "8": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "9": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"},

        "res": {"m": STEP, "id": "1", "am": "6"}
    },
    {
        "title": "C:Cobblestone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": STEP, "id": "3", "am": "6"}
    },
    {
        "title": "C:Brick Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": BRICK, "id": "", "link": "C:Brick"}, "8": {"m": BRICK, "id": "", "link": "C:Brick"}, "9": {"m": BRICK, "id": "", "link": "C:Brick"},

        "res": {"m": STEP, "id": "4", "am": "6"}
    },
    {
        "title": "C:Stone Brick Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "8": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "9": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"},

        "res": {"m": STEP, "id": "5", "am": "6"}
    },
    {
        "title": "C:Nether Brick Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "8": {"m": SANDSTONE, "id": "", "link": "C:NetherBricks"}, "9": {"m": SANDSTONE, "id": "", "link": "C:NetherBricks"},

        "res": {"m": STEP, "id": "6", "am": "6"}
    },
    {
        "title": "C:Quartz Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": QUARTZ, "id": "", "link": "C:"}, "8": {"m": QUARTZ, "id": "", "link": "C:"}, "9": {"m": QUARTZ, "id": "", "link": "C:"},

        "res": {"m": STEP, "id": "7", "am": "6"}
    },
    {
        "title": "C:Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "5": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "8": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BRICK, "id": "", "am": "1"}
    },
    {
        "title": "C:TNT",
        "type": fixed,

        "1": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "2": {"m": SAND, "id": "", "link": "G:Ore"}, "3": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"},
        "4": {"m": SAND, "id": "", "link": "G:Ore"}, "5": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "6": {"m": SAND, "id": "", "link": "G:Ore"},
        "7": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "8": {"m": SAND, "id": "", "link": "G:Ore"}, "9": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"},

        "res": {"m": TNT, "id": "", "am": "1"}
    },
    {
        "title": "C:Bookshelf",
        "type": fixed,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": BOOK, "id": "", "link": "C:Book"}, "5": {"m": BOOK, "id": "", "link": "C:Book"}, "6": {"m": BOOK, "id": "", "link": "C:Book"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": BOOKSHELF, "id": "", "am": "1"}
    },
    {
        "title": "C:Moss Stone",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": VINE, "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": MOSSY_COBBLESTONE, "id": "", "am": "1"}
    },
    {
        "title": "C:Torch",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": COAL, "id": "", "link": "C:Coal"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": TORCH, "id": "", "am": "1"}
    },
    {
        "title": "C:Oak Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Chest",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": CHEST, "id": "", "am": "1"}
    },
    {
        "title": "C:Block Of Diamond",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Crafting Table",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WORKBENCH, "id": "", "am": "1"}
    },
    {
        "title": "C:Furnace",
        "type": fixed,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": FURNACE, "id": "", "am": "1"}
    },
    {
        "title": "C:Ladder",
        "type": shaped,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": LADDER, "id": "", "am": "3"}
    },
    {
        "title": "C:Rail",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": RAILS, "id": "", "am": "1"}
    },
    {
        "title": "C:Cobblestone Stairs",
        "type": shaped,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": COBBLESTONE_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Lever",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": STICK, "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": COBBLESTONE, "link": "G:Cobblestone"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": LEVER, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Pressure Plate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Wooden Pressure Plate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Redstone Torch",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": REDSTONE_TORCH_ON, "id": "", "am": "1"}
    },
    {
        "title": "C:StoneButton",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STONE, "id": "", "link": "S:Stone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE_BUTTON, "id": "", "am": "1"}
    },
    {
        "title": "C:Snow",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SNOW_BLOCK, "id": "", "link": "S:StoneBlock"}, "8": {"m": SNOW_BLOCK, "id": "", "link": "S:StoneBlock"}, "9": {"m": SNOW_BLOCK, "id": "", "link": "S:StoneBlock"},

        "res": {"m": SNOW, "id": "", "am": "1"}
    },
    {
        "title": "C:Snow Block",
        "type": shaped,

        "1": {"m": SNOW_BALL, "id": "", "link": "C:"}, "2": {"m": SNOW_BALL, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SNOW_BALL, "id": "", "link": "C:"}, "5": {"m": SNOW_BALL, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SNOW_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Clay Block",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "5": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "8": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CLAY, "id": "", "am": "1"}
    },
    {
        "title": "C:Jukebox",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": JUKEBOX, "id": "", "am": "1"}
    },
    {
        "title": "C:Oak Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": FENCE, "id": "", "am": "3"}
    },
    {
        "title": "C:Glowstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "5": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "8": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GLOWSTONE, "id": "", "am": "1"}
    },
    {
        "title": "C:Jack O Lantern",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": PUMPKIN, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": TORCH, "id": "", "link": "C:Torch"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": JACK_O_LANTERN, "id": "", "am": "1"}
    },
    {
        "title": "C:White Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "", "am": "8"}
    },
    {
        "title": "C:Orange Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "14", "link": "C:OrangeDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "1", "am": "8"}
    },
    {
        "title": "C:Magenta Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "13", "link": "C:MagentaDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "2", "am": "8"}
    },
    {
        "title": "C:Light Blue Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "12", "link": "C:LightBlueDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "3", "am": "8"}
    },
    {
        "title": "C:Yellow Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "4", "am": "8"}
    },
    {
        "title": "C:Lime Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "10", "link": "C:LimeDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "5", "am": "8"}
    },
    {
        "title": "C:Pink Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "6", "am": "8"}
    },
    {
        "title": "C:Gray Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "7", "am": "8"}
    },
    {
        "title": "C:Light Gray Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "7", "link": "C:LightGrayDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "8", "am": "8"}
    },
    {
        "title": "C:Cyan Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "6", "link": "C:CyanDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "9", "am": "8"}
    },
    {
        "title": "C:Purple Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "10", "am": "8"}
    },
    {
        "title": "C:Blue Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "11", "am": "8"}
    },
    {
        "title": "C:Brown Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "3", "link": "C:CocoaBeans"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "12", "am": "8"}
    },
    {
        "title": "C:Green Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "2", "link": "C:GreenDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "13", "am": "8"}
    },
    {
        "title": "C:Red Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "14", "am": "8"}
    },
    {
        "title": "C:Black Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "", "link": "C:"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "15", "am": "8"}
    },
    {
        "title": "C:Wooden Trapdoor",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": TRAP_DOOR, "id": "", "am": "2"}
    },
    {
        "title": "C:Stone Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STONE, "id": "", "link": "S:Stone"}, "5": {"m": STONE, "id": "", "link": "S:Stone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SMOOTH_BRICK, "id": "", "am": "4"}
    },
    {
        "title": "C:Mossy Stone Bricks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SMOOTH_BRICK, "id": "StoneBricks", "link": "C:"}, "5": {"m": VINE, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SMOOTH_BRICK, "id": "1", "am": "1"}
    },
    {
        "title": "C:Chiseled Stone Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STEP, "id": "5", "link": "S:StoneBricksSlab"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STEP, "id": "5", "link": "S:StoneBricksSlab"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SMOOTH_BRICK, "id": "3", "am": "1"}
    },
    {
        "title": "C:Iron Bars",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_BARDING, "id": "", "am": "16"}
    },
    {
        "title": "C:Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": GLASS, "id": "", "link": "S:Glass"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": THIN_GLASS, "id": "", "am": "1"}
    },
    {
        "title": "C:Melon Block",
        "type": shaped,

        "1": {"m": MELON, "id": "", "link": "C:"}, "2": {"m": MELON, "id": "", "link": "C:"}, "3": {"m": MELON, "id": "", "link": "C:"},
        "4": {"m": MELON, "id": "", "link": "C:"}, "5": {"m": MELON, "id": "", "link": "C:"}, "6": {"m": MELON, "id": "", "link": "C:"},
        "7": {"m": MELON, "id": "", "link": "C:"}, "8": {"m": MELON, "id": "", "link": "C:"}, "9": {"m": MELON, "id": "", "link": "C:"},

        "res": {"m": MELON_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Oak Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Bricks Stairs",
        "type": shaped,

        "1": {"m": BRICK, "id": "", "link": "C:Bricks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": BRICK, "id": "", "link": "C:Bricks"}, "5": {"m": BRICK, "id": "", "link": "C:Bricks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": BRICK, "id": "", "link": "C:Bricks"}, "8": {"m": BRICK, "id": "", "link": "C:Bricks"}, "9": {"m": BRICK, "id": "", "link": "C:Bricks"},

        "res": {"m": BRICK_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Bricks Stairs",
        "type": shaped,

        "1": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "5": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "8": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "9": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"},

        "res": {"m": SMOOTH_STAIRS, "id": "", "am": "4"}
    },
    {
        "title": "C:Nether Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": NETHER_BRICK_ITEM, "id": "", "link": "S:NetherBrick"}, "5": {"m": NETHER_BRICK_ITEM, "id": "NetherBrick", "link": "S:NetherBrick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": NETHER_BRICK_ITEM, "id": "", "link": "S:NetherBrick"}, "8": {"m": NETHER_BRICK_ITEM, "id": "NetherBrick", "link": "S:NetherBrick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": NETHER_BRICK, "id": "", "am": "1"}
    },
    {
        "title": "C:Nether Bricks Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "5": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "6": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"},
        "7": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "8": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "9": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"},

        "res": {"m": NETHER_FENCE, "id": "", "am": "1"}
    },
    {
        "title": "C:Nether Bricks Stairs",
        "type": shaped,

        "1": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "5": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "8": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "9": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"},

        "res": {"m": NETHER_BRICK_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Enchantment Table",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": BOOK, "id": "", "link": "C:Book"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": OBSIDIAN, "id": "", "link": "C:"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": OBSIDIAN, "id": "", "link": "C:"}, "8": {"m": OBSIDIAN, "id": "", "link": "C:"}, "9": {"m": OBSIDIAN, "id": "", "link": "C:"},

        "res": {"m": ENCHANTMENT_TABLE, "id": "", "am": "1"}
    },
    {
        "title": "C:Redstone Lamp",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "5": {"m": GLOWSTONE, "id": "", "link": "C:Glowstone"}, "6": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": REDSTONE_LAMP_OFF, "id": "", "am": "1"}
    },
    {
        "title": "C:Oak Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:WoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:WoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "", "am": "6"}
    },
    {
        "title": "C:Spruce Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "1", "am": "6"}
    },
    {
        "title": "C:Birch Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "2", "am": "6"}
    },
    {
        "title": "C:Jungle Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "8": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "9": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "3", "am": "6"}
    },
    {
        "title": "C:Acacia Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "4", "am": "6"}
    },
    {
        "title": "C:Dark Oak Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "5", "am": "6"}
    },
    {
        "title": "C:Sandstone Stairs",
        "type": shaped,

        "1": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "5": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "8": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "9": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"},

        "res": {"m": SANDSTONE_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Ender Chest",
        "type": shaped,

        "1": {"m": OBSIDIAN, "id": "", "link": "C:"}, "2": {"m": OBSIDIAN, "id": "", "link": "C:"}, "3": {"m": OBSIDIAN, "id": "", "link": "C:"},
        "4": {"m": OBSIDIAN, "id": "", "link": "C:"}, "5": {"m": EYE_OF_ENDER, "id": "", "link": "C:"}, "6": {"m": OBSIDIAN, "id": "", "link": "C:"},
        "7": {"m": OBSIDIAN, "id": "", "link": "C:"}, "8": {"m": OBSIDIAN, "id": "", "link": "C:"}, "9": {"m": OBSIDIAN, "id": "", "link": "C:"},

        "res": {"m": ENDER_CHEST, "id": "", "am": "1"}
    },
    {
        "title": "C:Tripwire Hook",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": TRIPWIRE_HOOK, "id": "", "am": "1"}
    },
    {
        "title": "C:Block Of Emerald",
        "type": shaped,

        "1": {"m": EMERALD, "id": "", "link": "C:"}, "2": {"m": EMERALD, "id": "", "link": "C:"}, "3": {"m": EMERALD, "id": "", "link": "C:"},
        "4": {"m": EMERALD, "id": "", "link": "C:"}, "5": {"m": EMERALD, "id": "", "link": "C:"}, "6": {"m": EMERALD, "id": "", "link": "C:"},
        "7": {"m": EMERALD, "id": "", "link": "C:"}, "8": {"m": EMERALD, "id": "", "link": "C:"}, "9": {"m": EMERALD, "id": "", "link": "C:"},

        "res": {"m": EMERALD_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Spruce Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "5": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},

        "res": {"m": SPRUCE_WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Birch Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "5": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},

        "res": {"m": BIRCH_WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Jungle Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "5": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "9": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"},

        "res": {"m": JUNGLE_WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Beacon",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": NETHER_STAR, "id": "", "link": "C:NetherStar"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": OBSIDIAN, "id": "", "link": "C:"}, "8": {"m": OBSIDIAN, "id": "", "link": "C:"}, "9": {"m": OBSIDIAN, "id": "", "link": "C:"},

        "res": {"m": BEACON, "id": "", "am": "1"}
    },
    {
        "title": "C:Cobblestone Wall",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": COBBLE_WALL, "id": "", "am": "6"}
    },
    {
        "title": "C:Mossy Cobblestone Wall",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": MOSSY_COBBLESTONE, "id": "", "link": "C:"}, "5": {"m": MOSSY_COBBLESTONE, "id": "", "link": "C:"}, "6": {"m": MOSSY_COBBLESTONE, "id": "", "link": "C:"},
        "7": {"m": MOSSY_COBBLESTONE, "id": "", "link": "C:"}, "8": {"m": MOSSY_COBBLESTONE, "id": "", "link": "C:"}, "9": {"m": MOSSY_COBBLESTONE, "id": "", "link": "C:"},

        "res": {"m": COBBLE_WALL, "id": "1", "am": "1"}
    },
    {
        "title": "C:WoodButton",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD_BUTTON, "id": "", "am": "1"}
    },
    {
        "title": "C:Anvil",
        "type": shaped,

        "1": {"m": IRON_BLOCK, "id": "", "link": "C:IronBlock"}, "2": {"m": IRON_BLOCK, "id": "", "link": "C:IronBlock"}, "3": {"m": IRON_BLOCK, "id": "", "link": "C:IronBlock"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": ANVIL, "id": "", "am": "1"}
    },
    {
        "title": "C:Trapped Chest",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": TRIPWIRE_HOOK, "id": "", "link": "C:"}, "8": {"m": CHEST, "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": TRAPPED_CHEST, "id": "", "am": "1"}
    },
    {
        "title": "C:Weighted Pressure Plate (Light)",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Weighted Pressure Plate (Heavy)",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": IRON_INGOT, "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Daylight Sensor",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": QUARTZ, "id": "", "link": "C:"}, "5": {"m": QUARTZ, "id": "", "link": "C:"}, "6": {"m": QUARTZ, "id": "", "link": "C:"},
        "7": {"m": WOOD_STEP, "id": "", "link": "C:OakWoodSlab"}, "8": {"m": "", "id": "", "link": "C:OakWoodSlab"}, "9": {"m": "", "id": "", "link": "C:OakWoodSlab"},

        "res": {"m": DAYLIGHT_DETECTOR, "id": "", "am": "1"}
    },
    {
        "title": "C:Block Of Redstone",
        "type": shaped,

        "1": {"m": REDSTONE, "id": "", "link": "C:"}, "2": {"m": REDSTONE, "id": "", "link": "C:"}, "3": {"m": REDSTONE, "id": "", "link": "C:"},
        "4": {"m": REDSTONE, "id": "", "link": "C:"}, "5": {"m": REDSTONE, "id": "", "link": "C:"}, "6": {"m": REDSTONE, "id": "", "link": "C:"},
        "7": {"m": REDSTONE, "id": "", "link": "C:"}, "8": {"m": REDSTONE, "id": "", "link": "C:"}, "9": {"m": REDSTONE, "id": "", "link": "C:"},

        "res": {"m": REDSTONE_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Hopper",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": CHEST, "id": "", "link": "C:Chest"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": HOPPER, "id": "", "am": "1"}
    },
    {
        "title": "C:Block Of Quartz",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": QUARTZ, "id": "", "link": "C:"}, "5": {"m": QUARTZ, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": QUARTZ, "id": "", "link": "C:"}, "8": {"m": QUARTZ, "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": QUARTZ_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Chiseled Quartz Block",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STEP, "id": "7", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STEP, "id": "7", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": QUARTZ_BLOCK, "id": "1", "am": "1"}
    },
    {
        "title": "C:Pillar Quartz Block",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": QUARTZ_BLOCK, "id": "2", "am": "1"}
    },
    {
        "title": "C:Quartz Stairs",
        "type": shaped,

        "1": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "5": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "8": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "9": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"},

        "res": {"m": QUARTZ_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Activator Rail",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": ACTIVATOR_RAIL, "id": "", "am": "6"}
    },
    {
        "title": "C:Dropper",
        "type": shaped,

        "1": {"m": "Cobblestone", "id": "", "link": "C:"}, "2": {"m": "Cobblestone", "id": "", "link": "C:"}, "3": {"m": "Cobblestone", "id": "", "link": "C:"},
        "4": {"m": "Cobblestone", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "Cobblestone", "id": "", "link": "C:"},
        "7": {"m": "Cobblestone", "id": "", "link": "C:"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": "Cobblestone", "id": "", "link": "C:"},

        "res": {"m": DROPPER, "id": "", "am": "1"}
    },
    {
        "title": "C:White Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "", "am": "8"}
    },
    {
        "title": "C:Orange Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "14", "link": "C:OrangeDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "1", "am": "8"}
    },
    {
        "title": "C:Magenta Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "13", "link": "C:MagentaDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "2", "am": "8"}
    },
    {
        "title": "C:Light Blue Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "12", "link": "C:LightBlueDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "3", "am": "8"}
    },
    {
        "title": "C:Yellow Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "4", "am": "8"}
    },
    {
        "title": "C:Lime Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "10", "link": "C:LimeDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "5", "am": "8"}
    },
    {
        "title": "C:Pink Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "6", "am": "8"}
    },
    {
        "title": "C:Gray Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "7", "am": "8"}
    },
    {
        "title": "C:Light Gray Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "7", "link": "C:LightGrayDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "8", "am": "8"}
    },
    {
        "title": "C:Cyan Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "6", "link": "C:CyanDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "9", "am": "8"}
    },
    {
        "title": "C:Purple Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "10", "am": "8"}
    },
    {
        "title": "C:Blue Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "11", "am": "8"}
    },
    {
        "title": "C:Brown Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "3", "link": "C:CocoaBeans"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "12", "am": "8"}
    },
    {
        "title": "C:Green Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "2", "link": "C:GreenDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "13", "am": "8"}
    },
    {
        "title": "C:Red Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "14", "am": "8"}
    },
    {
        "title": "C:Black Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": "C:"}, "2": {"m": HARD_CLAY, "id": "", "link": "C:"}, "3": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "4": {"m": HARD_CLAY, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "", "link": "C:"}, "6": {"m": HARD_CLAY, "id": "", "link": "C:"},
        "7": {"m": HARD_CLAY, "id": "", "link": "C:"}, "8": {"m": HARD_CLAY, "id": "", "link": "C:"}, "9": {"m": HARD_CLAY, "id": "", "link": "C:"},

        "res": {"m": STAINED_CLAY, "id": "15", "am": "8"}
    },
    {
        "title": "C:White Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "", "am": "16"}
    },
    {
        "title": "C:Orange Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "1", "am": "16"}
    },
    {
        "title": "C:Magenta Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "2", "am": "16"}
    },
    {
        "title": "C:Light Blue Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "3", "am": "16"}
    },
    {
        "title": "C:Yellow Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "4", "am": "16"}
    },
    {
        "title": "C:Lime Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "5", "am": "16"}
    },
    {
        "title": "C:Pink Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "4", "link": "C:PinkStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "4", "link": "C:PinkStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "6", "am": "16"}
    },
    {
        "title": "C:Gray Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "6", "link": "C:GrayStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "6", "link": "C:GrayStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "7", "am": "16"}
    },
    {
        "title": "C:Light Gray Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "8", "am": "16"}
    },
    {
        "title": "C:Cyan Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "9", "am": "16"}
    },
    {
        "title": "C:Purple Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "11", "am": "16"}
    },
    {
        "title": "C:Blue Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "11", "am": "16"}
    },
    {
        "title": "C:Brown Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "12", "am": "16"}
    },
    {
        "title": "C:Green Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "13", "am": "16"}
    },
    {
        "title": "C:Red Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "15", "am": "16"}
    },
    {
        "title": "C:Black Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "15", "am": "16"}
    },
    {
        "title": "C:Acacia Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "5": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},

        "res": {"m": ACACIA_STAIRS, "id": "", "am": "4"}
    },
    {
        "title": "C:Dark Oak Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "5": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},

        "res": {"m": DARK_OAK_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Slime Block",
        "type": shaped,

        "1": {"m": SLIME_BALL, "id": "", "link": "C:"}, "2": {"m": SLIME_BALL, "id": "", "link": "C:"}, "3": {"m": SLIME_BALL, "id": "", "link": "C:"},
        "4": {"m": SLIME_BALL, "id": "", "link": "C:"}, "5": {"m": SLIME_BALL, "id": "", "link": "C:"}, "6": {"m": SLIME_BALL, "id": "", "link": "C:"},
        "7": {"m": SLIME_BALL, "id": "", "link": "C:"}, "8": {"m": SLIME_BALL, "id": "", "link": "C:"}, "9": {"m": SLIME_BALL, "id": "", "link": "C:"},

        "res": {"m": SLIME_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Tarpdoor",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_TRAPDOOR, "id": "", "am": "1"}
    },
    {
        "title": "C:Prismarine",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "2": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "5": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": PRISMARINE, "id": "", "am": "1"}
    },
    {
        "title": "C:Prismarine Bricks",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "2": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "3": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},
        "4": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "5": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "6": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},
        "7": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "8": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "9": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},

        "res": {"m": PRISMARINE, "id": "1", "am": "1"}
    },
    {
        "title": "C:Dark Prismarine",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "2": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "3": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},
        "4": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "5": {"m": INK_SACK, "id": "", "link": "C:"}, "6": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},
        "7": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "8": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "9": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},

        "res": {"m": PRISMARINE, "id": "2", "am": "1"}
    },
    {
        "title": "C:Sea Lantern",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "2": {"m": PRISMARINE_CRYSTALS, "id": "", "link": "C:"}, "3": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},
        "4": {"m": PRISMARINE_CRYSTALS, "id": "", "link": "C:"}, "5": {"m": PRISMARINE_CRYSTALS, "id": "", "link": "C:"}, "6": {"m": PRISMARINE_CRYSTALS, "id": "", "link": "C:"},
        "7": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"}, "8": {"m": PRISMARINE_CRYSTALS, "id": "", "link": "C:"}, "9": {"m": PRISMARINE_SHARD, "id": "", "link": "C:"},

        "res": {"m": SEA_LANTERN, "id": "", "am": "1"}
    },
    {
        "title": "C:Hay Bale",
        "type": shaped,

        "1": {"m": WHEAT, "id": "", "link": "C:"}, "2": {"m": WHEAT, "id": "", "link": "C:"}, "3": {"m": WHEAT, "id": "", "link": "C:"},
        "4": {"m": WHEAT, "id": "", "link": "C:"}, "5": {"m": WHEAT, "id": "", "link": "C:"}, "6": {"m": WHEAT, "id": "", "link": "C:"},
        "7": {"m": WHEAT, "id": "", "link": "C:"}, "8": {"m": WHEAT, "id": "", "link": "C:"}, "9": {"m": WHEAT, "id": "", "link": "C:"},

        "res": {"m": HAY_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:White Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "", "link": "C:WhiteWool"}, "8": {"m": WOOL,"id": "", "link": "C:WhiteWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "", "am": "3"}
    },
    {
        "title": "C:Orange Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "8": {"m": WOOL,"id": "1", "link": "C:OrangeWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "1", "am": "3"}
    },
    {
        "title": "C:MagentaCarpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "8": {"m": WOOL,"id": "2", "link": "C:MagentaWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "2", "am": "3"}
    },
    {
        "title": "C:LightBlueCarpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "8": {"m": WOOL,"id": "3", "link": "C:LightBlueWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "3", "am": "3"}
    },
    {
        "title": "C:YellowCarpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "8": {"m": WOOL,"id": "4", "link": "C:YellowWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "4", "am": "3"}
    },
    {
        "title": "C:LimeCarpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "8": {"m": WOOL,"id": "5", "link": "C:LimeWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "5", "am": "3"}
    },
    {
        "title": "C:PinkCarpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "8": {"m": WOOL,"id": "6", "link": "C:PinkWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "6", "am": "3"}
    },
    {
        "title": "C:GrayCarpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "8": {"m": WOOL,"id": "7", "link": "C:GrayWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "7", "am": "3"}
    },
    {
        "title": "C:LightGrayCarpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "8": {"m": WOOL,"id": "8", "link": "C:LightGrayWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "8", "am": "3"}
    },
    {
        "title": "C:Cyan Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "8": {"m": WOOL,"id": "9", "link": "C:CyanWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "9", "am": "3"}
    },
    {
        "title": "C:Purple Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "8": {"m": WOOL,"id": "10", "link": "C:PurpleWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "10", "am": "3"}
    },
    {
        "title": "C:Blue Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "8": {"m": WOOL,"id": "11", "link": "C:BlueWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "11", "am": "3"}
    },
    {
        "title": "C:Brown Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "12", "link": "C:Brown Wool"}, "8": {"m": WOOL,"id": "12", "link": "C:Brown Wool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "12", "am": "3"}
    },
    {
        "title": "C:Green Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "8": {"m": WOOL,"id": "13", "link": "C:GreenWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "13", "am": "3"}
    },
    {
        "title": "C:Red Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "8": {"m": WOOL,"id": "14", "link": "C:RedWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "14", "am": "3"}
    },
    {
        "title": "C:Black Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "8": {"m": WOOL,"id": "15", "link": "C:BlackWool"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARPET, "id": "15", "am": "3"}
    },
    {
        "title": "C:Block Of Coal",
        "type": shaped,

        "1": {"m": COAL, "id": "", "link": "C:Coal"}, "2": {"m": COAL, "id": "", "link": "C:Coal"}, "3": {"m": COAL, "id": "", "link": "C:Coal"},
        "4": {"m": COAL, "id": "", "link": "C:Coal"}, "5": {"m": COAL, "id": "", "link": "C:Coal"}, "6": {"m": COAL, "id": "", "link": "C:Coal"},
        "7": {"m": COAL, "id": "", "link": "C:Coal"}, "8": {"m": COAL, "id": "", "link": "C:Coal"}, "9": {"m": COAL, "id": "", "link": "C:Coal"},

        "res": {"m": COAL_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "C:Red Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SAND, "id": "1", "link": "C:RedSand"}, "5": {"m": SAND, "id": "1", "link": "C:RedSand"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SAND, "id": "1", "link": "C:RedSand"}, "8": {"m": SAND, "id": "1", "link": "C:RedSand"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": RED_SANDSTONE, "id": "", "am": "1"}
    },
    {
        "title": "C:Chiseled Red Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STONE_SLAB2, "id": "", "link": "C:RedSandstoneSlab"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STONE_SLAB2, "id": "", "link": "C:RedSandstoneSlab"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": RED_SANDSTONE, "id": "1", "am": "1"}
    },
    {
        "title": "C:Smooth Red Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "5": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "8": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": RED_SANDSTONE, "id": "2", "am": "1"}
    },
    {
        "title": "C:Red Sandstone Stairs",
        "type": shaped,

        "1": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "5": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "8": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "9": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"},

        "res": {"m": RED_SANDSTONE_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "C:Red Sandstone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "8": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "9": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"},

        "res": {"m": STONE_SLAB2, "id": "", "am": "1"}
    },
    {
        "title": "C:Spruce Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": SPRUCE_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Birch Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": BIRCH_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Jungle Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": JUNGLE_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Dark Oak Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": DARK_OAK_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Acacia Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": ACACIA_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Spruce Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},

        "res": {"m": SPRUCE_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "C:Birch Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},

        "res": {"m": BIRCH_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "C:Jungle Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"},
        "7": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"},

        "res": {"m": JUNGLE_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "C:Dark Oak Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},

        "res": {"m": DARK_OAK_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "C:Acacia Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},

        "res": {"m": ACACIA_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "C:Iron Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Pickaxe",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_AXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Flint And Steel",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": FLINT, "id": "", "link": "C:Flint"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": FLINT_AND_STEEL, "id": "", "am": "1"}
    },
    {
        "title": "C:Bow",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": STRING, "id": "", "link": "C:String"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": BOW, "id": "", "am": "1"}
    },
    {
        "title": "C:Arrow",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": FLINT, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": FEATHER, "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": ARROW, "id": "", "am": "1"}
    },
    {
        "title": "C:Coal",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": COAL_BLOCK, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": COAL, "id": "", "am": "9"}
    },
    {
        "title": "C:Diamond",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": DIAMOND_BLOCK, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DIAMOND, "id": "", "am": "9"}
    },
    {
        "title": "C:Iron Ingot",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_INGOT, "id": "", "am": "9"}
    },
    {
        "title": "C:Gold Ingot",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": GOLD_BLOCK, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "9"}
    },
    {
        "title": "C:Iron Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "C:Wooden Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "C:Wooden Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "C:Wooden Pickaxe",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Wooden Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD_AXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Pickaxe",
        "type": shaped,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE_AXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DIAMOND_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DIAMOND_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Pickaxe",
        "type": shaped,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DIAMOND_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DIAMOND_AXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Stick",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STICK, "id": "", "am": "4"}
    },
    {
        "title": "C:Bowl",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BOWL, "id": "", "am": "4"}
    },
    {
        "title": "C:Mushroom Stew",
        "type": shapeless,

        "1": {"m": RED_MUSHROOM, "id": "", "link": "C:"}, "2": {"m": BROWN_MUSHROOM, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": BOWL, "id": "", "link": "C:Bowl"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": MUSHROOM_SOUP, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Pickaxe",
        "type": shaped,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_AXE, "id": "", "am": "1"}
    },
    {
        "title": "C:Wooden Hoe",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOOD_HOE, "id": "", "am": "1"}
    },
    {
        "title": "C:Stone Hoe",
        "type": shaped,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STONE_HOE, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Hoe",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_HOE, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Hoe",
        "type": shaped,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DIAMOND_HOE, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Hoe",
        "type": shaped,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_HOE, "id": "", "am": "1"}
    },
    {
        "title": "C:Wheat",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": HAY_BLOCK, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WHEAT, "id": "", "am": "9"}
    },
    {
        "title": "C:Bread",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "8": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "9": {"m": WHEAT, "id": "", "link": "C:Wheat"},

        "res": {"m": BREAD, "id": "", "am": "1"}
    },
    {
        "title": "C:Leather Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": LEATHER, "id": "", "link": "C:Leather"}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "C:Leather Chestplate",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "C:Leather"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": LEATHER, "id": "", "link": "C:Leather"}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": LEATHER, "id": "", "link": "C:Leather"}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Leather Leggings",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "C:Leather"}, "2": {"m": LEATHER, "id": "", "link": "C:Leather"}, "3": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "C:Leather Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Chestplate",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Leggings",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Chestplate",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Leggings",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Chestplate",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Leggings",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "C:Painting",
        "type": shaped,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOL, "id": "", "link": "C:"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": PAINTING, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Apple",
        "type": shaped,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": APPLE, "id": "", "link": "C:"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLDEN_APPLE, "id": "", "am": "1"}
    },
    {
        "title": "C:Enchanted Golden Apple",
        "type": shaped,

        "1": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "2": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "3": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "4": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "5": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "6": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "7": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "8": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "9": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},

        "res": {"m": GOLDEN_APPLE, "id": "1", "am": "1"}
    },
    {
        "title": "C:Sign",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SIGN, "id": "", "am": "1"}
    },
    {
        "title": "C:Oak Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WOODEN_DOOR, "id": "", "am": "1"}
    },
    {
        "title": "C:Bucket",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BUCKET, "id": "", "am": "1"}
    },
    {
        "title": "C:Minecart",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": MINECART, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Door",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": IRON_DOOR, "id": "", "am": "3"}
    },
    {
        "title": "C:Redstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": REDSTONE_BLOCK, "id": "", "link": "C:BlockOfRedstone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": REDSTONE, "id": "", "am": "1"}
    },
    {
        "title": "C:Boat",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": BOAT, "id": "", "am": "1"}
    },
    {
        "title": "C:Leather",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": RABBIT_HIDE, "id": "", "link": "C:"}, "5": {"m": RABBIT_HIDE, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": RABBIT_HIDE, "id": "", "link": "C:"}, "8": {"m": RABBIT_HIDE, "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": LEATHER, "id": "", "am": "1"}
    },
    {
        "title": "C:Paper",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SUGAR_CANE, "id": "", "link": "C:"}, "8": {"m": SUGAR_CANE, "id": "", "link": "C:"}, "9": {"m": SUGAR_CANE, "id": "", "link": "C:"},

        "res": {"m": PAPER, "id": "", "am": "1"}
    },
    {
        "title": "C:Book",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": PAPER, "id": "", "link": "C:Paper"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BOOK, "id": "", "am": "1"}
    },
    {
        "title": "C:Slime Ball",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": SLIME_BLOCK, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SLIME_BALL, "id": "", "am": "9"}
    },
    {
        "title": "C:Minecart With Chest",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": CHEST, "id": "", "link": "C:Chest"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": STORAGE_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "C:Minecart With Furnace",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": FURNACE, "id": "", "link": "C:Furnace"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": POWERED_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "C:Compass",
        "type": fixed,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": COMPASS, "id": "", "am": "1"}
    },
    {
        "title": "C:Fishing Rod",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": STRING, "id": "", "link": "C:"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": STRING, "id": "", "link": "C:"},

        "res": {"m": FISHING_ROD, "id": "", "am": "1"}
    },
    {
        "title": "C:Clock",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": WATCH, "id": "", "am": "1"}
    },
    {
        "title": "C:Red Dye",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "1", "am": "1"}
    },
    {
        "title": "C:Red Dye 1",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "4", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "1", "am": "1"}
    },
    {
        "title": "C:Red Dye 2",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": DOUBLE_PLANT, "id": "4", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "1", "am": "2"}
    },
    {
        "title": "C:Purple Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "5", "am": "2"}
    },
    {
        "title": "C:Cyan Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "2", "link": "S:GreenDye"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "6", "am": "2"}
    },
    {
        "title": "C:Light Gray Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "7", "am": "2"}
    },
    {
        "title": "C:Light Gray Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "7", "am": "3"}
    },
    {
        "title": "C:Light Gray Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "3", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "7", "am": "1"}
    },
    {
        "title": "C:Light Gray Dye 3",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "6", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "7", "am": "1"}
    },
    {
        "title": "C:Light Gray Dye 4",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "8", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "7", "am": "1"}
    },
    {
        "title": "C:Gray Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "", "link": "C:"}, "8": {"m": INK_SACK, "id": "15", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "8", "am": "1"}
    },
    {
        "title": "C:Pink Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "9", "am": "2"}
    },
    {
        "title": "C:Pink Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "7", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "9", "am": "1"}
    },
    {
        "title": "C:Pink Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": DOUBLE_PLANT, "id": "5", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "9", "am": "2"}
    },
    {
        "title": "C:Lime Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "2", "link": "S:GreenDye"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "10", "am": "2"}
    },
    {
        "title": "C:Yellow Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": YELLOW_FLOWER, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "11", "am": "1"}
    },
    {
        "title": "C:Yellow Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": DOUBLE_PLANT, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "11", "am": "2"}
    },
    {
        "title": "C:Light Blue Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "12", "am": "1"}
    },
    {
        "title": "C:Light Blue Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "1", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "12", "am": "2"}
    },
    {
        "title": "C:Magenta Dye",
        "type": shapeless,

        "1": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "2": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "5": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "13", "am": "4"}
    },
    {
        "title": "C:Magenta Dye 1",
        "type": shapeless,

        "1": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "13", "am": "3"}
    },
    {
        "title": "C:Magenta Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "13", "am": "2"}
    },
    {
        "title": "C:Magenta Dye 3",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "2", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "13", "am": "1"}
    },
    {
        "title": "C:Magenta Dye 4",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": DOUBLE_PLANT, "id": "1", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "13", "am": "2"}
    },
    {
        "title": "C:Orange Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "8": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "14", "am": "2"}
    },
    {
        "title": "C:Orange Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": RED_ROSE, "id": "5", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "14", "am": "1"}
    },
    {
        "title": "C:Bone Meal",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": BONE, "id": "", "link": "C:Bone"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": INK_SACK, "id": "15", "am": "3"}
    },
    {
        "title": "C:Sugar",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": SUGAR_CANE, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SUGAR, "id": "", "am": "1"}
    },
    {
        "title": "C:Cake",
        "type": shaped,

        "1": {"m": MILK_BUCKET, "id": "", "link": "C:"}, "2": {"m": MILK_BUCKET, "id": "", "link": "C:"}, "3": {"m": MILK_BUCKET, "id": "", "link": "C:"},
        "4": {"m": SUGAR, "id": "", "link": "C:Sugar"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": SUGAR, "id": "", "link": "C:Sugar"},
        "7": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "8": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "9": {"m": WHEAT, "id": "", "link": "C:Wheat"},

        "res": {"m": CAKE, "id": "", "am": "1"}
    },
    {
        "title": "C:Bed",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOL, "id": "", "link": "C:Wool"}, "5": {"m": WOOL, "id": "", "link": "C:Wool"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": BED, "id": "", "am": "1"}
    },
    {
        "title": "C:Redsrone Repeater",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": STONE, "id": "", "link": "S:Stone"},

        "res": {"m": DIODE, "id": "", "am": "1"}
    },
    {
        "title": "C:Cookie",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "8": {"m": INK_SACK, "id": "3", "link": ""}, "9": {"m": WHEAT, "id": "", "link": "C:Wheat"},

        "res": {"m": COOKIE, "id": "", "am": "1"}
    },
    {
        "title": "C:Shears",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SHEARS, "id": "", "am": "1"}
    },
    {
        "title": "C:Pumpkin Seeds",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": PUMPKIN, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": PUMPKIN_SEEDS, "id": "", "am": "4"}
    },
    {
        "title": "C:Melon Seeds",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": MELON, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": MELON_SEEDS, "id": "", "am": "1"}
    },
    {
        "title": "C:Gold Nugget",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GOLD_NUGGET, "id": "", "am": "9"}
    },
    {
        "title": "C:Glass Bottle",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GLASS_BOTTLE, "id": "", "am": "9"}
    },
    {
        "title": "C:Fermented Spider Eye",
        "type": shapeless,

        "1": {"m": SPIDER_EYE, "id": "", "link": "C:"}, "2": {"m": BROWN_MUSHROOM, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": SUGAR, "id": "", "link": "C:Sugar"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": FERMENTED_SPIDER_EYE, "id": "", "am": "1"}
    },
    {
        "title": "C:Blaze Powder",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": BLAZE_ROD, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BLAZE_POWDER, "id": "", "am": "2"}
    },
    {
        "title": "C:Magma Cream",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": BLAZE_POWDER, "id": "", "link": "C:BlazePowder"}, "5": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": MAGMA_CREAM, "id": "", "am": "1"}
    },
    {
        "title": "C:Brewing Stand",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": BLAZE_ROD, "id": "", "link": "C:BlazeRod"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": BREWING_STAND_ITEM, "id": "", "am": "1"}
    },
    {
        "title": "C:Cauldron",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": CAULDRON_ITEM, "id": "", "am": "1"}
    },
    {
        "title": "C:Eye Of Ender",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": ENDER_PEARL, "id": "", "link": "C:"}, "5": {"m": BLAZE_POWDER, "id": "", "link": "C:BlazePowder"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": EYE_OF_ENDER, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Melon",
        "type": fixed,

        "1": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "2": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "3": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "4": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "5": {"m": MELON, "id": "", "link": "C:"}, "6": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "7": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "8": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "9": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},

        "res": {"m": SPECKLED_MELON, "id": "", "am": "1"}
    },
    {
        "title": "C:Fire Charge",
        "type": shapeless,

        "1": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "2": {"m": BLAZE_POWDER, "id": "", "link": "C:BlazePowder"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": COAL, "id": "", "link": "C:Coal"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": FIREWORK_CHARGE, "id": "", "am": "1"}
    },
    {
        "title": "C:Book And Quill",
        "type": shapeless,

        "1": {"m": BOOK, "id": "", "link": "C:Book"}, "2": {"m": INK_SACK, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": FEATHER, "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BOOK_AND_QUILL, "id": "", "am": "1"}
    },
    {
        "title": "C:Emerald",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": EMERALD, "id": "", "am": "9"}
    },
    {
        "title": "C:Item Frame",
        "type": fixed,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": LEATHER, "id": "", "link": "S:Leather"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": ITEM_FRAME, "id": "", "am": "1"}
    },
    {
        "title": "C:Flower Pot",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": FLOWER_POT_ITEM, "id": "", "am": "1"}
    },
    {
        "title": "C:Empty Map",
        "type": shaped,

        "1": {"m": PAPER, "id": "", "link": "C:Paper"}, "2": {"m": PAPER, "id": "", "link": "C:Paper"}, "3": {"m": PAPER, "id": "", "link": "C:Paper"},
        "4": {"m": PAPER, "id": "", "link": "C:Paper"}, "5": {"m": COMPASS, "id": "", "link": "C:Compass"}, "6": {"m": PAPER, "id": "", "link": "C:Paper"},
        "7": {"m": PAPER, "id": "", "link": "C:Paper"}, "8": {"m": PAPER, "id": "", "link": "C:Paper"}, "9": {"m": PAPER, "id": "", "link": "C:Paper"},

        "res": {"m": EMPTY_MAP, "id": "", "am": "1"}
    },
    {
        "title": "C:Golden Carrot",
        "type": fixed,

        "1": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "2": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "3": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "4": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "5": {"m": CARROT_ITEM, "id": "", "link": "C:"}, "6": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "7": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "8": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "9": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},

        "res": {"m": GOLDEN_CARROT, "id": "", "am": "1"}
    },
    {
        "title": "C:Carrot On A Stick",
        "type": shapeless,

        "1": {"m": FISHING_ROD, "id": "", "link": "C:FishingRod"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": CARROT_ITEM, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": CARROT_STICK, "id": "", "am": "1"}
    },
    {
        "title": "C:Pumpkin Pie",
        "type": shaped,

        "1": {"m": PUMPKIN, "id": "", "link": "C:"}, "2": {"m": SUGAR, "id": "", "link": "C:Sugar"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": EGG, "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": PUMPKIN_PIE, "id": "", "am": "1"}
    },
    {
        "title": "C:Redstone Comparator",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "5": {"m": QUARTZ, "id": "", "link": "C:"}, "6": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": STONE, "id": "", "link": "S:Stone"},

        "res": {"m": REDSTONE_COMPARATOR, "id": "", "am": "1"}
    },
    {
        "title": "C:Minecart With TNT",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": TNT, "id": "", "link": "C:TNT"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": EXPLOSIVE_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "C:Minecart With Hopper",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": HOPPER, "id": "", "link": "C:Hopper"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": HOPPER_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "C:Rabbit Stew",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": COOKED_RABBIT, "id": "", "link": "S:CookedRabbit"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": CARROT_ITEM, "id": "", "link": "C:"}, "5": {"m": BAKED_POTATO, "id": "", "link": "S:CookedPotato"}, "6": {"m": RED_MUSHROOM, "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": BOWL, "id": "", "link": "C:Bowl"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": RABBIT_STEW, "id": "", "am": "1"}
    },
    {
        "title": "C:Armor Stand",
        "type": fixed,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": STEP, "id": "", "link": "C:StoneSlab"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": ARMOR_STAND, "id": "", "am": "1"}
    },
    {
        "title": "C:Lead",
        "type": shaped,

        "1": {"m": STRING, "id": "", "link": "C:"}, "2": {"m": STRING, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STRING, "id": "", "link": "C:"}, "5": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": STRING, "id": "", "link": "C:"},

        "res": {"m": LEASH, "id": "", "am": "1"}
    },
    {
        "title": "C:White Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "", "link": "C:Wool"}, "2": {"m": WOOL, "id": "", "link": "C:Wool"}, "3": {"m": WOOL, "id": "", "link": "C:Wool"},
        "4": {"m": WOOL, "id": "", "link": "C:Wool"}, "5": {"m": WOOL, "id": "", "link": "C:Wool"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "15", "am": "1"}
    },
    {
        "title": "C:Orange Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "2": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "3": {"m": WOOL, "id": "1", "link": "C:OrangeWool"},
        "4": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "5": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "6": {"m": WOOL, "id": "1", "link": "C:OrangeWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "14", "am": "1"}
    },
    {
        "title": "C:Magenta Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "2": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "3": {"m": WOOL, "id": "2", "link": "C:MagentaWool"},
        "4": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "5": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "6": {"m": WOOL, "id": "2", "link": "C:MagentaWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "13", "am": "1"}
    },
    {
        "title": "C:Light Blue Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "2": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "3": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"},
        "4": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "5": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "6": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "12", "am": "1"}
    },
    {
        "title": "C:Yellow Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "2": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "3": {"m": WOOL, "id": "4", "link": "C:YellowWool"},
        "4": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "5": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "6": {"m": WOOL, "id": "4", "link": "C:YellowWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "11", "am": "1"}
    },
    {
        "title": "C:Lime Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "2": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "3": {"m": WOOL, "id": "5", "link": "C:LimeWool"},
        "4": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "5": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "6": {"m": WOOL, "id": "5", "link": "C:LimeWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "10", "am": "1"}
    },
    {
        "title": "C:Pink Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "2": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "3": {"m": WOOL, "id": "6", "link": "C:PinkWool"},
        "4": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "5": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "6": {"m": WOOL, "id": "6", "link": "C:PinkWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "9", "am": "1"}
    },
    {
        "title": "C:Gray Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "2": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "3": {"m": WOOL, "id": "7", "link": "C:GrayWool"},
        "4": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "5": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "6": {"m": WOOL, "id": "7", "link": "C:GrayWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "8", "am": "1"}
    },
    {
        "title": "C:Light Gray Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "2": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "3": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"},
        "4": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "5": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "6": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "7", "am": "1"}
    },
    {
        "title": "C:Cyan Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "2": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "3": {"m": WOOL, "id": "9", "link": "C:CyanWool"},
        "4": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "5": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "6": {"m": WOOL, "id": "9", "link": "C:CyanWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "6", "am": "1"}
    },
    {
        "title": "C:Purple Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "2": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "3": {"m": WOOL, "id": "10", "link": "C:PurpleWool"},
        "4": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "5": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "6": {"m": WOOL, "id": "10", "link": "C:PurpleWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "5", "am": "1"}
    },
    {
        "title": "C:Blue Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "2": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "3": {"m": WOOL, "id": "11", "link": "C:BlueWool"},
        "4": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "5": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "6": {"m": WOOL, "id": "11", "link": "C:BlueWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "4", "am": "1"}
    },
    {
        "title": "C:Brown Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "2": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "3": {"m": WOOL, "id": "12", "link": "C:BrownWool"},
        "4": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "5": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "6": {"m": WOOL, "id": "12", "link": "C:BrownWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "3", "am": "1"}
    },
    {
        "title": "C:Green Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "2": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "3": {"m": WOOL, "id": "13", "link": "C:GreenWool"},
        "4": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "5": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "6": {"m": WOOL, "id": "13", "link": "C:GreenWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "2", "am": "1"}
    },
    {
        "title": "C:Red Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "2": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "3": {"m": WOOL, "id": "14", "link": "C:RedWool"},
        "4": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "5": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "6": {"m": WOOL, "id": "14", "link": "C:RedWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "1", "am": "1"}
    },
    {
        "title": "C:Black Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "2": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "3": {"m": WOOL, "id": "15", "link": "C:BlackWool"},
        "4": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "5": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "6": {"m": WOOL, "id": "15", "link": "C:BlackWool"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BANNER, "id": "", "am": "1"}
    },
    {
        "title": "C:Spruce Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "2": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "5": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SPRUCE_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "C:Birch Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "2": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "5": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BIRCH_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "C:Jungle Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "2": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "5": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "8": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": JUNGLE_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "C:Acacia Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "2": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "5": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": ACACIA_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "C:Dark Oak Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "2": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "5": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DARK_OAK_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "C:Spawn Mooshroom",
        "type": fixed,

        "1": {"m": RED_MUSHROOM, "id": "96", "link": "C:"}, "2": {"m": RED_MUSHROOM, "id": "96", "link": "C:"}, "3": {"m": RED_MUSHROOM, "id": "96", "link": "C:"},
        "4": {"m": RED_MUSHROOM, "id": "96", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": RED_MUSHROOM, "id": "96", "link": "C:"},
        "7": {"m": RED_MUSHROOM, "id": "96", "link": "C:"}, "8": {"m": RED_MUSHROOM, "id": "96", "link": "C:"}, "9": {"m": RED_MUSHROOM, "id": "96", "link": "C:"},

        "res": {"m": MONSTER_EGG, "id": "96", "am": "1"}
    },
    {
        "title": "C:Spawn Sheep",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "91", "am": "1"}
    },
    {
        "title": "C:Spawn Cow",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "S:Leather"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": LEATHER, "id": "", "link": "S:Leather"},

        "res": {"m": MONSTER_EGG, "id": "92", "am": "1"}
    },
    {
        "title": "C:Spawn Chicken",
        "type": fixed,

        "1": {"m": FEATHER, "id": "", "link": "C:"}, "2": {"m": FEATHER, "id": "", "link": "C:"}, "3": {"m": FEATHER, "id": "", "link": "C:"},
        "4": {"m": FEATHER, "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": FEATHER, "id": "", "link": "C:"},
        "7": {"m": FEATHER, "id": "", "link": "C:"}, "8": {"m": FEATHER, "id": "", "link": "C:"}, "9": {"m": FEATHER, "id": "", "link": "C:"},

        "res": {"m": MONSTER_EGG, "id": "93", "am": "1"}
    },
    {
        "title": "C:Spawn Slime",
        "type": fixed,

        "1": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "2": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "3": {"m": GRASS, "id": "", "link": "C:GrassBlock"},
        "4": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": GRASS, "id": "", "link": "C:Grass"},
        "7": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "8": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "9": {"m": GRASS, "id": "", "link": "C:GrassBlock"},

        "res": {"m": MONSTER_EGG, "id": "55", "am": "1"}
    },
    {
        "title": "C:Spawn Witch",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": POTION, "id": "", "link": "C:"},

        "res": {"m": MONSTER_EGG, "id": "66", "am": "1"}
    },
    
    {
        "title": "C:Spawn Zombie Pigman",
        "type": fixed,

        "1": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "2": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "3": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "4": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "7": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "8": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "9": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},

        "res": {"m": MONSTER_EGG, "id": "57", "am": "1"}
    },
    {
        "title": "C:Spawn Zombie",
        "type": fixed,

        "1": {"m": ROTTEN_FLESH, "id": "", "link": "C:"}, "2": {"m": ROTTEN_FLESH, "id": "", "link": "C:"}, "3": {"m": ROTTEN_FLESH, "id": "", "link": "C:"},
        "4": {"m": ROTTEN_FLESH, "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": ROTTEN_FLESH, "id": "", "link": "C:"},
        "7": {"m": ROTTEN_FLESH, "id": "", "link": "C:"}, "8": {"m": ROTTEN_FLESH, "id": "", "link": "C:"}, "9": {"m": ROTTEN_FLESH, "id": "", "link": "C:"},

        "res": {"m": MONSTER_EGG, "id": "54", "am": "1"}
    },
    {
        "title": "C:Spawn Skeleton",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "2": {"m": BONE, "id": "", "link": "C:"}, "3": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "4": {"m": BONE, "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": BONE, "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": BONE, "id": "", "link": "C:"}, "9": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},

        "res": {"m": MONSTER_EGG, "id": "51", "am": "1"}
    },
    {
        "title": "C:Spawn Spider",
        "type": fixed,

        "1": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "2": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "3": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "4": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "7": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": REDSTONE, "id": "", "link": "C:Redstone"},

        "res": {"m": MONSTER_EGG, "id": "52", "am": "1"}
    },
    {
        "title": "C:Spawn Cave Spider",
        "type": fixed,

        "1": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": REDSTONE, "id": "", "link": "C:Redstone"},

        "res": {"m": MONSTER_EGG, "id": "59", "am": "1"}
    },
    {
        "title": "C:Spawn Ghast",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "56", "am": "1"}
    },
    {
        "title": "C:Spawn Horse",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": SADDLE, "id": "", "link": "C:Saddle"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": SADDLE, "id": "", "link": "C:Saddle"},
        "7": {"m": LEATHER, "id": "", "link": "S:Leather"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": LEATHER, "id": "", "link": "S:Leather"},

        "res": {"m": MONSTER_EGG, "id": "100", "am": "1"}
    },
    {
        "title": "C:Spawn Wolf",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "95", "am": "1"}
    },
    {
        "title": "C:Spawn Magma Cube",
        "type": fixed,

        "1": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "2": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "3": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"},
        "4": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"},
        "7": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "8": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "9": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"},

        "res": {"m": MONSTER_EGG, "id": "62", "am": "1"}
    },
    {
        "title": "C:Spawn Guardian",
        "type": fixed,

        "1": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "2": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "3": {"m": SPONGE, "id": "", "link": "C:Sponge"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "8": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "9": {"m": SPONGE, "id": "", "link": "C:Sponge"},

        "res": {"m": MONSTER_EGG, "id": "68", "am": "1"}
    },
    {
        "title": "C:Spawn Silverfish",
        "type": fixed,

        "1": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "2": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "3": {"m": GRAVEL, "id": "", "link": "G:Ore"},
        "4": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": GRAVEL, "id": "", "link": "G:Ore"},
        "7": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "8": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "9": {"m": GRAVEL, "id": "", "link": "G:Ore"},

        "res": {"m": MONSTER_EGG, "id": "60", "am": "1"}
    },
    {
        "title": "C:Spawn Enderman",
        "type": fixed,

        "1": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},

        "res": {"m": MONSTER_EGG, "id": "58", "am": "1"}
    },
    {
        "title": "C:Spawn Rabbit",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": SAND, "id": "", "link": "G:Ore"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": SAND, "id": "", "link": "G:Ore"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": SAND, "id": "", "link": "G:Ore"},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": SAND, "id": "", "link": "G:Ore"}, "9": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},

        "res": {"m": MONSTER_EGG, "id": "101", "am": "1"}
    },
    {
        "title": "C:Spawn Creeper",
        "type": fixed,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": MONSTER_EGG, "id": "50", "am": "1"}
    },
    {
        "title": "C:Spawn Pig",
        "type": fixed,

        "1": {"m": DIRT, "id": "", "link": "C:"}, "2": {"m": DIRT, "id": "", "link": "C:"}, "3": {"m": DIRT, "id": "", "link": "C:"},
        "4": {"m": DIRT, "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": DIRT, "id": "", "link": "C:"},
        "7": {"m": DIRT, "id": "", "link": "C:"}, "8": {"m": DIRT, "id": "", "link": "C:"}, "9": {"m": DIRT, "id": "", "link": "C:"},

        "res": {"m": MONSTER_EGG, "id": "90", "am": "1"}
    },
    {
        "title": "C:Spawn Villager",
        "type": fixed,

        "1": {"m": BONE, "id": "", "link": "C:"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": BONE, "id": "", "link": "C:"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": BONE, "id": "", "link": "C:"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": BONE, "id": "", "link": "C:"},

        "res": {"m": MONSTER_EGG, "id": "120", "am": "1"}
    },
    {
        "title": "C:Spawn Ocelot",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": RED_ROSE, "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": RED_ROSE, "id": "", "link": "C:"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "98", "am": "1"}
    },
    {
        "title": "C:Spawn Endermite",
        "type": fixed,

        "1": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},

        "res": {"m": MONSTER_EGG, "id": "67", "am": "1"}
    },
    {
        "title": "C:Spawn Bat",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": FEATHER, "id": "", "link": "C:"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": FEATHER, "id": "", "link": "C:"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "65", "am": "1"}
    },
    {
        "title": "C:Spawn Squid",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "2": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "3": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "4": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},

        "res": {"m": MONSTER_EGG, "id": "94", "am": "1"}
    },
    {
        "title": "C:Spawn Blaze",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": ""}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": FLINT, "id": "", "link": ""},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": EGG, "id": "", "link": "C:"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": FLINT, "id": "", "link": ""}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": FLINT, "id": "", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "61", "am": "1"}
    },
    {
        "title": "C:Tallgrass",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": LONG_GRASS, "id": "1", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": LONG_GRASS, "id": "1", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DOUBLE_PLANT, "id": "2", "am": "1"}
    },
    {
        "title": "C:Grass Block",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": LONG_GRASS, "id": "1", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": DIRT, "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": GRASS, "id": "", "am": "1"}
    },
    {
        "title": "C:Bone",
        "type": shaped,

        "1": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": BONE, "id": "", "am": "1"}
    },
    {
        "title": "C:Saddle",
        "type": shaped,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": STRING, "id": "", "link": "C:String"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": STRING, "id": "", "link": "C:String"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": SADDLE, "id": "", "am": "1"}
    },
    {
        "title": "C:Netherrack",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": NETHERRACK, "id": "", "am": "4"}
    },
    {
        "title": "C:Sponge",
        "type": shaped,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": STRING, "id": "", "link": "C:String"}, "5": {"m": STRING, "id": "", "link": "C:String"}, "6": {"m": STRING, "id": "", "link": "C:String"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": SPONGE, "id": "", "am": "1"}
    },
    {
        "title": "C:Mycelium",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": DIRT, "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SAPLING, "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": MYCEL, "id": "", "am": "1"}
    },
    {
        "title": "C:Dead Bush",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DEAD_BUSH, "id": "", "am": "1"}
    },
    {
        "title": "C:Ender Pearl",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": POTION, "id": "", "link": "C:"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": ENDER_PEARL, "id": "", "am": "1"}
    },
    {
        "title": "C:Water Bucket",
        "type": shaped,

        "1": {"m": LEAVES, "id": "", "link": "C:"}, "2": {"m": LEAVES, "id": "", "link": "C:"}, "3": {"m": LEAVES, "id": "", "link": "C:"},
        "4": {"m": LEAVES, "id": "", "link": "C:"}, "5": {"m": WATER_BUCKET, "id": "", "link": "C:"}, "6": {"m": LEAVES, "id": "", "link": "C:"},
        "7": {"m": LEAVES, "id": "", "link": "C:"}, "8": {"m": LEAVES, "id": "", "link": "C:"}, "9": {"m": LEAVES, "id": "", "link": "C:"},

        "res": {"m": WATER_BUCKET, "id": "", "am": "1"}
    },
    {
        "title": "C:Red Mushroom",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": MYCEL, "id": "", "link": "C:Mycelium"}, "5": {"m": "", "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": RED_MUSHROOM, "id": "", "am": "16"}
    },
    {
        "title": "C:Gunpowder",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": FLINT, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SULPHUR, "id": "", "am": "1"}
    },
    {
        "title": "C:Sapling",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": GRASS, "id": "", "link": "C:Grass"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": SAPLING, "id": "", "am": "1"}
    },
    {
        "title": "C:Dirt",
        "type": shaped,

        "1": {"m": LEAVES, "id": "", "link": "C:"}, "2": {"m": LEAVES, "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": LEAVES, "id": "", "link": "C:"}, "5": {"m": LEAVES, "id": "", "link": "C:"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": DIRT, "id": "", "am": "1"}
    },
    {
        "title": "C:1x Compress Flint",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:Flint"}, "2": {"m": FLINT, "id": "", "link": "C:Flint"}, "3": {"m": FLINT, "id": "", "link": "C:Flint"},
        "4": {"m": FLINT, "id": "", "link": "C:Flint"}, "5": {"m": FLINT, "id": "", "link": "C:Flint"}, "6": {"m": FLINT, "id": "", "link": "C:Flint"},
        "7": {"m": FLINT, "id": "", "link": "C:Flint"}, "8": {"m": FLINT, "id": "", "link": "C:Flint"}, "9": {"m": FLINT, "id": "", "link": "C:Flint"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
    {
        "title": "C:2x Compress Flint",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "2": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "3": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"},
        "4": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "5": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "6": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"},
        "7": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "8": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "9": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
    {
        "title": "C:3x Compress Flint",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "2": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "3": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"},
        "4": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "5": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "6": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"},
        "7": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "8": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "9": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
    {
        "title": "C:Flint Singularity",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "2": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "3": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"},
        "4": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "5": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "6": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"},
        "7": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "8": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "9": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
        {
        "title": "C:1x Compress Diamond",
        "type": fixed,

        "1": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "2": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "3": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"},
        "4": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "5": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "6": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"},
        "7": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "8": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "9": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1"}
    },
    {
        "title": "C:2x Compress Diamond",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1"}
    },
    {
        "title": "C:3x Compress Diamond",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1"}
    },
    {
        "title": "C:Diamond Singularity",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1"}
    },
        {
        "title": "C:1x Compress Emerald",
        "type": fixed,

        "1": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "2": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "3": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"},
        "4": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "5": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "6": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"},
        "7": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "8": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "9": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1"}
    },
    {
        "title": "C:2x Compress Emerald",
        "type": fixed,

        "1": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "2": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "3": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"},
        "4": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "5": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "6": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"},
        "7": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "8": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "9": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1"}
    },
    {
        "title": "C:3x Compress Emerald",
        "type": fixed,

        "1": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "2": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "3": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"},
        "4": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "5": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "6": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"},
        "7": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "8": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "9": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1"}
    },
    {
        "title": "C:Emerald Singularity",
        "type": fixed,

        "1": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "2": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "3": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"},
        "4": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "5": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "6": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"},
        "7": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "8": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "9": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1"}
    },
        {
        "title": "C:1x Compress Gold",
        "type": fixed,

        "1": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "2": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "3": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "4": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "5": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "6": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "7": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "8": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "9": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "C:2x Compress Gold",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "C:3x Compress Gold",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "C:Gold Singularity",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1"}
    },
        {
        "title": "C:1x Compress Iron",
        "type": fixed,

        "1": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "2": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "3": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"},
        "4": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "5": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "6": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"},
        "7": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "8": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "9": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "C:2x Compress Iron",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "C:3x Compress Iron",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "C:Iron Singularity",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1"}
    },
        {
        "title": "C:1x Compress Lapis Lazuli",
        "type": fixed,

        "1": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "2": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "3": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"},
        "4": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "5": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "6": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"},
        "7": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "8": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "9": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"},

        "res": {"m": INK_SACK, "id": "4", "am": "1"}
    },
    {
        "title": "C:2x Compress Lapis Lazuli",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"},

        "res": {"m": INK_SACK, "id": "4", "am": "1"}
    },
    {
        "title": "C:3x Compress Lapis Lazuli",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"},

        "res": {"m": INK_SACK, "id": "4", "am": "1"}
    },
    {
        "title": "C:Lapis Lazuli Singularity",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"},

        "res": {"m": INK_SACK, "id": "4", "am": "1"}
    },
        {
        "title": "C:1x Compress Coal",
        "type": fixed,

        "1": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "2": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "3": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"},
        "4": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "5": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "6": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"},
        "7": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "8": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "9": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"},

        "res": {"m": COAL, "id": "", "am": "1"}
    },
    {
        "title": "C:2x Compress Coal",
        "type": fixed,

        "1": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "2": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "3": {"m": COAL, "id": "", "link": "C:1xCompressCoal"},
        "4": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "5": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "6": {"m": COAL, "id": "", "link": "C:1xCompressCoal"},
        "7": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "8": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "9": {"m": COAL, "id": "", "link": "C:1xCompressCoal"},

        "res": {"m": COAL, "id": "", "am": "1"}
    },
    {
        "title": "C:3x Compress Coal",
        "type": fixed,

        "1": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "2": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "3": {"m": COAL, "id": "", "link": "C:2xCompressCoal"},
        "4": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "5": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "6": {"m": COAL, "id": "", "link": "C:2xCompressCoal"},
        "7": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "8": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "9": {"m": COAL, "id": "", "link": "C:2xCompressCoal"},

        "res": {"m": COAL, "id": "", "am": "1"}
    },
    {
        "title": "C:Coal Singularity",
        "type": fixed,

        "1": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "2": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "3": {"m": COAL, "id": "", "link": "C:3xCompressCoal"},
        "4": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "5": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "6": {"m": COAL, "id": "", "link": "C:3xCompressCoal"},
        "7": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "8": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "9": {"m": COAL, "id": "", "link": "C:3xCompressCoal"},

        "res": {"m": COAL, "id": "", "am": "1"}
    },
    {
        "title": "C:Flint",
        "type": shaped,

        "1": {"m": "", "id": "", "link": "C:"}, "2": {"m": "", "id": "", "link": "C:"}, "3": {"m": "", "id": "", "link": "C:"},
        "4": {"m": "", "id": "", "link": "C:"}, "5": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "6": {"m": "", "id": "", "link": "C:"},
        "7": {"m": "", "id": "", "link": "C:"}, "8": {"m": "", "id": "", "link": "C:"}, "9": {"m": "", "id": "", "link": "C:"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
    
]

f = open("crafting-recipe.yml", "wt")
fd = open("item-guide-book.yml", "wt")

for i in ss:
    temp_yml = """"""
    temp_dict_yml = """"""

    title = i["title"]
    type = i["type"]

    name = ""
    for titleSplit in title.split():
        name += titleSplit

    temp_1 = i["1"]
    temp_1_id = ""
    temp_1_link = ""
    temp_1_m = ""

    temp_2 = i["2"]
    temp_2_id = ""
    temp_2_link = ""
    temp_2_m = ""

    temp_3 = i["3"]
    temp_3_id = ""
    temp_3_link = ""
    temp_3_m = ""

    temp_4 = i["4"]
    temp_4_id = ""
    temp_4_link = ""
    temp_4_m = ""

    temp_5 = i["5"]
    temp_5_id = ""
    temp_5_link = ""
    temp_5_m = ""

    temp_6 = i["6"]
    temp_6_id = ""
    temp_6_link = ""
    temp_6_m = ""

    temp_7 = i["7"]
    temp_7_id = ""
    temp_7_link = ""
    temp_7_m = ""

    temp_8 = i["8"]
    temp_8_id = ""
    temp_8_link = ""
    temp_8_m = ""

    temp_9 = i["9"]
    temp_9_id = ""
    temp_9_link = ""
    temp_9_m = ""

    temp_res = i["res"]
    temp_res_m = temp_res["m"]
    temp_res_id = ""



    if(temp_res["m"] == ""):
        temp_res_m = AIR
    else:
        temp_res_m = temp_res["m"]

    if(temp_res["id"] == ""):
        temp_res_id = "0"
    else:
        temp_res_id = temp_res["id"]



    if(temp_1["m"] == ""):
        temp_1_m = AIR
    else:
        temp_1_m = temp_1["m"]

    if(temp_1["id"] == ""):
        temp_1_id = "0"
    else:
        temp_1_id = temp_1["id"]



    if(temp_2["m"] == ""):
        temp_2_m = AIR
    else:
        temp_2_m = temp_2["m"]

    if(temp_2["id"] == ""):
        temp_2_id = "0"
    else:
        temp_2_id = temp_2["id"]



    if(temp_3["m"] == ""):
        temp_3_m = AIR
    else:
        temp_3_m = temp_3["m"]

    if(temp_3["id"] == ""):
        temp_3_id = "0"
    else:
        temp_3_id = temp_3["id"]



    if(temp_4["m"] == ""):
        temp_4_m = AIR
    else:
        temp_4_m = temp_4["m"]

    if(temp_4["id"] == ""):
        temp_4_id = "0"
    else:
        temp_4_id = temp_4["id"]



    if(temp_5["m"] == ""):
        temp_5_m = AIR
    else:
        temp_5_m = temp_5["m"]

    if(temp_5["id"] == ""):
        temp_5_id = "0"
    else:
        temp_5_id = temp_5["id"]



    if(temp_6["m"] == ""):
        temp_6_m = AIR
    else:
        temp_6_m = temp_6["m"]

    if(temp_6["id"] == ""):
        temp_6_id = "0"
    else:
        temp_6_id = temp_6["id"]



    if(temp_7["m"] == ""):
        temp_7_m = AIR
    else:
        temp_7_m = temp_7["m"]

    if(temp_7["id"] == ""):
        temp_7_id = "0"
    else:
        temp_7_id = temp_7["id"]



    if(temp_8["m"] == ""):
        temp_8_m = AIR
    else:
        temp_8_m = temp_8["m"]

    if(temp_8["id"] == ""):
        temp_8_id = "0"
    else:
        temp_8_id = temp_8["id"]



    if(temp_9["m"] == ""):
        temp_9_m = AIR
    else:
        temp_9_m = temp_9["m"]

    if(temp_9["id"] == ""):
        temp_9_id = "0"
    else:
        temp_9_id = temp_9["id"]



    if(temp_1["link"] != "C:"):
        temp_1_link =f"""commands:\n          - open= {temp_1["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_2["link"] != "C:"):
        temp_2_link =f"""commands:\n          - open= {temp_2["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_3["link"] != "C:"):
        temp_3_link =f"""commands:\n          - open= {temp_3["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_4["link"] != "C:"):
        temp_4_link =f"""commands:\n          - open= {temp_4["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_5["link"] != "C:"):
        temp_5_link =f"""commands:\n          - open= {temp_5["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_6["link"] != "C:"):
        temp_6_link =f"""commands:\n          - open= {temp_6["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_7["link"] != "C:"):
        temp_7_link =f"""commands:\n          - open= {temp_7["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_8["link"] != "C:"):
        temp_8_link =f"""commands:\n          - open= {temp_8["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""

    if(temp_9["link"] != "C:"):
        temp_9_link =f"""commands:\n          - open= {temp_9["link"]}\n        lore:\n          - '&eClick to view recipe'\n"""
    
    temp_yml = f"""  {name}:\n    title: '&r{dt}{title}'\n    empty: STAINED_GLASS_PANE\n    emptyID: '15'\n    rows: '6'\n    item:\n      '10':\n        material: '{temp_1_m}'\n        ID: '{temp_1_id}'\n        {temp_1_link}\n      '11':\n        material: '{temp_2_m}'\n        ID: '{temp_2_id}'\n        {temp_2_link}\n      '12':\n        material: '{temp_3_m}'\n        ID: '{temp_3_id}'\n        {temp_3_link}\n      '19':\n        material: '{temp_4_m}'\n        ID: '{temp_4_id}'\n        {temp_4_link}\n      '20':\n        material: '{temp_5_m}'\n        ID: '{temp_5_id}'\n        {temp_5_link}\n      '21':\n        material: '{temp_6_m}'\n        ID: '{temp_6_id}'\n        {temp_6_link}\n      '28':\n        material: '{temp_7_m}'\n        ID: '{temp_7_id}'\n        {temp_7_link}\n      '29':\n        material: '{temp_8_m}'\n        ID: '{temp_8_id}'\n        {temp_8_link}\n      '30':\n        material: '{temp_9_m}'\n        ID: '{temp_9_id}'\n        {temp_9_link}\n      '25':\n        material: '{temp_res_m}'\n        ID: '{temp_res_id}'\n        stack: {i['res']["am"]}\n      '23':\n        material: '{WEB}'\n        name: '{type}'\n        enchanted:\n          - true\n      "48":\n        material: 'FEATHER'\n        name: '&e&lBack'\n        commands:\n          - open= item-guide-book-1\n\n      "50":\n        material: 'BARRIER'\n        name: "&c&lClose"\n        commands:\n          - cpc\n"""
    temp_dict_yml = f"""\n      '':\n        name: '{title}'\n        material: '{temp_res_m}'\n        id: '{temp_res_id}'\n        lore:\n          - '&eClick for more details.'"""
    resu_str += temp_yml + "\n\n\n"
    resu_dict += temp_dict_yml + "\n"

f.write(resu_str)
fd.write(resu_dict)