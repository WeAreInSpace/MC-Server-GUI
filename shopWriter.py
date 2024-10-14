from m import *
import yaml as yml
import json

u = ""

shop_name = "David's flowers shop"
shop_id = "DevidFlowersShop"

shop_warning_messages = '''No Warranty. Read https://www.weareinspace.net/docs/warranty'''
shop_warning_message = ''''''

arr = [
    {
        "name": "Dandelion", "m": YELLOW_FLOWER, "id": "", "price": 16
    },
    {
        "name": "Poppy", "m": RED_ROSE, "id": "", "price": 16
    },
    {
        "name": "Blue Orchid", "m": RED_ROSE, "id": "1", "price": 16
    },
    {
        "name": "Allium", "m": RED_ROSE, "id": "2", "price": 16
    },
    {
        "name": "Azure Bluet", "m": RED_ROSE, "id": "3", "price": 16
    },
    {
        "name": "Red Tulip", "m": RED_ROSE, "id": "4", "price": 16
    },
    {
        "name": "Orange Tulip", "m": RED_ROSE, "id": "5", "price": 16
    },
    {
        "name": "White Tulip", "m": RED_ROSE, "id": "6", "price": 16
    },
    {
        "name": "Pink Tulip", "m": RED_ROSE, "id": "7", "price": 16
    },
    {
        "name": "Oxeye Daisy", "m": RED_ROSE, "id": "8", "price": 16
    },
    {
        "name": "Oak Sapling", "m": SAPLING, "id": "", "price": 16
    },
    {
        "name": "Spruce Sapling", "m": SAPLING, "id": "1", "price": 16
    },
    {
        "name": "Birch Sapling", "m": SAPLING, "id": "2", "price": 16
    },
    {
        "name": "Jungle Sapling", "m": SAPLING, "id": "3", "price": 16
    },
    {
        "name": "Acacia Sapling", "m": SAPLING, "id": "4", "price": 16
    },
    {
        "name": "Dark Oak Sapling", "m": SAPLING, "id": "5", "price": 16
    }
]

print(len(arr))

ca = []

temp_page = []

temp_panels = {}

for i in range(0, len(arr), 28):
    ca.append(arr[i:i+28])

