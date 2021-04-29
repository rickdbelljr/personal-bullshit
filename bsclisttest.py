import pickle

address_dict = {
    'GorillaDiamond': '0xb7F2bca9b034f8cc143339Dd12bb31D3D50Cf27a',
    'SafeMoon': '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3'
    }
    
pickle.dump(address_dict, open("tokens.p", "wb"))
    