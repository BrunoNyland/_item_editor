

ITEM_SOCKET_REMAIN_SEC = 0

ITEM_NAME_MAX_LEN = 50
ITEM_NAME_MAX_LEN = 24
ITEM_VALUES_MAX_NUM = 6
ITEM_LIMIT_MAX_NUM = 2
ITEM_APPLY_MAX_NUM = 3
ITEM_SOCKET_MAX_NUM = 6
ITEM_ATTRIBUTE_MAX_NUM = 7
ITEM_ATTRIBUTE_MAX_LEVEL = 5
REFINE_MATERIAL_MAX_NUM = 5
ITEM_ELK_VNUM = 50026


ITEM_VALUE_CHARGING_AMOUNT_IDX = 0
ITEM_SOCKET_CHARGING_AMOUNT_IDX = 2


ITEM_SOCKET_UNIQUE_SAVE_TIME = ITEM_SOCKET_MAX_NUM - 2
ITEM_SOCKET_UNIQUE_REMAIN_TIME = ITEM_SOCKET_MAX_NUM - 1

class Types(list):
    ITEM_NONE = 0
    ITEM_WEAPON = 1
    ITEM_ARMOR = 2
    ITEM_USE = 3
    ITEM_AUTOUSE = 4
    ITEM_MATERIAL = 5
    ITEM_SPECIAL = 6
    ITEM_TOOL = 7
    ITEM_LOTTERY = 8
    ITEM_ELK = 9
    ITEM_METIN = 10
    ITEM_CONTAINER = 11
    ITEM_FISH = 12
    ITEM_ROD = 13
    ITEM_RESOURCE = 14
    ITEM_CAMPFIRE = 15
    ITEM_UNIQUE = 16
    ITEM_SKILLBOOK = 17
    ITEM_QUEST = 18
    ITEM_POLYMORPH = 19
    ITEM_TREASURE_BOX = 20
    ITEM_TREASURE_KEY = 21
    ITEM_SKILLFORGET = 22
    ITEM_GIFTBOX = 23
    ITEM_PICK = 24
    ITEM_HAIR = 25
    ITEM_BLEND = 26
    ITEM_COSTUME = 27
    ITEM_BELT = 28

    def __init__(self):
        super().__init__()
        self.extend([
            "ITEM_NONE",
            "ITEM_WEAPON",
            "ITEM_ARMOR",
            "ITEM_USE",
            "ITEM_AUTOUSE",
            "ITEM_MATERIAL",
            "ITEM_SPECIAL",
            "ITEM_TOOL",
            "ITEM_LOTTERY",
            "ITEM_ELK",
            "ITEM_METIN",
            "ITEM_CONTAINER",
            "ITEM_FISH",
            "ITEM_ROD",
            "ITEM_RESOURCE",
            "ITEM_CAMPFIRE",
            "ITEM_UNIQUE",
            "ITEM_SKILLBOOK",
            "ITEM_QUEST",
            "ITEM_POLYMORPH",
            "ITEM_TREASURE_BOX",
            "ITEM_TREASURE_KEY",
            "ITEM_SKILLFORGET",
            "ITEM_GIFTBOX",
            "ITEM_PICK",
            "ITEM_HAIR",
            "ITEM_BLEND",
            "ITEM_COSTUME",
            "ITEM_BELT",
        ])