for isw in range(len(ca)):
    new_arr = ca[isw]
    panelsss = {
        f"B:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&2&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }
    panelsss16 = {
        f"B16:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&2&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }
    panelsss32 = {
        f"B32:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&2&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }
    panelsss64 = {
        f"B64:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&2&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }

    sell_panelsss = {
        f"S:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&4&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }
    sell_panelsss16 = {
        f"S16:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&4&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }
    sell_panelsss32 = {
        f"S32:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&4&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }
    sell_panelsss64 = {
        f"S64:{shop_id}{isw+1}": {
            "rows": '6',
            "title": f'&4&l{shop_name} &r&0{isw+1}',
            "empty": AIR,
            "item": {},
            "custom-item": {}
        }
    }

    for ddd in range(len(new_arr)):
        items_arr = new_arr[ddd]

        temp_name = items_arr["name"]
        temp_m = items_arr["m"]
        temp_id = items_arr["id"]
        temp_p = items_arr["price"]

        if ddd+10 >= 17:
            ddd += 2
        elif ddd+10 >= 18:
            ddd += 1

        if ddd+10 >= 26:
            ddd += 2
        elif ddd+10 >= 27:
            ddd += 1

        if ddd+10 >= 35:
            ddd += 2
        elif ddd+10 >= 36:
            ddd += 1

        print(ddd+10)

        buy_lore = [
            "",
            "  &a&lBuy",
            f"  &aAmount: 1  ",
            f"  &ePrice: {temp_p}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        buy_lore16 = [
            "",
            "  &a&lBuy",
            f"  &aAmount: 16  ",
            f"  &ePrice: {(temp_p*16.0) - ((temp_p*16.0)*(10/100))}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        buy_lore32 = [
            "",
            "  &a&lBuy",
            f"  &aAmount: 32  ",
            f"  &ePrice: {(temp_p*32.0) - ((temp_p*32.0)*(10/100))}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        buy_lore64 = [
            "",
            "  &a&lBuy",
            f"  &aAmount: 64  ",
            f"  &ePrice: {(temp_p*64.0) - ((temp_p*64.0)*(10/100))}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        sell_lore = [
            "",
            "  &a&lSell",
            f"  &aAmount: 1  ",
            f"  &ePrice: {temp_p}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        sell_lore16 = [
            "",
            "  &a&lSell"
            f"  &aAmount: 16  ",
            f"  &ePrice: {(temp_p*16) + ((temp_p*16)*(10/100))}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        sell_lore32 = [
            "",
            "  &a&lSell",
            f"  &aAmount: 32  ",
            f"  &ePrice: {(temp_p*32) + ((temp_p*32)*(10/100))}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        sell_lore64 = [
            "",
            "  &a&lSell",
            f"  &aAmount: 64  ",
            f"  &ePrice: {(temp_p*64) + ((temp_p*64)*(10/100))}  ",
            f"  &7{shop_warning_message}  ",
            "",
        ]

        if temp_id == "":
            temp_id = "0"

        buy_temp_custom_item_data = {
            f"custom_{temp_m}:{temp_id}*{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
            }
        }

        buy_temp_item_data = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"paywall= {temp_p}",
                    f"give-item= custom_{temp_m}:{temp_id}*{ddd+10} 1"
                ],
                "name": f"&r{temp_name}",
                "lore": buy_lore
            }
        }

        buy_temp_item_data16 = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"paywall= {(temp_p*16.0) - ((temp_p*16.0)*(10/100))}",
                    f"give-item= custom_{temp_m}:{temp_id}*{ddd+10} 16"
                ],
                "name": f"&r{temp_name}",
                "lore": buy_lore16
            }
        }
        buy_temp_item_data32 = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"paywall= {(temp_p*32) - ((temp_p*32)*(10/100))}",
                    f"give-item= custom_{temp_m}:{temp_id}*{ddd+10} 32"
                ],
                "name": f"&r{temp_name}",
                "lore": buy_lore32
            }
        }
        buy_temp_item_data64 = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"paywall= {(temp_p*64) - ((temp_p*64)*(10/100))}",
                    f"give-item= custom_{temp_m}:{temp_id}*{ddd+10} 64"
                ],
                "name": f"&r{temp_name}",
                "lore": buy_lore64
            }
        }

        sell_temp_item_data = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"item-paywall= custom_{temp_m}:{temp_id}*{ddd+10} 1",
                    f"eeconomy give %cp-player-name% {temp_p}"
                ],
                "name": f"&r{temp_name}",
                "lore": sell_lore
            }
        }
        sell_temp_item_data16 = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"item-paywall= custom_{temp_m}:{temp_id}*{ddd+10} 16",
                    f"eeconomy give %cp-player-name% {(temp_p*16) + ((temp_p*16)*(10/100))}"
                ],
                "name": f"&r{temp_name}",
                "lore": sell_lore16
            }
        }
        sell_temp_item_data32 = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"item-paywall= custom_{temp_m}:{temp_id}*{ddd+10} 32",
                    f"eeconomy give %cp-player-name% {(temp_p*32) + ((temp_p*32)*(10/100))}"
                ],
                "name": f"&r{temp_name}",
                "lore": sell_lore32
            }
        }
        sell_temp_item_data64 = {
            f"{ddd+10}": {
                "material": temp_m,
                "ID": int(temp_id),
                "commands": [
                    f"item-paywall= custom_{temp_m}:{temp_id}*{ddd+10} 64",
                    f"eeconomy give %cp-player-name% {(temp_p*64) + ((temp_p*64)*(10/100))}"
                ],
                "name": f"&r{temp_name}",
                "lore": sell_lore64
            },
        }

        panelsss[f"B:{shop_id}{isw+1}"]["item"].update(buy_temp_item_data)
        panelsss16[f"B16:{shop_id}{isw+1}"]["item"].update(buy_temp_item_data16)
        panelsss32[f"B32:{shop_id}{isw+1}"]["item"].update(buy_temp_item_data32)
        panelsss64[f"B64:{shop_id}{isw+1}"]["item"].update(buy_temp_item_data64)

        panelsss[f"B:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)
        panelsss16[f"B16:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)
        panelsss32[f"B32:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)
        panelsss64[f"B64:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)

        sell_panelsss[f"S:{shop_id}{isw+1}"]["item"].update(sell_temp_item_data)
        sell_panelsss16[f"S16:{shop_id}{isw+1}"]["item"].update(sell_temp_item_data16)
        sell_panelsss32[f"S32:{shop_id}{isw+1}"]["item"].update(sell_temp_item_data32)
        sell_panelsss64[f"S64:{shop_id}{isw+1}"]["item"].update(sell_temp_item_data64)

        sell_panelsss[f"S:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)
        sell_panelsss16[f"S16:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)
        sell_panelsss32[f"S32:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)
        sell_panelsss64[f"S64:{shop_id}{isw+1}"]["custom-item"].update(buy_temp_custom_item_data)

    buy_panels_price_selector = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= B16:{shop_id}{isw+1}",
                f"right= open= B64:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&a> &lPrice &r1  ",
                "  &r&lPrice &r16  ",
                "  &r&lPrice &r32  ",
                "  &r&lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    buy_panels_price_selector16 = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= B32:{shop_id}{isw+1}",
                f"right= open= B:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lPrice &r1  ",
                "  &r&a> &lPrice &r16  ",
                "  &r&lPrice &r32  ",
                "  &r&lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    buy_panels_price_selector32 = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= B64:{shop_id}{isw+1}",
                f"right= open= B16:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lPrice &r1  ",
                "  &r&lPrice &r16  ",
                "  &r&a> &lPrice &r32  ",
                "  &r&lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    buy_panels_price_selector64 = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= B:{shop_id}{isw+1}",
                f"right= open= B32:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lPrice &r1  ",
                "  &r&lPrice &r16  ",
                "  &r&lPrice &r32  ",
                "  &r&a> &lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_price_selector = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= S16:{shop_id}{isw+1}",
                f"right= open= S64:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&a> &lPrice &r1  ",
                "  &r&lPrice &r16  ",
                "  &r&lPrice &r32  ",
                "  &r&lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_price_selector16 = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= S32:{shop_id}{isw+1}",
                f"right= open= S:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lPrice &r1  ",
                "  &r&a> &lPrice &r16  ",
                "  &r&lPrice &r32  ",
                "  &r&lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_price_selector32 = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= S64:{shop_id}{isw+1}",
                f"right= open= S16:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lPrice &r1  ",
                "  &r&lPrice &r16  ",
                "  &r&a> &lPrice &r32  ",
                "  &r&lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_price_selector64 = {
        "5": {
            "material": GLOWSTONE,
            "commands": [
                f"left= open= S:{shop_id}{isw+1}",
                f"right= open= S32:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lPrice &r1  ",
                "  &r&lPrice &r16  ",
                "  &r&lPrice &r32  ",
                "  &r&a> &lPrice &r64  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    #------------------------------------------
    buy_panels_mode_selector = {
        "3": {
            "material": GLOWSTONE_DUST,
            "commands": [
                f"open= S:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&a> &lMode &rbuy  ",
                "  &r&lMode &rSell  ",
                "",
                "  &r&lPrice &r1  ",
                "",
            ]
        }
    }
    buy_panels_mode_selector16 = {
        "3": {
            "material": GLOWSTONE_DUST,
            "commands": [
                f"open= S16:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&a> &lMode &rbuy  ",
                "  &r&lMode &rSell  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    buy_panels_mode_selector32 = {
        "3": {
            "material": GLOWSTONE_DUST,
            "commands": [
                f"open= S32:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&a> &lMode &rbuy  ",
                "  &r&lMode &rSell  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    buy_panels_mode_selector64 = {
        "3": {
            "material": GLOWSTONE_DUST,
            "commands": [
                f"open= S64:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&a> &lMode &rbuy  ",
                "  &r&lMode &rSell  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_mode_selector = {
        "3": {
            "material": REDSTONE,
            "commands": [
                f"open= B:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lMode &rbuy  ",
                "  &r&a> &lMode &rSell  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_mode_selector16 = {
        "3": {
            "material": REDSTONE,
            "commands": [
                f"open= B16:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lMode &rbuy  ",
                "  &r&a> &lMode &rSell  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_mode_selector32 = {
        "3": {
            "material": REDSTONE,
            "commands": [
                f"open= B32:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lMode &rbuy  ",
                "  &r&a> &lMode &rSell  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    sell_panels_mode_selector64 = {
        "3": {
            "material": REDSTONE,
            "commands": [
                f"open= B64:{shop_id}{isw+1}"
            ],
            "lore": [
                "",
                "  &r&lMode &rbuy  ",
                "  &r&a> &lMode &rSell  ",
                "",
                "  &r&e˄ Right click  ",
                "  &r&e˅ Left click  ",
                ""
            ]
        }
    }
    
    panels_selector_button = {
        "8": {
            "material": BARRIER,
            "commands": [
                "cpc"
            ],
            "name": "&c&lClose"
        }
    }
    panels_frame = {
        "0": {
            "material": STAINED_GLASS_PANE,
            "ID": 15,
            "name": "&f",
            "duplicate": "1-2,4,6-7,9,17-18,26-27,35-36,44-47,49,51"
        }
    }

    panelsss[f"B:{shop_id}{isw+1}"]["item"].update(buy_panels_mode_selector)
    panelsss[f"B:{shop_id}{isw+1}"]["item"].update(buy_panels_price_selector)
    panelsss[f"B:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    panelsss[f"B:{shop_id}{isw+1}"]["item"].update(panels_frame)

    panelsss16[f"B16:{shop_id}{isw+1}"]["item"].update(buy_panels_mode_selector16)
    panelsss16[f"B16:{shop_id}{isw+1}"]["item"].update(buy_panels_price_selector16)
    panelsss16[f"B16:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    panelsss16[f"B16:{shop_id}{isw+1}"]["item"].update(panels_frame)

    panelsss32[f"B32:{shop_id}{isw+1}"]["item"].update(buy_panels_mode_selector32)
    panelsss32[f"B32:{shop_id}{isw+1}"]["item"].update(buy_panels_price_selector32)
    panelsss32[f"B32:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    panelsss32[f"B32:{shop_id}{isw+1}"]["item"].update(panels_frame)

    panelsss64[f"B64:{shop_id}{isw+1}"]["item"].update(buy_panels_mode_selector64)
    panelsss64[f"B64:{shop_id}{isw+1}"]["item"].update(buy_panels_price_selector64)
    panelsss64[f"B64:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    panelsss64[f"B64:{shop_id}{isw+1}"]["item"].update(panels_frame)

    #---------------------------

    sell_panelsss[f"S:{shop_id}{isw+1}"]["item"].update(sell_panels_mode_selector)
    sell_panelsss[f"S:{shop_id}{isw+1}"]["item"].update(sell_panels_price_selector)
    sell_panelsss[f"S:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    sell_panelsss[f"S:{shop_id}{isw+1}"]["item"].update(panels_frame)

    sell_panelsss16[f"S16:{shop_id}{isw+1}"]["item"].update(sell_panels_mode_selector16)
    sell_panelsss16[f"S16:{shop_id}{isw+1}"]["item"].update(sell_panels_price_selector16)
    sell_panelsss16[f"S16:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    sell_panelsss16[f"S16:{shop_id}{isw+1}"]["item"].update(panels_frame)

    sell_panelsss32[f"S32:{shop_id}{isw+1}"]["item"].update(sell_panels_mode_selector32)
    sell_panelsss32[f"S32:{shop_id}{isw+1}"]["item"].update(sell_panels_price_selector32)
    sell_panelsss32[f"S32:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    sell_panelsss32[f"S32:{shop_id}{isw+1}"]["item"].update(panels_frame)

    sell_panelsss64[f"S64:{shop_id}{isw+1}"]["item"].update(sell_panels_mode_selector64)
    sell_panelsss64[f"S64:{shop_id}{isw+1}"]["item"].update(sell_panels_price_selector64)
    sell_panelsss64[f"S64:{shop_id}{isw+1}"]["item"].update(panels_selector_button)
    sell_panelsss64[f"S64:{shop_id}{isw+1}"]["item"].update(panels_frame)

    temp_panels.update(panelsss)
    temp_panels.update(panelsss16)
    temp_panels.update(panelsss32)
    temp_panels.update(panelsss64)

    temp_panels.update(sell_panelsss)
    temp_panels.update(sell_panelsss16)
    temp_panels.update(sell_panelsss32)
    temp_panels.update(sell_panelsss64)
    
#paywall= give-item= W if have id

a = {
    "panels": temp_panels
}



yass = json.dumps(a)

adf = json.loads(yass)

mc = yml.dump(
    data=adf,
    sort_keys=False
)

with open("panels/flowers-shop.yml","wt") as file:
    file.write(mc)

with open("flowers-shop.json","wt") as file:
    file.write(yass)