from SpecImports import *
from toontown.toonbase import ToontownGlobals
import random
CogParent = 10000
BattleCellId = 0
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 1,
  'level': ToontownGlobals.CashbotMintBossLevel,
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1]),
  'revives': random.choice([0, 1])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1]),
  'revives': random.choice([0, 1])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1]),
  'revives': random.choice([0, 1])},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': ToontownGlobals.CashbotMintCogLevel + 1,
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1]),
  'revives': random.choice([0, 1])}]
ReserveCogData = []
