from SpecImports import *
from toontown.toonbase import ToontownGlobals
import random
CogParent = 10000
BattleParent = 10005
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': BattleParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 1,
  'level': ToontownGlobals.CashbotMintBossLevel,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0,
  'revives': 1},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10, 11]),
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10, 11]),
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([8, 9, 10, 11]),
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
