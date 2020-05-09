# these values are lifted from: http://reveng.sourceforge.net/crc-catalogue/
# they constitute values for the parameterized/generalized CRC algorithm from:
# Ross Wiliams' "A PAINLESS GUIDE TO CRC ERROR DETECTION ALGORITHMS" https://www.zlib.net/crc_v3.txt
#
# poly is highest x term implied at msb, x^0 at lsb, regardless of reflection (refin, refout)

database = [
{'name':'CRC-3/GSM', 'width':3, 'poly':0x3, 'init':0x0, 'refin':False, 'refout':False, 'xorout':0x7, 'check':0x4, 'residue':0x2},
{'name':'CRC-3/ROHC', 'width':3, 'poly':0x3, 'init':0x7, 'refin':True, 'refout':True, 'xorout':0x0, 'check':0x6, 'residue':0x0},
{'name':'CRC-4/G-704', 'width':4, 'poly':0x3, 'init':0x0, 'refin':True, 'refout':True, 'xorout':0x0, 'check':0x7, 'residue':0x0},
{'name':'CRC-4/INTERLAKEN', 'width':4, 'poly':0x3, 'init':0xf, 'refin':False, 'refout':False, 'xorout':0xf, 'check':0xb, 'residue':0x2},
{'name':'CRC-5/EPC-C1G2', 'width':5, 'poly':0x09, 'init':0x09, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x00, 'residue':0x00},
{'name':'CRC-5/G-704', 'width':5, 'poly':0x15, 'init':0x00, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x07, 'residue':0x00},
{'name':'CRC-5/USB', 'width':5, 'poly':0x05, 'init':0x1f, 'refin':True, 'refout':True, 'xorout':0x1f, 'check':0x19, 'residue':0x06},
{'name':'CRC-6/CDMA2000-A', 'width':6, 'poly':0x27, 'init':0x3f, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x0d, 'residue':0x00},
{'name':'CRC-6/CDMA2000-B', 'width':6, 'poly':0x07, 'init':0x3f, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x3b, 'residue':0x00},
{'name':'CRC-6/DARC', 'width':6, 'poly':0x19, 'init':0x00, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x26, 'residue':0x00},
{'name':'CRC-6/G-704', 'width':6, 'poly':0x03, 'init':0x00, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x06, 'residue':0x00},
{'name':'CRC-6/GSM', 'width':6, 'poly':0x2f, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x3f, 'check':0x13, 'residue':0x3a},
{'name':'CRC-7/MMC', 'width':7, 'poly':0x09, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x75, 'residue':0x00},
{'name':'CRC-7/ROHC', 'width':7, 'poly':0x4f, 'init':0x7f, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x53, 'residue':0x00},
{'name':'CRC-7/UMTS', 'width':7, 'poly':0x45, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x61, 'residue':0x00},
{'name':'CRC-8/AUTOSAR', 'width':8, 'poly':0x2f, 'init':0xff, 'refin':False, 'refout':False, 'xorout':0xff, 'check':0xdf, 'residue':0x42},
{'name':'CRC-8/BLUETOOTH', 'width':8, 'poly':0xa7, 'init':0x00, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x26, 'residue':0x00},
{'name':'CRC-8/CDMA2000', 'width':8, 'poly':0x9b, 'init':0xff, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0xda, 'residue':0x00},
{'name':'CRC-8/DARC', 'width':8, 'poly':0x39, 'init':0x00, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x15, 'residue':0x00},
{'name':'CRC-8/DVB-S2', 'width':8, 'poly':0xd5, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0xbc, 'residue':0x00},
{'name':'CRC-8/GSM-A', 'width':8, 'poly':0x1d, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x37, 'residue':0x00},
{'name':'CRC-8/GSM-B', 'width':8, 'poly':0x49, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0xff, 'check':0x94, 'residue':0x53},
{'name':'CRC-8/I-432-1', 'width':8, 'poly':0x07, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x55, 'check':0xa1, 'residue':0xac},
{'name':'CRC-8/I-CODE', 'width':8, 'poly':0x1d, 'init':0xfd, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x7e, 'residue':0x00},
{'name':'CRC-8/LTE', 'width':8, 'poly':0x9b, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0xea, 'residue':0x00},
{'name':'CRC-8/MAXIM-DOW', 'width':8, 'poly':0x31, 'init':0x00, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0xa1, 'residue':0x00},
{'name':'CRC-8/MIFARE-MAD', 'width':8, 'poly':0x1d, 'init':0xc7, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x99, 'residue':0x00},
{'name':'CRC-8/NRSC-5', 'width':8, 'poly':0x31, 'init':0xff, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0xf7, 'residue':0x00},
{'name':'CRC-8/OPENSAFETY', 'width':8, 'poly':0x2f, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0x3e, 'residue':0x00},
{'name':'CRC-8/ROHC', 'width':8, 'poly':0x07, 'init':0xff, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0xd0, 'residue':0x00},
{'name':'CRC-8/SAE-J1850', 'width':8, 'poly':0x1d, 'init':0xff, 'refin':False, 'refout':False, 'xorout':0xff, 'check':0x4b, 'residue':0xc4},
{'name':'CRC-8/SMBUS', 'width':8, 'poly':0x07, 'init':0x00, 'refin':False, 'refout':False, 'xorout':0x00, 'check':0xf4, 'residue':0x00},
{'name':'CRC-8/TECH-3250', 'width':8, 'poly':0x1d, 'init':0xff, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x97, 'residue':0x00},
{'name':'CRC-8/WCDMA', 'width':8, 'poly':0x9b, 'init':0x00, 'refin':True, 'refout':True, 'xorout':0x00, 'check':0x25, 'residue':0x00},
{'name':'CRC-10/ATM', 'width':10, 'poly':0x233, 'init':0x000, 'refin':False, 'refout':False, 'xorout':0x000, 'check':0x199, 'residue':0x000},
{'name':'CRC-10/CDMA2000', 'width':10, 'poly':0x3d9, 'init':0x3ff, 'refin':False, 'refout':False, 'xorout':0x000, 'check':0x233, 'residue':0x000},
{'name':'CRC-10/GSM', 'width':10, 'poly':0x175, 'init':0x000, 'refin':False, 'refout':False, 'xorout':0x3ff, 'check':0x12a, 'residue':0x0c6},
{'name':'CRC-11/FLEXRAY', 'width':11, 'poly':0x385, 'init':0x01a, 'refin':False, 'refout':False, 'xorout':0x000, 'check':0x5a3, 'residue':0x000},
{'name':'CRC-11/UMTS', 'width':11, 'poly':0x307, 'init':0x000, 'refin':False, 'refout':False, 'xorout':0x000, 'check':0x061, 'residue':0x000},
{'name':'CRC-12/CDMA2000', 'width':12, 'poly':0xf13, 'init':0xfff, 'refin':False, 'refout':False, 'xorout':0x000, 'check':0xd4d, 'residue':0x000},
{'name':'CRC-12/DECT', 'width':12, 'poly':0x80f, 'init':0x000, 'refin':False, 'refout':False, 'xorout':0x000, 'check':0xf5b, 'residue':0x000},
{'name':'CRC-12/GSM', 'width':12, 'poly':0xd31, 'init':0x000, 'refin':False, 'refout':False, 'xorout':0xfff, 'check':0xb34, 'residue':0x178},
{'name':'CRC-12/UMTS', 'width':12, 'poly':0x80f, 'init':0x000, 'refin':False, 'refout':True, 'xorout':0x000, 'check':0xdaf, 'residue':0x000},
{'name':'CRC-13/BBC', 'width':13, 'poly':0x1cf5, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x04fa, 'residue':0x0000},
{'name':'CRC-14/DARC', 'width':14, 'poly':0x0805, 'init':0x0000, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0x082d, 'residue':0x0000},
{'name':'CRC-14/GSM', 'width':14, 'poly':0x202d, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x3fff, 'check':0x30ae, 'residue':0x031e},
{'name':'CRC-15/CAN', 'width':15, 'poly':0x4599, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x059e, 'residue':0x0000},
{'name':'CRC-15/MPT1327', 'width':15, 'poly':0x6815, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0001, 'check':0x2566, 'residue':0x6815},
{'name':'CRC-16/ARC', 'width':16, 'poly':0x8005, 'init':0x0000, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0xbb3d, 'residue':0x0000},
{'name':'CRC-16/CDMA2000', 'width':16, 'poly':0xc867, 'init':0xffff, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x4c06, 'residue':0x0000},
{'name':'CRC-16/CMS', 'width':16, 'poly':0x8005, 'init':0xffff, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0xaee7, 'residue':0x0000},
{'name':'CRC-16/DDS-110', 'width':16, 'poly':0x8005, 'init':0x800d, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x9ecf, 'residue':0x0000},
{'name':'CRC-16/DECT-R', 'width':16, 'poly':0x0589, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0001, 'check':0x007e, 'residue':0x0589},
{'name':'CRC-16/DECT-X', 'width':16, 'poly':0x0589, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x007f, 'residue':0x0000},
{'name':'CRC-16/DNP', 'width':16, 'poly':0x3d65, 'init':0x0000, 'refin':True, 'refout':True, 'xorout':0xffff, 'check':0xea82, 'residue':0x66c5},
{'name':'CRC-16/EN-13757', 'width':16, 'poly':0x3d65, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0xffff, 'check':0xc2b7, 'residue':0xa366},
{'name':'CRC-16/GENIBUS', 'width':16, 'poly':0x1021, 'init':0xffff, 'refin':False, 'refout':False, 'xorout':0xffff, 'check':0xd64e, 'residue':0x1d0f},
{'name':'CRC-16/GSM', 'width':16, 'poly':0x1021, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0xffff, 'check':0xce3c, 'residue':0x1d0f},
{'name':'CRC-16/IBM-3740', 'width':16, 'poly':0x1021, 'init':0xffff, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x29b1, 'residue':0x0000},
{'name':'CRC-16/IBM-SDLC', 'width':16, 'poly':0x1021, 'init':0xffff, 'refin':True, 'refout':True, 'xorout':0xffff, 'check':0x906e, 'residue':0xf0b8},
{'name':'CRC-16/ISO-IEC-14443-3-A', 'width':16, 'poly':0x1021, 'init':0xc6c6, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0xbf05, 'residue':0x0000},
{'name':'CRC-16/KERMIT', 'width':16, 'poly':0x1021, 'init':0x0000, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0x2189, 'residue':0x0000},
{'name':'CRC-16/LJ1200', 'width':16, 'poly':0x6f63, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0xbdf4, 'residue':0x0000},
{'name':'CRC-16/MAXIM-DOW', 'width':16, 'poly':0x8005, 'init':0x0000, 'refin':True, 'refout':True, 'xorout':0xffff, 'check':0x44c2, 'residue':0xb001},
{'name':'CRC-16/MCRF4XX', 'width':16, 'poly':0x1021, 'init':0xffff, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0x6f91, 'residue':0x0000},
{'name':'CRC-16/MODBUS', 'width':16, 'poly':0x8005, 'init':0xffff, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0x4b37, 'residue':0x0000},
{'name':'CRC-16/NRSC-5', 'width':16, 'poly':0x080b, 'init':0xffff, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0xa066, 'residue':0x0000},
{'name':'CRC-16/OPENSAFETY-A', 'width':16, 'poly':0x5935, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x5d38, 'residue':0x0000},
{'name':'CRC-16/OPENSAFETY-B', 'width':16, 'poly':0x755b, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x20fe, 'residue':0x0000},
{'name':'CRC-16/PROFIBUS', 'width':16, 'poly':0x1dcf, 'init':0xffff, 'refin':False, 'refout':False, 'xorout':0xffff, 'check':0xa819, 'residue':0xe394},
{'name':'CRC-16/RIELLO', 'width':16, 'poly':0x1021, 'init':0xb2aa, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0x63d0, 'residue':0x0000},
{'name':'CRC-16/SPI-FUJITSU', 'width':16, 'poly':0x1021, 'init':0x1d0f, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0xe5cc, 'residue':0x0000},
{'name':'CRC-16/T10-DIF', 'width':16, 'poly':0x8bb7, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0xd0db, 'residue':0x0000},
{'name':'CRC-16/TELEDISK', 'width':16, 'poly':0xa097, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x0fb3, 'residue':0x0000},
{'name':'CRC-16/TMS37157', 'width':16, 'poly':0x1021, 'init':0x89ec, 'refin':True, 'refout':True, 'xorout':0x0000, 'check':0x26b1, 'residue':0x0000},
{'name':'CRC-16/UMTS', 'width':16, 'poly':0x8005, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0xfee8, 'residue':0x0000},
{'name':'CRC-16/USB', 'width':16, 'poly':0x8005, 'init':0xffff, 'refin':True, 'refout':True, 'xorout':0xffff, 'check':0xb4c8, 'residue':0xb001},
{'name':'CRC-16/XMODEM', 'width':16, 'poly':0x1021, 'init':0x0000, 'refin':False, 'refout':False, 'xorout':0x0000, 'check':0x31c3, 'residue':0x0000},
{'name':'CRC-17/CAN-FD', 'width':17, 'poly':0x1685b, 'init':0x00000, 'refin':False, 'refout':False, 'xorout':0x00000, 'check':0x04f03, 'residue':0x00000},
{'name':'CRC-21/CAN-FD', 'width':21, 'poly':0x102899, 'init':0x000000, 'refin':False, 'refout':False, 'xorout':0x000000, 'check':0x0ed841, 'residue':0x000000},
{'name':'CRC-24/BLE', 'width':24, 'poly':0x00065b, 'init':0x555555, 'refin':True, 'refout':True, 'xorout':0x000000, 'check':0xc25a56, 'residue':0x000000},
{'name':'CRC-24/FLEXRAY-A', 'width':24, 'poly':0x5d6dcb, 'init':0xfedcba, 'refin':False, 'refout':False, 'xorout':0x000000, 'check':0x7979bd, 'residue':0x000000},
{'name':'CRC-24/FLEXRAY-B', 'width':24, 'poly':0x5d6dcb, 'init':0xabcdef, 'refin':False, 'refout':False, 'xorout':0x000000, 'check':0x1f23b8, 'residue':0x000000},
{'name':'CRC-24/INTERLAKEN', 'width':24, 'poly':0x328b63, 'init':0xffffff, 'refin':False, 'refout':False, 'xorout':0xffffff, 'check':0xb4f3e6, 'residue':0x144e63},
{'name':'CRC-24/LTE-A', 'width':24, 'poly':0x864cfb, 'init':0x000000, 'refin':False, 'refout':False, 'xorout':0x000000, 'check':0xcde703, 'residue':0x000000},
{'name':'CRC-24/LTE-B', 'width':24, 'poly':0x800063, 'init':0x000000, 'refin':False, 'refout':False, 'xorout':0x000000, 'check':0x23ef52, 'residue':0x000000},
{'name':'CRC-24/OPENPGP', 'width':24, 'poly':0x864cfb, 'init':0xb704ce, 'refin':False, 'refout':False, 'xorout':0x000000, 'check':0x21cf02, 'residue':0x000000},
{'name':'CRC-24/OS-9', 'width':24, 'poly':0x800063, 'init':0xffffff, 'refin':False, 'refout':False, 'xorout':0xffffff, 'check':0x200fa5, 'residue':0x800fe3},
{'name':'CRC-30/CDMA', 'width':30, 'poly':0x2030b9c7, 'init':0x3fffffff, 'refin':False, 'refout':False, 'xorout':0x3fffffff, 'check':0x04c34abf, 'residue':0x34efa55a},
{'name':'CRC-31/PHILIPS', 'width':31, 'poly':0x04c11db7, 'init':0x7fffffff, 'refin':False, 'refout':False, 'xorout':0x7fffffff, 'check':0x0ce9e46c, 'residue':0x4eaf26f1},
{'name':'CRC-32/AIXM', 'width':32, 'poly':0x814141ab, 'init':0x00000000, 'refin':False, 'refout':False, 'xorout':0x00000000, 'check':0x3010bf7f, 'residue':0x00000000},
{'name':'CRC-32/AUTOSAR', 'width':32, 'poly':0xf4acfb13, 'init':0xffffffff, 'refin':True, 'refout':True, 'xorout':0xffffffff, 'check':0x1697d06a, 'residue':0x904cddbf},
{'name':'CRC-32/BASE91-D', 'width':32, 'poly':0xa833982b, 'init':0xffffffff, 'refin':True, 'refout':True, 'xorout':0xffffffff, 'check':0x87315576, 'residue':0x45270551},
{'name':'CRC-32/BZIP2', 'width':32, 'poly':0x04c11db7, 'init':0xffffffff, 'refin':False, 'refout':False, 'xorout':0xffffffff, 'check':0xfc891918, 'residue':0xc704dd7b},
{'name':'CRC-32/CD-ROM-EDC', 'width':32, 'poly':0x8001801b, 'init':0x00000000, 'refin':True, 'refout':True, 'xorout':0x00000000, 'check':0x6ec2edc4, 'residue':0x00000000},
{'name':'CRC-32/CKSUM', 'width':32, 'poly':0x04c11db7, 'init':0x00000000, 'refin':False, 'refout':False, 'xorout':0xffffffff, 'check':0x765e7680, 'residue':0xc704dd7b},
{'name':'CRC-32/ISCSI', 'width':32, 'poly':0x1edc6f41, 'init':0xffffffff, 'refin':True, 'refout':True, 'xorout':0xffffffff, 'check':0xe3069283, 'residue':0xb798b438},
{'name':'CRC-32/ISO-HDLC', 'width':32, 'poly':0x04c11db7, 'init':0xffffffff, 'refin':True, 'refout':True, 'xorout':0xffffffff, 'check':0xcbf43926, 'residue':0xdebb20e3},
{'name':'CRC-32/JAMCRC', 'width':32, 'poly':0x04c11db7, 'init':0xffffffff, 'refin':True, 'refout':True, 'xorout':0x00000000, 'check':0x340bc6d9, 'residue':0x00000000},
{'name':'CRC-32/MPEG-2', 'width':32, 'poly':0x04c11db7, 'init':0xffffffff, 'refin':False, 'refout':False, 'xorout':0x00000000, 'check':0x0376e6e7, 'residue':0x00000000},
{'name':'CRC-32/XFER', 'width':32, 'poly':0x000000af, 'init':0x00000000, 'refin':False, 'refout':False, 'xorout':0x00000000, 'check':0xbd0be338, 'residue':0x00000000},
{'name':'CRC-40/GSM', 'width':40, 'poly':0x0004820009, 'init':0x0000000000, 'refin':False, 'refout':False, 'xorout':0xffffffffff, 'check':0xd4164fc646, 'residue':0xc4ff8071ff},
{'name':'CRC-64/ECMA-182', 'width':64, 'poly':0x42f0e1eba9ea3693, 'init':0x0000000000000000, 'refin':False, 'refout':False, 'xorout':0x0000000000000000, 'check':0x6c40df5f0b497347, 'residue':0x0000000000000000},
{'name':'CRC-64/GO-ISO', 'width':64, 'poly':0x000000000000001b, 'init':0xffffffffffffffff, 'refin':True, 'refout':True, 'xorout':0xffffffffffffffff, 'check':0xb90956c775a41001, 'residue':0x5300000000000000},
{'name':'CRC-64/WE', 'width':64, 'poly':0x42f0e1eba9ea3693, 'init':0xffffffffffffffff, 'refin':False, 'refout':False, 'xorout':0xffffffffffffffff, 'check':0x62ec59e3f1a4f00a, 'residue':0xfcacbebd5931a992},
{'name':'CRC-64/XZ', 'width':64, 'poly':0x42f0e1eba9ea3693, 'init':0xffffffffffffffff, 'refin':True, 'refout':True, 'xorout':0xffffffffffffffff, 'check':0x995dc9bbdf1939fa, 'residue':0x49958c9abd7d353f},
{'name':'CRC-82/DARC', 'width':82, 'poly':0x0308c0111011401440411, 'init':0x000000000000000000000, 'refin':True, 'refout':True, 'xorout':0x000000000000000000000, 'check':0x09ea83f625023801fd612, 'residue':0x000000000000000000000}
]