class SubType(list):
    class ITEM_METIN(list):
        METIN_NORMAL = 0
        METIN_GOLD = 1

    def __init__(self):
        super().__init__()
        self.extend([
            "METIN_NORMAL",
            "METIN_GOLD",
        ])

    class ITEM_WEAPON(list):
        WEAPON_SWORD = 0
        WEAPON_DAGGER = 1
        WEAPON_BOW = 2
        WEAPON_TWO_HANDED = 3
        WEAPON_BELL = 4
        WEAPON_FAN = 5
        WEAPON_ARROW = 6
        WEAPON_UNLIMITED_ARROW = 7

        def __init__(self):
            super().__init__()
            self.extend([
                "WEAPON_SWORD",
                "WEAPON_DAGGER",
                "WEAPON_BOW",
                "WEAPON_TWO_HANDED",
                "WEAPON_BELL",
                "WEAPON_FAN",
                "WEAPON_ARROW",
                "WEAPON_UNLIMITED_ARROW",
            ])

    class ITEM_ARMOR(list):
        ARMOR_BODY = 0
        ARMOR_HEAD = 1
        ARMOR_SHIELD = 2
        ARMOR_WRIST = 3
        ARMOR_FOOTS = 4
        ARMOR_NECK = 5
        ARMOR_EAR = 6

        def __init__(self):
            super().__init__()
            self.extend([
                "ARMOR_BODY",
                "ARMOR_HEAD",
                "ARMOR_SHIELD",
                "ARMOR_WRIST",
                "ARMOR_FOOTS",
                "ARMOR_NECK",
                "ARMOR_EAR",
            ])

    class ITEM_COSTUME(list):
        COSTUME_BODY = 0
        COSTUME_HAIR = 1
        COSTUME_WEAPON = 2
        COSTUME_MOUNT = 3

        def __init__(self):
            super().__init__()
            self.extend([
                "METIN_NORMAL",
                "METIN_GOLD",
            ])

    class ITEM_FISH(list):
        FISH_ALIVE = 0
        FISH_DEAD = 1

        def __init__(self):
            super().__init__()
            self.extend([
                "FISH_ALIVE",
                "FISH_DEAD",
            ])

    class ITEM_RESOURCE(list):
        RESOURCE_FISHBONE = 0
        RESOURCE_WATERSTONEPIECE = 1
        RESOURCE_WATERSTONE = 2
        RESOURCE_BLOOD_PEARL = 3
        RESOURCE_BLUE_PEARL = 4
        RESOURCE_WHITE_PEARL = 5
        RESOURCE_BUCKET = 6
        RESOURCE_CRYSTAL = 7
        RESOURCE_GEM = 8
        RESOURCE_STONE = 9
        RESOURCE_METIN = 10
        RESOURCE_ORE = 11

        def __init__(self):
            super().__init__()
            self.extend([
                "RESOURCE_FISHBONE",
                "RESOURCE_WATERSTONEPIECE",
                "RESOURCE_WATERSTONE",
                "RESOURCE_BLOOD_PEARL",
                "RESOURCE_BLUE_PEARL",
                "RESOURCE_WHITE_PEARL",
                "RESOURCE_BUCKET",
                "RESOURCE_CRYSTAL",
                "RESOURCE_GEM",
                "RESOURCE_STONE",
                "RESOURCE_METIN",
                "RESOURCE_ORE",
            ])

    class ITEM_UNIQUE(list):
        UNIQUE_NONE = 0
        UNIQUE_SPECIAL_RIDE = 1
        UNIQUE_SPECIAL_MOUNT_RIDE = 2
        UNIQUE_SPECIAL = 3

        def __init__(self):
            super().__init__()
            self.extend([
                "UNIQUE_NONE",
                "UNIQUE_SPECIAL_RIDE",
                "UNIQUE_SPECIAL_MOUNT_RIDE",
                "UNIQUE_SPECIAL",
            ])

    class ITEM_USE(list):
        USE_POTION = 0
        USE_TALISMAN = 1
        USE_TUNING = 2
        USE_MOVE = 3
        USE_TREASURE_BOX = 4
        USE_MONEYBAG = 5
        USE_BAIT = 6
        USE_ABILITY_UP = 7
        USE_AFFECT = 8
        USE_CREATE_STONE = 9
        USE_SPECIAL = 10
        USE_POTION_NODELAY = 11
        USE_CLEAR = 12
        USE_INVISIBILITY = 13
        USE_DETACHMENT = 14
        USE_BUCKET = 15
        USE_POTION_CONTINUE = 16
        USE_CLEAN_SOCKET = 17
        USE_CHANGE_ATTRIBUTE = 18
        USE_ADD_ATTRIBUTE = 19
        USE_ADD_ACCESSORY_SOCKET = 20
        USE_PUT_INTO_ACCESSORY_SOCKET = 21
        USE_ADD_ATTRIBUTE2 = 22
        USE_RECIPE = 23
        USE_CHANGE_ATTRIBUTE2 = 24
        USE_BIND = 25
        USE_UNBIND = 26
        USE_TIME_CHARGE_PER = 27
        USE_TIME_CHARGE_FIX = 28
        USE_PUT_INTO_BELT_SOCKET = 29
        USE_PET = 32

        def __init__(self):
            super().__init__()
            self.extend([
                "USE_POTION",
                "USE_TALISMAN",
                "USE_TUNING",
                "USE_MOVE",
                "USE_TREASURE_BOX",
                "USE_MONEYBAG",
                "USE_BAIT",
                "USE_ABILITY_UP",
                "USE_AFFECT",
                "USE_CREATE_STONE",
                "USE_SPECIAL",
                "USE_POTION_NODELAY",
                "USE_CLEAR",
                "USE_INVISIBILITY",
                "USE_DETACHMENT",
                "USE_BUCKET",
                "USE_POTION_CONTINUE",
                "USE_CLEAN_SOCKET",
                "USE_CHANGE_ATTRIBUTE",
                "USE_ADD_ATTRIBUTE",
                "USE_ADD_ACCESSORY_SOCKET",
                "USE_PUT_INTO_ACCESSORY_SOCKET",
                "USE_ADD_ATTRIBUTE2",
                "USE_RECIPE",
                "USE_CHANGE_ATTRIBUTE2",
                "USE_BIND",
                "USE_UNBIND",
                "USE_TIME_CHARGE_PER",
                "USE_TIME_CHARGE_FIX",
                "USE_PUT_INTO_BELT_SOCKET",
                "USE_CHANGE_COSTUME_ATTR",
                "USE_RESET_COSTUME_ATTR",
                "USE_PET",
            ])

    class ITEM_AUTOUSE(list):
        AUTOUSE_POTION = 0
        AUTOUSE_ABILITY_UP = 1
        AUTOUSE_BOMB = 2
        AUTOUSE_GOLD = 3
        AUTOUSE_MONEYBAG = 4
        AUTOUSE_TREASURE_BOX = 5

        def __init__(self):
            super().__init__()
            self.extend([
                "AUTOUSE_POTION",
                "AUTOUSE_ABILITY_UP",
                "AUTOUSE_BOMB",
                "AUTOUSE_GOLD",
                "AUTOUSE_MONEYBAG",
                "AUTOUSE_TREASURE_BOX",
            ])

    class ITEM_MATERIAL(list):
        MATERIAL_LEATHER = 0
        MATERIAL_BLOOD = 1
        MATERIAL_ROOT = 2
        MATERIAL_NEEDLE = 3
        MATERIAL_JEWEL = 4

        def __init__(self):
            super().__init__()
            self.extend([
                "MATERIAL_LEATHER",
                "MATERIAL_BLOOD",
                "MATERIAL_ROOT",
                "MATERIAL_NEEDLE",
                "MATERIAL_JEWEL",
            ])

    class ITEM_SPECIAL(list):
        SPECIAL_MAP = 0
        SPECIAL_KEY = 1
        SPECIAL_DOC = 2
        SPECIAL_SPIRIT = 3

        def __init__(self):
            super().__init__()
            self.extend([
                "SPECIAL_MAP",
                "SPECIAL_KEY",
                "SPECIAL_DOC",
                "SPECIAL_SPIRIT",
            ])

    class ITEM_TOOL(list):
        TOOL_FISHING_ROD = 0

        def __init__(self):
            super().__init__()
            self.extend([
                "TOOL_FISHING_ROD",
            ])

    class ITEM_LOTTERY(list):
        LOTTERY_TICKET = 0
        LOTTERY_INSTANT = 1

        def __init__(self):
            super().__init__()
            self.extend([
                "LOTTERY_TICKET",
                "LOTTERY_INSTANT",
            ])


