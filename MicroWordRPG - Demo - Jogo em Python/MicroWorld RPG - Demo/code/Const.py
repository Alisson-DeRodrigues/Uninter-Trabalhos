

# window
WIN_WIDTH = 512
WIN_HEIGHT = 448
TILESIZE = 32
FPS = 60

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ITEM_BOX_SIZE = 40
UI_FONT = './Mapa/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
UI_BORDER_COLOR_ACTIVE = 'gold'

tool_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': './Mapa/Tool/sword/full.png'},
    'sickle': {'cooldown': 100, 'damage': 10, 'graphic': './Mapa/Tool/sickle/full.png'},
    'pickaxe': {'cooldown': 100, 'damage': 10, 'graphic': './Mapa/Tool/pickaxe/full.png'}
}

farm_data = {
    'corn': {'amount': 2, 'graphic': './Mapa/Farm/corn/full/0.png'},
    'tomato': {'amount': 12, 'graphic': './Mapa/Farm/tomato/full/0.png'},
}

deposit_data = {
    'stone': {'amount': 4, 'graphic': './Mapa/DepositOre/stone/full/0.png'},
    'coal': {'amount': 4, 'graphic': './Mapa/DepositOre/coal/full/0.png'},
    'iron': {'amount': 4, 'graphic': './Mapa/DepositOre/iron/full/0.png'}
}

monster_data = {
    'beast': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'speed': 3, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 180}
}

UI_INFO = {
    0: 'M - Abre ou fecha o menu',
    1: 'Q - Troca de ferramenta',
    2: 'Space - Usa a ferramenta',
    3: '========================',
    4: 'Utilize a picareta para',
    5: 'minerar, a foice para a',
    6: 'colheita e a espada para',
    7: 'atacar.'
}

UI_INFO_POS = {
    0:  (80, 120),
    1: (80, 140),
    2: (80, 160),
    3: (80, 180),
    4: (80, 200),
    5: (80, 220),
    6: (80, 240),
    7: (80, 260)
}