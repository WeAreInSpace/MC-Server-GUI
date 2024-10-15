from time import sleep
import yaml as yml
import json as jso
from m import *

fixed = "&cFixed"
shaped = "&6Shaped"
shapeless = "&eShapeless"

dt = "&0&l>> &r"

craftingRecipes = [
    {
        "title": "Granite",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STONE, "id": "3", "link": "C:Diorite"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": QUARTZ, "id": "", "link": "S:Quartz"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE, "id": "1", "am": "1"}
    },
    {
        "title": "Polished Granite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STONE, "id": "1", "link": "C:Granite"}, "5": {"m": STONE, "id": "1", "link": "C:Granite"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STONE, "id": "1", "link": "C:Granite"}, "8": {"m": STONE, "id": "1", "link": "C:Granite"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE, "id": "2", "am": "4"}
    },
    {
        "title": "Diorite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": QUARTZ, "id": "", "link": ""}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": QUARTZ, "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE, "id": "3", "am": "2"}
    },
    {
        "title": "Polished Diorite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STONE, "id": "3", "link": "C:Diorite"}, "5": {"m": STONE, "id": "3", "link": "C:Diorite"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STONE, "id": "3", "link": "C:Diorite"}, "8": {"m": STONE, "id": "3", "link": "C:Diorite"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE, "id": "4", "am": "4"}
    },
    {
        "title": "Andesite",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STONE, "id": "3", "link": "C:Diorite"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE, "id": "5", "am": "2"}
    },
    {
        "title": "Polished Andesite",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STONE, "id": "5", "link": "C:Andesite"}, "5": {"m": STONE, "id": "5", "link": "C:Andesite"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STONE, "id": "5", "link": "C:Andesite"}, "8": {"m": STONE, "id": "5", "link": "C:Andesite"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE, "id": "6", "am": "4"}
    },
    {
        "title": "Oak Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": LOG, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD, "id": "", "am": "1"}
    },
   {
        "title": "Spruce Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": LOG, "id": "1", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD, "id": "1", "am": "1"}
    },
    {
        "title": "Birch Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": LOG, "id": "2", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD, "id": "2", "am": "1"}
    },
    {
        "title": "Jungle Wood Planks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": LOG, "id": "3", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD, "id": "3", "am": "1"}
    },
    {
        "title": "Acacia Wood Planks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": LOG_2, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD, "id": "4", "am": "1"}
    },
    {
        "title": "Dark Oak Wood Planks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": LOG_2, "id": "1", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD, "id": "5", "am": "1"}
    },
    {
        "title": "Lapis Lazuli Block",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"},

        "res": {"m": LAPIS_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Dispenser",
        "type": fixed,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": BOW, "id": "", "link": "C:Bow"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": DISPENSER, "id": "", "am": "1"}
    },
    {
        "title": "Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SAND, "id": "", "link": "G:Ore"}, "5": {"m": SAND, "id": "", "link": "G:Ore"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SAND, "id": "", "link": "G:Ore"}, "8": {"m": SAND, "id": "", "link": "G:Ore"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SANDSTONE, "id": "", "am": "1"}
    },
    {
        "title": "Chiseled Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STONE_SLAB2, "id": '', "link": "C:SandstoneSlab"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STONE_SLAB2, "id": "", "link": "C:SandstoneSlab"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SANDSTONE, "id": "1", "am": "1"}
    },
    {
        "title": "Smooth Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "5": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "8": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SANDSTONE, "id": "2", "am": "4"}
    },
    {
        "title": "Note Block",
        "type": fixed,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": NOTE_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Powered Rail",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": POWERED_RAIL, "id": "", "am": "1"}
    },
    {
        "title": "Detector Rail",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": STONE_PLATE, "id": "", "link": "S:StonePressurePlate"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": DETECTOR_RAIL, "id": "", "am": "1"}
    },
    {
        "title": "Sticky Piston",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": PISTON_BASE, "id": "", "link": "C:Piston"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": PISTON_STICKY_BASE, "id": "", "am": "1"}
    },
    {
        "title": "Piston",
        "type": fixed,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": PISTON_BASE, "id": "", "am": "1"}
    },
    {
        "title": "Wool",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STRING, "id": "", "link": ""}, "5": {"m": STRING, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STRING, "id": "", "link": ""}, "8": {"m": STRING, "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "", "am": "1"}
    },
    {
        "title": "Orange Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "14", "link": "C:OrangeDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "1", "am": "1"}
    },
    {
        "title": "Magenta Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "13", "link": "C:MagentaDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "2", "am": "1"}
    },
    {
        "title": "Light Blue Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "12", "link": "C:LightBlueDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "3", "am": "1"}
    },
    {
        "title": "Yellow Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "4", "am": "1"}
    },
    {
        "title": "Lime Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "10", "link": "C:LimeDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "5", "am": "1"}
    },
    {
        "title": "Pink Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "6", "am": "1"}
    },
    {
        "title": "Gray Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "7", "am": "1"}
    },
    {
        "title": "Light Gray Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "7", "link": "C:LightGrayDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "8", "am": "1"}
    },
    {
        "title": "Cyan Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "6", "link": "C:CyanDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "9", "am": "1"}
    },
    {
        "title": "Purple Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "10", "am": "1"}
    },
    {
        "title": "Blue Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "11", "am": "1"}
    },
    {
        "title": "Brown Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "3", "link": "C:CocoaBeans"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "12", "am": "1"}
    },
    {
        "title": "Green Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "2", "link": "C:GreenDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "13", "am": "1"}
    },
    {
        "title": "Red Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "14", "am": "1"}
    },
    {
        "title": "Black Wool",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOL, "id": "15", "am": "1"}
    },
    {
        "title": "Block Of Gold",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": ""}, "2": {"m": GOLD_INGOT, "id": "", "link": ""}, "3": {"m": GOLD_INGOT, "id": "", "link": ""},
        "4": {"m": GOLD_INGOT, "id": "", "link": ""}, "5": {"m": GOLD_INGOT, "id": "", "link": ""}, "6": {"m": GOLD_INGOT, "id": "", "link": ""},
        "7": {"m": GOLD_INGOT, "id": "", "link": ""}, "8": {"m": GOLD_INGOT, "id": "", "link": ""}, "9": {"m": GOLD_INGOT, "id": "", "link": ""},

        "res": {"m": GOLD_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Block Of Iron",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": ""}, "2": {"m": IRON_INGOT, "id": "", "link": ""}, "3": {"m": IRON_INGOT, "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": ""}, "5": {"m": IRON_INGOT, "id": "", "link": ""}, "6": {"m": IRON_INGOT, "id": "", "link": ""},
        "7": {"m": IRON_INGOT, "id": "", "link": ""}, "8": {"m": IRON_INGOT, "id": "", "link": ""}, "9": {"m": IRON_INGOT, "id": "", "link": ""},

        "res": {"m": IRON_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Stone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": STONE, "id": "", "link": "S:Stone"},

        "res": {"m": STEP, "id": "", "am": "6"}
    },
    {
        "title": "Sandstone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "8": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "9": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"},

        "res": {"m": STEP, "id": "1", "am": "6"}
    },
    {
        "title": "Cobblestone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": STEP, "id": "3", "am": "6"}
    },
    {
        "title": "Brick Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": BRICK, "id": "", "link": "C:Brick"}, "8": {"m": BRICK, "id": "", "link": "C:Brick"}, "9": {"m": BRICK, "id": "", "link": "C:Brick"},

        "res": {"m": STEP, "id": "4", "am": "6"}
    },
    {
        "title": "Stone Brick Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "8": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "9": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"},

        "res": {"m": STEP, "id": "5", "am": "6"}
    },
    {
        "title": "Nether Brick Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "8": {"m": SANDSTONE, "id": "", "link": "C:NetherBricks"}, "9": {"m": SANDSTONE, "id": "", "link": "C:NetherBricks"},

        "res": {"m": STEP, "id": "6", "am": "6"}
    },
    {
        "title": "Quartz Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": QUARTZ, "id": "", "link": ""}, "8": {"m": QUARTZ, "id": "", "link": ""}, "9": {"m": QUARTZ, "id": "", "link": ""},

        "res": {"m": STEP, "id": "7", "am": "6"}
    },
    {
        "title": "Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "5": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "8": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BRICK, "id": "", "am": "1"}
    },
    {
        "title": "TNT",
        "type": fixed,

        "1": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "2": {"m": SAND, "id": "", "link": "G:Ore"}, "3": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"},
        "4": {"m": SAND, "id": "", "link": "G:Ore"}, "5": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "6": {"m": SAND, "id": "", "link": "G:Ore"},
        "7": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "8": {"m": SAND, "id": "", "link": "G:Ore"}, "9": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"},

        "res": {"m": TNT, "id": "", "am": "1"}
    },
    {
        "title": "Bookshelf",
        "type": fixed,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": BOOK, "id": "", "link": "C:Book"}, "5": {"m": BOOK, "id": "", "link": "C:Book"}, "6": {"m": BOOK, "id": "", "link": "C:Book"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": BOOKSHELF, "id": "", "am": "1"}
    },
    {
        "title": "Moss Stone",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": VINE, "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": MOSSY_COBBLESTONE, "id": "", "am": "1"}
    },
    {
        "title": "Torch",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": COAL, "id": "", "link": "C:Coal"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": TORCH, "id": "", "am": "1"}
    },
    {
        "title": "Oak Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Chest",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": CHEST, "id": "", "am": "1"}
    },
    {
        "title": "Block Of Diamond",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Crafting Table",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WORKBENCH, "id": "", "am": "1"}
    },
    {
        "title": "Furnace",
        "type": fixed,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": FURNACE, "id": "", "am": "1"}
    },
    {
        "title": "Ladder",
        "type": shaped,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": LADDER, "id": "", "am": "3"}
    },
    {
        "title": "Rail",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": RAILS, "id": "", "am": "1"}
    },
    {
        "title": "Cobblestone Stairs",
        "type": shaped,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": COBBLESTONE_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Lever",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": STICK, "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": COBBLESTONE, "link": "G:Cobblestone"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": LEVER, "id": "", "am": "1"}
    },
    {
        "title": "Stone Pressure Plate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "Wooden Pressure Plate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "Redstone Torch",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": REDSTONE_TORCH_ON, "id": "", "am": "1"}
    },
    {
        "title": "Stone Button",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STONE, "id": "", "link": "S:Stone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE_BUTTON, "id": "", "am": "1"}
    },
    {
        "title": "Snow",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SNOW_BLOCK, "id": "", "link": "S:StoneBlock"}, "8": {"m": SNOW_BLOCK, "id": "", "link": "S:StoneBlock"}, "9": {"m": SNOW_BLOCK, "id": "", "link": "S:StoneBlock"},

        "res": {"m": SNOW, "id": "", "am": "1"}
    },
    {
        "title": "Snow Block",
        "type": shaped,

        "1": {"m": SNOW_BALL, "id": "", "link": ""}, "2": {"m": SNOW_BALL, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SNOW_BALL, "id": "", "link": ""}, "5": {"m": SNOW_BALL, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SNOW_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Clay Block",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "5": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "8": {"m": CLAY_BALL, "id": "", "link": "C:ClayBall"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CLAY, "id": "", "am": "1"}
    },
    {
        "title": "Jukebox",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": JUKEBOX, "id": "", "am": "1"}
    },
    {
        "title": "Oak Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": FENCE, "id": "", "am": "3"}
    },
    {
        "title": "Glowstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "5": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "8": {"m": GLOWSTONE_DUST, "id": "", "link": "C:GlowstoneDust"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GLOWSTONE, "id": "", "am": "1"}
    },
    {
        "title": "Jack O Lantern",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": PUMPKIN, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": TORCH, "id": "", "link": "C:Torch"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": JACK_O_LANTERN, "id": "", "am": "1"}
    },
    {
        "title": "White Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "", "am": "8"}
    },
    {
        "title": "Orange Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "14", "link": "C:OrangeDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "1", "am": "8"}
    },
    {
        "title": "Magenta Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "13", "link": "C:MagentaDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "2", "am": "8"}
    },
    {
        "title": "Light Blue Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "12", "link": "C:LightBlueDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "3", "am": "8"}
    },
    {
        "title": "Yellow Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "4", "am": "8"}
    },
    {
        "title": "Lime Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "10", "link": "C:LimeDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "5", "am": "8"}
    },
    {
        "title": "Pink Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "6", "am": "8"}
    },
    {
        "title": "Gray Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "7", "am": "8"}
    },
    {
        "title": "Light Gray Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "7", "link": "C:LightGrayDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "8", "am": "8"}
    },
    {
        "title": "Cyan Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "6", "link": "C:CyanDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "9", "am": "8"}
    },
    {
        "title": "Purple Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "10", "am": "8"}
    },
    {
        "title": "Blue Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "11", "am": "8"}
    },
    {
        "title": "Brown Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "3", "link": "C:CocoaBeans"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "12", "am": "8"}
    },
    {
        "title": "Green Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "2", "link": "C:GreenDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "13", "am": "8"}
    },
    {
        "title": "Red Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "14", "am": "8"}
    },
    {
        "title": "Black Stained Glass",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": INK_SACK, "id": "", "link": ""}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": STAINED_GLASS, "id": "15", "am": "8"}
    },
    {
        "title": "Wooden Trapdoor",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": TRAP_DOOR, "id": "", "am": "2"}
    },
    {
        "title": "Stone Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STONE, "id": "", "link": "S:Stone"}, "5": {"m": STONE, "id": "", "link": "S:Stone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SMOOTH_BRICK, "id": "", "am": "4"}
    },
    {
        "title": "Mossy Stone Bricks",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SMOOTH_BRICK, "id": "StoneBricks", "link": ""}, "5": {"m": VINE, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SMOOTH_BRICK, "id": "1", "am": "1"}
    },
    {
        "title": "Chiseled Stone Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STEP, "id": "5", "link": "S:StoneBricksSlab"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STEP, "id": "5", "link": "S:StoneBricksSlab"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SMOOTH_BRICK, "id": "3", "am": "1"}
    },
    {
        "title": "Iron Bars",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_BARDING, "id": "", "am": "16"}
    },
    {
        "title": "Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": GLASS, "id": "", "link": "S:Glass"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": GLASS, "id": "", "link": "S:Glass"}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": GLASS, "id": "", "link": "S:Glass"},

        "res": {"m": THIN_GLASS, "id": "", "am": "1"}
    },
    {
        "title": "Melon Block",
        "type": shaped,

        "1": {"m": MELON, "id": "", "link": ""}, "2": {"m": MELON, "id": "", "link": ""}, "3": {"m": MELON, "id": "", "link": ""},
        "4": {"m": MELON, "id": "", "link": ""}, "5": {"m": MELON, "id": "", "link": ""}, "6": {"m": MELON, "id": "", "link": ""},
        "7": {"m": MELON, "id": "", "link": ""}, "8": {"m": MELON, "id": "", "link": ""}, "9": {"m": MELON, "id": "", "link": ""},

        "res": {"m": MELON_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Oak Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "Bricks Stairs",
        "type": shaped,

        "1": {"m": BRICK, "id": "", "link": "C:Bricks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": BRICK, "id": "", "link": "C:Bricks"}, "5": {"m": BRICK, "id": "", "link": "C:Bricks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": BRICK, "id": "", "link": "C:Bricks"}, "8": {"m": BRICK, "id": "", "link": "C:Bricks"}, "9": {"m": BRICK, "id": "", "link": "C:Bricks"},

        "res": {"m": BRICK_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Stone Bricks Stairs",
        "type": shaped,

        "1": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "5": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "8": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"}, "9": {"m": SMOOTH_BRICK, "id": "", "link": "S:StoneBricks"},

        "res": {"m": SMOOTH_STAIRS, "id": "", "am": "4"}
    },
    {
        "title": "Nether Bricks",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": NETHER_BRICK_ITEM, "id": "", "link": "S:NetherBrick"}, "5": {"m": NETHER_BRICK_ITEM, "id": "NetherBrick", "link": "S:NetherBrick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": NETHER_BRICK_ITEM, "id": "", "link": "S:NetherBrick"}, "8": {"m": NETHER_BRICK_ITEM, "id": "NetherBrick", "link": "S:NetherBrick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": NETHER_BRICK, "id": "", "am": "1"}
    },
    {
        "title": "Nether Bricks Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "5": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "6": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"},
        "7": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "8": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "9": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"},

        "res": {"m": NETHER_FENCE, "id": "", "am": "1"}
    },
    {
        "title": "Nether Bricks Stairs",
        "type": shaped,

        "1": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "5": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "8": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"}, "9": {"m": NETHER_BRICK, "id": "", "link": "C:NetherBricks"},

        "res": {"m": NETHER_BRICK_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Enchantment Table",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": BOOK, "id": "", "link": "C:Book"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": OBSIDIAN, "id": "", "link": ""}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": OBSIDIAN, "id": "", "link": ""}, "8": {"m": OBSIDIAN, "id": "", "link": ""}, "9": {"m": OBSIDIAN, "id": "", "link": ""},

        "res": {"m": ENCHANTMENT_TABLE, "id": "", "am": "1"}
    },
    {
        "title": "Redstone Lamp",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "5": {"m": GLOWSTONE, "id": "", "link": "C:Glowstone"}, "6": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": REDSTONE_LAMP_OFF, "id": "", "am": "1"}
    },
    {
        "title": "Oak Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:WoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:WoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "", "am": "6"}
    },
    {
        "title": "Spruce Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "1", "am": "6"}
    },
    {
        "title": "Birch Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "2", "am": "6"}
    },
    {
        "title": "Jungle Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "8": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "9": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "3", "am": "6"}
    },
    {
        "title": "Acacia Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "4", "am": "6"}
    },
    {
        "title": "Dark Oak Wood Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},

        "res": {"m": WOOD_STEP, "id": "5", "am": "6"}
    },
    {
        "title": "Sandstone Stairs",
        "type": shaped,

        "1": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "5": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "8": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"}, "9": {"m": SANDSTONE, "id": "", "link": "C:Sandstone"},

        "res": {"m": SANDSTONE_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Ender Chest",
        "type": shaped,

        "1": {"m": OBSIDIAN, "id": "", "link": ""}, "2": {"m": OBSIDIAN, "id": "", "link": ""}, "3": {"m": OBSIDIAN, "id": "", "link": ""},
        "4": {"m": OBSIDIAN, "id": "", "link": ""}, "5": {"m": EYE_OF_ENDER, "id": "", "link": ""}, "6": {"m": OBSIDIAN, "id": "", "link": ""},
        "7": {"m": OBSIDIAN, "id": "", "link": ""}, "8": {"m": OBSIDIAN, "id": "", "link": ""}, "9": {"m": OBSIDIAN, "id": "", "link": ""},

        "res": {"m": ENDER_CHEST, "id": "", "am": "1"}
    },
    {
        "title": "Tripwire Hook",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": TRIPWIRE_HOOK, "id": "", "am": "1"}
    },
    {
        "title": "Block Of Emerald",
        "type": shaped,

        "1": {"m": EMERALD, "id": "", "link": ""}, "2": {"m": EMERALD, "id": "", "link": ""}, "3": {"m": EMERALD, "id": "", "link": ""},
        "4": {"m": EMERALD, "id": "", "link": ""}, "5": {"m": EMERALD, "id": "", "link": ""}, "6": {"m": EMERALD, "id": "", "link": ""},
        "7": {"m": EMERALD, "id": "", "link": ""}, "8": {"m": EMERALD, "id": "", "link": ""}, "9": {"m": EMERALD, "id": "", "link": ""},

        "res": {"m": EMERALD_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Spruce Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "5": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},

        "res": {"m": SPRUCE_WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Birch Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "5": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},

        "res": {"m": BIRCH_WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Jungle Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "5": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"}, "9": {"m": WOOD, "id": "1", "link": "C:JungleWoodPlanks"},

        "res": {"m": JUNGLE_WOOD_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Beacon",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": NETHER_STAR, "id": "", "link": "C:NetherStar"}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": OBSIDIAN, "id": "", "link": ""}, "8": {"m": OBSIDIAN, "id": "", "link": ""}, "9": {"m": OBSIDIAN, "id": "", "link": ""},

        "res": {"m": BEACON, "id": "", "am": "1"}
    },
    {
        "title": "Cobblestone Wall",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": COBBLE_WALL, "id": "", "am": "6"}
    },
    {
        "title": "Mossy Cobblestone Wall",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": MOSSY_COBBLESTONE, "id": "", "link": ""}, "5": {"m": MOSSY_COBBLESTONE, "id": "", "link": ""}, "6": {"m": MOSSY_COBBLESTONE, "id": "", "link": ""},
        "7": {"m": MOSSY_COBBLESTONE, "id": "", "link": ""}, "8": {"m": MOSSY_COBBLESTONE, "id": "", "link": ""}, "9": {"m": MOSSY_COBBLESTONE, "id": "", "link": ""},

        "res": {"m": COBBLE_WALL, "id": "1", "am": "1"}
    },
    {
        "title": "WoodButton",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_BUTTON, "id": "", "am": "1"}
    },
    {
        "title": "Anvil",
        "type": shaped,

        "1": {"m": IRON_BLOCK, "id": "", "link": "C:IronBlock"}, "2": {"m": IRON_BLOCK, "id": "", "link": "C:IronBlock"}, "3": {"m": IRON_BLOCK, "id": "", "link": "C:IronBlock"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": ANVIL, "id": "", "am": "1"}
    },
    {
        "title": "Trapped Chest",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": TRIPWIRE_HOOK, "id": "", "link": ""}, "8": {"m": CHEST, "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": TRAPPED_CHEST, "id": "", "am": "1"}
    },
    {
        "title": "Weighted Pressure Plate (Light)",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "Weighted Pressure Plate (Heavy)",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": IRON_INGOT, "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_PLATE, "id": "", "am": "1"}
    },
    {
        "title": "Daylight Sensor",
        "type": shaped,

        "1": {"m": GLASS, "id": "", "link": "S:Glass"}, "2": {"m": GLASS, "id": "", "link": "S:Glass"}, "3": {"m": GLASS, "id": "", "link": "S:Glass"},
        "4": {"m": QUARTZ, "id": "", "link": ""}, "5": {"m": QUARTZ, "id": "", "link": ""}, "6": {"m": QUARTZ, "id": "", "link": ""},
        "7": {"m": WOOD_STEP, "id": "", "link": "C:OakWoodSlab"}, "8": {"m": "", "id": "", "link": "C:OakWoodSlab"}, "9": {"m": "", "id": "", "link": "C:OakWoodSlab"},

        "res": {"m": DAYLIGHT_DETECTOR, "id": "", "am": "1"}
    },
    {
        "title": "Block Of Redstone",
        "type": shaped,

        "1": {"m": REDSTONE, "id": "", "link": ""}, "2": {"m": REDSTONE, "id": "", "link": ""}, "3": {"m": REDSTONE, "id": "", "link": ""},
        "4": {"m": REDSTONE, "id": "", "link": ""}, "5": {"m": REDSTONE, "id": "", "link": ""}, "6": {"m": REDSTONE, "id": "", "link": ""},
        "7": {"m": REDSTONE, "id": "", "link": ""}, "8": {"m": REDSTONE, "id": "", "link": ""}, "9": {"m": REDSTONE, "id": "", "link": ""},

        "res": {"m": REDSTONE_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Hopper",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": CHEST, "id": "", "link": "C:Chest"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": HOPPER, "id": "", "am": "1"}
    },
    {
        "title": "Block Of Quartz",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": QUARTZ, "id": "", "link": ""}, "5": {"m": QUARTZ, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": QUARTZ, "id": "", "link": ""}, "8": {"m": QUARTZ, "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": QUARTZ_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Chiseled Quartz Block",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STEP, "id": "7", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STEP, "id": "7", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": QUARTZ_BLOCK, "id": "1", "am": "1"}
    },
    {
        "title": "Pillar Quartz Block",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": QUARTZ_BLOCK, "id": "2", "am": "1"}
    },
    {
        "title": "Quartz Stairs",
        "type": shaped,

        "1": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "5": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "8": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"}, "9": {"m": QUARTZ_BLOCK, "id": "", "link": "C:BlockOfQuartz"},

        "res": {"m": QUARTZ_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Activator Rail",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": ACTIVATOR_RAIL, "id": "", "am": "6"}
    },
    {
        "title": "Dropper",
        "type": shaped,

        "1": {"m": "Cobblestone", "id": "", "link": ""}, "2": {"m": "Cobblestone", "id": "", "link": ""}, "3": {"m": "Cobblestone", "id": "", "link": ""},
        "4": {"m": "Cobblestone", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "Cobblestone", "id": "", "link": ""},
        "7": {"m": "Cobblestone", "id": "", "link": ""}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": "Cobblestone", "id": "", "link": ""},

        "res": {"m": DROPPER, "id": "", "am": "1"}
    },
    {
        "title": "White Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "", "am": "8"}
    },
    {
        "title": "Orange Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "14", "link": "C:OrangeDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "1", "am": "8"}
    },
    {
        "title": "Magenta Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "13", "link": "C:MagentaDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "2", "am": "8"}
    },
    {
        "title": "Light Blue Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "12", "link": "C:LightBlueDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "3", "am": "8"}
    },
    {
        "title": "Yellow Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "4", "am": "8"}
    },
    {
        "title": "Lime Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "10", "link": "C:LimeDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "5", "am": "8"}
    },
    {
        "title": "Pink Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "6", "am": "8"}
    },
    {
        "title": "Gray Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "7", "am": "8"}
    },
    {
        "title": "Light Gray Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "7", "link": "C:LightGrayDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "8", "am": "8"}
    },
    {
        "title": "Cyan Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "6", "link": "C:CyanDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "9", "am": "8"}
    },
    {
        "title": "Purple Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "10", "am": "8"}
    },
    {
        "title": "Blue Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "11", "am": "8"}
    },
    {
        "title": "Brown Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "3", "link": "C:CocoaBeans"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "12", "am": "8"}
    },
    {
        "title": "Green Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "2", "link": "C:GreenDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "13", "am": "8"}
    },
    {
        "title": "Red Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "14", "am": "8"}
    },
    {
        "title": "Black Stained Clay",
        "type": shaped,

        "1": {"m": HARD_CLAY, "id": "", "link": ""}, "2": {"m": HARD_CLAY, "id": "", "link": ""}, "3": {"m": HARD_CLAY, "id": "", "link": ""},
        "4": {"m": HARD_CLAY, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "", "link": ""}, "6": {"m": HARD_CLAY, "id": "", "link": ""},
        "7": {"m": HARD_CLAY, "id": "", "link": ""}, "8": {"m": HARD_CLAY, "id": "", "link": ""}, "9": {"m": HARD_CLAY, "id": "", "link": ""},

        "res": {"m": STAINED_CLAY, "id": "15", "am": "8"}
    },
    {
        "title": "White Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "", "link": "C:WhiteStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "", "am": "16"}
    },
    {
        "title": "Orange Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "1", "link": "C:OrangeStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "1", "am": "16"}
    },
    {
        "title": "Magenta Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "2", "link": "C:MagentaStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "2", "am": "16"}
    },
    {
        "title": "Light Blue Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "3", "link": "C:LightBlueStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "3", "am": "16"}
    },
    {
        "title": "Yellow Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "4", "link": "C:YellowStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "4", "am": "16"}
    },
    {
        "title": "Lime Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "5", "link": "C:LimeStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "5", "am": "16"}
    },
    {
        "title": "Pink Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "4", "link": "C:PinkStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "6", "link": "C:PinkStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "4", "link": "C:PinkStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "6", "am": "16"}
    },
    {
        "title": "Gray Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "6", "link": "C:GrayStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "7", "link": "C:GrayStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "6", "link": "C:GrayStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "7", "am": "16"}
    },
    {
        "title": "Light Gray Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "8", "link": "C:LightGrayStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "8", "am": "16"}
    },
    {
        "title": "Cyan Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "9", "link": "C:CyanStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "9", "am": "16"}
    },
    {
        "title": "Purple Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "10", "link": "C:PurpleStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "11", "am": "16"}
    },
    {
        "title": "Blue Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "11", "link": "C:BlueStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "11", "am": "16"}
    },
    {
        "title": "Brown Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "12", "link": "C:BrownStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "12", "am": "16"}
    },
    {
        "title": "Green Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "13", "link": "C:GreenStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "13", "am": "16"}
    },
    {
        "title": "Red Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "14", "link": "C:RedStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "15", "am": "16"}
    },
    {
        "title": "Black Stained Glass Pane",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "5": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "6": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"},
        "7": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "8": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"}, "9": {"m": STAINED_GLASS, "id": "15", "link": "C:BlackStainedGlass"},

        "res": {"m": STAINED_GLASS_PANE, "id": "15", "am": "16"}
    },
    {
        "title": "Acacia Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "5": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},

        "res": {"m": ACACIA_STAIRS, "id": "", "am": "4"}
    },
    {
        "title": "Dark Oak Wood Stairs",
        "type": shaped,

        "1": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "5": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},

        "res": {"m": DARK_OAK_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Slime Block",
        "type": shaped,

        "1": {"m": SLIME_BALL, "id": "", "link": ""}, "2": {"m": SLIME_BALL, "id": "", "link": ""}, "3": {"m": SLIME_BALL, "id": "", "link": ""},
        "4": {"m": SLIME_BALL, "id": "", "link": ""}, "5": {"m": SLIME_BALL, "id": "", "link": ""}, "6": {"m": SLIME_BALL, "id": "", "link": ""},
        "7": {"m": SLIME_BALL, "id": "", "link": ""}, "8": {"m": SLIME_BALL, "id": "", "link": ""}, "9": {"m": SLIME_BALL, "id": "", "link": ""},

        "res": {"m": SLIME_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Iron Tarpdoor",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_TRAPDOOR, "id": "", "am": "1"}
    },
    {
        "title": "Prismarine",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "2": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "5": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": PRISMARINE, "id": "", "am": "1"}
    },
    {
        "title": "Prismarine Bricks",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "2": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "3": {"m": PRISMARINE_SHARD, "id": "", "link": ""},
        "4": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "5": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "6": {"m": PRISMARINE_SHARD, "id": "", "link": ""},
        "7": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "8": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "9": {"m": PRISMARINE_SHARD, "id": "", "link": ""},

        "res": {"m": PRISMARINE, "id": "1", "am": "1"}
    },
    {
        "title": "Dark Prismarine",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "2": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "3": {"m": PRISMARINE_SHARD, "id": "", "link": ""},
        "4": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "5": {"m": INK_SACK, "id": "", "link": ""}, "6": {"m": PRISMARINE_SHARD, "id": "", "link": ""},
        "7": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "8": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "9": {"m": PRISMARINE_SHARD, "id": "", "link": ""},

        "res": {"m": PRISMARINE, "id": "2", "am": "1"}
    },
    {
        "title": "Sea Lantern",
        "type": shaped,

        "1": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "2": {"m": PRISMARINE_CRYSTALS, "id": "", "link": ""}, "3": {"m": PRISMARINE_SHARD, "id": "", "link": ""},
        "4": {"m": PRISMARINE_CRYSTALS, "id": "", "link": ""}, "5": {"m": PRISMARINE_CRYSTALS, "id": "", "link": ""}, "6": {"m": PRISMARINE_CRYSTALS, "id": "", "link": ""},
        "7": {"m": PRISMARINE_SHARD, "id": "", "link": ""}, "8": {"m": PRISMARINE_CRYSTALS, "id": "", "link": ""}, "9": {"m": PRISMARINE_SHARD, "id": "", "link": ""},

        "res": {"m": SEA_LANTERN, "id": "", "am": "1"}
    },
    {
        "title": "Hay Bale",
        "type": shaped,

        "1": {"m": WHEAT, "id": "", "link": ""}, "2": {"m": WHEAT, "id": "", "link": ""}, "3": {"m": WHEAT, "id": "", "link": ""},
        "4": {"m": WHEAT, "id": "", "link": ""}, "5": {"m": WHEAT, "id": "", "link": ""}, "6": {"m": WHEAT, "id": "", "link": ""},
        "7": {"m": WHEAT, "id": "", "link": ""}, "8": {"m": WHEAT, "id": "", "link": ""}, "9": {"m": WHEAT, "id": "", "link": ""},

        "res": {"m": HAY_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "White Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "", "link": "C:WhiteWool"}, "8": {"m": WOOL,"id": "", "link": "C:WhiteWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "", "am": "3"}
    },
    {
        "title": "Orange Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "8": {"m": WOOL,"id": "1", "link": "C:OrangeWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "1", "am": "3"}
    },
    {
        "title": "Magenta Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "8": {"m": WOOL,"id": "2", "link": "C:MagentaWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "2", "am": "3"}
    },
    {
        "title": "Light Blue Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "8": {"m": WOOL,"id": "3", "link": "C:LightBlueWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "3", "am": "3"}
    },
    {
        "title": "Yellow Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "8": {"m": WOOL,"id": "4", "link": "C:YellowWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "4", "am": "3"}
    },
    {
        "title": "Lime Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "8": {"m": WOOL,"id": "5", "link": "C:LimeWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "5", "am": "3"}
    },
    {
        "title": "Pink Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "8": {"m": WOOL,"id": "6", "link": "C:PinkWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "6", "am": "3"}
    },
    {
        "title": "Gray Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "8": {"m": WOOL,"id": "7", "link": "C:GrayWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "7", "am": "3"}
    },
    {
        "title": "Light Gray Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "8": {"m": WOOL,"id": "8", "link": "C:LightGrayWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "8", "am": "3"}
    },
    {
        "title": "Cyan Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "8": {"m": WOOL,"id": "9", "link": "C:CyanWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "9", "am": "3"}
    },
    {
        "title": "Purple Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "8": {"m": WOOL,"id": "10", "link": "C:PurpleWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "10", "am": "3"}
    },
    {
        "title": "Blue Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "8": {"m": WOOL,"id": "11", "link": "C:BlueWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "11", "am": "3"}
    },
    {
        "title": "Brown Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "12", "link": "C:Brown Wool"}, "8": {"m": WOOL,"id": "12", "link": "C:Brown Wool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "12", "am": "3"}
    },
    {
        "title": "Green Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "8": {"m": WOOL,"id": "13", "link": "C:GreenWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "13", "am": "3"}
    },
    {
        "title": "Red Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "8": {"m": WOOL,"id": "14", "link": "C:RedWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "14", "am": "3"}
    },
    {
        "title": "Black Carpet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "8": {"m": WOOL,"id": "15", "link": "C:BlackWool"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARPET, "id": "15", "am": "3"}
    },
    {
        "title": "Block Of Coal",
        "type": shaped,

        "1": {"m": COAL, "id": "", "link": "C:Coal"}, "2": {"m": COAL, "id": "", "link": "C:Coal"}, "3": {"m": COAL, "id": "", "link": "C:Coal"},
        "4": {"m": COAL, "id": "", "link": "C:Coal"}, "5": {"m": COAL, "id": "", "link": "C:Coal"}, "6": {"m": COAL, "id": "", "link": "C:Coal"},
        "7": {"m": COAL, "id": "", "link": "C:Coal"}, "8": {"m": COAL, "id": "", "link": "C:Coal"}, "9": {"m": COAL, "id": "", "link": "C:Coal"},

        "res": {"m": COAL_BLOCK, "id": "", "am": "1"}
    },
    {
        "title": "Red Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SAND, "id": "1", "link": "C:RedSand"}, "5": {"m": SAND, "id": "1", "link": "C:RedSand"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SAND, "id": "1", "link": "C:RedSand"}, "8": {"m": SAND, "id": "1", "link": "C:RedSand"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": RED_SANDSTONE, "id": "", "am": "1"}
    },
    {
        "title": "Chiseled Red Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STONE_SLAB2, "id": "", "link": "C:RedSandstoneSlab"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STONE_SLAB2, "id": "", "link": "C:RedSandstoneSlab"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": RED_SANDSTONE, "id": "1", "am": "1"}
    },
    {
        "title": "Smooth Red Sandstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "5": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "8": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": RED_SANDSTONE, "id": "2", "am": "1"}
    },
    {
        "title": "Red Sandstone Stairs",
        "type": shaped,

        "1": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "5": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "8": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "9": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"},

        "res": {"m": RED_SANDSTONE_STAIRS, "id": "", "am": "1"}
    },
    {
        "title": "Red Sandstone Slab",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "8": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"}, "9": {"m": RED_SANDSTONE, "id": "", "link": "C:RedSandstone"},

        "res": {"m": STONE_SLAB2, "id": "", "am": "1"}
    },
    {
        "title": "Spruce Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": SPRUCE_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "Birch Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": BIRCH_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "Jungle Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": JUNGLE_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "Dark Oak Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": DARK_OAK_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "Acacia Fence Gate",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": ACACIA_FENCE_GATE, "id": "", "am": "1"}
    },
    {
        "title": "Spruce Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"},

        "res": {"m": SPRUCE_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "Birch Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"},

        "res": {"m": BIRCH_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "Jungle Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"},
        "7": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"},

        "res": {"m": JUNGLE_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "Dark Oak Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"},

        "res": {"m": DARK_OAK_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "Acacia Fence",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"},

        "res": {"m": ACACIA_FENCE, "id": "", "am": "3"}
    },
    {
        "title": "Iron Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "Iron Pickaxe",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "Iron Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_AXE, "id": "", "am": "1"}
    },
    {
        "title": "Flint And Steel",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": FLINT, "id": "", "link": "C:Flint"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": FLINT_AND_STEEL, "id": "", "am": "1"}
    },
    {
        "title": "Bow",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": STRING, "id": "", "link": "C:String"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": BOW, "id": "", "am": "1"}
    },
    {
        "title": "Arrow",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": FLINT, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": FEATHER, "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": ARROW, "id": "", "am": "1"}
    },
    {
        "title": "Coal",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": COAL_BLOCK, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": COAL, "id": "", "am": "9"}
    },
    {
        "title": "Diamond",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": DIAMOND_BLOCK, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DIAMOND, "id": "", "am": "9"}
    },
    {
        "title": "Iron Ingot",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_INGOT, "id": "", "am": "9"}
    },
    {
        "title": "Gold Ingot",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": GOLD_BLOCK, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_INGOT, "id": "", "am": "9"}
    },
    {
        "title": "Iron Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "Wooden Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "Wooden Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "Wooden Pickaxe",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "Wooden Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_AXE, "id": "", "am": "1"}
    },
    {
        "title": "Stone Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "Stone Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "Stone Pickaxe",
        "type": shaped,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "Stone Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE_AXE, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DIAMOND_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DIAMOND_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Pickaxe",
        "type": shaped,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DIAMOND_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DIAMOND_AXE, "id": "", "am": "1"}
    },
    {
        "title": "Stick",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STICK, "id": "", "am": "4"}
    },
    {
        "title": "Bowl",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BOWL, "id": "", "am": "4"}
    },
    {
        "title": "Mushroom Stew",
        "type": shapeless,

        "1": {"m": RED_MUSHROOM, "id": "", "link": ""}, "2": {"m": BROWN_MUSHROOM, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": BOWL, "id": "", "link": "C:Bowl"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": MUSHROOM_SOUP, "id": "", "am": "1"}
    },
    {
        "title": "Golden Sword",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_SWORD, "id": "", "am": "1"}
    },
    {
        "title": "Golden Shovel",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_SPADE, "id": "", "am": "1"}
    },
    {
        "title": "Golden Pickaxe",
        "type": shaped,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_PICKAXE, "id": "", "am": "1"}
    },
    {
        "title": "Golden Axe",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_AXE, "id": "", "am": "1"}
    },
    {
        "title": "Wooden Hoe",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_HOE, "id": "", "am": "1"}
    },
    {
        "title": "Stone Hoe",
        "type": shaped,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STONE_HOE, "id": "", "am": "1"}
    },
    {
        "title": "Iron Hoe",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_HOE, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Hoe",
        "type": shaped,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DIAMOND_HOE, "id": "", "am": "1"}
    },
    {
        "title": "Golden Hoe",
        "type": shaped,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_HOE, "id": "", "am": "1"}
    },
    {
        "title": "Wheat",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": HAY_BLOCK, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WHEAT, "id": "", "am": "9"}
    },
    {
        "title": "Bread",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "8": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "9": {"m": WHEAT, "id": "", "link": "C:Wheat"},

        "res": {"m": BREAD, "id": "", "am": "1"}
    },
    {
        "title": "Leather Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": LEATHER, "id": "", "link": "C:Leather"}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "Leather Chestplate",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "C:Leather"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": LEATHER, "id": "", "link": "C:Leather"}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": LEATHER, "id": "", "link": "C:Leather"}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "Leather Leggings",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "C:Leather"}, "2": {"m": LEATHER, "id": "", "link": "C:Leather"}, "3": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "Leather Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": LEATHER, "id": "", "link": "C:Leather"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": LEATHER, "id": "", "link": "C:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "C:Leather"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": LEATHER, "id": "", "link": "C:Leather"},

        "res": {"m": LEATHER_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "Iron Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "Iron Chestplate",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "Iron Leggings",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "Iron Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": IRON_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Chestplate",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Leggings",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": DIAMOND, "id": "", "link": "C:Diamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:Diamond"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": DIAMOND, "id": "", "link": "C:Diamond"},

        "res": {"m": DIAMOND_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "Golden Helmet",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_HELMET, "id": "", "am": "1"}
    },
    {
        "title": "Golden Chestplate",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_CHESTPLATE, "id": "", "am": "1"}
    },
    {
        "title": "Golden Leggings",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_LEGGINGS, "id": "", "am": "1"}
    },
    {
        "title": "Golden Boots",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLD_BOOTS, "id": "", "am": "1"}
    },
    {
        "title": "Painting",
        "type": shaped,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": WOOL, "id": "", "link": ""}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": PAINTING, "id": "", "am": "1"}
    },
    {
        "title": "Golden Apple",
        "type": shaped,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": APPLE, "id": "", "link": ""}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},

        "res": {"m": GOLDEN_APPLE, "id": "", "am": "1"}
    },
    {
        "title": "Enchanted Golden Apple",
        "type": shaped,

        "1": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "2": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "3": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "4": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "5": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "6": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "7": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "8": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "9": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},

        "res": {"m": GOLDEN_APPLE, "id": "1", "am": "1"}
    },
    {
        "title": "Sign",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SIGN, "id": "", "am": "1"}
    },
    {
        "title": "Oak Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "2": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WOOD_DOOR, "id": "", "am": "1"}
    },
    {
        "title": "Bucket",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BUCKET, "id": "", "am": "1"}
    },
    {
        "title": "Minecart",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": MINECART, "id": "", "am": "1"}
    },
    {
        "title": "Iron Door",
        "type": shaped,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": IRON_DOOR, "id": "", "am": "3"}
    },
    {
        "title": "Redstone",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": REDSTONE_BLOCK, "id": "", "link": "C:BlockOfRedstone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": REDSTONE, "id": "", "am": "1"}
    },
    {
        "title": "Boat",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": BOAT, "id": "", "am": "1"}
    },
    {
        "title": "Leather",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": RABBIT_HIDE, "id": "", "link": ""}, "5": {"m": RABBIT_HIDE, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": RABBIT_HIDE, "id": "", "link": ""}, "8": {"m": RABBIT_HIDE, "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": LEATHER, "id": "", "am": "1"}
    },
    {
        "title": "Paper",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SUGAR_CANE, "id": "", "link": ""}, "8": {"m": SUGAR_CANE, "id": "", "link": ""}, "9": {"m": SUGAR_CANE, "id": "", "link": ""},

        "res": {"m": PAPER, "id": "", "am": "1"}
    },
    {
        "title": "Book",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": PAPER, "id": "", "link": "C:Paper"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BOOK, "id": "", "am": "1"}
    },
    {
        "title": "Slime Ball",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": SLIME_BLOCK, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SLIME_BALL, "id": "", "am": "9"}
    },
    {
        "title": "Minecart With Chest",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": CHEST, "id": "", "link": "C:Chest"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": STORAGE_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "Minecart With Furnace",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": FURNACE, "id": "", "link": "C:Furnace"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": POWERED_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "Compass",
        "type": fixed,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": COMPASS, "id": "", "am": "1"}
    },
    {
        "title": "Fishing Rod",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": STRING, "id": "", "link": ""},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": STRING, "id": "", "link": ""},

        "res": {"m": FISHING_ROD, "id": "", "am": "1"}
    },
    {
        "title": "Clock",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:GoldIngot"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": WATCH, "id": "", "am": "1"}
    },
    {
        "title": "Red Dye",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "1", "am": "1"}
    },
    {
        "title": "Red Dye 1",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "4", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "1", "am": "1"}
    },
    {
        "title": "Red Dye 2",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": DOUBLE_PLANT, "id": "4", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "1", "am": "2"}
    },
    {
        "title": "Purple Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "5", "am": "2"}
    },
    {
        "title": "Cyan Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "2", "link": "S:GreenDye"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "6", "am": "2"}
    },
    {
        "title": "Light Gray Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "8", "link": "C:GrayDye"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "7", "am": "2"}
    },
    {
        "title": "Light Gray Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "7", "am": "3"}
    },
    {
        "title": "Light Gray Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "3", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "7", "am": "1"}
    },
    {
        "title": "Light Gray Dye 3",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "6", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "7", "am": "1"}
    },
    {
        "title": "Light Gray Dye 4",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "8", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "7", "am": "1"}
    },
    {
        "title": "Gray Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "", "link": ""}, "8": {"m": INK_SACK, "id": "15", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "8", "am": "1"}
    },
    {
        "title": "Pink Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "9", "am": "2"}
    },
    {
        "title": "Pink Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "7", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "9", "am": "1"}
    },
    {
        "title": "Pink Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": DOUBLE_PLANT, "id": "5", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "9", "am": "2"}
    },
    {
        "title": "Lime Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "2", "link": "S:GreenDye"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "10", "am": "2"}
    },
    {
        "title": "Yellow Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": YELLOW_FLOWER, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "11", "am": "1"}
    },
    {
        "title": "Yellow Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": DOUBLE_PLANT, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "11", "am": "2"}
    },
    {
        "title": "Light Blue Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "12", "am": "1"}
    },
    {
        "title": "Light Blue Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "1", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "12", "am": "2"}
    },
    {
        "title": "Magenta Dye",
        "type": shapeless,

        "1": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "2": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "5": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "13", "am": "4"}
    },
    {
        "title": "Magenta Dye 1",
        "type": shapeless,

        "1": {"m": INK_SACK, "id": "4", "link": "C:LapisLazuli"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "13", "am": "3"}
    },
    {
        "title": "Magenta Dye 2",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "5", "link": "C:PurpleDye"}, "5": {"m": INK_SACK, "id": "9", "link": "C:PinkDye"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "13", "am": "2"}
    },
    {
        "title": "Magenta Dye 3",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "2", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "13", "am": "1"}
    },
    {
        "title": "Magenta Dye 4",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": DOUBLE_PLANT, "id": "1", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "13", "am": "2"}
    },
    {
        "title": "Orange Dye",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "1", "link": "C:RedDye"}, "8": {"m": INK_SACK, "id": "11", "link": "C:YellowDye"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "14", "am": "2"}
    },
    {
        "title": "Orange Dye 1",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": RED_ROSE, "id": "5", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "14", "am": "1"}
    },
    {
        "title": "Bone Meal",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": BONE, "id": "", "link": "C:Bone"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": INK_SACK, "id": "15", "am": "3"}
    },
    {
        "title": "Sugar",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": SUGAR_CANE, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SUGAR, "id": "", "am": "1"}
    },
    {
        "title": "Cake",
        "type": shaped,

        "1": {"m": MILK_BUCKET, "id": "", "link": ""}, "2": {"m": MILK_BUCKET, "id": "", "link": ""}, "3": {"m": MILK_BUCKET, "id": "", "link": ""},
        "4": {"m": SUGAR, "id": "", "link": "C:Sugar"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": SUGAR, "id": "", "link": "C:Sugar"},
        "7": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "8": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "9": {"m": WHEAT, "id": "", "link": "C:Wheat"},

        "res": {"m": CAKE, "id": "", "am": "1"}
    },
    {
        "title": "Bed",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOL, "id": "", "link": "C:Wool"}, "5": {"m": WOOL, "id": "", "link": "C:Wool"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "8": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"}, "9": {"m": WOOD, "id": "", "link": "C:OakWoodPlanks"},

        "res": {"m": BED, "id": "", "am": "1"}
    },
    {
        "title": "Redsrone Repeater",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "5": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "6": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": STONE, "id": "", "link": "S:Stone"},

        "res": {"m": DIODE, "id": "", "am": "1"}
    },
    {
        "title": "Cookie",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WHEAT, "id": "", "link": "C:Wheat"}, "8": {"m": INK_SACK, "id": "3", "link": ""}, "9": {"m": WHEAT, "id": "", "link": "C:Wheat"},

        "res": {"m": COOKIE, "id": "", "am": "1"}
    },
    {
        "title": "Shears",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SHEARS, "id": "", "am": "1"}
    },
    {
        "title": "Pumpkin Seeds",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": PUMPKIN, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": PUMPKIN_SEEDS, "id": "", "am": "4"}
    },
    {
        "title": "Melon Seeds",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": MELON, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": MELON_SEEDS, "id": "", "am": "1"}
    },
    {
        "title": "Gold Nugget",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": GOLD_INGOT, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GOLD_NUGGET, "id": "", "am": "9"}
    },
    {
        "title": "Glass Bottle",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": GLASS, "id": "", "link": "S:Glass"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": GLASS, "id": "", "link": "S:Glass"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": GLASS, "id": "", "link": "S:Glass"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GLASS_BOTTLE, "id": "", "am": "9"}
    },
    {
        "title": "Fermented Spider Eye",
        "type": shapeless,

        "1": {"m": SPIDER_EYE, "id": "", "link": ""}, "2": {"m": BROWN_MUSHROOM, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": SUGAR, "id": "", "link": "C:Sugar"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": FERMENTED_SPIDER_EYE, "id": "", "am": "1"}
    },
    {
        "title": "Blaze Powder",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": BLAZE_ROD, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BLAZE_POWDER, "id": "", "am": "2"}
    },
    {
        "title": "Magma Cream",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": BLAZE_POWDER, "id": "", "link": "C:BlazePowder"}, "5": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": MAGMA_CREAM, "id": "", "am": "1"}
    },
    {
        "title": "Brewing Stand",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": BLAZE_ROD, "id": "", "link": "C:BlazeRod"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": BREWING_STAND_ITEM, "id": "", "am": "1"}
    },
    {
        "title": "Cauldron",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": CAULDRON_ITEM, "id": "", "am": "1"}
    },
    {
        "title": "Eye Of Ender",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": ENDER_PEARL, "id": "", "link": ""}, "5": {"m": BLAZE_POWDER, "id": "", "link": "C:BlazePowder"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": EYE_OF_ENDER, "id": "", "am": "1"}
    },
    {
        "title": "Golden Melon",
        "type": fixed,

        "1": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "2": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "3": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "4": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "5": {"m": MELON, "id": "", "link": ""}, "6": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "7": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "8": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "9": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},

        "res": {"m": SPECKLED_MELON, "id": "", "am": "1"}
    },
    {
        "title": "Fire Charge",
        "type": shapeless,

        "1": {"m": SULPHUR, "id": "", "link": "C:Gunpowder"}, "2": {"m": BLAZE_POWDER, "id": "", "link": "C:BlazePowder"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": COAL, "id": "", "link": "C:Coal"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": FIREWORK_CHARGE, "id": "", "am": "1"}
    },
    {
        "title": "Book And Quill",
        "type": shapeless,

        "1": {"m": BOOK, "id": "", "link": "C:Book"}, "2": {"m": INK_SACK, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": FEATHER, "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BOOK_AND_QUILL, "id": "", "am": "1"}
    },
    {
        "title": "Emerald",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": EMERALD, "id": "", "am": "9"}
    },
    {
        "title": "Item Frame",
        "type": fixed,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": LEATHER, "id": "", "link": "S:Leather"}, "6": {"m": STICK, "id": "", "link": "C:Stick"},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": ITEM_FRAME, "id": "", "am": "1"}
    },
    {
        "title": "Flower Pot",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": CLAY_BRICK, "id": "", "link": "S:Brick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": FLOWER_POT_ITEM, "id": "", "am": "1"}
    },
    {
        "title": "Empty Map",
        "type": shaped,

        "1": {"m": PAPER, "id": "", "link": "C:Paper"}, "2": {"m": PAPER, "id": "", "link": "C:Paper"}, "3": {"m": PAPER, "id": "", "link": "C:Paper"},
        "4": {"m": PAPER, "id": "", "link": "C:Paper"}, "5": {"m": COMPASS, "id": "", "link": "C:Compass"}, "6": {"m": PAPER, "id": "", "link": "C:Paper"},
        "7": {"m": PAPER, "id": "", "link": "C:Paper"}, "8": {"m": PAPER, "id": "", "link": "C:Paper"}, "9": {"m": PAPER, "id": "", "link": "C:Paper"},

        "res": {"m": EMPTY_MAP, "id": "", "am": "1"}
    },
    {
        "title": "Golden Carrot",
        "type": fixed,

        "1": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "2": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "3": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "4": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "5": {"m": CARROT_ITEM, "id": "", "link": ""}, "6": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "7": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "8": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "9": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},

        "res": {"m": GOLDEN_CARROT, "id": "", "am": "1"}
    },
    {
        "title": "Carrot On A Stick",
        "type": shapeless,

        "1": {"m": FISHING_ROD, "id": "", "link": "C:FishingRod"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": CARROT_ITEM, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": CARROT_STICK, "id": "", "am": "1"}
    },
    {
        "title": "Pumpkin Pie",
        "type": shaped,

        "1": {"m": PUMPKIN, "id": "", "link": ""}, "2": {"m": SUGAR, "id": "", "link": "C:Sugar"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": EGG, "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": PUMPKIN_PIE, "id": "", "am": "1"}
    },
    {
        "title": "Redstone Comparator",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"}, "5": {"m": QUARTZ, "id": "", "link": ""}, "6": {"m": REDSTONE_TORCH_ON, "id": "", "link": "C:RedstoneTorch"},
        "7": {"m": STONE, "id": "", "link": "S:Stone"}, "8": {"m": STONE, "id": "", "link": "S:Stone"}, "9": {"m": STONE, "id": "", "link": "S:Stone"},

        "res": {"m": REDSTONE_COMPARATOR, "id": "", "am": "1"}
    },
    {
        "title": "Minecart With TNT",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": TNT, "id": "", "link": "C:TNT"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": EXPLOSIVE_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "Minecart With Hopper",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": HOPPER, "id": "", "link": "C:Hopper"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": MINECART, "id": "", "link": "C:Minecart"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": HOPPER_MINECART, "id": "", "am": "1"}
    },
    {
        "title": "Rabbit Stew",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": COOKED_RABBIT, "id": "", "link": "S:CookedRabbit"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": CARROT_ITEM, "id": "", "link": ""}, "5": {"m": BAKED_POTATO, "id": "", "link": "S:CookedPotato"}, "6": {"m": RED_MUSHROOM, "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": BOWL, "id": "", "link": "C:Bowl"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": RABBIT_STEW, "id": "", "am": "1"}
    },
    {
        "title": "Armor Stand",
        "type": fixed,

        "1": {"m": STICK, "id": "", "link": "C:Stick"}, "2": {"m": STICK, "id": "", "link": "C:Stick"}, "3": {"m": STICK, "id": "", "link": "C:Stick"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": STICK, "id": "", "link": "C:Stick"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": STEP, "id": "", "link": "C:StoneSlab"}, "9": {"m": STICK, "id": "", "link": "C:Stick"},

        "res": {"m": ARMOR_STAND, "id": "", "am": "1"}
    },
    {
        "title": "Lead",
        "type": shaped,

        "1": {"m": STRING, "id": "", "link": ""}, "2": {"m": STRING, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STRING, "id": "", "link": ""}, "5": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": STRING, "id": "", "link": ""},

        "res": {"m": LEASH, "id": "", "am": "1"}
    },
    {
        "title": "White Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "", "link": "C:Wool"}, "2": {"m": WOOL, "id": "", "link": "C:Wool"}, "3": {"m": WOOL, "id": "", "link": "C:Wool"},
        "4": {"m": WOOL, "id": "", "link": "C:Wool"}, "5": {"m": WOOL, "id": "", "link": "C:Wool"}, "6": {"m": WOOL, "id": "", "link": "C:Wool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "15", "am": "1"}
    },
    {
        "title": "Orange Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "2": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "3": {"m": WOOL, "id": "1", "link": "C:OrangeWool"},
        "4": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "5": {"m": WOOL, "id": "1", "link": "C:OrangeWool"}, "6": {"m": WOOL, "id": "1", "link": "C:OrangeWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "14", "am": "1"}
    },
    {
        "title": "Magenta Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "2": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "3": {"m": WOOL, "id": "2", "link": "C:MagentaWool"},
        "4": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "5": {"m": WOOL, "id": "2", "link": "C:MagentaWool"}, "6": {"m": WOOL, "id": "2", "link": "C:MagentaWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "13", "am": "1"}
    },
    {
        "title": "Light Blue Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "2": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "3": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"},
        "4": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "5": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"}, "6": {"m": WOOL, "id": "3", "link": "C:LightBlueWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "12", "am": "1"}
    },
    {
        "title": "Yellow Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "2": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "3": {"m": WOOL, "id": "4", "link": "C:YellowWool"},
        "4": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "5": {"m": WOOL, "id": "4", "link": "C:YellowWool"}, "6": {"m": WOOL, "id": "4", "link": "C:YellowWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "11", "am": "1"}
    },
    {
        "title": "Lime Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "2": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "3": {"m": WOOL, "id": "5", "link": "C:LimeWool"},
        "4": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "5": {"m": WOOL, "id": "5", "link": "C:LimeWool"}, "6": {"m": WOOL, "id": "5", "link": "C:LimeWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "10", "am": "1"}
    },
    {
        "title": "Pink Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "2": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "3": {"m": WOOL, "id": "6", "link": "C:PinkWool"},
        "4": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "5": {"m": WOOL, "id": "6", "link": "C:PinkWool"}, "6": {"m": WOOL, "id": "6", "link": "C:PinkWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "9", "am": "1"}
    },
    {
        "title": "Gray Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "2": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "3": {"m": WOOL, "id": "7", "link": "C:GrayWool"},
        "4": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "5": {"m": WOOL, "id": "7", "link": "C:GrayWool"}, "6": {"m": WOOL, "id": "7", "link": "C:GrayWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "8", "am": "1"}
    },
    {
        "title": "Light Gray Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "2": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "3": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"},
        "4": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "5": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"}, "6": {"m": WOOL, "id": "8", "link": "C:LightGrayWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "7", "am": "1"}
    },
    {
        "title": "Cyan Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "2": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "3": {"m": WOOL, "id": "9", "link": "C:CyanWool"},
        "4": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "5": {"m": WOOL, "id": "9", "link": "C:CyanWool"}, "6": {"m": WOOL, "id": "9", "link": "C:CyanWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "6", "am": "1"}
    },
    {
        "title": "Purple Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "2": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "3": {"m": WOOL, "id": "10", "link": "C:PurpleWool"},
        "4": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "5": {"m": WOOL, "id": "10", "link": "C:PurpleWool"}, "6": {"m": WOOL, "id": "10", "link": "C:PurpleWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "5", "am": "1"}
    },
    {
        "title": "Blue Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "2": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "3": {"m": WOOL, "id": "11", "link": "C:BlueWool"},
        "4": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "5": {"m": WOOL, "id": "11", "link": "C:BlueWool"}, "6": {"m": WOOL, "id": "11", "link": "C:BlueWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "4", "am": "1"}
    },
    {
        "title": "Brown Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "2": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "3": {"m": WOOL, "id": "12", "link": "C:BrownWool"},
        "4": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "5": {"m": WOOL, "id": "12", "link": "C:BrownWool"}, "6": {"m": WOOL, "id": "12", "link": "C:BrownWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "3", "am": "1"}
    },
    {
        "title": "Green Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "2": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "3": {"m": WOOL, "id": "13", "link": "C:GreenWool"},
        "4": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "5": {"m": WOOL, "id": "13", "link": "C:GreenWool"}, "6": {"m": WOOL, "id": "13", "link": "C:GreenWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "2", "am": "1"}
    },
    {
        "title": "Red Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "2": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "3": {"m": WOOL, "id": "14", "link": "C:RedWool"},
        "4": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "5": {"m": WOOL, "id": "14", "link": "C:RedWool"}, "6": {"m": WOOL, "id": "14", "link": "C:RedWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "1", "am": "1"}
    },
    {
        "title": "Black Banner",
        "type": shaped,

        "1": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "2": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "3": {"m": WOOL, "id": "15", "link": "C:BlackWool"},
        "4": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "5": {"m": WOOL, "id": "15", "link": "C:BlackWool"}, "6": {"m": WOOL, "id": "15", "link": "C:BlackWool"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": STICK, "id": "", "link": "C:Stick"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BANNER, "id": "", "am": "1"}
    },
    {
        "title": "Spruce Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "2": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "5": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "8": {"m": WOOD, "id": "1", "link": "C:SpruceWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SPRUCE_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "Birch Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "2": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "5": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "8": {"m": WOOD, "id": "2", "link": "C:BirchWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BIRCH_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "Jungle Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "2": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "5": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "8": {"m": WOOD, "id": "3", "link": "C:JungleWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": JUNGLE_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "Acacia Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "2": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "5": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "8": {"m": WOOD, "id": "4", "link": "C:AcaciaWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": ACACIA_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "Dark Oak Door",
        "type": shaped,

        "1": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "2": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "5": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "8": {"m": WOOD, "id": "5", "link": "C:DarkOakWoodPlanks"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DARK_OAK_DOOR_ITEM, "id": "", "am": "3"}
    },
    {
        "title": "Spawn Mooshroom",
        "type": fixed,

        "1": {"m": RED_MUSHROOM, "id": "96", "link": ""}, "2": {"m": RED_MUSHROOM, "id": "96", "link": ""}, "3": {"m": RED_MUSHROOM, "id": "96", "link": ""},
        "4": {"m": RED_MUSHROOM, "id": "96", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": RED_MUSHROOM, "id": "96", "link": ""},
        "7": {"m": RED_MUSHROOM, "id": "96", "link": ""}, "8": {"m": RED_MUSHROOM, "id": "96", "link": ""}, "9": {"m": RED_MUSHROOM, "id": "96", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "96", "am": "1"}
    },
    {
        "title": "Spawn Sheep",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "91", "am": "1"}
    },
    {
        "title": "Spawn Cow",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": LEATHER, "id": "", "link": "S:Leather"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": LEATHER, "id": "", "link": "S:Leather"},

        "res": {"m": MONSTER_EGG, "id": "92", "am": "1"}
    },
    {
        "title": "Spawn Chicken",
        "type": fixed,

        "1": {"m": FEATHER, "id": "", "link": ""}, "2": {"m": FEATHER, "id": "", "link": ""}, "3": {"m": FEATHER, "id": "", "link": ""},
        "4": {"m": FEATHER, "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": FEATHER, "id": "", "link": ""},
        "7": {"m": FEATHER, "id": "", "link": ""}, "8": {"m": FEATHER, "id": "", "link": ""}, "9": {"m": FEATHER, "id": "", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "93", "am": "1"}
    },
    {
        "title": "Spawn Slime",
        "type": fixed,

        "1": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "2": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "3": {"m": GRASS, "id": "", "link": "C:GrassBlock"},
        "4": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": GRASS, "id": "", "link": "C:Grass"},
        "7": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "8": {"m": GRASS, "id": "", "link": "C:GrassBlock"}, "9": {"m": GRASS, "id": "", "link": "C:GrassBlock"},

        "res": {"m": MONSTER_EGG, "id": "55", "am": "1"}
    },
    {
        "title": "Spawn Witch",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": POTION, "id": "", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "66", "am": "1"}
    },
    
    {
        "title": "Spawn Zombie Pigman",
        "type": fixed,

        "1": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "2": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "3": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "4": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},
        "7": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "8": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"}, "9": {"m": GOLD_NUGGET, "id": "", "link": "C:GoldNugget"},

        "res": {"m": MONSTER_EGG, "id": "57", "am": "1"}
    },
    {
        "title": "Spawn Zombie",
        "type": fixed,

        "1": {"m": ROTTEN_FLESH, "id": "", "link": ""}, "2": {"m": ROTTEN_FLESH, "id": "", "link": ""}, "3": {"m": ROTTEN_FLESH, "id": "", "link": ""},
        "4": {"m": ROTTEN_FLESH, "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": ROTTEN_FLESH, "id": "", "link": ""},
        "7": {"m": ROTTEN_FLESH, "id": "", "link": ""}, "8": {"m": ROTTEN_FLESH, "id": "", "link": ""}, "9": {"m": ROTTEN_FLESH, "id": "", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "54", "am": "1"}
    },
    {
        "title": "Spawn Skeleton",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "2": {"m": BONE, "id": "", "link": ""}, "3": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "4": {"m": BONE, "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": BONE, "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": BONE, "id": "", "link": ""}, "9": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},

        "res": {"m": MONSTER_EGG, "id": "51", "am": "1"}
    },
    {
        "title": "Spawn Spider",
        "type": fixed,

        "1": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "2": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "3": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "4": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "7": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": REDSTONE, "id": "", "link": "C:Redstone"},

        "res": {"m": MONSTER_EGG, "id": "52", "am": "1"}
    },
    {
        "title": "Spawn Cave Spider",
        "type": fixed,

        "1": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": REDSTONE, "id": "", "link": "C:Redstone"},

        "res": {"m": MONSTER_EGG, "id": "59", "am": "1"}
    },
    {
        "title": "Spawn Ghast",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "56", "am": "1"}
    },
    {
        "title": "Spawn Horse",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": SADDLE, "id": "", "link": "C:Saddle"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": SADDLE, "id": "", "link": "C:Saddle"},
        "7": {"m": LEATHER, "id": "", "link": "S:Leather"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": LEATHER, "id": "", "link": "S:Leather"},

        "res": {"m": MONSTER_EGG, "id": "100", "am": "1"}
    },
    {
        "title": "Spawn Wolf",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "95", "am": "1"}
    },
    {
        "title": "Spawn Magma Cube",
        "type": fixed,

        "1": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "2": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "3": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"},
        "4": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"},
        "7": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "8": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"}, "9": {"m": NETHERRACK, "id": "", "link": "C:Netherrack"},

        "res": {"m": MONSTER_EGG, "id": "62", "am": "1"}
    },
    {
        "title": "Spawn Guardian",
        "type": fixed,

        "1": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "2": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "3": {"m": SPONGE, "id": "", "link": "C:Sponge"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "8": {"m": SPONGE, "id": "", "link": "C:Sponge"}, "9": {"m": SPONGE, "id": "", "link": "C:Sponge"},

        "res": {"m": MONSTER_EGG, "id": "68", "am": "1"}
    },
    {
        "title": "Spawn Silverfish",
        "type": fixed,

        "1": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "2": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "3": {"m": GRAVEL, "id": "", "link": "G:Ore"},
        "4": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": GRAVEL, "id": "", "link": "G:Ore"},
        "7": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "8": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "9": {"m": GRAVEL, "id": "", "link": "G:Ore"},

        "res": {"m": MONSTER_EGG, "id": "60", "am": "1"}
    },
    {
        "title": "Spawn Enderman",
        "type": fixed,

        "1": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},

        "res": {"m": MONSTER_EGG, "id": "58", "am": "1"}
    },
    {
        "title": "Spawn Rabbit",
        "type": fixed,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": SAND, "id": "", "link": "G:Ore"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": SAND, "id": "", "link": "G:Ore"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": SAND, "id": "", "link": "G:Ore"},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": SAND, "id": "", "link": "G:Ore"}, "9": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},

        "res": {"m": MONSTER_EGG, "id": "101", "am": "1"}
    },
    {
        "title": "Spawn Creeper",
        "type": fixed,

        "1": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},

        "res": {"m": MONSTER_EGG, "id": "50", "am": "1"}
    },
    {
        "title": "Spawn Pig",
        "type": fixed,

        "1": {"m": DIRT, "id": "", "link": ""}, "2": {"m": DIRT, "id": "", "link": ""}, "3": {"m": DIRT, "id": "", "link": ""},
        "4": {"m": DIRT, "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": DIRT, "id": "", "link": ""},
        "7": {"m": DIRT, "id": "", "link": ""}, "8": {"m": DIRT, "id": "", "link": ""}, "9": {"m": DIRT, "id": "", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "90", "am": "1"}
    },
    {
        "title": "Spawn Villager",
        "type": fixed,

        "1": {"m": BONE, "id": "", "link": ""}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": BONE, "id": "", "link": ""},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": BONE, "id": "", "link": ""}, "8": {"m": LEATHER, "id": "", "link": "S:Leather"}, "9": {"m": BONE, "id": "", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "120", "am": "1"}
    },
    {
        "title": "Spawn Ocelot",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": RED_ROSE, "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": RED_ROSE, "id": "", "link": ""},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "98", "am": "1"}
    },
    {
        "title": "Spawn Endermite",
        "type": fixed,

        "1": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": ENDER_PEARL, "id": "", "link": "C:EnderPearl"},

        "res": {"m": MONSTER_EGG, "id": "67", "am": "1"}
    },
    {
        "title": "Spawn Bat",
        "type": fixed,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": FEATHER, "id": "", "link": ""}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": LEATHER, "id": "", "link": "S:Leather"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": FEATHER, "id": "", "link": ""}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": MONSTER_EGG, "id": "65", "am": "1"}
    },
    {
        "title": "Spawn Squid",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "2": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "3": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "4": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "9": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"},

        "res": {"m": MONSTER_EGG, "id": "94", "am": "1"}
    },
    {
        "title": "Spawn Blaze",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": ""}, "2": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "3": {"m": FLINT, "id": "", "link": ""},
        "4": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "5": {"m": EGG, "id": "", "link": ""}, "6": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"},
        "7": {"m": FLINT, "id": "", "link": ""}, "8": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "9": {"m": FLINT, "id": "", "link": ""},

        "res": {"m": MONSTER_EGG, "id": "61", "am": "1"}
    },
    {
        "title": "Tallgrass",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": LONG_GRASS, "id": "1", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": LONG_GRASS, "id": "1", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DOUBLE_PLANT, "id": "2", "am": "1"}
    },
    {
        "title": "Grass Block",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": LONG_GRASS, "id": "1", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": DIRT, "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": GRASS, "id": "", "am": "1"}
    },
    {
        "title": "Bone",
        "type": shaped,

        "1": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": INK_SACK, "id": "15", "link": "C:BoneMeal"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": BONE, "id": "", "am": "1"}
    },
    {
        "title": "Saddle",
        "type": shaped,

        "1": {"m": LEATHER, "id": "", "link": "S:Leather"}, "2": {"m": LEATHER, "id": "", "link": "S:Leather"}, "3": {"m": LEATHER, "id": "", "link": "S:Leather"},
        "4": {"m": STRING, "id": "", "link": "C:String"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": STRING, "id": "", "link": "C:String"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": IRON_INGOT, "id": "", "link": "C:IronIngot"},

        "res": {"m": SADDLE, "id": "", "am": "1"}
    },
    {
        "title": "Netherrack",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "5": {"m": COBBLESTONE, "id": "", "link": "G:Cobblestone"}, "6": {"m": REDSTONE, "id": "", "link": "C:Redstone"},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": REDSTONE, "id": "", "link": "C:Redstone"}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": NETHERRACK, "id": "", "am": "4"}
    },
    {
        "title": "Sponge",
        "type": shaped,

        "1": {"m": STRING, "id": "", "link": "C:String"}, "2": {"m": STRING, "id": "", "link": "C:String"}, "3": {"m": STRING, "id": "", "link": "C:String"},
        "4": {"m": STRING, "id": "", "link": "C:String"}, "5": {"m": STRING, "id": "", "link": "C:String"}, "6": {"m": STRING, "id": "", "link": "C:String"},
        "7": {"m": STRING, "id": "", "link": "C:String"}, "8": {"m": STRING, "id": "", "link": "C:String"}, "9": {"m": STRING, "id": "", "link": "C:String"},

        "res": {"m": SPONGE, "id": "", "am": "1"}
    },
    {
        "title": "Mycelium",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": DIRT, "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SAPLING, "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": MYCEL, "id": "", "am": "1"}
    },
    {
        "title": "Dead Bush",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": STICK, "id": "", "link": "C:Stick"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": STICK, "id": "", "link": "C:Stick"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DEAD_BUSH, "id": "", "am": "1"}
    },
    {
        "title": "Ender Pearl",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": POTION, "id": "", "link": ""}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": SLIME_BALL, "id": "", "link": "C:SlimeBall"}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": ENDER_PEARL, "id": "", "am": "1"}
    },
    {
        "title": "Water Bucket",
        "type": shaped,

        "1": {"m": LEAVES, "id": "", "link": ""}, "2": {"m": LEAVES, "id": "", "link": ""}, "3": {"m": LEAVES, "id": "", "link": ""},
        "4": {"m": LEAVES, "id": "", "link": ""}, "5": {"m": WATER_BUCKET, "id": "", "link": ""}, "6": {"m": LEAVES, "id": "", "link": ""},
        "7": {"m": LEAVES, "id": "", "link": ""}, "8": {"m": LEAVES, "id": "", "link": ""}, "9": {"m": LEAVES, "id": "", "link": ""},

        "res": {"m": WATER_BUCKET, "id": "", "am": "1"}
    },
    {
        "title": "Red Mushroom",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": MYCEL, "id": "", "link": "C:Mycelium"}, "5": {"m": "", "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": RED_MUSHROOM, "id": "", "am": "16"}
    },
    {
        "title": "Gunpowder",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": FLINT, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SULPHUR, "id": "", "am": "1"}
    },
    {
        "title": "Sapling",
        "type": shapeless,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": GRASS, "id": "", "link": "C:Grass"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": SAPLING, "id": "", "am": "1"}
    },
    {
        "title": "Dirt",
        "type": shaped,

        "1": {"m": LEAVES, "id": "", "link": ""}, "2": {"m": LEAVES, "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": LEAVES, "id": "", "link": ""}, "5": {"m": LEAVES, "id": "", "link": ""}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": DIRT, "id": "", "am": "1"}
    },
    {
        "title": "1x Compress Flint",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:Flint"}, "2": {"m": FLINT, "id": "", "link": "C:Flint"}, "3": {"m": FLINT, "id": "", "link": "C:Flint"},
        "4": {"m": FLINT, "id": "", "link": "C:Flint"}, "5": {"m": FLINT, "id": "", "link": "C:Flint"}, "6": {"m": FLINT, "id": "", "link": "C:Flint"},
        "7": {"m": FLINT, "id": "", "link": "C:Flint"}, "8": {"m": FLINT, "id": "", "link": "C:Flint"}, "9": {"m": FLINT, "id": "", "link": "C:Flint"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
    {
        "title": "2x Compress Flint",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "2": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "3": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"},
        "4": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "5": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "6": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"},
        "7": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "8": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"}, "9": {"m": FLINT, "id": "", "link": "C:1xCompressFlint"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
    {
        "title": "3x Compress Flint",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "2": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "3": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"},
        "4": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "5": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "6": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"},
        "7": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "8": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"}, "9": {"m": FLINT, "id": "", "link": "C:2xCompressFlint"},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
    {
        "title": "Flint Singularity",
        "type": fixed,

        "1": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "2": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "3": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"},
        "4": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "5": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "6": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"},
        "7": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "8": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"}, "9": {"m": FLINT, "id": "", "link": "C:3xCompressFlint"},

        "res": {"m": FLINT, "id": "", "am": "1", "e": True}
    },
        {
        "title": "1x Compress Diamond",
        "type": fixed,

        "1": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "2": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "3": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"},
        "4": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "5": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "6": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"},
        "7": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "8": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"}, "9": {"m": DIAMOND_BLOCK, "id": "", "link": "C:BlockOfDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1"}
    },
    {
        "title": "2x Compress Diamond",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:1xCompressDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1"}
    },
    {
        "title": "3x Compress Diamond",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:2xCompressDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1"}
    },
    {
        "title": "Diamond Singularity",
        "type": fixed,

        "1": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "2": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "3": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"},
        "4": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "5": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "6": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"},
        "7": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "8": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"}, "9": {"m": DIAMOND, "id": "", "link": "C:3xCompressDiamond"},

        "res": {"m": DIAMOND, "id": "", "am": "1", "e": True}
    },
        {
        "title": "1x Compress Emerald",
        "type": fixed,

        "1": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "2": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "3": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"},
        "4": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "5": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "6": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"},
        "7": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "8": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"}, "9": {"m": EMERALD_BLOCK, "id": "", "link": "C:BlockOfEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1"}
    },
    {
        "title": "2x Compress Emerald",
        "type": fixed,

        "1": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "2": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "3": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"},
        "4": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "5": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "6": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"},
        "7": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "8": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"}, "9": {"m": EMERALD, "id": "", "link": "C:1xCompressEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1"}
    },
    {
        "title": "3x Compress Emerald",
        "type": fixed,

        "1": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "2": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "3": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"},
        "4": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "5": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "6": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"},
        "7": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "8": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"}, "9": {"m": EMERALD, "id": "", "link": "C:2xCompressEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1"}
    },
    {
        "title": "Emerald Singularity",
        "type": fixed,

        "1": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "2": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "3": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"},
        "4": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "5": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "6": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"},
        "7": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "8": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"}, "9": {"m": EMERALD, "id": "", "link": "C:3xCompressEmerald"},

        "res": {"m": EMERALD, "id": "", "am": "1", "e": True}
    },
        {
        "title": "1x Compress Gold",
        "type": fixed,

        "1": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "2": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "3": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "4": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "5": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "6": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},
        "7": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "8": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"}, "9": {"m": GOLD_BLOCK, "id": "", "link": "C:BlockOfGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "2x Compress Gold",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:1xCompressGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "3x Compress Gold",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:2xCompressGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "Gold Singularity",
        "type": fixed,

        "1": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "2": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "3": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"},
        "4": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "5": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "6": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"},
        "7": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "8": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"}, "9": {"m": GOLD_INGOT, "id": "", "link": "C:3xCompressGold"},

        "res": {"m": GOLD_INGOT, "id": "", "am": "1", "e": True}
    },
        {
        "title": "1x Compress Iron",
        "type": fixed,

        "1": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "2": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "3": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"},
        "4": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "5": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "6": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"},
        "7": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "8": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"}, "9": {"m": IRON_BLOCK, "id": "", "link": "C:BlockOfIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "2x Compress Iron",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:1xCompressIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "3x Compress Iron",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:2xCompressIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1"}
    },
    {
        "title": "Iron Singularity",
        "type": fixed,

        "1": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "2": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "3": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"},
        "4": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "5": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "6": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"},
        "7": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "8": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"}, "9": {"m": IRON_INGOT, "id": "", "link": "C:3xCompressIron"},

        "res": {"m": IRON_INGOT, "id": "", "am": "1", "e": True}
    },
        {
        "title": "1x Compress Lapis Lazuli",
        "type": fixed,

        "1": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "2": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "3": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"},
        "4": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "5": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "6": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"},
        "7": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "8": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"}, "9": {"m": LAPIS_BLOCK, "id": "", "link": "C:LapisLazuliBlock"},

        "res": {"m": INK_SACK, "id": "4", "am": "1"}
    },
    {
        "title": "2x Compress Lapis Lazuli",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:1xCompressLapisLazuli"},

        "res": {"m": INK_SACK, "id": "4", "am": "1"}
    },
    {
        "title": "3x Compress Lapis Lazuli",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:2xCompressLapisLazuli"},

        "res": {"m": INK_SACK, "id": "4", "am": "1"}
    },
    {
        "title": "Lapis Lazuli Singularity",
        "type": fixed,

        "1": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "2": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "3": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"},
        "4": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "5": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "6": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"},
        "7": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "8": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"}, "9": {"m": INK_SACK, "id": "4", "link": "C:3xCompressLapisLazuli"},

        "res": {"m": INK_SACK, "id": "4", "am": "1", "e": True}
    },
        {
        "title": "1x Compress Coal",
        "type": fixed,

        "1": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "2": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "3": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"},
        "4": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "5": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "6": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"},
        "7": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "8": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"}, "9": {"m": COAL_BLOCK, "id": "", "link": "C:BlockOfCoal"},

        "res": {"m": COAL, "id": "", "am": "1"}
    },
    {
        "title": "2x Compress Coal",
        "type": fixed,

        "1": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "2": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "3": {"m": COAL, "id": "", "link": "C:1xCompressCoal"},
        "4": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "5": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "6": {"m": COAL, "id": "", "link": "C:1xCompressCoal"},
        "7": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "8": {"m": COAL, "id": "", "link": "C:1xCompressCoal"}, "9": {"m": COAL, "id": "", "link": "C:1xCompressCoal"},

        "res": {"m": COAL, "id": "", "am": "1"}
    },
    {
        "title": "3x Compress Coal",
        "type": fixed,

        "1": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "2": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "3": {"m": COAL, "id": "", "link": "C:2xCompressCoal"},
        "4": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "5": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "6": {"m": COAL, "id": "", "link": "C:2xCompressCoal"},
        "7": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "8": {"m": COAL, "id": "", "link": "C:2xCompressCoal"}, "9": {"m": COAL, "id": "", "link": "C:2xCompressCoal"},

        "res": {"m": COAL, "id": "", "am": "1"}
    },
    {
        "title": "Coal Singularity",
        "type": fixed,

        "1": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "2": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "3": {"m": COAL, "id": "", "link": "C:3xCompressCoal"},
        "4": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "5": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "6": {"m": COAL, "id": "", "link": "C:3xCompressCoal"},
        "7": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "8": {"m": COAL, "id": "", "link": "C:3xCompressCoal"}, "9": {"m": COAL, "id": "", "link": "C:3xCompressCoal"},

        "res": {"m": COAL, "id": "", "am": "1", "e": True}
    },
    {
        "title": "Flint",
        "type": shaped,

        "1": {"m": "", "id": "", "link": ""}, "2": {"m": "", "id": "", "link": ""}, "3": {"m": "", "id": "", "link": ""},
        "4": {"m": "", "id": "", "link": ""}, "5": {"m": GRAVEL, "id": "", "link": "G:Ore"}, "6": {"m": "", "id": "", "link": ""},
        "7": {"m": "", "id": "", "link": ""}, "8": {"m": "", "id": "", "link": ""}, "9": {"m": "", "id": "", "link": ""},

        "res": {"m": FLINT, "id": "", "am": "1"}
    },
]

tempRecipePanels = {"panels": {}}


def itemMaker(itemObject, key):
    matt = itemObject["m"]
    iddd = itemObject["id"]
    link = itemObject["link"]
    ench = itemObject.get("e")

    slot = key+9

    if key > 3:
        slot += 6
    if key > 6:
        slot += 6

    items = {
        f"{slot}": {
            "material": matt,
        }
    }

    if iddd:
        items[f"{slot}"].update({"ID": str(iddd)})
    if link:
        items[f"{slot}"].update({"commands": [f"open= {link}"]})
        items[f"{slot}"].update({"lore": ["&eClick to view recipe"]})

    if ench:
        items[f"{slot}"].update({"enchanted": [bool(ench)]})

    return items


def resMaker(itemObj):
    matt = itemObj["m"]
    iddd = itemObj["id"]
    amou = itemObj["am"]

    tempRes = {
        "24": {
            "material": matt,
        }
    }

    if iddd:
        tempRes["24"].update({"ID": str(iddd)})

    if amou:
        tempRes["24"].update({"stack": int(amou)})

    return tempRes

def bookItemMaker(itemObj, slot, title):
    matt = itemObj["m"]
    iddd = itemObj["id"]
    amou = itemObj["am"]
    ench = itemObj.get("e")
    titl = ""

    for titless in title.split():
        titl += titless

    tempRes = {
        f"{slot}": {
            "material": matt,
            "name": f"&r{title}",
            "commands": [f"open= C:{titl}"]
        }
    }

    if iddd:
        tempRes[f"{slot}"].update({"ID": str(iddd)})

    if amou:
        tempRes[f"{slot}"].update({"stack": int(amou)})

    if ench:
        tempRes[f"{slot}"].update({"enchanted": [bool(ench)]})

    return tempRes

# book maker

cutRecipe = []

tempBookPanels = {"panels": {}}

for i in range(0, len(craftingRecipes), 16):
    cutRecipe.append(craftingRecipes[i : i + 16])

with open("panels/crafting-recipes.yml", "wt") as fl:
    with open("panels/crafting-recipe-book.yml", "wt") as fll:
        for craftingIndex in range(len(cutRecipe)):
            items = cutRecipe[craftingIndex]
            pageNumber = craftingIndex + 1
            tempBookItem = {}
            tempBookPage = {
                f"crafting_recipe_book{pageNumber}": {
                    "title": f"&4&lCrafting Recipe Book &r&0{pageNumber}",
                    "rows": "6",
                    "item": {
                        "0": {
                            "material": FEATHER,
                            "name": "&b&l< Back",
                            "commands": ["open= item_info_book"]
                        },
                        "1": {
                            "material": STAINED_GLASS_PANE,
                            "ID": "15",
                            "name": "&f",
                            "duplicate": "2-7,9,17,18,26,27,35,36,44,45-47,49,51-53",
                        },
                        "8": {
                            "material": BARRIER,
                            "name": "&c&lClose",
                            "commands": ["cpc"],
                        },
                        "48": {
                            "material": GLOWSTONE_DUST,
                            "name": "&6&l< Previous page",
                            "commands": [
                                f"open= crafting_recipe_book{pageNumber-1}"
                            ]
                        },
                        "50": {
                            "material": REDSTONE,
                            "name": "&a&lNext page >",
                            "commands": [
                                f"open= crafting_recipe_book{pageNumber+1}"
                            ]
                        }
                    },
                }
            }

            for itemsIndex in range(len(items)):
                item = items[itemsIndex]

                slot = itemsIndex + 10

                if itemsIndex > 0:
                    slot += 1
                if itemsIndex > 1:
                    slot += 1
                if itemsIndex > 2:
                    slot += 1
                if itemsIndex > 3:
                    slot += 2
                if itemsIndex > 4:
                    slot += 1
                if itemsIndex > 5:
                    slot += 1
                if itemsIndex > 6:
                    slot += 1
                if itemsIndex > 7:
                    slot += 2
                if itemsIndex > 8:
                    slot += 1
                if itemsIndex > 9:
                    slot += 1
                if itemsIndex > 10:
                    slot += 1
                if itemsIndex > 11:
                    slot += 2
                if itemsIndex > 12:
                    slot += 1
                if itemsIndex > 13:
                    slot += 1
                if itemsIndex > 14:
                    slot += 1

                tempBookItem.update(bookItemMaker(item["res"], slot, item["title"]))

            tempBookPage[f"crafting_recipe_book{pageNumber}"]["item"].update(tempBookItem)
            tempBookPanels["panels"].update(tempBookPage)

            for recipeIndex in range(len(items)):
                craft = items[recipeIndex]
                recipeTitle = craft["title"]
                recipeType = craft["type"]

                tempItem = {}

                if recipeTitle == "":
                    print(f"ERROR: {recipeTitle} == ''")

                if recipeType == "":
                    print(f"ERROR: {recipeTitle} > {recipeType} == ''")

                recipe1 = craft["1"]
                if recipe1["m"] != "":
                    tempItem.update(itemMaker(recipe1, 1))

                recipe2 = craft["2"]
                if recipe2["m"] != "":
                    tempItem.update(itemMaker(recipe2, 2))

                recipe3 = craft["3"]
                if recipe3["m"] != "":
                    tempItem.update(itemMaker(recipe3, 3))

                recipe4 = craft["4"]
                if recipe4["m"] != "":
                    tempItem.update(itemMaker(recipe4, 4))

                recipe5 = craft["5"]
                if recipe5["m"] != "":
                    tempItem.update(itemMaker(recipe5, 5))

                recipe6 = craft["6"]
                if recipe6["m"] != "":
                    tempItem.update(itemMaker(recipe6, 6))

                recipe7 = craft["7"]
                if recipe7["m"] != "":
                    tempItem.update(itemMaker(recipe7, 7))

                recipe8 = craft["8"]
                if recipe8["m"] != "":
                    tempItem.update(itemMaker(recipe8, 8))

                recipe9 = craft["9"]
                if recipe9["m"] != "":
                    tempItem.update(itemMaker(recipe9, 9))

                recipeRes = craft["res"]

                tempTitle = ""

                for titless in recipeTitle.split():
                    tempTitle += titless

                craftingId = f"C:{tempTitle}"

                tempPage = {
                    craftingId: {
                        "title": f"&0&l>> &r{recipeTitle}",
                        "rows": "6",
                        "item": {
                            "0": {
                                "material": FEATHER,
                                "name": "&b&l< Back",
                                "commands": [f"open= crafting_recipe_book{pageNumber}"]
                            },
                            "1": {
                                "material": STAINED_GLASS_PANE,
                                "ID": "15",
                                "name": "&f",
                                "duplicate": "2-7,9,13,17,18,26,27,31,35,36-44",
                            },
                            "8": {
                                "material": BARRIER,
                                "name": "&c&lClose",
                                "commands": ["cpc"],
                            },
                            "22": {
                                "material": WEB,
                                "name": recipeType,
                                "enchanted": [True]
                            },
                            "14": {
                                "material": STAINED_GLASS_PANE,
                                "name": "&f",
                                "duplicate": "15-16,23,25,32-34",
                            },
                            "45": {
                                "material": WORKBENCH,
                                "name": "&6Crafting"
                            }
                        },
                    }
                }

                # 45++   #46++     #47++
                # craft  #furnace  #Shop

                tempPage[craftingId]["item"].update(tempItem)
                tempPage[craftingId]["item"].update(resMaker(recipeRes))

                tempRecipePanels["panels"].update(tempPage)

        fl.write(yml.dump(data=tempRecipePanels, sort_keys=False, allow_unicode=True))
        fll.write(yml.dump(data=tempBookPanels, sort_keys=False, allow_unicode=True))