class Flag(dict):
    ITEM_FLAG_REFINEABLE = (1 << 0)
    ITEM_FLAG_SAVE = (1 << 1)
    ITEM_FLAG_STACKABLE = (1 << 2)
    ITEM_FLAG_COUNT_PER_1GOLD = (1 << 3)
    ITEM_FLAG_SLOW_QUERY = (1 << 4)
    ITEM_FLAG_UNIQUE = (1 << 5)
    ITEM_FLAG_MAKECOUNT = (1 << 6)
    ITEM_FLAG_IRREMOVABLE = (1 << 7)
    ITEM_FLAG_CONFIRM_WHEN_USE = (1 << 8)
    ITEM_FLAG_QUEST_USE = (1 << 9)
    ITEM_FLAG_QUEST_USE_MULTIPLE = (1 << 10)
    ITEM_FLAG_QUEST_GIVE = (1 << 11)
    ITEM_FLAG_LOG = (1 << 12)
    ITEM_FLAG_APPLICABLE = (1 << 13)

    def __init__(self):
        super().__init__()
        self.update({
            'ITEM_TUNABLE' : (1 << 0),
            'ITEM_SAVE' : (1 << 1),
            'ITEM_STACKABLE' : (1 << 2),
            'COUNT_PER_1GOLD' : (1 << 3),
            'ITEM_SLOW_QUERY' : (1 << 4),
            'ITEM_UNIQUE' : (1 << 5),
            'ITEM_MAKECOUNT' : (1 << 6),
            'ITEM_IRREMOVABLE' : (1 << 7),
            'CONFIRM_WHEN_USE' : (1 << 8),
            'QUEST_USE' : (1 << 9),
            'QUEST_USE_MULTIPLE' : (1 << 10),
            'QUEST_GIVE' : (1 << 11),
            'ITEM_QUEST' : (1 << 12),
            'LOG' : (1 << 13),
        })

class AntiFlag(dict):
    ITEM_ANTIFLAG_FEMALE = (1 << 0)
    ITEM_ANTIFLAG_MALE = (1 << 1)
    ITEM_ANTIFLAG_WARRIOR = (1 << 2)
    ITEM_ANTIFLAG_ASSASSIN = (1 << 3)
    ITEM_ANTIFLAG_SURA = (1 << 4)
    ITEM_ANTIFLAG_SHAMAN = (1 << 5)
    ITEM_ANTIFLAG_GET = (1 << 6)
    ITEM_ANTIFLAG_DROP = (1 << 7)
    ITEM_ANTIFLAG_SELL = (1 << 8)
    ITEM_ANTIFLAG_EMPIRE_A = (1 << 9)
    ITEM_ANTIFLAG_EMPIRE_B = (1 << 10)
    ITEM_ANTIFLAG_EMPIRE_C = (1 << 11)
    ITEM_ANTIFLAG_SAVE = (1 << 12)
    ITEM_ANTIFLAG_GIVE = (1 << 13)
    ITEM_ANTIFLAG_PKDROP = (1 << 14)
    ITEM_ANTIFLAG_STACK = (1 << 15)
    ITEM_ANTIFLAG_MYSHOP = (1 << 16)
    ITEM_ANTIFLAG_SAFEBOX = (1 << 17)
    ITEM_ANTIFLAG_WOLFMAN = (1 << 18)
    ITEM_ANTIFLAG_MY_OFFLINE_SHOP = (1 << 19)
    ITEM_ANTIFLAG_BIND = (1 << 20)

    def __init__(self):
        super().__init__()
        self.update({
            'ANTI_FEMALE' : (1 << 0),
            'ANTI_MUSA' : (1 << 1),
            'ITEM_ANTIFLAG_WARRIOR' : (1 << 2),
            'ANTI_ASSASSIN' : (1 << 3),
            'ANTI_SURA' : (1 << 4),
            'ANTI_MUDANG' : (1 << 5),
            'ANTI_GET' : (1 << 6),
            'ANTI_DROP' : (1 << 7),
            'ANTI_SELL' : (1 << 8),
            'ANTI_EMPIRE_A' : (1 << 9),
            'ANTI_EMPIRE_B' : (1 << 10),
            'ANTI_EMPIRE_C' : (1 << 11),
            'ANTI_SAVE' : (1 << 12),
            'ANTI_GIVE' : (1 << 13),
            'ANTI_PKDROP' : (1 << 14),
            'ANTI_STACK' : (1 << 15),
            'ANTI_MYSHOP' : (1 << 16),
            'ANTI_SAFEBOX' : (1 << 17),
            'ANTI_WOLFMAN' : (1 << 18),
            'ANTI_MYOFFLINESHOP' : (1 << 19),
            'ANTI_BIND' : (1 << 20),
        })

class WearFlag(list):
    WEAR_BODY = 0
    WEAR_HEAD = 1
    WEAR_FOOTS = 2
    WEAR_WRIST = 3
    WEAR_WEAPON = 4
    WEAR_NECK = 5
    WEAR_EAR = 6
    WEAR_SHIELD = 7
    WEAR_UNIQUE = 8
    WEAR_ARROW = 9
    WEAR_BELT = 10
    WEAR_PET = 11
    WEAR_COSTUME_BODY = 12
    WEAR_COSTUME_HAIR = 13
    WEAR_COSTUME_WEAPON = 14
    WEAR_COSTUME_MOUNT = 15

    def __init__(self):
        super().__init__()
        self.extend([
            "WEAR_BODY",
            "WEAR_HEAD",
            "WEAR_FOOTS",
            "WEAR_WRIST",
            "WEAR_WEAPON",
            "WEAR_NECK",
            "WEAR_EAR",
            "WEAR_SHIELD",
            "WEAR_UNIQUE",
            "WEAR_ARROW",
            "WEAR_BELT",
            "WEAR_PET",
            "WEAR_COSTUME_BODY",
            "WEAR_COSTUME_HAIR",
            "WEAR_COSTUME_WEAPON",
            "WEAR_COSTUME_MOUNT",
    ])

class LimitTypes(list):
    LIMIT_NONE = 0
    LIMIT_LEVEL = 1
    LIMIT_STR = 2
    LIMIT_DEX = 3
    LIMIT_INT = 4
    LIMIT_CON = 5
    LIMIT_REAL_TIME = 7
    LIMIT_REAL_TIME_START_FIRST_USE = 8
    LIMIT_TIMER_BASED_ON_WEAR = 9

    def __init__(self):
        super().__init__()
        self.extend([
            "LIMIT_NONE",
            "LEVEL",
            "STR",
            "DEX",
            "INT",
            "CON",
            "NONE",
            "REAL_TIME",
            "REAL_TIME_FIRST_USE",
            "TIMER_BASED_ON_WEAR",
        ])

class RefineTypes(list):
    REFINE_TYPE_NORMAL = 0
    REFINE_TYPE_SCROLL = 1
    REFINE_TYPE_HYUNIRON = 2
    REFINE_TYPE_MONEY_ONLY = 3
    REFINE_TYPE_MUSIN = 4

    def __init__(self):
        super().__init__()
        self.extend([
        ])

class ImuneFlag(dict):
    PARA = (1 << 0)
    CURSE = (1 << 1)
    STUN = (1 << 2)
    SLEEP = (1 << 3)
    SLOW = (1 << 4)
    POISON = (1 << 5)
    TERROR = (1 << 6)

    def __init__(self):
        super().__init__()
        self.update({
            "PARA" : (1 << 0),
            "CURSE" : (1 << 1),
            "STUN" : (1 << 2),
            "SLEEP" : (1 << 3),
            "SLOW" : (1 << 4),
            "POISON" : (1 << 5),
            "TERROR" : (1 << 6),
        })

class ApplyType(list):
    def __init__(self):
        super().__init__()
        self.extend([
            "APPLY_NONE",
            "APPLY_MAX_HP",
            "APPLY_MAX_SP",
            "APPLY_CON",
            "APPLY_INT",
            "APPLY_STR",
            "APPLY_DEX",
            "APPLY_ATT_SPEED",
            "APPLY_MOV_SPEED",
            "APPLY_CAST_SPEED",
            "APPLY_HP_REGEN",
            "APPLY_SP_REGEN",
            "APPLY_POISON_PCT",
            "APPLY_STUN_PCT",
            "APPLY_SLOW_PCT",
            "APPLY_CRITICAL_PCT",
            "APPLY_PENETRATE_PCT",
            "APPLY_ATTBONUS_HUMAN",
            "APPLY_ATTBONUS_ANIMAL",
            "APPLY_ATTBONUS_ORC",
            "APPLY_ATTBONUS_MILGYO",
            "APPLY_ATTBONUS_UNDEAD",
            "APPLY_ATTBONUS_DEVIL",
            "APPLY_STEAL_HP",
            "APPLY_STEAL_SP",
            "APPLY_MANA_BURN_PCT",
            "APPLY_DAMAGE_SP_RECOVER",
            "APPLY_BLOCK",
            "APPLY_DODGE",
            "APPLY_RESIST_SWORD",
            "APPLY_RESIST_TWOHAND",
            "APPLY_RESIST_DAGGER",
            "APPLY_RESIST_BELL",
            "APPLY_RESIST_FAN",
            "APPLY_RESIST_BOW",
            "APPLY_RESIST_FIRE",
            "APPLY_RESIST_ELEC",
            "APPLY_RESIST_MAGIC",
            "APPLY_RESIST_WIND",
            "APPLY_REFLECT_MELEE",
            "APPLY_REFLECT_CURSE",
            "APPLY_POISON_REDUCE",
            "APPLY_KILL_SP_RECOVER",
            "APPLY_EXP_DOUBLE_BONUS",
            "APPLY_GOLD_DOUBLE_BONUS",
            "APPLY_ITEM_DROP_BONUS",
            "APPLY_POTION_BONUS",
            "APPLY_KILL_HP_RECOVER",
            "APPLY_IMMUNE_STUN",
            "APPLY_IMMUNE_SLOW",
            "APPLY_IMMUNE_FALL",
            "APPLY_SKILL",
            "APPLY_BOW_DISTANCE",
            "APPLY_ATT_GRADE_BONUS",
            "APPLY_DEF_GRADE_BONUS",
            "APPLY_MAGIC_ATT_GRADE",
            "APPLY_MAGIC_DEF_GRADE",
            "APPLY_CURSE_PCT",
            "APPLY_MAX_STAMINA",
            "APPLY_ATTBONUS_WARRIOR",
            "APPLY_ATTBONUS_ASSASSIN",
            "APPLY_ATTBONUS_SURA",
            "APPLY_ATTBONUS_SHAMAN",
            "APPLY_ATTBONUS_MONSTER",
            "APPLY_MALL_ATTBONUS",
            "APPLY_MALL_DEFBONUS",
            "APPLY_MALL_EXPBONUS",
            "APPLY_MALL_ITEMBONUS",
            "APPLY_MALL_GOLDBONUS",
            "APPLY_MAX_HP_PCT",
            "APPLY_MAX_SP_PCT",
            "APPLY_SKILL_DAMAGE_BONUS",
            "APPLY_NORMAL_HIT_DAMAGE_BONUS",
            "APPLY_SKILL_DEFEND_BONUS",
            "APPLY_NORMAL_HIT_DEFEND_BONUS",
            "NONE",
            "NONE",
            "APPLY_EXTRACT_HP_PCT",
            "APPLY_RESIST_WARRIOR",
            "APPLY_RESIST_ASSASSIN",
            "APPLY_RESIST_SURA",
            "APPLY_RESIST_SHAMAN",
            "APPLY_ENERGY",
            "APPLY_DEF_GRADE",
            "APPLY_COSTUME_ATTR_BONUS",
            "APPLY_MAGIC_ATTBONUS_PER",
            "APPLY_MELEE_MAGIC_ATTBONUS_PER",
            "APPLY_RESIST_ICE",
            "APPLY_RESIST_EARTH",
            "APPLY_RESIST_DARK",
            "APPLY_ANTI_CRITICAL_PCT",
            "APPLY_ANTI_PENETRATE_PCT",
            "APPLY_BLEEDING_REDUCE",
            "APPLY_BLEEDING_PCT",
            "APPLY_ATTBONUS_WOLFMAN",
            "APPLY_RESIST_WOLFMAN",
            "APPLY_RESIST_CLAW",
            "APPLY_RESIST_HUMAN",
        ])
    
class Item():

    Vnum = 0
    Name = ''
    Type = 0
    SubType = 0
    Size = 1
    AntiFlags = 0
    Flags = 0
    WearFlags = 0
    Gold = 0
    ShopBuyPrice = 0
    RefinedVnum = 0
    RefineSet = 0
    LimitType0 = 0
    LimitValue0 = 0
    LimitType1 = 0
    LimitValue1 = 0
    ApplyType0 = 0
    ApplyValue0 = 0
    ApplyType1 = 0
    ApplyValue1 = 0
    ApplyType2 = 0
    ApplyValue2 = 0
    Value0 = 0
    Value1 = 0
    Value2 = 0
    Value3 = 0
    Value4 = 0
    Value5 = 0
    Specular = 0
    GainSocketPercent = 0
    AddonType = 0
