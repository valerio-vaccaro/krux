import pytest
from .shared_mocks import MockFile, mock_open


@pytest.fixture
def tdata(mocker):
    from collections import namedtuple
    from ur.ur import UR
    from urtypes.crypto.psbt import PSBT
    from krux.bbqr import encode_bbqr

    TEST_MNEMONIC = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

    # Legacy Singlesig
    P2PKH_PSBT = b'psbt\xff\x01\x00\xa4\x02\x00\x00\x00\x03\xae\xe25\xaf(\x9a\xc9\xee\xc23\xca"\x15\xbf?\xf4\xc1\xcaxAP\xd6\x0f[\x94kA\x87\x8b\x15\x04,\x00\x00\x00\x00\x00\xfd\xff\xff\xffT\xc9\x91i\xc4ZIg Z!\xd6)\xbf+z\x161\xc4uoS \xf0\x9d\x96\xcf#\xdc\xdbc\xa0\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x04\x1eVt\x8d\x80H\x1f\x89k\x07T(\xca\xaf\x91\x1e"\x1a2\xef\xa5_\\s\xf9\x8b\xc2J\xa0\xc8\x11\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x01\xe8\x03\x00\x00\x00\x00\x00\x00\x16\x00\x14\xae\xcd\x1e\xdc>\xffe\xaa \x9d\x02\x15\xe7=p\x90]\xc1hlZ\x0f+\x00O\x01\x045\x87\xcf\x03\x06\xb07\xf6\x80\x00\x00\x00k"\xc5\x12;\xa1\n\xde\xafK\xfc\xbbE\xd1\xa0-\x82\x8f%\xbf\x86F\x95z\x98\xd0b\x87\xc4\xe2\xb8P\x02\x8bB\xcdGv7l\x82y\x1bIAU\x15\x1fV\xc2\xd7\xb4q\xe0\xc7\xa5&\xa7\xce`\xdd\x87.8g\x10s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x01\x00~\x02\x00\x00\x00\x02\x9a\x9b\xe1\xca)\x10\\\x97t<\x0f\xd1\xeey\xc0\xe6\r"\x8aa\xc8\xec\xbft\xf9\xe7\xcf\xfa\x01\x19\x0c{\x02\x00\x00\x00\x00\xfd\xff\xff\xff\x9a\x9b\xe1\xca)\x10\\\x97t<\x0f\xd1\xeey\xc0\xe6\r"\x8aa\xc8\xec\xbft\xf9\xe7\xcf\xfa\x01\x19\x0c{\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x01@\x07\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xacZ\x0f+\x00\x01\x03\x04\x01\x00\x00\x00"\x06\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6\x18s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00U\x02\x00\x00\x00\x01\x873 i\xd7\x11\xa7\xcd*`\xd5\x84\x1c8\n,U\xe8\xa2\n\xdd\xdaV\xa2\x9c\x00\x84e\xef\xf6[\xa2\x01\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xac\x00\x00\x00\x00\x01\x03\x04\x01\x00\x00\x00"\x06\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6\x18s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00U\x02\x00\x00\x00\x01\x05j\xc0\xa7"\x1f\xe5\x82x\xc9\xa7h\xd0\x1a!\xe6\xb6GJ\x01\x9a\xf6\xe7?\x08\xc8R\xe6\x86|\xad\xa5\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xac\x00\x00\x00\x00\x01\x03\x04\x01\x00\x00\x00"\x06\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6\x18s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    P2PKH_PSBT_B43 = "GG*F8Q17IWZRLD2-18VY*1TXTGM*I+$R6ZULQ0*57H0JP/$S*/1MU2DNKKAF2TQ9DRXY:RGZ78NURNB7C8TK6LY29E7BIE9G7.99+L1U.2/PW68CG$AUH-2.S2YIFN9UQT4XMR5M1$TT5W+YR3U+XG:5RG/F+V5+4J9AFUW.ZE:YFX+/SE8T0MVUG5GR--W:9:7.ZRXCXM+$0JI:VPIF5GRR4K.LYVYRHR6C532UV++/AXRKCDNXT8CO-UZ+C4:XA/5SWA/Q.1G*.QAINY88NQ4JI-/7V+AW/Y9DFHU/L8FHLI0NRJI2C5$R1P2NS37$-K9-C-2-*5JJP.0:GD:B4D9.336TSMF*09EV4H+N-ZZXFV57+Z*GO-QTKZZ4R$9LCG+N97G-VOG:UCSKQTH.Y7O/RHS3LBM*/I+CFV2QODT7SJA*9N47MGX*Z/X4ZY2OY2-0TH7JKSU$ZTTB32Y4L0BKQCF*41$KFA1PEO2*/4+3$YV9/$DN*OZIO9Q:/HI7$94Q::8C9AG9U-/3UFQVJ94BZY*8DMT5QDBY4207KE12IKKWWYHN7+1.T*QVQYHQ2.Y-+VSM21FIB9CG4.63.I-OLBT-/M28*O-6+*DQV9HB-J/HEXIE.7$0H.UPJPRNIE.8TEYQCDYDPE9Q0E0D+HYP8YMJF2ODHGAT/E15-X:J.4J9P3Z-2R4:L2-S6CX7LF+I3A35M.BYF/XQLAJX92G1A-R0FF036U4Y2BKSI*/LAXWO9Q4KQBGJRLF:WZOE-:L76F2LJ5/-25TK7H$PMZON1AK735JQ0U9YZTLE$WMT.APZ65T8FR$NC9ZBXI46$B5-IG0$D8I-LF:TZCBJ81/0:V4$4*QX84ZP$Q/4120FZS:98YODBIL5W+EZ-+AXSPEW9/L+8Q0SGV*AX:8PSOAX+17:O+4V*7RA8YHD3OO-$57XMH7QH5TGCVBJHLZWQDI0*2VP6-5XNSK187-Y1C747124EI4B/XO3Z+-126R.5RA1.74WBV2DF:ECPVXEOXHPPAMP3ARKRH.IZQ.CQP9IKZN6+Z70WY+X:QSFHQFQJ-OZTM5F**E+KL4W:RE7OCI4ZC8SOEF89T5AA1O8XZGYZ*Q5AJSF2NQHE3H8DF-1S$GWHKFQX5JX0YWUV$"
    P2PKH_PSBT_B58 = "23c6ymBTk6EPbwvP3j8ozTBrkZ8TSBgW19wbakNqZTW8m7ac1XmyY8j9F7PezXGAa28kf8hdq2wF75LZhJWUNaCEwKMomEaRqcQwAfVXkTF9CzhGFtTv8XdhY7Xe8j1Phj9zJFCQ8MJ2d9Eb8kmRGmA6BcPHArVe9c5UrxQrUoXw3nJeLyGELYm6sd2bcu3gotYTejiJW2r3YcYxwnpKN32G9PsAeZ6oULLWG4rH7tKCUMWZkrPiQKdviZkpXJj3KybK21RsZCyvJnqWtCMKZBjE55TXkfWM3EC9TAStk2n85o72v2chGwJojXDdET4ZWpZgX9Qzfh9C24nsbedTGq1zNECwpbdvz43VUjz7LUtzNcfHhYipk6hD69he4dwFM4ACE2prm7b7wwmqonN7JMt59v1oZpDRphXbRxxPNvdao2kryGfrzhrk4H1UJWPouoUA7QaNW3wYENFHafw6cLyuQAETZ8RCYN2gujxw5QNZLSGB4HiKvPY1aQK6rvnE9DsiTzhEs5Rbrsd3H9BfRxoerAbUN4zxYPmgosrTNwnpDUtHvr2n6c1qGBJTu4o3wLHfm6VpyWiLrK9eissxhqAAuB2CnmdKhQq5t1RLDykYVbhJPCKzwchWr75jmAPKJRzAfZ7GUXx49YqdKcDtkJiRxHRUChh5ww2zYo8TpjHMAbHELosS7GsLhnzzPsyDnVPFaxWYwV6R7pFfZHXgMjp8zE6yEnHXoFvfNVegGFC9hnJgHm3VWw6k1cGKnh78kpW9pXih4GhV2KN6DueSonRtY6gVqVMp8jbtoXohr1vHuBag1VMvntfnFJDorjb1dtwRfbZ6bVNmY1C1efiwmF433hyEEbXPS477F2teZ2Guhj7EuEF785WxENndw27Knh4Z5DjStX9i7busoyFnE2vtZgEhrioa5cipTvaMins89yxSVNMJXf1aq6HCkqhE6p3seBPodq26KoJZNAB9qx4KhQpobGiM2y1bdpxourumW8cWJAWEJS1bFfJUSAH8b7u4y3DvxMYMpK3AjE1CqGtLECiyuikMwekuHtXTJX"
    P2PKH_PSBT_B64 = "cHNidP8BAKQCAAAAA67iNa8omsnuwjPKIhW/P/TBynhBUNYPW5RrQYeLFQQsAAAAAAD9////VMmRacRaSWcgWiHWKb8rehYxxHVvUyDwnZbPI9zbY6AAAAAAAP3///8EHlZ0jYBIH4lrB1Qoyq+RHiIaMu+lX1xz+YvCSqDIEQAAAAAA/f///wHoAwAAAAAAABYAFK7NHtw+/2WqIJ0CFec9cJBdwWhsWg8rAE8BBDWHzwMGsDf2gAAAAGsixRI7oQrer0v8u0XRoC2CjyW/hkaVepjQYofE4rhQAotCzUd2N2yCeRtJQVUVH1bC17Rx4MelJqfOYN2HLjhnEHPF2gosAACAAQAAgAAAAIAAAQB+AgAAAAKam+HKKRBcl3Q8D9HuecDmDSKKYcjsv3T558/6ARkMewIAAAAA/f///5qb4copEFyXdDwP0e55wOYNIophyOy/dPnnz/oBGQx7AQAAAAD9////AUAHAAAAAAAAGXapFDotQUWk8JhSOz6BJ/Hah8/FW455iKxaDysAAQMEAQAAACIGAqdFE5VzU2ny7N/IKcD3dOiO8TA9/lsvBNuqswpTXf3WGHPF2gosAACAAQAAgAAAAIAAAAAAAAAAAAABAFUCAAAAAYczIGnXEafNKmDVhBw4CixV6KIK3dpWopwAhGXv9luiAQAAAAD/////AQAAAAAAAAAAGXapFDotQUWk8JhSOz6BJ/Hah8/FW455iKwAAAAAAQMEAQAAACIGAqdFE5VzU2ny7N/IKcD3dOiO8TA9/lsvBNuqswpTXf3WGHPF2gosAACAAQAAgAAAAIAAAAAAAAAAAAABAFUCAAAAAQVqwKciH+WCeMmnaNAaIea2R0oBmvbnPwjIUuaGfK2lAAAAAAD/////AQAAAAAAAAAAGXapFDotQUWk8JhSOz6BJ/Hah8/FW455iKwAAAAAAQMEAQAAACIGAqdFE5VzU2ny7N/IKcD3dOiO8TA9/lsvBNuqswpTXf3WGHPF2gosAACAAQAAgAAAAIAAAAAAAAAAAAAA"
    P2PKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2PKH_PSBT).to_cbor())

    SIGNED_P2PKH_PSBT = b'psbt\xff\x01\x00\xa4\x02\x00\x00\x00\x03\xae\xe25\xaf(\x9a\xc9\xee\xc23\xca"\x15\xbf?\xf4\xc1\xcaxAP\xd6\x0f[\x94kA\x87\x8b\x15\x04,\x00\x00\x00\x00\x00\xfd\xff\xff\xffT\xc9\x91i\xc4ZIg Z!\xd6)\xbf+z\x161\xc4uoS \xf0\x9d\x96\xcf#\xdc\xdbc\xa0\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x04\x1eVt\x8d\x80H\x1f\x89k\x07T(\xca\xaf\x91\x1e"\x1a2\xef\xa5_\\s\xf9\x8b\xc2J\xa0\xc8\x11\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x01\xe8\x03\x00\x00\x00\x00\x00\x00\x16\x00\x14\xae\xcd\x1e\xdc>\xffe\xaa \x9d\x02\x15\xe7=p\x90]\xc1hlZ\x0f+\x00\x00\x01\x00~\x02\x00\x00\x00\x02\x9a\x9b\xe1\xca)\x10\\\x97t<\x0f\xd1\xeey\xc0\xe6\r"\x8aa\xc8\xec\xbft\xf9\xe7\xcf\xfa\x01\x19\x0c{\x02\x00\x00\x00\x00\xfd\xff\xff\xff\x9a\x9b\xe1\xca)\x10\\\x97t<\x0f\xd1\xeey\xc0\xe6\r"\x8aa\xc8\xec\xbft\xf9\xe7\xcf\xfa\x01\x19\x0c{\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x01@\x07\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xacZ\x0f+\x00"\x02\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6G0D\x02 \x14\x1e\xa4X\xff>l\x9d\xd8Dg\xda\xaf\x1b\xba9B\x94@eb\xbc\xb3\\\xe4\xa5O:N\xc8\x9c\xeb\x02 /\xa3%\xb6Qw\x8e\x1c\xda\xca\r\xa0\xb1,,ZCL\xa320u\xd5\xc7gT\'+\x82\x80\x00\xe5\x01\x00\x01\x00U\x02\x00\x00\x00\x01\x873 i\xd7\x11\xa7\xcd*`\xd5\x84\x1c8\n,U\xe8\xa2\n\xdd\xdaV\xa2\x9c\x00\x84e\xef\xf6[\xa2\x01\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xac\x00\x00\x00\x00"\x02\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6G0D\x02 a\xf4`\xa5W\xbd\xc5+\xa4\xaej\xfd\xf5,\x16\x98l\xd2\xd3X\x1aB\xee\xed\x13\xee\xd5\r\xf0J\xc9\x8d\x02 R\xa8\xfe\xa2]\xe6Y \xf3Q\xb1\xd5^G\xeaEpr\xcf,-\x90\xe5,\x18\xd4\x92\x84\xe5y\x8c\x02\x01\x00\x01\x00U\x02\x00\x00\x00\x01\x05j\xc0\xa7"\x1f\xe5\x82x\xc9\xa7h\xd0\x1a!\xe6\xb6GJ\x01\x9a\xf6\xe7?\x08\xc8R\xe6\x86|\xad\xa5\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xac\x00\x00\x00\x00"\x02\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6G0D\x02 /\xf9wQJ\x85J\xd6\xc0\xa7fY9S\x1ae\x7f\xedq\xc0\xc0\x98\x89\x80\x9a~\xe2\xf04\x90n\xb5\x02 (\x9bx\x99\xe0\xef\xc2\x0b\x01\r\xe1J\x93\xfc]Q\xed&Q\xce}\xb5\x91a\xc06\xdd\x1a\xaf\xd4\xb8\xaf\x01\x00\x00'
    SIGNED_P2PKH_PSBT_B43 = "BR$75LAJ*NO3F5WJXNJ1A:EL:+BDHMS4-Z5WYFOJ1854D.:B/CIMW*I35ZX6X:M:H:D-2RC51JGDI7G12DA4SLF$WS3/07UG8I7RNOKDFSE43J0+7R0J6..CAI5-OY-ATI:*L055QSOAOY9XZ2WQNNK9+55T9N-EX0/UV1WJ+32C5D1LRF9$MX:9B3RCO5NYRSGC..28STID/8F188UUUD2A:3$IP:UQBYV5-UU:4N8P1*YF2AU+H2YRH9W2OA5OS1YO6Z.DY/AFOWMN*IBZ6:7T1ZTT2/Z6ZE3BMDQ5QTPKZ76BBR0.YL$53WG*WT+742I0DEXIFSU8UCJJ4XOI25$N*THS4B.7J$B4YM:XWK$-DMI0-31FI9N.KS0$J2R4+597*/GTCHD*CUM.O102D7UC7MH7QI86NHAYPSO*UV-E4JL7CNKGLGLK4ZRJ-KYVDA$VBER.AV*ZKEG7/VUC8P2V5G7HG64+3YOCSU/K049/OFRB$$.2:Z77OHECAUSM99TXT1S/KAR-V8FBX4UHYU-7MWCSL68K61FLU1-TIUUNM616M/7HNN8J..06V63EQI*ACVR*Q2HQL:8LW3E/ID:EU$PUEG/E09FVJQ2IVI0WH:Q$Q$.X8OSH58YNUB3Y5DIJQ-IKW*69VT5/TQ6L20ZLDIEP4UBUQW8FJBD/+O9J:T/80HNI9KUC18JM59.WZQ8*DAT46-2*--08GZV8ZQC8$-QZHKUQ.+T.Y1A65VRK6I1YJDFULKFV4GW+/+0CC..ELCA3GGBP4XXZ7L1GJH7-25QWSF95F8W3A$39BJ7LCZGM/0:NO983:KGUBBQ:C5F:V7MA4QKOZYKFD4WH**YMMCQ2Y4GURTQ3+-6KBM1X6$/POH75K9LG:IKCS+E/.QF2R*D6:I.$E7VJN2:02DMP9$QL.PK5NCRBM*JL/J-+TY5ZU6OO07*X-6TO/K.5IQR+.5V7Z-INJ93SMRDR0FS+$6UV-E4N5TZEV38EREOX9C3:35VNHB722-$D2X-TP9ZA7T+K9$M0+/X*Q0.C-NCBAFLW+FWUSUU*B9V*TJRHF$U5YA3YNH*LP176A8EY-O5U.E-MMJK5X*4XP*RLXIKQG-/I3G7R+QET:FD8HJYRS:54LW5MPNLCPJBP3JVUAK+BEP7W8T-8CBS50U$R44-91.KZ0PEE"
    SIGNED_P2PKH_PSBT_B58 = "6XT9mnsYS6MLhfs4uWirQJGRNWXt7Qrs2f94yDPQ3y9c7ZmRhzpuGCvKnZLfFgDepYGRtqF4sDyfwykXMjppJZy4zxgkatKvZaoB8M9cp4jEYeWjTeqxTNXKVjDCHVRhswofDYqtEowhUsg76HhHzL1sZ4RitQJ1oQoqojkphmX1jjHL4AzJzkgoSCpMLvKh2TAVmqfhuv4Vid9gLiVBu5X1jHVdwUqQ8qnmcoP6ypGaVVoYWWaDhf9vrWi2tUhP4fNPWTVfj4txdC4a6yui28fdPW8UWu9f4h85tekokRpUWCHzJUhuXpahtiTbFsLhaw1PhpAbN5M3PEbs53poHiNFbG6rjLveyiDnyeW6vTGEecGcAgktvVzv2f5cBc9VwcfLUDqYN4bwdUpbzeuuHC3JeNwx2Q1pEspqZDhm94R3a6jw3g35CzaHZ5cMDfMKp7LFsbh4AgKD2HhvWMLk2EpSRc31Avet6j8ARCUXHRNRE9eay3NKy9AhE2zdQnEg42PVK5Sjs7PpT6QcvifdfaNAZ852eBQSTUk9X3oLXG43RaA2eNXmu92ydAfdWr9SyQ5WHKDhZq1xzcGnB4eaz1qJ1TpbWhkTnsEqsw3h6aqL2MWEpKjopKLn88gFSKN4nBUTz2ZvXdPqyZMuFVqnZ79LY1JaM77pyrdyc8G68VFhyMWADd4ABEeLdFq2a8yrTGkdq1V1ef3KWLJCKFV3WHEXcwQkKyS2t8XFgpKMJ1gGu5tQ8BYEzboUjP6EJs5dVZmcjNgwyh1MYpSHorm4AUyfGAoSiNjwWjjfM2F8z4JEWxLdfk4ufoG25gbrzbKrhQJjFNr3TeqZJBfVpEgsn8QjmaV7RBzrk7Whx3K51hx6HZe9JkUG9z5abmBA7FZQMACx8FRLRaZBxc7GiEf3hiT4Sv7fyUmTagViamSXbzvpHGqyaVnN7PD62yfxSzkFWwjVfPG78ufotrQ7fxJ4gfAcz7DgpH8xBe1GhPLuDZP1kDHi3JcoJ6CF8w9w3q4pkZVCtwB7AqTwimMXztLhdULWGDjBc3PVXmzfziCbc2CzJHzfzbxVqSAi8UA5WJzNXaiZhFTXV"
    SIGNED_P2PKH_PSBT_B64 = "cHNidP8BAKQCAAAAA67iNa8omsnuwjPKIhW/P/TBynhBUNYPW5RrQYeLFQQsAAAAAAD9////VMmRacRaSWcgWiHWKb8rehYxxHVvUyDwnZbPI9zbY6AAAAAAAP3///8EHlZ0jYBIH4lrB1Qoyq+RHiIaMu+lX1xz+YvCSqDIEQAAAAAA/f///wHoAwAAAAAAABYAFK7NHtw+/2WqIJ0CFec9cJBdwWhsWg8rAAABAH4CAAAAApqb4copEFyXdDwP0e55wOYNIophyOy/dPnnz/oBGQx7AgAAAAD9////mpvhyikQXJd0PA/R7nnA5g0iimHI7L90+efP+gEZDHsBAAAAAP3///8BQAcAAAAAAAAZdqkUOi1BRaTwmFI7PoEn8dqHz8VbjnmIrFoPKwAiAgKnRROVc1Np8uzfyCnA93TojvEwPf5bLwTbqrMKU1391kcwRAIgFB6kWP8+bJ3YRGfarxu6OUKUQGVivLNc5KVPOk7InOsCIC+jJbZRd44c2soNoLEsLFpDTKMyMHXVx2dUJyuCgADlAQABAFUCAAAAAYczIGnXEafNKmDVhBw4CixV6KIK3dpWopwAhGXv9luiAQAAAAD/////AQAAAAAAAAAAGXapFDotQUWk8JhSOz6BJ/Hah8/FW455iKwAAAAAIgICp0UTlXNTafLs38gpwPd06I7xMD3+Wy8E26qzClNd/dZHMEQCIGH0YKVXvcUrpK5q/fUsFphs0tNYGkLu7RPu1Q3wSsmNAiBSqP6iXeZZIPNRsdVeR+pFcHLPLC2Q5SwY1JKE5XmMAgEAAQBVAgAAAAEFasCnIh/lgnjJp2jQGiHmtkdKAZr25z8IyFLmhnytpQAAAAAA/////wEAAAAAAAAAABl2qRQ6LUFFpPCYUjs+gSfx2ofPxVuOeYisAAAAACICAqdFE5VzU2ny7N/IKcD3dOiO8TA9/lsvBNuqswpTXf3WRzBEAiAv+XdRSoVK1sCnZlk5Uxplf+1xwMCYiYCafuLwNJButQIgKJt4meDvwgsBDeFKk/xdUe0mUc59tZFhwDbdGq/UuK8BAAA="
    SIGNED_P2PKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(SIGNED_P2PKH_PSBT).to_cbor())
    SIGNED_P2PKH_PSBT_SD = b'psbt\xff\x01\x00\xa4\x02\x00\x00\x00\x03\xae\xe25\xaf(\x9a\xc9\xee\xc23\xca"\x15\xbf?\xf4\xc1\xcaxAP\xd6\x0f[\x94kA\x87\x8b\x15\x04,\x00\x00\x00\x00\x00\xfd\xff\xff\xffT\xc9\x91i\xc4ZIg Z!\xd6)\xbf+z\x161\xc4uoS \xf0\x9d\x96\xcf#\xdc\xdbc\xa0\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x04\x1eVt\x8d\x80H\x1f\x89k\x07T(\xca\xaf\x91\x1e"\x1a2\xef\xa5_\\s\xf9\x8b\xc2J\xa0\xc8\x11\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x01\xe8\x03\x00\x00\x00\x00\x00\x00\x16\x00\x14\xae\xcd\x1e\xdc>\xffe\xaa \x9d\x02\x15\xe7=p\x90]\xc1hlZ\x0f+\x00O\x01\x045\x87\xcf\x03\x06\xb07\xf6\x80\x00\x00\x00k"\xc5\x12;\xa1\n\xde\xafK\xfc\xbbE\xd1\xa0-\x82\x8f%\xbf\x86F\x95z\x98\xd0b\x87\xc4\xe2\xb8P\x02\x8bB\xcdGv7l\x82y\x1bIAU\x15\x1fV\xc2\xd7\xb4q\xe0\xc7\xa5&\xa7\xce`\xdd\x87.8g\x10s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x01\x00~\x02\x00\x00\x00\x02\x9a\x9b\xe1\xca)\x10\\\x97t<\x0f\xd1\xeey\xc0\xe6\r"\x8aa\xc8\xec\xbft\xf9\xe7\xcf\xfa\x01\x19\x0c{\x02\x00\x00\x00\x00\xfd\xff\xff\xff\x9a\x9b\xe1\xca)\x10\\\x97t<\x0f\xd1\xeey\xc0\xe6\r"\x8aa\xc8\xec\xbft\xf9\xe7\xcf\xfa\x01\x19\x0c{\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x01@\x07\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xacZ\x0f+\x00"\x02\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6G0D\x02 \x14\x1e\xa4X\xff>l\x9d\xd8Dg\xda\xaf\x1b\xba9B\x94@eb\xbc\xb3\\\xe4\xa5O:N\xc8\x9c\xeb\x02 /\xa3%\xb6Qw\x8e\x1c\xda\xca\r\xa0\xb1,,ZCL\xa320u\xd5\xc7gT\'+\x82\x80\x00\xe5\x01\x01\x03\x04\x01\x00\x00\x00"\x06\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6\x18s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00U\x02\x00\x00\x00\x01\x873 i\xd7\x11\xa7\xcd*`\xd5\x84\x1c8\n,U\xe8\xa2\n\xdd\xdaV\xa2\x9c\x00\x84e\xef\xf6[\xa2\x01\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xac\x00\x00\x00\x00"\x02\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6G0D\x02 a\xf4`\xa5W\xbd\xc5+\xa4\xaej\xfd\xf5,\x16\x98l\xd2\xd3X\x1aB\xee\xed\x13\xee\xd5\r\xf0J\xc9\x8d\x02 R\xa8\xfe\xa2]\xe6Y \xf3Q\xb1\xd5^G\xeaEpr\xcf,-\x90\xe5,\x18\xd4\x92\x84\xe5y\x8c\x02\x01\x01\x03\x04\x01\x00\x00\x00"\x06\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6\x18s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00U\x02\x00\x00\x00\x01\x05j\xc0\xa7"\x1f\xe5\x82x\xc9\xa7h\xd0\x1a!\xe6\xb6GJ\x01\x9a\xf6\xe7?\x08\xc8R\xe6\x86|\xad\xa5\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x19v\xa9\x14:-AE\xa4\xf0\x98R;>\x81\'\xf1\xda\x87\xcf\xc5[\x8ey\x88\xac\x00\x00\x00\x00"\x02\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6G0D\x02 /\xf9wQJ\x85J\xd6\xc0\xa7fY9S\x1ae\x7f\xedq\xc0\xc0\x98\x89\x80\x9a~\xe2\xf04\x90n\xb5\x02 (\x9bx\x99\xe0\xef\xc2\x0b\x01\r\xe1J\x93\xfc]Q\xed&Q\xce}\xb5\x91a\xc06\xdd\x1a\xaf\xd4\xb8\xaf\x01\x01\x03\x04\x01\x00\x00\x00"\x06\x02\xa7E\x13\x95sSi\xf2\xec\xdf\xc8)\xc0\xf7t\xe8\x8e\xf10=\xfe[/\x04\xdb\xaa\xb3\nS]\xfd\xd6\x18s\xc5\xda\n,\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    SIGNED_P2PKH_PSBT_B64_SD = "cHNidP8BAKQCAAAAA67iNa8omsnuwjPKIhW/P/TBynhBUNYPW5RrQYeLFQQsAAAAAAD9////VMmRacRaSWcgWiHWKb8rehYxxHVvUyDwnZbPI9zbY6AAAAAAAP3///8EHlZ0jYBIH4lrB1Qoyq+RHiIaMu+lX1xz+YvCSqDIEQAAAAAA/f///wHoAwAAAAAAABYAFK7NHtw+/2WqIJ0CFec9cJBdwWhsWg8rAE8BBDWHzwMGsDf2gAAAAGsixRI7oQrer0v8u0XRoC2CjyW/hkaVepjQYofE4rhQAotCzUd2N2yCeRtJQVUVH1bC17Rx4MelJqfOYN2HLjhnEHPF2gosAACAAQAAgAAAAIAAAQB+AgAAAAKam+HKKRBcl3Q8D9HuecDmDSKKYcjsv3T558/6ARkMewIAAAAA/f///5qb4copEFyXdDwP0e55wOYNIophyOy/dPnnz/oBGQx7AQAAAAD9////AUAHAAAAAAAAGXapFDotQUWk8JhSOz6BJ/Hah8/FW455iKxaDysAIgICp0UTlXNTafLs38gpwPd06I7xMD3+Wy8E26qzClNd/dZHMEQCIBQepFj/Pmyd2ERn2q8bujlClEBlYryzXOSlTzpOyJzrAiAvoyW2UXeOHNrKDaCxLCxaQ0yjMjB11cdnVCcrgoAA5QEBAwQBAAAAIgYCp0UTlXNTafLs38gpwPd06I7xMD3+Wy8E26qzClNd/dYYc8XaCiwAAIABAACAAAAAgAAAAAAAAAAAAAEAVQIAAAABhzMgadcRp80qYNWEHDgKLFXoogrd2lainACEZe/2W6IBAAAAAP////8BAAAAAAAAAAAZdqkUOi1BRaTwmFI7PoEn8dqHz8VbjnmIrAAAAAAiAgKnRROVc1Np8uzfyCnA93TojvEwPf5bLwTbqrMKU1391kcwRAIgYfRgpVe9xSukrmr99SwWmGzS01gaQu7tE+7VDfBKyY0CIFKo/qJd5lkg81Gx1V5H6kVwcs8sLZDlLBjUkoTleYwCAQEDBAEAAAAiBgKnRROVc1Np8uzfyCnA93TojvEwPf5bLwTbqrMKU1391hhzxdoKLAAAgAEAAIAAAACAAAAAAAAAAAAAAQBVAgAAAAEFasCnIh/lgnjJp2jQGiHmtkdKAZr25z8IyFLmhnytpQAAAAAA/////wEAAAAAAAAAABl2qRQ6LUFFpPCYUjs+gSfx2ofPxVuOeYisAAAAACICAqdFE5VzU2ny7N/IKcD3dOiO8TA9/lsvBNuqswpTXf3WRzBEAiAv+XdRSoVK1sCnZlk5Uxplf+1xwMCYiYCafuLwNJButQIgKJt4meDvwgsBDeFKk/xdUe0mUc59tZFhwDbdGq/UuK8BAQMEAQAAACIGAqdFE5VzU2ny7N/IKcD3dOiO8TA9/lsvBNuqswpTXf3WGHPF2gosAACAAQAAgAAAAIAAAAAAAAAAAAAA"

    # Native Segwit Singlesig
    P2WPKH_PSBT = b'psbt\xff\x01\x00q\x02\x00\x00\x00\x01\xcf<X\xc3)\x82\xae P\x88\xd9\xbdI\xeb\x9b\x02\xac\xdfM=\xaev\xa5\x16\xc6\xb3\x06\xb1]\xe3\xa1N\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02|?]\x05\x00\x00\x00\x00\x16\x00\x14/4\xaa\x1c\xf0\nS\xb0U\xa2\x91\xa0:}E\xf0\xa6\x98\x8bR\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01\x1f\x00\xe1\xf5\x05\x00\x00\x00\x00\x16\x00\x14\xd0\xc4\xa3\xef\t\xe9\x97\xb6\xe9\x9e9~Q\x8f\xe3\xe4\x1a\x11\x8c\xa1"\x06\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x02\x03]I\xec\xcdT\xd0\t\x9eCgbw\xc7\xa6\xd4b]a\x1d\xa8\x8a]\xf4\x9b\xf9Qzw\x91\xa7w\xa5\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    P2WPKH_PSBT_B43 = "1N0HGUN:R2Q*R86JDWEOBMHAETS.D$7T+SEGWXJO3JPKXA+O3JNN$$VLXOA4R/O+2+T$0BL68OC3*:/B4SOZWX3MY9B1R0AXW5-KVBGEJJWUNUTMA5-XE+IX*M5$/.++VV9F/RHZC9:E9JT$NLGK39-VJKFHLA*C90GDVYE01C17+N*JBV0RQLT8D*1*BVK+K2K/$8.VYDK3JPC2X634YJKT57OJNX61X$4J39$.4*TZK55UAA0ALQC0PLZC61AYGB$J:SKX63U23TBU.C9NB.9C0N$RKANBNTQTYPVL1ZG6SHLT093GQFJILC0QMUYEY9F-K8.-3:JMZ4ESOL8AO+CD*7U06IVD3U6Y.$HH5PU/NPL037224KA-1A09MM76ZJ.:HY4TS-Y/8MZC6P/D6*DQF6A9"
    P2WPKH_PSBT_B58 = "UUucvki6KWyS35DhetbWPw1DiaccbHKywScF96E8VUwEnN1gss947UasRfkNxtrkzCeHziHyMCuoiQ2mSYsbYXuV3YwYBZwFh1c6xtBAEK1aDgPwMgqf74xTzf3m4KH4iUU5nHTqroDpoRZR59meafTCUBChZ5NJ8MoUdKE6avyYdSm5kUb4npmFpMpJ9S3qd2RedHMoQFRiXK3jwdH81emAEsFYSW3Kb7caPcWjkza4S4EEWWbaggofGFmxE5gNNg4A4LNC2ZUGLsALZffNvg3yh3qg6rFxhkiyzWc44kx9Khp6Evm1j4Njh8kjifkngLTPFtX3uWNLAB1XrvpPMx6kkkhr7RnFVrA4JsDp5BwVGAXBoSBLTqweFevZ5"
    P2WPKH_PSBT_B64 = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAABAR8A4fUFAAAAABYAFNDEo+8J6Ze26Z45flGP4+QaEYyhIgYC56slN7XUnpcDCargbp5J82zhyf671E7I4NHMoLT5wxkYc8XaClQAAIABAACAAAAAgAAAAAAAAAAAACICA11J7M1U0AmeQ2did8em1GJdYR2oil30m/lReneRp3elGHPF2gpUAACAAQAAgAAAAIABAAAAAAAAAAAA"
    P2WPKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2WPKH_PSBT).to_cbor())
    P2WPKH_PSBT_BBQR_PSBT = P2WPKH_PSBT  # BBQr is decoded to binary before being passed to the PSBT constructor

    SIGNED_P2WPKH_PSBT = b'psbt\xff\x01\x00q\x02\x00\x00\x00\x01\xcf<X\xc3)\x82\xae P\x88\xd9\xbdI\xeb\x9b\x02\xac\xdfM=\xaev\xa5\x16\xc6\xb3\x06\xb1]\xe3\xa1N\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02|?]\x05\x00\x00\x00\x00\x16\x00\x14/4\xaa\x1c\xf0\nS\xb0U\xa2\x91\xa0:}E\xf0\xa6\x98\x8bR\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01\x1f\x00\xe1\xf5\x05\x00\x00\x00\x00\x16\x00\x14\xd0\xc4\xa3\xef\t\xe9\x97\xb6\xe9\x9e9~Q\x8f\xe3\xe4\x1a\x11\x8c\xa1"\x02\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19G0D\x02 >e\xff;L\xd4\x7f\x12\x1f\xa7\xc9\x82(F\x18\xdb\x801G\xb0V\xd3\x93\x94\xd4\xecB\x0e\xfd\xfck\xa1\x02 l\xbd\xd8\x8a\xc5\x18l?.\xfd$%1\xedy\x17uvQ\xac&#t\xf3\xd3\x1d\x85\xd6\x16\xcdj\x81\x01\x00\x00\x00'
    SIGNED_P2WPKH_PSBT_B43 = "ZF1XCF+Z*C015XRRLXYR*QCNLC+GG904*T:WKMSDWEXX2VS57*S7X9FJGRN/0Q0$-OBHIJ8/B.C-BG*2ITD2B9C5VJ0AVI5GAH7LMHJ3.EY3KL*/6I*ERF8GTDFTN5KA6Z-NUJ0UV/2NBXH43OSU3T98BSCAIZ.:HWRXU/L.HMUDEJEO$3.C/80-LULS/CM0DV*$3*EM/736NIXS-0+:E-A4TDYZRGW9W181MRBNJ6A*O$VO/VT+SAX+TVO4DH.$Q$MKU6OFVP94EX8LXOK6F69TJI8T.38.BLI.55W3/928OSS-1SK022VB+Q0WZ3F33NB*EE:$*YD+*1BK.SU1EV3M2C4UG.PA.T--YRP8BB/QH:V-9F4B/XUZYCDUDAYG/CR4VT15"
    SIGNED_P2WPKH_PSBT_B58 = "2HkajtjMgNpiuo5QQYDP4zEc3vrWa1f7qgwNkMySr8EJbPoEtguwAQ2qkgA7k7NzAvLjA3FA4C9ejVxLx8vSemVQxcda4LjDyrbpinuPeSakKBjvR1XrCa5jxU29xfiaYjLTKDPPAPHCdTJy4r7Zcc9kqaTk9NxoqMhdUiNqxfyuBoDeCwMemE2UE4D5GrDMMuhJvJ2vyJkK6w9a1P7cE6gwL4CVx7LrLtwRGbUUiQ3tkr8ve57kWjyTLT1FALNVVyNfDb4kJccqZ6Nv1riwPaRRUpr2yaBkTogG4nAK31ywpiAwqxZpswjUF6gpbnLJUQDsowNjYeW9NEA83S2oL3FshKWsfcB1vhKT5DvCQZzo"
    SIGNED_P2WPKH_PSBT_B64 = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAABAR8A4fUFAAAAABYAFNDEo+8J6Ze26Z45flGP4+QaEYyhIgIC56slN7XUnpcDCargbp5J82zhyf671E7I4NHMoLT5wxlHMEQCID5l/ztM1H8SH6fJgihGGNuAMUewVtOTlNTsQg79/GuhAiBsvdiKxRhsPy79JCUx7XkXdXZRrCYjdPPTHYXWFs1qgQEAAAA="
    SIGNED_P2WPKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(SIGNED_P2WPKH_PSBT).to_cbor())
    SIGNED_P2WPKH_PSBT_BBQR_PSBT = encode_bbqr(SIGNED_P2WPKH_PSBT, "Z", "P")
    SIGNED_P2WPKH_PSBT_SD = b'psbt\xff\x01\x00q\x02\x00\x00\x00\x01\xcf<X\xc3)\x82\xae P\x88\xd9\xbdI\xeb\x9b\x02\xac\xdfM=\xaev\xa5\x16\xc6\xb3\x06\xb1]\xe3\xa1N\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02|?]\x05\x00\x00\x00\x00\x16\x00\x14/4\xaa\x1c\xf0\nS\xb0U\xa2\x91\xa0:}E\xf0\xa6\x98\x8bR\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01\x1f\x00\xe1\xf5\x05\x00\x00\x00\x00\x16\x00\x14\xd0\xc4\xa3\xef\t\xe9\x97\xb6\xe9\x9e9~Q\x8f\xe3\xe4\x1a\x11\x8c\xa1"\x02\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19G0D\x02 >e\xff;L\xd4\x7f\x12\x1f\xa7\xc9\x82(F\x18\xdb\x801G\xb0V\xd3\x93\x94\xd4\xecB\x0e\xfd\xfck\xa1\x02 l\xbd\xd8\x8a\xc5\x18l?.\xfd$%1\xedy\x17uvQ\xac&#t\xf3\xd3\x1d\x85\xd6\x16\xcdj\x81\x01"\x06\x02\xe7\xab%7\xb5\xd4\x9e\x97\x03\t\xaa\xe0n\x9eI\xf3l\xe1\xc9\xfe\xbb\xd4N\xc8\xe0\xd1\xcc\xa0\xb4\xf9\xc3\x19\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00"\x02\x03]I\xec\xcdT\xd0\t\x9eCgbw\xc7\xa6\xd4b]a\x1d\xa8\x8a]\xf4\x9b\xf9Qzw\x91\xa7w\xa5\x18s\xc5\xda\nT\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    SIGNED_P2WPKH_PSBT_B64_SD = "cHNidP8BAHECAAAAAc88WMMpgq4gUIjZvUnrmwKs3009rnalFsazBrFd46FOAAAAAAD9////Anw/XQUAAAAAFgAULzSqHPAKU7BVopGgOn1F8KaYi1KAlpgAAAAAABYAFOZq/v/Dg45x8KJ7B+OwDt5q6OFgAAAAAAABAR8A4fUFAAAAABYAFNDEo+8J6Ze26Z45flGP4+QaEYyhIgIC56slN7XUnpcDCargbp5J82zhyf671E7I4NHMoLT5wxlHMEQCID5l/ztM1H8SH6fJgihGGNuAMUewVtOTlNTsQg79/GuhAiBsvdiKxRhsPy79JCUx7XkXdXZRrCYjdPPTHYXWFs1qgQEiBgLnqyU3tdSelwMJquBunknzbOHJ/rvUTsjg0cygtPnDGRhzxdoKVAAAgAEAAIAAAACAAAAAAAAAAAAAIgIDXUnszVTQCZ5DZ2J3x6bUYl1hHaiKXfSb+VF6d5Gnd6UYc8XaClQAAIABAACAAAAAgAEAAAAAAAAAAAA="

    # Nested Segwit Singlesig
    P2SH_P2WPKH_PSBT = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01v\xefk\xf2\xbd\xd0@\xf3\xc1\xd8:\xcc\xb9t9\xf1\xab\xb1\xa5V\xad\x1d\x0fR\x96\x81\xff\xa7\xe8\xca\x94\x8a\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02\x9c=]\x05\x00\x00\x00\x00\x17\xa9\x14%\x1d\xd1\x14W\xa2Y\xc3\xbaG\xe5\xcc\xa3q\x7f\xe4!N\x02\x98\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x143l\xaa\x13\xe0\x8b\x96\x08\n2\xb5\xd8\x18\xd5\x9bJ\xb3\xb3gB\x87\x01\x04\x16\x00\x148\x97\x1fs\x93\x0fl\x14\x1d\x97z\xc4\xfdJr|\x85I5\xb3"\x06\x03\xa1\xaf\x80J\xc1\x08\xa8\xa5\x17\x82\x19\x8c-\x03K(\xbf\x90\xc8\x80?ZS\xf7bv\xfai\xa4\xea\xe7\x7f\x18s\xc5\xda\n1\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x16\x00\x14p\xbe\xb1\xe0JP\t@\xe9\xf3\xab\xaaf\xe1\xa4\x9a\xc5[\x8f5"\x02\x02\xa2\xfc\x89\x96\xc5&"H\xb5\xda\xef\xc5\xa4\xd0\xcd\xcd\x00\xc10G\xd0\xcb\x13\x02\x816\xeac\r\x87Z\x87\x18s\xc5\xda\n1\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    P2SH_P2WPKH_PSBT_B43 = "ISOGTD+S3R8H0DQLFI44D9XVW+NU6FLJ-.-6DZON$.R31OG$AFCWZGO40V:6HQ.DT2C3.CPVM-F+V+GB$A9G:.K3B:KCWPOU8.LZ4SO1D-W/:PCK5Y1.B$HQGWWR1BN8:9J-HXGFVVL1D3R+MTLP/10MGI6AN$1*5ITO3105-C1QBR+LAR5D7VM/1P*KBYJH6P4LH9GCU5DE2*8MP3*YT2K.KDV32OAMNKHV/VGLX9XJ0*B6850S794RVAWR*LEY40SCBLQ.*OR7T$RZ9581/GKU4KYV48LDPURZMDKBEZXRG2SDL4UYGF330F$4*1JCUL5TS+:*X*+E6D::-0L1L63IAMW:*IVLP$YQUV922+G$OJY.INJRHY/A$0.UFB.VD21PM8ED92HKS5TXCAPFS9LT199UMOMBNKM$HE*7*VOJQ*J7JY1PLG188K8IB97211B+AH$4$GDJ750S--S.H45Y4HA4N$PK5S03HS4K"
    P2SH_P2WPKH_PSBT_B58 = "W7hsNtPR1YU4YQRATn9QwVubQ3s4aLKhoSpCJQtZuiqGxTQPhu1FB4bqZdtL2MpygirLgext5jZpLSRKGQEhcuiUjg5wvnyP5EP7w1RxkE4Zc5mxDKyEhRH7k3wcSA8TTahF7Rg7r2cWry4c7LySnwoAGtYP1VRwcgMfbYXroHrrKqgdfaKLmMD1M5bCYpU6fMCzcEK5hXQSFaupmhTyAPHiGAczMSmnsoaeZ4cCNpZzexK6FkYES1XTBkroLD68tYejJTjkEpASRVTwS1LUJHEUVmAgASWQ1r3x9yGQaSamXqvedoZ3dNuUsmVJNdGNjKFJRsQugzxEHEj2PWJCpYCUo4Ms79wRkSYjeaQaEEHnBLnkbhPdL6rUu5oGCpzkkgewTcH5hSPA8GefzSgLo3CrGQgY5K3GvPTH5aP6VvMWpUBHGiPqddjQzqeAePxKHi6T"
    P2SH_P2WPKH_PSBT_B64 = "cHNidP8BAHICAAAAAXbva/K90EDzwdg6zLl0OfGrsaVWrR0PUpaB/6foypSKAQAAAAD9////Apw9XQUAAAAAF6kUJR3RFFeiWcO6R+XMo3F/5CFOApiHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAAAAAQEgAOH1BQAAAAAXqRQzbKoT4IuWCAoytdgY1ZtKs7NnQocBBBYAFDiXH3OTD2wUHZd6xP1KcnyFSTWzIgYDoa+ASsEIqKUXghmMLQNLKL+QyIA/WlP3Ynb6aaTq538Yc8XaCjEAAIABAACAAAAAgAAAAAAAAAAAAAEAFgAUcL6x4EpQCUDp86uqZuGkmsVbjzUiAgKi/ImWxSYiSLXa78Wk0M3NAMEwR9DLEwKBNupjDYdahxhzxdoKMQAAgAEAAIAAAACAAQAAAAAAAAAAAA=="
    P2SH_P2WPKH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2SH_P2WPKH_PSBT).to_cbor())

    SIGNED_P2SH_P2WPKH_PSBT = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01v\xefk\xf2\xbd\xd0@\xf3\xc1\xd8:\xcc\xb9t9\xf1\xab\xb1\xa5V\xad\x1d\x0fR\x96\x81\xff\xa7\xe8\xca\x94\x8a\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02\x9c=]\x05\x00\x00\x00\x00\x17\xa9\x14%\x1d\xd1\x14W\xa2Y\xc3\xbaG\xe5\xcc\xa3q\x7f\xe4!N\x02\x98\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x143l\xaa\x13\xe0\x8b\x96\x08\n2\xb5\xd8\x18\xd5\x9bJ\xb3\xb3gB\x87"\x02\x03\xa1\xaf\x80J\xc1\x08\xa8\xa5\x17\x82\x19\x8c-\x03K(\xbf\x90\xc8\x80?ZS\xf7bv\xfai\xa4\xea\xe7\x7fG0D\x02 u\x0c\xf8\xe6\x03\x15l\xab\xaa7a`\x1f\xcb\xc5\xd92TC\x97\xbd\xed\xfeS\xeeC\xf4\x1d\xddc\x1cx\x02 4{\xe5K\xe5\xf2F\x04\xd5\x05V\xe8}K\x00\xcc\x93)\x90\x1f\r\x02,\xee?\xd8\xed\xd2\xb8\x97\xcaS\x01\x01\x04\x16\x00\x148\x97\x1fs\x93\x0fl\x14\x1d\x97z\xc4\xfdJr|\x85I5\xb3\x00\x00\x00'
    SIGNED_P2SH_P2WPKH_PSBT_B43 = "H2ZW15J2ZL-VL/WIC5AQ67IT6:2*PR$1PNPWZ67EY3.D*MU1XLGL2:M$73JM9*$9Q6EJCOAWF:258LFQ$D209+HXGLHAW1P7F0GS3/9*+TM4.972T18+WAVDG0FBTR7KD*GY.UQ*2$$O:7L015ZB$TIRBR0X0JW7FTWZJOFA2BXZ-+F2DCNJ6CGT0:5GR5BJE8XE/G*Y3S0$11D4*F.C8OGM-M*UQDY-2X0+NF6X106N2$9FZSA-*6WIW+ET$79KLN8AVDGO*6Z+ON4J43Z5S*A$UZEH5VNKO.ZQKD+VC/BJANEHK+OLCBD5H1GSQUMOHJ6VO//5Q1515V6YKJ4FLMG8OU-2M-S.+GS+T10EI6EP*GCYGQPD9389V01Q52.$A+3O-YCO55.Q*BOXPW2CF.VEPR:.HWZ**QA5NITVI3:MQWKL"
    SIGNED_P2SH_P2WPKH_PSBT_B58 = "mbNU9ochR3r2kucYTPNx2gt6qUqhQ2BCrRrQkjve3E7b4YoV1fG7Nno8bcE4Rtq5jiXfYNV1LYeRYPwek67KsJdfTL1y2pxK6Kis2hA2GF7s3eJkUzXdTBPGpmMW39bAnU2315fnDjfanJxRJsj9iefvwteXmCR2mY1vFZwDJ9E66mmtjXQjQ57bD33WoAbZqJjYucy5u8d1HmSAwBaMqfzYYNyjNkAKDCD1Jd3CZfcwo5jB1qLeq3i3hu4XGB8puf4fJ9B3uGjMAaL5Po32Wrw5RaAPBJ39hXJBskvsEKC6gcHEP92oXsTTDHQWrsAnLMs1fkjEBsvjHsWsff6PebdDCLdzRGoJavc5TUTyaydbitxWfUQT99ZCuoKQkxhGqVC65euWJCFSSR67"
    SIGNED_P2SH_P2WPKH_PSBT_B64 = "cHNidP8BAHICAAAAAXbva/K90EDzwdg6zLl0OfGrsaVWrR0PUpaB/6foypSKAQAAAAD9////Apw9XQUAAAAAF6kUJR3RFFeiWcO6R+XMo3F/5CFOApiHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAAAAAQEgAOH1BQAAAAAXqRQzbKoT4IuWCAoytdgY1ZtKs7NnQociAgOhr4BKwQiopReCGYwtA0sov5DIgD9aU/didvpppOrnf0cwRAIgdQz45gMVbKuqN2FgH8vF2TJUQ5e97f5T7kP0Hd1jHHgCIDR75Uvl8kYE1QVW6H1LAMyTKZAfDQIs7j/Y7dK4l8pTAQEEFgAUOJcfc5MPbBQdl3rE/UpyfIVJNbMAAAA="
    SIGNED_P2SH_P2WPKH_PSBT_UR_PSBT = UR(
        "crypto-psbt", PSBT(SIGNED_P2SH_P2WPKH_PSBT).to_cbor()
    )
    SIGNED_P2SH_P2WPKH_PSBT_SD = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01v\xefk\xf2\xbd\xd0@\xf3\xc1\xd8:\xcc\xb9t9\xf1\xab\xb1\xa5V\xad\x1d\x0fR\x96\x81\xff\xa7\xe8\xca\x94\x8a\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02\x9c=]\x05\x00\x00\x00\x00\x17\xa9\x14%\x1d\xd1\x14W\xa2Y\xc3\xbaG\xe5\xcc\xa3q\x7f\xe4!N\x02\x98\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x143l\xaa\x13\xe0\x8b\x96\x08\n2\xb5\xd8\x18\xd5\x9bJ\xb3\xb3gB\x87"\x02\x03\xa1\xaf\x80J\xc1\x08\xa8\xa5\x17\x82\x19\x8c-\x03K(\xbf\x90\xc8\x80?ZS\xf7bv\xfai\xa4\xea\xe7\x7fG0D\x02 u\x0c\xf8\xe6\x03\x15l\xab\xaa7a`\x1f\xcb\xc5\xd92TC\x97\xbd\xed\xfeS\xeeC\xf4\x1d\xddc\x1cx\x02 4{\xe5K\xe5\xf2F\x04\xd5\x05V\xe8}K\x00\xcc\x93)\x90\x1f\r\x02,\xee?\xd8\xed\xd2\xb8\x97\xcaS\x01\x01\x04\x16\x00\x148\x97\x1fs\x93\x0fl\x14\x1d\x97z\xc4\xfdJr|\x85I5\xb3"\x06\x03\xa1\xaf\x80J\xc1\x08\xa8\xa5\x17\x82\x19\x8c-\x03K(\xbf\x90\xc8\x80?ZS\xf7bv\xfai\xa4\xea\xe7\x7f\x18s\xc5\xda\n1\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x16\x00\x14p\xbe\xb1\xe0JP\t@\xe9\xf3\xab\xaaf\xe1\xa4\x9a\xc5[\x8f5"\x02\x02\xa2\xfc\x89\x96\xc5&"H\xb5\xda\xef\xc5\xa4\xd0\xcd\xcd\x00\xc10G\xd0\xcb\x13\x02\x816\xeac\r\x87Z\x87\x18s\xc5\xda\n1\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    SIGNED_P2SH_P2WPKH_PSBT_B64_SD = "cHNidP8BAHICAAAAAXbva/K90EDzwdg6zLl0OfGrsaVWrR0PUpaB/6foypSKAQAAAAD9////Apw9XQUAAAAAF6kUJR3RFFeiWcO6R+XMo3F/5CFOApiHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAAAAAQEgAOH1BQAAAAAXqRQzbKoT4IuWCAoytdgY1ZtKs7NnQociAgOhr4BKwQiopReCGYwtA0sov5DIgD9aU/didvpppOrnf0cwRAIgdQz45gMVbKuqN2FgH8vF2TJUQ5e97f5T7kP0Hd1jHHgCIDR75Uvl8kYE1QVW6H1LAMyTKZAfDQIs7j/Y7dK4l8pTAQEEFgAUOJcfc5MPbBQdl3rE/UpyfIVJNbMiBgOhr4BKwQiopReCGYwtA0sov5DIgD9aU/didvpppOrnfxhzxdoKMQAAgAEAAIAAAACAAAAAAAAAAAAAAQAWABRwvrHgSlAJQOnzq6pm4aSaxVuPNSICAqL8iZbFJiJItdrvxaTQzc0AwTBH0MsTAoE26mMNh1qHGHPF2goxAACAAQAAgAAAAIABAAAAAAAAAAAA"

    # Taproot Singlesig
    P2TR_PSBT = b"psbt\xff\x01\x00\xa8\x02\x00\x00\x00\x01\xf9\xfe\xa6\x15\x16\xa0\x07\xe4v2WHAq\x8d\xc0\xda\\\x1a\xf6\xd9\x173\x7f\x06\x8eT\xda\xbeI\xbe?\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x03:\x1e\x00\x00\x00\x00\x00\x00\"Q u\xe6_\x88=\xe5\x87'1\xd9\x8e\xa8o_\x08b\xf0\x929\xd0\xe9\xb0\x0fI\xf5\x92\x06\x9c\x18M\x02\xa2\xe8\x03\x00\x00\x00\x00\x00\x00\"Q \x9d-\x9bm\xe6\x0c\xdc\xddY\x07\xc1\xc0\x961I\x1b\xddCN\xee\xaa\x8a\xaf;;\xf1\x9dc\xd5>@\x99\xe8\x03\x00\x00\x00\x00\x00\x00\x16\x00\x14\xae\xcd\x1e\xdc>\xffe\xaa \x9d\x02\x15\xe7=p\x90]\xc1hl\x83\xbf+\x00O\x01\x045\x87\xcf\x03\xe0\x17\xd1\xbb\x80\x00\x00\x00\x01\x83\\\x0bQ!\x83v\xc6\x14UB\x8a\x9fG\xbf\xcc\xe1\xf6\xce\x83\x97\xea\xd7\xb0\x03\x87\xe9\xd9\xeaV\x83\x02\xcf\xbdq\x001\x1e\x0e\x85\x84L78r\x83\x149N\xb80*kPp\xd6\x92\xe4\x1b\x14\xba\x81\x80\x90\x10s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x01\x01+\x7f'\x00\x00\x00\x00\x00\x00\"Q \x06\xac\x82\xfc6\xdb\xb6\rHy\x1d\x81\xc3\xc1\xeb9\x7f\xa9s\xe4V\xc8\xc6\xfbT\xc1\x04!\x1f\x04{\x1a\x01\x03\x04\x00\x00\x00\x00!\x16E\xc6\xb1\xe44\x82<\xe9\xe6\xb4H\xfb\xc1\xe4\x05' 8:\r!(\x82\xbc\xbavSMwR\x8a\xad\x19\x00s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\t\x00\x00\x00\x01\x17 E\xc6\xb1\xe44\x82<\xe9\xe6\xb4H\xfb\xc1\xe4\x05' 8:\r!(\x82\xbc\xbavSMwR\x8a\xad\x00!\x07 \xeb\x90P\x06\x8b\x01;\xde= M\xb5\x9a\xc5\xdb*\x1cx\xa8\xaa%\x07?\xbf.z\xd4\x9d\x05\x15\xc6\x19\x00s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x01\x00\x00\x00\x01\x05  \xeb\x90P\x06\x8b\x01;\xde= M\xb5\x9a\xc5\xdb*\x1cx\xa8\xaa%\x07?\xbf.z\xd4\x9d\x05\x15\xc6\x00!\x07\xdc\xab\x8eB3\xd9\x14\xf2\x98\x08\x9e]\x8d;'a\x8a\x07\xf5!?\x89\x9a+\xbd\xbax\xfd\xb9\x02\xc5\xcf\x19\x00s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\n\x00\x00\x00\x01\x05 \xdc\xab\x8eB3\xd9\x14\xf2\x98\x08\x9e]\x8d;'a\x8a\x07\xf5!?\x89\x9a+\xbd\xbax\xfd\xb9\x02\xc5\xcf\x00\x00"
    P2TR_PSBT_B43 = "$MYCB*Z8$F$U43$$$AYNPYV7P2O$0N:NND-4/R6WA3K5UCTN2W2UH1W+-OO$GDVLG22/ZLRV1Q8.E8J7N420ZF-M4JE.DG07WFA+62X4.4ZA-OVEWYBN:QE73QV1QF+4N7281Z2I5S1N6Y9644OHRR*SE9ZV14W2K$43KBK:SHCYT$B0YG1-J6YXZKKN4676SPPD4DGPLT3L.8E117P1-7E4YOJWP2IPW81BC3TQ3YX2OP8MONZD+O8DV95:K93RLFWQSYIDM2YKLVSKZ*+K:WWO6-3H4:.J97WXTVTUL3/+8HAKSL9+8BPQHJK-MQ5SALS79II3T:P*C6D*1ZYSDDAZ82F0W*WRR91/:YOFKC9EFMQ1CSK2HN-HCLBXVRKS4/G:6MJ61OP$08QL0X:YAJGL*IL:D*/56V1/ZFDEM*3*F-NVZNQAIEFMF08Z2MM0I$S2B61W$EY++.6X**AH0CWY9DWE4D2U*E3AECQE2Y5R1ZHTOG1MKTZ3GHTBD7F02K-DPZL+ABUVMIELQWT:M+5.FT9-RAY3OS05+/J-S*BIOI0Q6YT$UQ-RI/.429T2/:66YNAHKCVH3J7AGS46TAHCI$JSJ9*NPE2XZWW+1L30SDVFNULC4T75VP:XBBXP9I750LGP1:8ZDP0YF*BKWQZ93-U2Q0EJSJ9WB3A0ZJGLNQ57BXMVSRPDDSI+7D9B8ZKBG7X+:U84V5DMYSW3W/*I*/*UB8MJQV0+2BSQTARB$DND/9N9.+T-6O8D*74K5M+LXP*-4I:P79JX-RJH2-MKW:X5DSO13Y0AASMVOAS/28/F9Q4$B*VL.$RW0ZO.UH5T7ODJS47.MA$AK3RQ/3L4O+KWU5E:SJ..:*X:GU*HCV9-HX7$2T-/9ZAY7J3W.7W+1Y-$IM6-"
    P2TR_PSBT_B58 = "2C2dk2DpdViMV7XztuFHDKYpnMmQYUHxBC97tosVRCndABjAHMnx5Vjw2Hugev5DyrLPXfM58fxKHCcGdReZxLRr4ZDaXRy7SCssavWr9NgP7aPqbGnDZJirLEgau5p12f1FmEwoSMD9ZnrjoFwPZF5AhYr3R7ixUn7Kf7LDW63sdPV45a5z6CeUQvDELrxxyKVG4qej4GEH5DgED8PWFNQ4nq8cKU2TJL8oNZrMMSGSopG1YzEvoFf7fUzpZR6dC2hgBnEBGZWTccnAoA418aauwZU2dBqWYire6nhXsKZF4cVKweMFt8ZGFT3YRjM5uqc4i2ii4a9XrFJQd7DTLqsNHY2fUSfNSfuTdBSy7zh4eiDEU44XJcnBp1QJzb63nrAJnZjRnz6NcmRY2YrRgDq4LgRAyPCYs7UpGa1JgCK3hupDH8bPCbbtECqBXQ8nuZtNk3H6weCR4vuri2r9mMWhXY5thnyhcTjAwi51Cir3iHnjKcGPepL15U6BnNjfTAoQ6wKX3nN2pZDhn5RwyDpv7qPnouhLds7dKEn64HJqqBTVrDjTuWHNCBUMj6TcXTuPdSYH8CeL8YMfcMjhbRPHh1aSyhgLWuwBqL1eSW7wTAGLfJXoHcCJsMheMDma9MEMeP4UEAeEhNVQ5QEFFTCRH8MkMev4Fo6q4L39yhT1C5LAKkRMSnkJwKuUSAxqW4YiYH68dFjsW1MFwfXngDpcxS1QVBzhpW95Bb32VCLWHQzbCx3XcEMi5Q77MVW6aVyMHzYUNadH4Wbhn4QxQM11gPW2LQNyqwZjuxEesFJ8sqX2pCRHX6J5mBJKzyT9pyhvvQkxMu"
    P2TR_PSBT_B64 = "cHNidP8BAKgCAAAAAfn+phUWoAfkdjJXSEFxjcDaXBr22RczfwaOVNq+Sb4/AAAAAAD9////AzoeAAAAAAAAIlEgdeZfiD3lhycx2Y6ob18IYvCSOdDpsA9J9ZIGnBhNAqLoAwAAAAAAACJRIJ0tm23mDNzdWQfBwJYxSRvdQ07uqoqvOzvxnWPVPkCZ6AMAAAAAAAAWABSuzR7cPv9lqiCdAhXnPXCQXcFobIO/KwBPAQQ1h88D4BfRu4AAAAABg1wLUSGDdsYUVUKKn0e/zOH2zoOX6tewA4fp2epWgwLPvXEAMR4OhYRMNzhygxQ5TrgwKmtQcNaS5BsUuoGAkBBzxdoKVgAAgAEAAIAAAACAAAEBK38nAAAAAAAAIlEgBqyC/Dbbtg1IeR2Bw8HrOX+pc+RWyMb7VMEEIR8EexoBAwQAAAAAIRZFxrHkNII86ea0SPvB5AUnIDg6DSEogry6dlNNd1KKrRkAc8XaClYAAIABAACAAAAAgAAAAAAJAAAAARcgRcax5DSCPOnmtEj7weQFJyA4Og0hKIK8unZTTXdSiq0AIQcg65BQBosBO949IE21msXbKhx4qKolBz+/LnrUnQUVxhkAc8XaClYAAIABAACAAAAAgAEAAAABAAAAAQUgIOuQUAaLATvePSBNtZrF2yoceKiqJQc/vy561J0FFcYAIQfcq45CM9kU8pgInl2NOydhigf1IT+Jmiu9unj9uQLFzxkAc8XaClYAAIABAACAAAAAgAAAAAAKAAAAAQUg3KuOQjPZFPKYCJ5djTsnYYoH9SE/iZorvbp4/bkCxc8AAA=="
    P2TR_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2TR_PSBT).to_cbor())

    SIGNED_P2TR_PSBT = b'psbt\xff\x01\x00\xa8\x02\x00\x00\x00\x01\xf9\xfe\xa6\x15\x16\xa0\x07\xe4v2WHAq\x8d\xc0\xda\\\x1a\xf6\xd9\x173\x7f\x06\x8eT\xda\xbeI\xbe?\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x03:\x1e\x00\x00\x00\x00\x00\x00"Q u\xe6_\x88=\xe5\x87\'1\xd9\x8e\xa8o_\x08b\xf0\x929\xd0\xe9\xb0\x0fI\xf5\x92\x06\x9c\x18M\x02\xa2\xe8\x03\x00\x00\x00\x00\x00\x00"Q \x9d-\x9bm\xe6\x0c\xdc\xddY\x07\xc1\xc0\x961I\x1b\xddCN\xee\xaa\x8a\xaf;;\xf1\x9dc\xd5>@\x99\xe8\x03\x00\x00\x00\x00\x00\x00\x16\x00\x14\xae\xcd\x1e\xdc>\xffe\xaa \x9d\x02\x15\xe7=p\x90]\xc1hl\x83\xbf+\x00\x00\x01\x01+\x7f\'\x00\x00\x00\x00\x00\x00"Q \x06\xac\x82\xfc6\xdb\xb6\rHy\x1d\x81\xc3\xc1\xeb9\x7f\xa9s\xe4V\xc8\xc6\xfbT\xc1\x04!\x1f\x04{\x1a\x01\x08B\x01@(\xb0\x7f\x8d\x19\x9a\xa5\xa3\xae_ ti\x10G\x95\xc3)\x18\x1e\xca=Lq^\x9ah\xe7\xb58=\x87\x80\xd8\x1a\xbd\x0bb\x06@}\xd2\x0c?\xd9G\xac\xe9!%{\xe0E\x8bY\xca\xedH\xebh`\xbc\xbb\x13\x01\x13@(\xb0\x7f\x8d\x19\x9a\xa5\xa3\xae_ ti\x10G\x95\xc3)\x18\x1e\xca=Lq^\x9ah\xe7\xb58=\x87\x80\xd8\x1a\xbd\x0bb\x06@}\xd2\x0c?\xd9G\xac\xe9!%{\xe0E\x8bY\xca\xedH\xebh`\xbc\xbb\x13\x00\x00\x00\x00'
    SIGNED_P2TR_PSBT_B43 = "$JBJ$DT-D-U/1AEWDTQ*PH4J+H:1+I467L27$UINP.QOHP:ZYLDCPD8/LI+DN/A.X7-PC4UCX-K$/OQO-G-H.CGX.+9:5JKUVI:PVG+C37HW*MVZDUS$J-CLTWQ6WQ.A0MGXBUZF:X:276$9AZTBLV82BDNXAV1XQ6..R3I+.LV4OLAXU0MO:KY3KB.:-2PFJOYQ/*95CD:5HPWA/HJ2OW1ZPNB*S39+EAP+60B73/9W9KU.A:DTLVNCOCV1/BBLE9O14Z5ACDF0N$PHZ-B:IEJHV17V91KA/WPGFPSZNSIB/-WNYY./+5VQV.DUAIILF88LFSGJ/E36.B6WJ1$I/FWPOI/L*3.8F2B1TNQS-24N8QJAF**+S13/RFDR9ZZ3/N4CP7S9Y9HKJ-$/B43SC*+BRP44+DUH+$79DJB1-9AY7N/SZPZSHJP6+KYW+4/GIWNVRW$DUE08UMY-7/FH3*ZPPAL2PWR$1+R996Y.E9H:PIB*SJQY.JOEQL/X+2Q5V91UL*/WNCH$$DY*GK.I9XN"
    SIGNED_P2TR_PSBT_B58 = "9eehoGbwQ78EoHBL2mrxCSrMophCYTK9PxBW3WqL69ZFwj5F1ESdYXt9GdSKA3xxCgfDKhQt9PqBtSkNoKRFgnm6WyTASro6r5za7Nd2JtywPgYe1JdErssp47WvjrbkBBYV5jvWrzPTJhFrpyis8LLyKExp1XY4VwfSTrcFXfDEM7QoRDehks7s7w7CbLHg8zJEDqRjCdcZpzbVunb3FR7ypZHv41S8VKvhiGHFq1nW99F3dErPYbEs8Pc7gVwhJ6XuhmkpHArZp8pyFd3pQJhyBYQwqUR4QU41buYuFQ465SyMuCLyXhcevALrcjJRJVJsCpsEEZgqTk5z2oqsNPXNVHweNjeHBUdN9uJBgtQ6v5mVWRdsYUfmwFeQqyvDEaioqAnNNSpSe2ByNfcv8ftSfzocbNHLahUqTbjSvxThW84LpEwMUitaUQoguJweVscdRRitkx1kCmsaMC5JwrRH13zHVoFnJqPEUHZwqYTzAJCf"
    SIGNED_P2TR_PSBT_B64 = "cHNidP8BAKgCAAAAAfn+phUWoAfkdjJXSEFxjcDaXBr22RczfwaOVNq+Sb4/AAAAAAD9////AzoeAAAAAAAAIlEgdeZfiD3lhycx2Y6ob18IYvCSOdDpsA9J9ZIGnBhNAqLoAwAAAAAAACJRIJ0tm23mDNzdWQfBwJYxSRvdQ07uqoqvOzvxnWPVPkCZ6AMAAAAAAAAWABSuzR7cPv9lqiCdAhXnPXCQXcFobIO/KwAAAQErfycAAAAAAAAiUSAGrIL8Ntu2DUh5HYHDwes5f6lz5FbIxvtUwQQhHwR7GgEIQgFAKLB/jRmapaOuXyB0aRBHlcMpGB7KPUxxXppo57U4PYeA2Bq9C2IGQH3SDD/ZR6zpISV74EWLWcrtSOtoYLy7EwETQCiwf40ZmqWjrl8gdGkQR5XDKRgeyj1McV6aaOe1OD2HgNgavQtiBkB90gw/2Ues6SEle+BFi1nK7UjraGC8uxMAAAAA"
    SIGNED_P2TR_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(SIGNED_P2TR_PSBT).to_cbor())
    SIGNED_P2TR_PSBT_SD = b"psbt\xff\x01\x00\xa8\x02\x00\x00\x00\x01\xf9\xfe\xa6\x15\x16\xa0\x07\xe4v2WHAq\x8d\xc0\xda\\\x1a\xf6\xd9\x173\x7f\x06\x8eT\xda\xbeI\xbe?\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x03:\x1e\x00\x00\x00\x00\x00\x00\"Q u\xe6_\x88=\xe5\x87'1\xd9\x8e\xa8o_\x08b\xf0\x929\xd0\xe9\xb0\x0fI\xf5\x92\x06\x9c\x18M\x02\xa2\xe8\x03\x00\x00\x00\x00\x00\x00\"Q \x9d-\x9bm\xe6\x0c\xdc\xddY\x07\xc1\xc0\x961I\x1b\xddCN\xee\xaa\x8a\xaf;;\xf1\x9dc\xd5>@\x99\xe8\x03\x00\x00\x00\x00\x00\x00\x16\x00\x14\xae\xcd\x1e\xdc>\xffe\xaa \x9d\x02\x15\xe7=p\x90]\xc1hl\x83\xbf+\x00O\x01\x045\x87\xcf\x03\xe0\x17\xd1\xbb\x80\x00\x00\x00\x01\x83\\\x0bQ!\x83v\xc6\x14UB\x8a\x9fG\xbf\xcc\xe1\xf6\xce\x83\x97\xea\xd7\xb0\x03\x87\xe9\xd9\xeaV\x83\x02\xcf\xbdq\x001\x1e\x0e\x85\x84L78r\x83\x149N\xb80*kPp\xd6\x92\xe4\x1b\x14\xba\x81\x80\x90\x10s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x01\x01+\x7f'\x00\x00\x00\x00\x00\x00\"Q \x06\xac\x82\xfc6\xdb\xb6\rHy\x1d\x81\xc3\xc1\xeb9\x7f\xa9s\xe4V\xc8\xc6\xfbT\xc1\x04!\x1f\x04{\x1a\x01\x03\x04\x00\x00\x00\x00\x01\x08B\x01@(\xb0\x7f\x8d\x19\x9a\xa5\xa3\xae_ ti\x10G\x95\xc3)\x18\x1e\xca=Lq^\x9ah\xe7\xb58=\x87\x80\xd8\x1a\xbd\x0bb\x06@}\xd2\x0c?\xd9G\xac\xe9!%{\xe0E\x8bY\xca\xedH\xebh`\xbc\xbb\x13\x01\x13@(\xb0\x7f\x8d\x19\x9a\xa5\xa3\xae_ ti\x10G\x95\xc3)\x18\x1e\xca=Lq^\x9ah\xe7\xb58=\x87\x80\xd8\x1a\xbd\x0bb\x06@}\xd2\x0c?\xd9G\xac\xe9!%{\xe0E\x8bY\xca\xedH\xebh`\xbc\xbb\x13!\x16E\xc6\xb1\xe44\x82<\xe9\xe6\xb4H\xfb\xc1\xe4\x05' 8:\r!(\x82\xbc\xbavSMwR\x8a\xad\x19\x00s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\t\x00\x00\x00\x01\x17 E\xc6\xb1\xe44\x82<\xe9\xe6\xb4H\xfb\xc1\xe4\x05' 8:\r!(\x82\xbc\xbavSMwR\x8a\xad\x00\x01\x05  \xeb\x90P\x06\x8b\x01;\xde= M\xb5\x9a\xc5\xdb*\x1cx\xa8\xaa%\x07?\xbf.z\xd4\x9d\x05\x15\xc6!\x07 \xeb\x90P\x06\x8b\x01;\xde= M\xb5\x9a\xc5\xdb*\x1cx\xa8\xaa%\x07?\xbf.z\xd4\x9d\x05\x15\xc6\x19\x00s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x05 \xdc\xab\x8eB3\xd9\x14\xf2\x98\x08\x9e]\x8d;'a\x8a\x07\xf5!?\x89\x9a+\xbd\xbax\xfd\xb9\x02\xc5\xcf!\x07\xdc\xab\x8eB3\xd9\x14\xf2\x98\x08\x9e]\x8d;'a\x8a\x07\xf5!?\x89\x9a+\xbd\xbax\xfd\xb9\x02\xc5\xcf\x19\x00s\xc5\xda\nV\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\n\x00\x00\x00\x00\x00"
    SIGNED_P2TR_PSBT_B64_SD = "cHNidP8BAKgCAAAAAfn+phUWoAfkdjJXSEFxjcDaXBr22RczfwaOVNq+Sb4/AAAAAAD9////AzoeAAAAAAAAIlEgdeZfiD3lhycx2Y6ob18IYvCSOdDpsA9J9ZIGnBhNAqLoAwAAAAAAACJRIJ0tm23mDNzdWQfBwJYxSRvdQ07uqoqvOzvxnWPVPkCZ6AMAAAAAAAAWABSuzR7cPv9lqiCdAhXnPXCQXcFobIO/KwBPAQQ1h88D4BfRu4AAAAABg1wLUSGDdsYUVUKKn0e/zOH2zoOX6tewA4fp2epWgwLPvXEAMR4OhYRMNzhygxQ5TrgwKmtQcNaS5BsUuoGAkBBzxdoKVgAAgAEAAIAAAACAAAEBK38nAAAAAAAAIlEgBqyC/Dbbtg1IeR2Bw8HrOX+pc+RWyMb7VMEEIR8EexoBAwQAAAAAAQhCAUAosH+NGZqlo65fIHRpEEeVwykYHso9THFemmjntTg9h4DYGr0LYgZAfdIMP9lHrOkhJXvgRYtZyu1I62hgvLsTARNAKLB/jRmapaOuXyB0aRBHlcMpGB7KPUxxXppo57U4PYeA2Bq9C2IGQH3SDD/ZR6zpISV74EWLWcrtSOtoYLy7EyEWRcax5DSCPOnmtEj7weQFJyA4Og0hKIK8unZTTXdSiq0ZAHPF2gpWAACAAQAAgAAAAIAAAAAACQAAAAEXIEXGseQ0gjzp5rRI+8HkBScgODoNISiCvLp2U013UoqtAAEFICDrkFAGiwE73j0gTbWaxdsqHHioqiUHP78uetSdBRXGIQcg65BQBosBO949IE21msXbKhx4qKolBz+/LnrUnQUVxhkAc8XaClYAAIABAACAAAAAgAEAAAABAAAAAAEFINyrjkIz2RTymAieXY07J2GKB/UhP4maK726eP25AsXPIQfcq45CM9kU8pgInl2NOydhigf1IT+Jmiu9unj9uQLFzxkAc8XaClYAAIABAACAAAAAgAAAAAAKAAAAAAA="

    # Native Segwit Multisig
    P2WSH_PSBT = b'psbt\xff\x01\x00\xb2\x02\x00\x00\x00\x02\xadC\x87\x14J\xfae\x07\xe1>\xaeP\xda\x1b\xf1\xb5\x1ag\xb3\x0f\xfb\x8e\x0c[\x8f\x98\xf5\xb3\xb1\xa68Y\x00\x00\x00\x00\x00\xfd\xff\xff\xffig%Y\x0f\xb8\xe4r\xab#N\xeb\xf3\xbf\x04\xd9J\xc0\xba\x94\xf6\xa5\xa4\xf8B\xea\xdb\x9a\xd3c`\xd4\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02@B\x0f\x00\x00\x00\x00\x00"\x00 \xa9\x903\xc3\x86b3>Y\t\xae<=\x03\xbdq\x8d\xb2\x14Y\xfd\xd5P\x1e\xe8\xa0RaMY\xb4\xe2\xd8\xd2!\x01\x00\x00\x00\x00"\x00 \x8d\x02\x85\r\xab\x88^\xc5y\xbbm\xcb\x05\xd6 ;\x05\xf5\x17\x01\x86\xac\xb8\x90}l\xc1\xb4R\x99\xed\xd2\x00\x00\x00\x00O\x01\x045\x87\xcf\x04>b\xdf~\x80\x00\x00\x02A+I\x84\xd5I\xba^\xef\x1c\xa6\xe8\xf3u]\x9a\xe0\x16\xdam\x16ir\xca\x0eQ@6~\xddP\xda\x025\xb8K1\xdc8*|\xfbC\xba:{\x17K\xe9AaA\xe8\x16\xf6r[\xd1%\x12\xb5\xb2\xc4\xa5\xac\x14\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\x9d\xb1\xd0\x00\x80\x00\x00\x02?\xd8\xd7;\xc7\xb8\x8c\xa4\x93Z\xa57\xbf8\x94\xd5\xe2\x88\x9f\xab4\x1ca\x8fJWo\x8f\x19\x18\xc2u\x02h\xc3\rV\x9d#j}\xccW\x1b+\xb1\xd2\xadO\xa9\xf9\xb3R\xa8\t6\xa2\x89\n\x99\xaa#\xdbx\xec\x14&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\xba\xc1H9\x80\x00\x00\x02\x1dO\xbe\xbd\xd9g\xe1\xafqL\t\x97\xd3\x8f\xcfg\x0b\\\xe9\xd3\x01\xc0D\x0b\xbc\xc3\xb6\xa2\x0e\xb7r\x1c\x03V\x8e\xa1\xf3`Q\x91n\xd1\xb6\x90\xc3\x9e\x12\xa8\xe7\x06\x03\xb2\x80\xbd0\xce_(\x1f)\x18\xa5Sc\xaa\x14s\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 \x89\x801pn\xdd\x9e\xb1"g\x85G\x15Q\xce\xa3_\x17\t\xa9o\x85\x96.2\xa0k\xf6~\xc7\x11$\x01\x05iR!\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2!\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87S\xae"\x06\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 3w\xad03\xd1\x05\x9c\xf1\xd25\xbb\x12%\xfc\xa2\xa4\xbf&\xc9R\xd5?o\xef\xc3:-UD\x8d\xc5\x01\x05iR!\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"!\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t!\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01S\xae"\x06\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01iR!\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe!\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v!\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2kS\xae"\x02\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2k\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    P2WSH_PSBT_B43 = "9YO76-S3DRXKI-6JS23**6N$12A3MTF2R66Q0-C-*BD+VB.V3O1EM2VDNMX:*DHL-RMVYZ/.W:9XKN7$4/1M0$$U8+$77KE5:40Z527KZOHA-$MLTL21L3*ON6SCCF:4HMW2K1IS7VUOUF6JW/A+DGMGVF17C0BFK/Y*FDJQWWLX*EEJUR12L3*R0.F6W5674M-+KZUKD+77RB$PGQSTPRX49C25391EP+5/ZJ7$N$F+8*CU24O78HRO0-YO51IO7+A8RZ386S5AK200DG92O6P/QT3W.T$NA7*:GYGTFT+ZC9JWTD-BMVZPBNMT9/EGO.ZHBHAPYHU6MN.U.UZ118L8G4PXR5+*SOXHDQGS$+ZY0HX9X016901VG2$.22I8LNKUGLVRBP.G4Y6DXIAO5B6TPES$F8ALOIDB30SH:29L.*/GSED*V-L0CXWM3SI6YZB59SVDKAJPMCBMDF4:8/Y9FEFIN+5AJ:UQ.J*AC+3N5Y/OOU/HCMOBNRHMN-0QZH8*CQ4-7CSJ7+KU:UX5KFO9XUQG+5U2-2VD6NZCF+N0Y97CP8HR$+N2K98A+0Z8ILV0KI634*/WEI+97-B3E*TW-5F82$N.QRDP/4R9Z6/:0H0$A2DKP2V.RUNDT0E56489TJTX48.1DPCP1KY71RVFFEC:/8:3S6EIS2DETQ2U9.N6TK$6+:H6+UH7KG3ZDW39CLSET-V6MEZSTDL*/A65IK.F3TEJSF++3FOO+-F2SOYFS.V/*SSMCJ7$2Z63SS0K+*O88Y-9+A-IQ04-3VE7PAI$MCR*J6O0$*ZJ9W07:/G+ZVGHJIE:/00UE0*CXLY8COUJIB1ITXR.YNFTLT9B.-IA6KQ7R/56G.54NTU2E657O0KNC0DT$+EGI**JM5F0YNRL01/Y*O:1WQU5J*TTZJGG-HJZA2Q+0F:ML1PY1MXYWNM8ABM4*F33XH6HUZMAW82FRSP302M4NARGWWA2DI8CC1$84B/NFJ5WOJE.5UOUUMUILQJZIK3PA2P-18SQTV*R258MJQ+:++DYHCHI6B5I+J3$OB1AKOLKY4I5XD.3Q2JK*RJ1E1LOU1IV/H7555LHI:RKDV-W995M3-*H4-DBBLDSI9BC*C+U978N2-9K$6+0V/PN-TR.-WIBBBI:3QNPXZ/N4MHI+JI:NIN/80OOG39A9$$G3FE+V71:/Y1VD0UUW.+XTVSO$6SHD:1JXTWYUEAPZUD5/28Z5KW843*BS*2.$WYMG+7YI1.H38BL7YN8/4-34XGFS/L.+V0:RSOAU8NP4ZCAU3Q:GL1/SG5ZU$:*58DIWF8.RNIRG22S18LLNKJXQSY.PH3+66PH0J9*I8S9E70-+*W4ADFYICDA4-0$-MTPE7LO*1*UT/Q6DTUBY0MYTKELTSOGJ0*IFU-N9L3E*8T9/Z:D2JMAI-JJQ7EKP859SIN:+I:Z3G209-DA0$9*H7GBEMOM3V5S/T$LLA/J.U-C5+ZIALSP37NKX2*PWB216D6OITOLQ:3.OAG4U/R45PH$$:K1D/$75QC9SK6S7.O0UJFZK7F*PFY8XJHGP-O.P4E07/M-RKIHQ7L$VFN292+UN8F7KZYP$NF/JY4N+9.RXV1DS**QPYQVY2+U9QR/+1T7-2/YAG9K*T549*:/578Q.AI0/1TQZCCG9FLLL4J$+ETZ0LKF+*3DN84F8GC-P4EYLAF923H9JRXNHXDDPN/NX$O$4SELXX$S8QNZJO$Y7GD/LKH$5:-9J6PMTVT/G3+WS-T*FBFTI3JB/A0OWEPAY:GTOFMBV/M$L1.P$N0S2DL/O4D4SUVJ76S21/:Y$VKF4V+SV-0/UO1GSK:G*H-GGL+ST8MBNG*DUEZHCC-$4J9KRL39V9G00YDA6SW2IF8AKCR9L7YV05RGHEJA0BYZVPYOL:KV/UL+$5ZMHJ9F84Q4YU-XR9THI-/$2W9ZQNR-J-N+WXC+A3FSA$2B4$FQH$71P0T8EBR+WM3W-XT*UG$YKZV3*$HU8Q-XRBXD6Q8K.4$COENY4/V3VL5O7SP.0$5+R5VHO./ULKTKC0G/WG8-5*IXB.4QHRYG90IV48VVNZ2-W*Q0QN7XPJIXK1FNPVQNECX:1$+C.U7*I1.WF.N-UVXNPJZCIOCIFJC1-Z7SWS:3SP7N1OCJK.PB4PVGM*.H6BC8ED4*587E:UD"
    P2WSH_PSBT_B58 = "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"
    P2WSH_PSBT_B64 = "cHNidP8BALICAAAAAq1DhxRK+mUH4T6uUNob8bUaZ7MP+44MW4+Y9bOxpjhZAAAAAAD9////aWclWQ+45HKrI07r878E2UrAupT2paT4QurbmtNjYNQBAAAAAP3///8CQEIPAAAAAAAiACCpkDPDhmIzPlkJrjw9A71xjbIUWf3VUB7ooFJhTVm04tjSIQEAAAAAIgAgjQKFDauIXsV5u23LBdYgOwX1FwGGrLiQfWzBtFKZ7dIAAAAATwEENYfPBD5i336AAAACQStJhNVJul7vHKbo83VdmuAW2m0WaXLKDlFANn7dUNoCNbhLMdw4Knz7Q7o6exdL6UFhQegW9nJb0SUStbLEpawUAgjLdzAAAIABAACAAAAAgAIAAIBPAQQ1h88EnbHQAIAAAAI/2Nc7x7iMpJNapTe/OJTV4oifqzQcYY9KV2+PGRjCdQJoww1WnSNqfcxXGyux0q1PqfmzUqgJNqKJCpmqI9t47BQmu4PEMAAAgAEAAIAAAACAAgAAgE8BBDWHzwS6wUg5gAAAAh1Pvr3ZZ+GvcUwJl9OPz2cLXOnTAcBEC7zDtqIOt3IcA1aOofNgUZFu0baQw54SqOcGA7KAvTDOXygfKRilU2OqFHPF2gowAACAAQAAgAAAAIACAACAAAEBK4CWmAAAAAAAIgAgiYAxcG7dnrEiZ4VHFVHOo18XCalvhZYuMqBr9n7HESQBBWlSIQJOjQgMfX26XEf+trHIEk3rYkEX5Y2NfrFKQARPcd2X8iEDBWHUgq25PfHvE+hlcBryJG7wo2y8jKUSPY7sd85OOMchA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHU64iBgJOjQgMfX26XEf+trHIEk3rYkEX5Y2NfrFKQARPcd2X8hwmu4PEMAAAgAEAAIAAAACAAgAAgAAAAAABAAAAIgYDBWHUgq25PfHvE+hlcBryJG7wo2y8jKUSPY7sd85OOMccAgjLdzAAAIABAACAAAAAgAIAAIAAAAAAAQAAACIGA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHHHPF2gowAACAAQAAgAAAAIACAACAAAAAAAEAAAAAAQErgJaYAAAAAAAiACAzd60wM9EFnPHSNbsSJfyipL8myVLVP2/vwzotVUSNxQEFaVIhAiKCMRLlzIhLkRbLIUIMx5KYJM0v6LcjW/mS6K7eFGwiIQKDzUflU23LeecRgzDo5IBCEvaWGfHW7JkNxzXvuc7FdCEDC5DtLoa61/Kk/pdpu0F9e6nKoRJIB9v7Ni377rZefgFTriIGAiKCMRLlzIhLkRbLIUIMx5KYJM0v6LcjW/mS6K7eFGwiHAIIy3cwAACAAQAAgAAAAIACAACAAAAAAAAAAAAiBgKDzUflU23LeecRgzDo5IBCEvaWGfHW7JkNxzXvuc7FdBwmu4PEMAAAgAEAAIAAAACAAgAAgAAAAAAAAAAAIgYDC5DtLoa61/Kk/pdpu0F9e6nKoRJIB9v7Ni377rZefgEcc8XaCjAAAIABAACAAAAAgAIAAIAAAAAAAAAAAAABAWlSIQKtIdmtKKuZrH7f2R4iIU8RWVOrCdHVWBCS+0e9pZJy/iEDoH074LrWPIA10hyXtBCJDT06GdLkA6+z/PxoJqomPHYhA6GoQ/otQdk71nUpYZFfbkSKdBkkSj4CuPTPYrzGp6JrU64iAgKtIdmtKKuZrH7f2R4iIU8RWVOrCdHVWBCS+0e9pZJy/hwCCMt3MAAAgAEAAIAAAACAAgAAgAEAAAAAAAAAIgIDoH074LrWPIA10hyXtBCJDT06GdLkA6+z/PxoJqomPHYcc8XaCjAAAIABAACAAAAAgAIAAIABAAAAAAAAACICA6GoQ/otQdk71nUpYZFfbkSKdBkkSj4CuPTPYrzGp6JrHCa7g8QwAACAAQAAgAAAAIACAACAAQAAAAAAAAAAAA=="
    P2WSH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2WSH_PSBT).to_cbor())

    SIGNED_P2WSH_PSBT = b'psbt\xff\x01\x00\xb2\x02\x00\x00\x00\x02\xadC\x87\x14J\xfae\x07\xe1>\xaeP\xda\x1b\xf1\xb5\x1ag\xb3\x0f\xfb\x8e\x0c[\x8f\x98\xf5\xb3\xb1\xa68Y\x00\x00\x00\x00\x00\xfd\xff\xff\xffig%Y\x0f\xb8\xe4r\xab#N\xeb\xf3\xbf\x04\xd9J\xc0\xba\x94\xf6\xa5\xa4\xf8B\xea\xdb\x9a\xd3c`\xd4\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02@B\x0f\x00\x00\x00\x00\x00"\x00 \xa9\x903\xc3\x86b3>Y\t\xae<=\x03\xbdq\x8d\xb2\x14Y\xfd\xd5P\x1e\xe8\xa0RaMY\xb4\xe2\xd8\xd2!\x01\x00\x00\x00\x00"\x00 \x8d\x02\x85\r\xab\x88^\xc5y\xbbm\xcb\x05\xd6 ;\x05\xf5\x17\x01\x86\xac\xb8\x90}l\xc1\xb4R\x99\xed\xd2\x00\x00\x00\x00\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 \x89\x801pn\xdd\x9e\xb1"g\x85G\x15Q\xce\xa3_\x17\t\xa9o\x85\x96.2\xa0k\xf6~\xc7\x11$"\x02\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87G0D\x02 h?m\x19\x04C\x89\x95\x8b\xba\xed\xbb\xba8)\t\xae^\xe3`\x16G\xc8\x8bq\x9c\x0e\xbc\xc5\xb1j\xa2\x02 \x05\rP(\xe0\x9cc])q\xe5\xe2S\x9f\xaf+\xe4_\xa9\xc6\xf9\r"%\xf4\xa2\x00;\xa2\xaf2W\x01\x01\x05iR!\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2!\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87S\xae\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 3w\xad03\xd1\x05\x9c\xf1\xd25\xbb\x12%\xfc\xa2\xa4\xbf&\xc9R\xd5?o\xef\xc3:-UD\x8d\xc5"\x02\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01G0D\x02 ~O\x1b\x8c\xbb\x87x\xa3\xbb\xff\x04\xd8\x10Cq\xc8Y\x0f;N6\x97\xd8S\xfeti\x80\xb3\x12\xe0>\x02 l\x93=\x02m\xb4<\x90\xf4%\xf9Z${\xb7\xecO\x19\x15\xa3\xa3S\xf2Q\x81\xdcX\xfb\xd5&\x9e\xc5\x01\x01\x05iR!\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"!\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t!\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01S\xae\x00\x00\x00'
    SIGNED_P2WSH_PSBT_B43 = "*SPXND+LRIGD5M1*NM-KV3RHL.*VA-BKB4S768T1HCIA:IJ:U+OW:72QTH6YLJ2ZVYJW90CFVID.GA2O1G$TG1K3I4759UGCO/U3Z$030$GR5R*OXST6TO$34/UZ*VJ+Z*A2CQVJ8CSN2Z5FK79JTWD$HDPEWX7C8C220T24FZ-RSZ:GM3Y578HCV*FG1QG-/$Q5H0LMI*I1HD$51K6UP.5N0/FOPFC/MIGLLXJP:YTGR11+1JX90+GDZ5+3$/BD*ISW36V$ZK5-3V5ID0VJ9U*X6PL*QH$SP5YQW/SWFNV80VD5MTEN46$P.7EUD4A1A$.5E7H5+51OZAD-.RY9HU*B8/+-TSQ2C4OA6+M6ZBDALSJ5IY2:XB481FZO.WLXUQND-FAB+XAESK9303ZFYA:6CX9AXG/2US*N+*79Y4U68*P/LNPP1PNCC.I3ATP:EN/MBPXU+P*3MX5HDBOR4HT:8RF.WO6HGFL8T*H-+61R+R6V-CJ*-VVLB83QPH*.G0/3T4FN2029Y96+3XMJPPSLU+Q6YW101MH8A3J2CYB*CFS$$NSL5I3OCN*:3V001Z:8PEG:+:HE54GUB2UM*GRY46/639A*40K$SB*G2P$D7PWJHP6SGNO.Z827V6$+09WZR-2GC4-2D9KSNAGK38WUFEV$1UIDZ/+83HX$IKJDYF3AEWR-L9ZX$/5QHW-1HA26CECX52/FQPAFE7ZRPCH9RA9XA556ASF8YW6I4+*ID/8VYMW.I-LQTMVLYFLTV097P*ZGRYONCULW37MFJ408I$CVCV2M.LJ+SV-49.33.WNDE2X5KCC4IVO8F9BH95UN$Q:SCZSR*M2UK/0BWQUO*YT.IB3UW8YV/8NGGOEZGA4QJ2-ICL5MIZ+4U1-QZFMXS6PEEH5IO5RU$+W.DF$5-AMFMQJV1LRLUAHJ9ZGM:WW*.06UQFBBDUO0:YVVO85FSFXE*/:1UIHQW5DJCY2CX0W94Q:D:T8ES9HZON85YXQZTC9+ASY/B525SCPL44BTZ8R1*15:+6-6FQ112E1$G9L"
    SIGNED_P2WSH_PSBT_B58 = "8zF2eD2uMaxb2DsPbbKRp9Mpm1UH66wJ4uSMZPn5MA1nJwE8S3RAGDWCCvsguUhQDPCPVw5S8GsAJvAc811WwP71guKubiPxppUKqaWUkQN71B18krk1K2NrWCA9ewdJE1d1BopmzNBr5Qg3qZNCsN6EDSCn8uow2r97h2rnokSq4nXfy3KE2v7hBrGvSZw8A96WAJDSEnS1sP7U5wgtiSYdWxEHBfKocVC3G3sayPuMEjzA9QcYWpy1U6S3EW8YWw5kvQW88LKg8b3js9R7w9aWFnQwMdRg3CFSfGkoHegiWSufPejQ65Airoo8WqNvGVacmSZybkmcvu57KRobPuhZCDPbtJ5435eJsarQ9nmRpac6VJNoLrdHvkeWRZ9QEXk654TW7z6NV87it5vPVDNEnFW3c9pAdtZsYXHafw7CMSiWRPEsCoRKzodieHJFfeHiJGT5zqcP3bgmHTszp3GPMdRy3onHeFRCoyftuAEBkwsCyaYFwoSBE6YUgjHT1T4mWCoe7W4ktoDEKXsHawFC6sw6KCPzDbuTZJuaDoWijHeo7FnC97QVvMNHdVgz1ZmCerxQLrkFJsT8x5WYuVoMmcHRpbyRcuCV64YYPgFFfCZs7VVedPsgSNdkQ7qKCqVYnTaNiBpeE5NB4gwcMcCYUJMWXkqCq7t91o9Mi5ozv4R9yPonSUaTH13D6FSPY9RSZbU1F9SMgFXBoB4DdssC36RGpqZ3Fnm77RJB5v1WJAQ95RNXHuSuKB43X1HiiKYKohtFrwd7jCtbUGuUUs9mpd7VqdvVtbSE9jpQxgxJHvF983X43ZxKcE2K8AMr4WyL8s2Pi2Xj644V9zauy2qmLeNusxudGNgPdTsktjEoWCSuFPtxuqcmC8MwXh5cSQqiFkULgFNuGtkUajJQEnfW9jMfjm5y7Va5DhJN4S7MN371DgiusGnsmb5YZGBeycptyDykdsFXYs"
    SIGNED_P2WSH_PSBT_B64 = "cHNidP8BALICAAAAAq1DhxRK+mUH4T6uUNob8bUaZ7MP+44MW4+Y9bOxpjhZAAAAAAD9////aWclWQ+45HKrI07r878E2UrAupT2paT4QurbmtNjYNQBAAAAAP3///8CQEIPAAAAAAAiACCpkDPDhmIzPlkJrjw9A71xjbIUWf3VUB7ooFJhTVm04tjSIQEAAAAAIgAgjQKFDauIXsV5u23LBdYgOwX1FwGGrLiQfWzBtFKZ7dIAAAAAAAEBK4CWmAAAAAAAIgAgiYAxcG7dnrEiZ4VHFVHOo18XCalvhZYuMqBr9n7HESQiAgNolXLiiw/tqdaYHAI32eXe2/7BbecUP2gKAu1dFZ91h0cwRAIgaD9tGQRDiZWLuu27ujgpCa5e42AWR8iLcZwOvMWxaqICIAUNUCjgnGNdKXHl4lOfryvkX6nG+Q0iJfSiADuirzJXAQEFaVIhAk6NCAx9fbpcR/62scgSTetiQRfljY1+sUpABE9x3ZfyIQMFYdSCrbk98e8T6GVwGvIkbvCjbLyMpRI9jux3zk44xyEDaJVy4osP7anWmBwCN9nl3tv+wW3nFD9oCgLtXRWfdYdTrgABASuAlpgAAAAAACIAIDN3rTAz0QWc8dI1uxIl/KKkvybJUtU/b+/DOi1VRI3FIgIDC5DtLoa61/Kk/pdpu0F9e6nKoRJIB9v7Ni377rZefgFHMEQCIH5PG4y7h3iju/8E2BBDcchZDztONpfYU/50aYCzEuA+AiBskz0CbbQ8kPQl+Voke7fsTxkVo6NT8lGB3Fj71SaexQEBBWlSIQIigjES5cyIS5EWyyFCDMeSmCTNL+i3I1v5kuiu3hRsIiECg81H5VNty3nnEYMw6OSAQhL2lhnx1uyZDcc177nOxXQhAwuQ7S6GutfypP6XabtBfXupyqESSAfb+zYt++62Xn4BU64AAAA="
    SIGNED_P2WSH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(SIGNED_P2WSH_PSBT).to_cbor())
    SIGNED_P2WSH_PSBT_SD = b'psbt\xff\x01\x00\xb2\x02\x00\x00\x00\x02\xadC\x87\x14J\xfae\x07\xe1>\xaeP\xda\x1b\xf1\xb5\x1ag\xb3\x0f\xfb\x8e\x0c[\x8f\x98\xf5\xb3\xb1\xa68Y\x00\x00\x00\x00\x00\xfd\xff\xff\xffig%Y\x0f\xb8\xe4r\xab#N\xeb\xf3\xbf\x04\xd9J\xc0\xba\x94\xf6\xa5\xa4\xf8B\xea\xdb\x9a\xd3c`\xd4\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x02@B\x0f\x00\x00\x00\x00\x00"\x00 \xa9\x903\xc3\x86b3>Y\t\xae<=\x03\xbdq\x8d\xb2\x14Y\xfd\xd5P\x1e\xe8\xa0RaMY\xb4\xe2\xd8\xd2!\x01\x00\x00\x00\x00"\x00 \x8d\x02\x85\r\xab\x88^\xc5y\xbbm\xcb\x05\xd6 ;\x05\xf5\x17\x01\x86\xac\xb8\x90}l\xc1\xb4R\x99\xed\xd2\x00\x00\x00\x00O\x01\x045\x87\xcf\x04>b\xdf~\x80\x00\x00\x02A+I\x84\xd5I\xba^\xef\x1c\xa6\xe8\xf3u]\x9a\xe0\x16\xdam\x16ir\xca\x0eQ@6~\xddP\xda\x025\xb8K1\xdc8*|\xfbC\xba:{\x17K\xe9AaA\xe8\x16\xf6r[\xd1%\x12\xb5\xb2\xc4\xa5\xac\x14\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\x9d\xb1\xd0\x00\x80\x00\x00\x02?\xd8\xd7;\xc7\xb8\x8c\xa4\x93Z\xa57\xbf8\x94\xd5\xe2\x88\x9f\xab4\x1ca\x8fJWo\x8f\x19\x18\xc2u\x02h\xc3\rV\x9d#j}\xccW\x1b+\xb1\xd2\xadO\xa9\xf9\xb3R\xa8\t6\xa2\x89\n\x99\xaa#\xdbx\xec\x14&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80O\x01\x045\x87\xcf\x04\xba\xc1H9\x80\x00\x00\x02\x1dO\xbe\xbd\xd9g\xe1\xafqL\t\x97\xd3\x8f\xcfg\x0b\\\xe9\xd3\x01\xc0D\x0b\xbc\xc3\xb6\xa2\x0e\xb7r\x1c\x03V\x8e\xa1\xf3`Q\x91n\xd1\xb6\x90\xc3\x9e\x12\xa8\xe7\x06\x03\xb2\x80\xbd0\xce_(\x1f)\x18\xa5Sc\xaa\x14s\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 \x89\x801pn\xdd\x9e\xb1"g\x85G\x15Q\xce\xa3_\x17\t\xa9o\x85\x96.2\xa0k\xf6~\xc7\x11$"\x02\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87G0D\x02 h?m\x19\x04C\x89\x95\x8b\xba\xed\xbb\xba8)\t\xae^\xe3`\x16G\xc8\x8bq\x9c\x0e\xbc\xc5\xb1j\xa2\x02 \x05\rP(\xe0\x9cc])q\xe5\xe2S\x9f\xaf+\xe4_\xa9\xc6\xf9\r"%\xf4\xa2\x00;\xa2\xaf2W\x01\x01\x05iR!\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2!\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87S\xae"\x06\x02N\x8d\x08\x0c}}\xba\\G\xfe\xb6\xb1\xc8\x12M\xebbA\x17\xe5\x8d\x8d~\xb1J@\x04Oq\xdd\x97\xf2\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03\x05a\xd4\x82\xad\xb9=\xf1\xef\x13\xe8ep\x1a\xf2$n\xf0\xa3l\xbc\x8c\xa5\x12=\x8e\xecw\xceN8\xc7\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01+\x80\x96\x98\x00\x00\x00\x00\x00"\x00 3w\xad03\xd1\x05\x9c\xf1\xd25\xbb\x12%\xfc\xa2\xa4\xbf&\xc9R\xd5?o\xef\xc3:-UD\x8d\xc5"\x02\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01G0D\x02 ~O\x1b\x8c\xbb\x87x\xa3\xbb\xff\x04\xd8\x10Cq\xc8Y\x0f;N6\x97\xd8S\xfeti\x80\xb3\x12\xe0>\x02 l\x93=\x02m\xb4<\x90\xf4%\xf9Z${\xb7\xecO\x19\x15\xa3\xa3S\xf2Q\x81\xdcX\xfb\xd5&\x9e\xc5\x01\x01\x05iR!\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"!\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t!\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01S\xae"\x06\x02"\x821\x12\xe5\xcc\x88K\x91\x16\xcb!B\x0c\xc7\x92\x98$\xcd/\xe8\xb7#[\xf9\x92\xe8\xae\xde\x14l"\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x02\x83\xcdG\xe5Sm\xcby\xe7\x11\x830\xe8\xe4\x80B\x12\xf6\x96\x19\xf1\xd6\xec\x99\r\xc75\xef\xb9\xce\xc5t\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03\x0b\x90\xed.\x86\xba\xd7\xf2\xa4\xfe\x97i\xbbA}{\xa9\xca\xa1\x12H\x07\xdb\xfb6-\xfb\xee\xb6^~\x01\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01iR!\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe!\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v!\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2kS\xae"\x02\x02\xad!\xd9\xad(\xab\x99\xac~\xdf\xd9\x1e"!O\x11YS\xab\t\xd1\xd5X\x10\x92\xfbG\xbd\xa5\x92r\xfe\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa0};\xe0\xba\xd6<\x805\xd2\x1c\x97\xb4\x10\x89\r=:\x19\xd2\xe4\x03\xaf\xb3\xfc\xfch&\xaa&<v\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xa1\xa8C\xfa-A\xd9;\xd6u)a\x91_nD\x8at\x19$J>\x02\xb8\xf4\xcfb\xbc\xc6\xa7\xa2k\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    # Nested Segwit Multisig
    P2SH_P2WSH_PSBT = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01\x1d\xf4\'\xad\xbd\x8bv?G\xcc(F\x92\xd0\xf4\x95\x1a\xdfZ\xca\xc7#>7.\r\x12\xc9\x9e\xe3\xc1\x96\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02\xdc9]\x05\x00\x00\x00\x00\x17\xa9\x14u!\x12s7Xj\x012N\x85TI|\x93\xf1T\xcd\xcf\xe3\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00O\x01\x045\x87\xcf\x04>b\xdf~\x80\x00\x00\x01\xdd\\H\xf6v\x7f\x04`\x9f\xabE\xd5\xc4b\xeeej\xae\xa5$\x8eL\xa7\xed\xed\xebw$\xc2\xdc\xb4\xe5\x02\xab$\x13O{\x08pA\xa1\x8fa\x18\x9f\xeb\xe5\xda\xc6\x8c\xc5^\xf4\xd7\x9f\xbaT\xdb\x81\xfa}\x1c\xb5\x17\x14\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80O\x01\x045\x87\xcf\x04\x9d\xb1\xd0\x00\x80\x00\x00\x01\xe7\x8e\xbf\x9e\xa8y\xa6\x85N\xb3h\x9c\xc2\x83\x1eMB\xf1\xba\xdbXaovW\x9cV\xe7\xbe\xbfO\xd1\x02\x7f\xe0\xe3"7\xa1\x8b2z~\xce9\xc4\xfbq\xa6%\xe0\xc9\xfb\x9d\x06\xf2\xa2q\xdc\xba\xc5\x11\xf8hs\x14&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80O\x01\x045\x87\xcf\x04\xba\xc1H9\x80\x00\x00\x01\xa7:\xdb\xe2\x87\x84\x87cM\xcb\xfc?~\xbd\xe8\xb1\xfc\x99O\x1e\xc0h`\xcf\x01\xc3\xfe.\xa7\x91\xdd\xb6\x02\xe6**\x99s\xeek:z\xf4|"\x9a[\xdep\xbc\xa5\x9b\xd0K\xbb)\x7fV\x93\xd7\xaa%k\x97m\x14s\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x14\xaf\xde\t\'\xf3\xbd\xf5\xa9\xc3\xdbH;\xb8L\x93\xa5$\x96\x7f>\x87\x01\x04"\x00 \xe7\xa2\x14\x15\xf9\xc7K\xd7\xe8&\x9c\xac\x05\x15\xa2\xfa\xec\xd40\xc2p\xa2R\xe6\xaam\x15-\xec\x8e\x90\xe9\x01\x05iR!\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03!\x03f rK\xb0\x8d\xa8v\xf7\x08\x95F\x00:\xc0\\y\xd7\xee\x9a\xca\xbc\xde\x08\x846xN3\x7f\x13\xed!\x03\xa7RPg\xdbg\'\xd8#\xc2fC\x12#\xa7\x03i\x92\xb6JR\xd5\xdbJ\xd3\xea\x9a\x8c\xa1\x00\x89\xb0S\xae"\x06\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03f rK\xb0\x8d\xa8v\xf7\x08\x95F\x00:\xc0\\y\xd7\xee\x9a\xca\xbc\xde\x08\x846xN3\x7f\x13\xed\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03\xa7RPg\xdbg\'\xd8#\xc2fC\x12#\xa7\x03i\x92\xb6JR\xd5\xdbJ\xd3\xea\x9a\x8c\xa1\x00\x89\xb0\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00"\x00 d\x1c\x13\xabNQ\x92\x9a\x8a\xbf\xa1U\xe8\xb4#\xb8\xcd;B\xfd?m\x87\xd6U\xcfMQ\x03\x85\xbf\x04\x01\x01iR!\x027\xda5Ru8\x1e\xbb\xbf\x98d\xaa\xd6~\x03\x99\xd8\x9f\xcbW~\x9c\xe6\xb0h\x02\x94\xf3\x86\xb3e\x0c!\x02\xfa\x11*\x9bu\xe6F\xdf:\xd8\x01E{"{\xa7Y\xbc\x03\xe5{s8\xfa9\xa8\xd46\x00\x9f\x83\x81!\x03\xf3\x14U\xfcF\x87\x897>\x8d\xcb\x07\xc0\xa61\x1b/ w\x064\xed\x1e\x95H\x04M\xa2\x13d\r\xd4S\xae"\x02\x027\xda5Ru8\x1e\xbb\xbf\x98d\xaa\xd6~\x03\x99\xd8\x9f\xcbW~\x9c\xe6\xb0h\x02\x94\xf3\x86\xb3e\x0c\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x02\xfa\x11*\x9bu\xe6F\xdf:\xd8\x01E{"{\xa7Y\xbc\x03\xe5{s8\xfa9\xa8\xd46\x00\x9f\x83\x81\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xf3\x14U\xfcF\x87\x897>\x8d\xcb\x07\xc0\xa61\x1b/ w\x064\xed\x1e\x95H\x04M\xa2\x13d\r\xd4\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    P2SH_P2WSH_PSBT_B43 = "7ZB23D47D0SL*Y69MFM-Y64LVJD48X$9XZO1J/-L0B.624*OS$T6-RL6--2HB:BJ/CZLFHQ8XWAXNB5UZ91+Y*/SV.4J:VE$J9MMCCOVW$EB6++CJ.X-O8OJ$TSAWI8W38*U:08G+2NKH*CCZRGY0ZABPJ3ESQ6VFNNSDNEYC8KG/QX8R72LXF*4Z+8373D*LLYIOUH+LKJKP5LM+2ZOXD05+G2-H-ZL5N585FA7BF9SYRFRX:U59MND9DEKQ13CKD7+M9TA*3/UP$IIY/9MSQKFLAOQ71UC98XLJ2DP+YP0+-WRV.9CNTV2/X/*1+VQK2:Z0MPT$1H$I:RS1T3.+072$4EWIC:.C0QK4M7JA:HE19Q$9H3U.APAPQN$K7$A6.G6S*K.X2NAAARU5E1-$SOXU3D$$AFF-CF9QMXU4UDF.*7:2DV5P+J$59J8P$4I.FII$FK0U/S6LV$B9.ZG73BC57G77:.03T7B1A1IB6S8-Z:93C$GZO.Q+O/ZSEFG9TRQWACXPPA1KDTTAS4WDT9*/J72B+U52S2ER58Y93VQ4SEQ:X54CW4-8*YXIRZVPV6EOHRE:F.EFUU4LQO+3ZOX706F+GJ2AP+UIEB*XY$*9Z4Q0S3JC1+9J07AA21I3$S8:V0EOY$F$XO/T9PDFY*0D+3YSJW7QVTOT6KID::3F.3:K1-S*243V53H+W.$Y3:C$V8.7GMF7BDZST:7D$C$6AKI3BUVNR2.0Q+BPVC2-I/TUN93WBXM495N8T.7PRSSCZM1M1ZJU.W+G-Z94JK69UVKJI.Q8$WV2MGZENWV26NR14GD83GKE5UTMANK+/X4+CJI*6UI63UEDVN3-FY5R2-B$3JD1SY3+:0ELB/IPL4LM8R$W2*:+.G1PX6X.I-4:CY.TP-Q7XN3.PHRD://U+-LJ6LI9QB477PKMJWT.GS7RC*DLCKE4KW4PL4NP$90:LJHR*5-52JV$DCHL33QBPCQVUO:Z5U+U+XALJ.:AJV+ZBD:JFB+0V:5TZ:GEBFSNTQJOPIGBL6QSG9QLINU3*928744+NWR3NV90670ZN7*V1ET5:A:DUSFHCR64YBKVESO$Q5TYD/QR3$N9Z.ZS09+L*.7UWBVXG63TFA33CNGX0:T+VVTG-Y-H:6Y9OX79R6COJJ:A00PO/8I/UIA2*E+ILV/6/C29QHJL05HINPAJZEMYVZNUVSB5TZT0*GWRMYT*W95M:GO0.NE*/S9EU86IS.M/1DO9DP41HA8-BI.XK6VCPEPX3LAAW*842PZ+8/889ODKLRE2PHP0HY9GB3Q6Y74NYHFI:1XHPGURQ+6YLRLCB5OW9/XLDORE6ZC-AQO++I71AWR0FXHAOF0WCY:JWXONP:L*Y7Z-6I6PSF0V-D87MYD:9W2LS8CU8YCVOT978VUB:6JA:/5U+70JM-I5T+RHHF-3FA+IBPVUBKVZV11.+SN71G7X3:L+RV-79GTG$3QAYAVR2F24/-M0FG2DVJ$4RGHRT55RQHVJ5JVS+H3:0+B1YSX57Y94/Z0-+Z07B4-M0BZREBSGUXZU+IL1C59B5QRAR:6BG9+2J.MIJJ5GJT6*2R1D5Z2.H*$L09W$0KLP4C/HIQ$D8AQS*K8:DGKSISC:LW.BR:JSCV+2EVOFAP.O+WOV6P1DMUQX3LYG/3KXK"
    P2SH_P2WSH_PSBT_B58 = "iKPPtgBuDNJvZAkJsisSSKkAar78K5TV6Yt41d6teHVeAnqMdnN9j6cd3vgbKtuVYUFg6QJ6RyqarHnqd6jkYSxZxFPimGq9LG4BDffByiQnRkSzTm9CGVK5XYMP1U5REj1PVebpKoQrgXJyWdjautuAVrpkuAhUm7aHDYj5fYBVzqVRJ8GWpJrY3ZzhMNXLdej9UT3DhBHRf8ATeCZrn5JK3CKSkwTjF7Q97DqwjjSDnx9x8NX5v9UcWJyLnxc9Sj5TJDfBQ2MAjFgCd7fFXBxYbavLnhgfjjzades8wgAVxqMJSSN7tbhQacqu1FxVXLBxZsueHK6e4w2o7z3CGUYqJh53TN3KFENTyRh55HrnsAiBy9Kvnho3E4ey141PToTD3uShXef1s3kKKGhgUtYXmoCMqZshuce3wxjJP6A2Kzn6r9kcEXtNbrXEArnuihJ1bq2dS58Kg55WuwmXLZqMFwXTxj96Ds3hjeG8pJMpBKvUNRuJyPUUKPTtGAHUEsDzVL7kzcBLKdHiG8qPgS5PQHUW7jkik32BrHrDsvHK1t6SBLF8PKpdkZjPo6Pad4p7uS3vyXkV3bvucpjcR2jq4kmj1p5y73cUKFiopBujFRUTfX5dzU96KXZK5tkiWVcUF9hRvmaEfSKwfvVN5B7ThQrZkuMdKoB5VHAie3LrqEyzduJbwcA2ErTGCjArkJxY2YH9KeostknMwNn83C843L38nxqh2UXgd9CGgG57tvPg2BHqBd7pWXfbHCvazHao5i3M1QesrhDvW4tteabJjRQqsEaxiumg8R5J7ByRgxZFBgGQnU6PH8VkNQCVPBWpAdm4XCpccgFsSkbB1VaYJCfXF1qVCDvC9HZ2VfJCKwHvmagZ6hTeoxx1M4nh51tNeJEGSZahTxnWsF49me35MNXBS3agEQ42RACSgDUdPvCveyK2yUqnX5Ka4A5fMznqEZDhFQsfMrude688TKLyqtc4KfVXSDjZgK2xdpt8BsXHM77mA1vynDSkAps9L7qnPwx4UaGimG8XESSHBQSvyxE7U6j3UZiDLtuWeSwJMcjzEUAKuVhAAYAdv6qQkjwueHMPNifpgpoahUqhphExtzxsQujpsNAiYg5U3RqfbWQ77appzjFmGmvKrC8vXyGMzwM11Fve5ac8CKPssfjxeeZ53ufpCdgbLFLd7AVSA3HHhUpiEyuRVnhL5BGtQCvz1MvpbcNYyBwAZ6uRxnhjMmbxTnZ5qiyJEdmssTxZxhV5cYjZtngQun27QffbMqMvB83zrJKcr6SrahWmGabjXULdJVqqqbaY5KWsq5jFBh6B4FMR6zhxYj742d32zHWJWf4PwEQ1HdHZKiQgYrUKE5Rys2XKRSMK9AvYxEcMRTvW2Zhv4uDeDNS1ESsFQcS3ZR1kmZV8ZXzEfQFcXUa5dyjfYyoAXqkJZP8LcdjrUmWjdHezcn1CPJ4pf8zNirSufggFYhRbFkahK4rx9QzD2T4qCT5ygabSqUZHXgqnAxsHmoSD6w4oH7BrH55trHjRChXCVhs4qoU34s"
    P2SH_P2WSH_PSBT_B64 = "cHNidP8BAHICAAAAAR30J629i3Y/R8woRpLQ9JUa31rKxyM+Ny4NEsme48GWAAAAAAD9////Atw5XQUAAAAAF6kUdSESczdYagEyToVUSXyT8VTNz+OHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAABPAQQ1h88EPmLffoAAAAHdXEj2dn8EYJ+rRdXEYu5laq6lJI5Mp+3t63ckwty05QKrJBNPewhwQaGPYRif6+XaxozFXvTXn7pU24H6fRy1FxQCCMt3MAAAgAEAAIAAAACAAQAAgE8BBDWHzwSdsdAAgAAAAeeOv56oeaaFTrNonMKDHk1C8brbWGFvdlecVue+v0/RAn/g4yI3oYsyen7OOcT7caYl4Mn7nQbyonHcusUR+GhzFCa7g8QwAACAAQAAgAAAAIABAACATwEENYfPBLrBSDmAAAABpzrb4oeEh2NNy/w/fr3osfyZTx7AaGDPAcP+LqeR3bYC5ioqmXPuazp69HwimlvecLylm9BLuyl/VpPXqiVrl20Uc8XaCjAAAIABAACAAAAAgAEAAIAAAQEgAOH1BQAAAAAXqRSv3gkn8731qcPbSDu4TJOlJJZ/PocBBCIAIOeiFBX5x0vX6CacrAUVovrs1DDCcKJS5qptFS3sjpDpAQVpUiECZ+pFYkOTVjB+eG+vQFA3MNjZWiA6DjRcs1Wl36A/zgMhA2Ygckuwjah29wiVRgA6wFx51+6ayrzeCIQ2eE4zfxPtIQOnUlBn22cn2CPCZkMSI6cDaZK2SlLV20rT6pqMoQCJsFOuIgYCZ+pFYkOTVjB+eG+vQFA3MNjZWiA6DjRcs1Wl36A/zgMcc8XaCjAAAIABAACAAAAAgAEAAIAAAAAAAAAAACIGA2Ygckuwjah29wiVRgA6wFx51+6ayrzeCIQ2eE4zfxPtHCa7g8QwAACAAQAAgAAAAIABAACAAAAAAAAAAAAiBgOnUlBn22cn2CPCZkMSI6cDaZK2SlLV20rT6pqMoQCJsBwCCMt3MAAAgAEAAIAAAACAAQAAgAAAAAAAAAAAAAEAIgAgZBwTq05RkpqKv6FV6LQjuM07Qv0/bYfWVc9NUQOFvwQBAWlSIQI32jVSdTgeu7+YZKrWfgOZ2J/LV36c5rBoApTzhrNlDCEC+hEqm3XmRt862AFFeyJ7p1m8A+V7czj6OajUNgCfg4EhA/MUVfxGh4k3Po3LB8CmMRsvIHcGNO0elUgETaITZA3UU64iAgI32jVSdTgeu7+YZKrWfgOZ2J/LV36c5rBoApTzhrNlDBwCCMt3MAAAgAEAAIAAAACAAQAAgAEAAAAAAAAAIgIC+hEqm3XmRt862AFFeyJ7p1m8A+V7czj6OajUNgCfg4EcJruDxDAAAIABAACAAAAAgAEAAIABAAAAAAAAACICA/MUVfxGh4k3Po3LB8CmMRsvIHcGNO0elUgETaITZA3UHHPF2gowAACAAQAAgAAAAIABAACAAQAAAAAAAAAAAA=="
    P2SH_P2WSH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(P2SH_P2WSH_PSBT).to_cbor())

    SIGNED_P2SH_P2WSH_PSBT = b"psbt\xff\x01\x00r\x02\x00\x00\x00\x01\x1d\xf4'\xad\xbd\x8bv?G\xcc(F\x92\xd0\xf4\x95\x1a\xdfZ\xca\xc7#>7.\r\x12\xc9\x9e\xe3\xc1\x96\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02\xdc9]\x05\x00\x00\x00\x00\x17\xa9\x14u!\x12s7Xj\x012N\x85TI|\x93\xf1T\xcd\xcf\xe3\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x14\xaf\xde\t'\xf3\xbd\xf5\xa9\xc3\xdbH;\xb8L\x93\xa5$\x96\x7f>\x87\"\x02\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03G0D\x02 \x1f\xa0f\x1ct\xd6\xb9S\xbd\xc4\"\x0cY\x19\xe0\xe4p\xdc\xe8qR\xc8$\xf4Hf\xa6\x07\x8e\xda\x16b\x02 W;\xfb\xc0\xbaWo]/\xcc\xd8\xdb\xe8\xc85\xee\x9bx\x1c\xea\xba\xf4[vM\xac\xc2\x11\xae-G\xc7\x01\x01\x04\"\x00 \xe7\xa2\x14\x15\xf9\xc7K\xd7\xe8&\x9c\xac\x05\x15\xa2\xfa\xec\xd40\xc2p\xa2R\xe6\xaam\x15-\xec\x8e\x90\xe9\x01\x05iR!\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03!\x03f rK\xb0\x8d\xa8v\xf7\x08\x95F\x00:\xc0\\y\xd7\xee\x9a\xca\xbc\xde\x08\x846xN3\x7f\x13\xed!\x03\xa7RPg\xdbg'\xd8#\xc2fC\x12#\xa7\x03i\x92\xb6JR\xd5\xdbJ\xd3\xea\x9a\x8c\xa1\x00\x89\xb0S\xae\x00\x00\x00"
    SIGNED_P2SH_P2WSH_PSBT_B43 = "CLQSGDZJQB4QIYKX08*DIBD23JSA8U413ZNG9T3LLKAV.2DC.M8794QPU1:E4Z06VG/+F$UKCBSIQH3V:N++4QS1NS:YJ1Z.JQ*+3T6D6PX-:WY8SYCHKR2GYKWNO46W:E$J65W$Y:1L*W0P5AUI9W:*PFQ*LX*+M$-BPO6-T31GOZFN$GMQ5RIB3VUKGNK-DXJKC6I236.$ZOEXVHM*D6ZM9+6QCXPMLG.P6O6O/P/QGGUEP8BMD.14T4H.1HEOF2*QI1PF*R.386+U8NOCJ3UE30ME5W$R*3APP:44M-WYBCU53QI1QV/QPVWF.T0$6EVP-YRSGZB34L+UTZ83H*NRJAYG79SXZATFWO9$R4XM5.O0WMVQ.3-*84Z8QVF38:O:6-PAOOUYUF1HK*+VKPC*JL6OSR-TH*FEQRPN4-9P4R*RWILCM5A:Y$48G4*B60N*E48WUH7$Q5PM8BCKWV-7UB0P4+TNUXR*P+E8/9FS$C$BFBOBL0GEU+5TGLVO:+8D-$OBU92TC43:0P17WZ1MINZKXD$B8.2$/9Z$Z*K7:QASII2WDNX7TQB416Q-C$J.:4-QCUF0X$FG+NRRD0-ABQ+ZX280T"
    SIGNED_P2SH_P2WSH_PSBT_B58 = "UHKpqoaYsQu3iUJNB2senWYdHBJvWXgfwPpJqqeAgk8xfULMYw45dxfzet7W38RH77S7DsUfemWVfASNVja4cwR3oN4233ve3Ma5tKQ3JoU9wLCkbRywAqepAah5sGDtx6QpS5G2w5ZYeVWjBdZ4obcNBQkT4umEjsALQfMwTHk31xivf9rmvQEizfP7geH6wufyXbMa3kg2h4c1CYE2eZC6tvcCKnHDJurq5yLfrhUSEjw8JpgSYxMiqmrMa8auJ25XQhpaPdcpYKXT9c7xhUNrTFuokHbfHiosxe8UMhRAHwmR2opgUBJvLq6ACokkn5UupGxrNmRSc1iJBBghokW1U9Wa9NtjiZLFcy86CS2wtt5UdtQ31BA3Capr5sBHER6vFLfVTqG6tdZ9LDaZmScBEzKsc6DRmhGGYFcGfaEBreiC6hvtHiN3xEFXS1DuJ4Xf6cE6QXit1q4vu1cMjhvnHV2LPTW8P6B696CXSa5FK4gn64FAn5G9WJNjJUfVuV3RHUgJwVXV83C2i5cXk2diUBFtDgzsboeqnh82GKKLkP5rjvBh"
    SIGNED_P2SH_P2WSH_PSBT_B64 = "cHNidP8BAHICAAAAAR30J629i3Y/R8woRpLQ9JUa31rKxyM+Ny4NEsme48GWAAAAAAD9////Atw5XQUAAAAAF6kUdSESczdYagEyToVUSXyT8VTNz+OHgJaYAAAAAAAWABTmav7/w4OOcfCiewfjsA7eaujhYAAAAAAAAQEgAOH1BQAAAAAXqRSv3gkn8731qcPbSDu4TJOlJJZ/PociAgJn6kViQ5NWMH54b69AUDcw2NlaIDoONFyzVaXfoD/OA0cwRAIgH6BmHHTWuVO9xCIMWRng5HDc6HFSyCT0SGamB47aFmICIFc7+8C6V29dL8zY2+jINe6beBzquvRbdk2swhGuLUfHAQEEIgAg56IUFfnHS9foJpysBRWi+uzUMMJwolLmqm0VLeyOkOkBBWlSIQJn6kViQ5NWMH54b69AUDcw2NlaIDoONFyzVaXfoD/OAyEDZiByS7CNqHb3CJVGADrAXHnX7prKvN4IhDZ4TjN/E+0hA6dSUGfbZyfYI8JmQxIjpwNpkrZKUtXbStPqmoyhAImwU64AAAA="
    SIGNED_P2SH_P2WSH_PSBT_UR_PSBT = UR(
        "crypto-psbt", PSBT(SIGNED_P2SH_P2WSH_PSBT).to_cbor()
    )
    SIGNED_P2SH_P2WSH_PSBT_SD = b'psbt\xff\x01\x00r\x02\x00\x00\x00\x01\x1d\xf4\'\xad\xbd\x8bv?G\xcc(F\x92\xd0\xf4\x95\x1a\xdfZ\xca\xc7#>7.\r\x12\xc9\x9e\xe3\xc1\x96\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x02\xdc9]\x05\x00\x00\x00\x00\x17\xa9\x14u!\x12s7Xj\x012N\x85TI|\x93\xf1T\xcd\xcf\xe3\x87\x80\x96\x98\x00\x00\x00\x00\x00\x16\x00\x14\xe6j\xfe\xff\xc3\x83\x8eq\xf0\xa2{\x07\xe3\xb0\x0e\xdej\xe8\xe1`\x00\x00\x00\x00O\x01\x045\x87\xcf\x04>b\xdf~\x80\x00\x00\x01\xdd\\H\xf6v\x7f\x04`\x9f\xabE\xd5\xc4b\xeeej\xae\xa5$\x8eL\xa7\xed\xed\xebw$\xc2\xdc\xb4\xe5\x02\xab$\x13O{\x08pA\xa1\x8fa\x18\x9f\xeb\xe5\xda\xc6\x8c\xc5^\xf4\xd7\x9f\xbaT\xdb\x81\xfa}\x1c\xb5\x17\x14\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80O\x01\x045\x87\xcf\x04\x9d\xb1\xd0\x00\x80\x00\x00\x01\xe7\x8e\xbf\x9e\xa8y\xa6\x85N\xb3h\x9c\xc2\x83\x1eMB\xf1\xba\xdbXaovW\x9cV\xe7\xbe\xbfO\xd1\x02\x7f\xe0\xe3"7\xa1\x8b2z~\xce9\xc4\xfbq\xa6%\xe0\xc9\xfb\x9d\x06\xf2\xa2q\xdc\xba\xc5\x11\xf8hs\x14&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80O\x01\x045\x87\xcf\x04\xba\xc1H9\x80\x00\x00\x01\xa7:\xdb\xe2\x87\x84\x87cM\xcb\xfc?~\xbd\xe8\xb1\xfc\x99O\x1e\xc0h`\xcf\x01\xc3\xfe.\xa7\x91\xdd\xb6\x02\xe6**\x99s\xeek:z\xf4|"\x9a[\xdep\xbc\xa5\x9b\xd0K\xbb)\x7fV\x93\xd7\xaa%k\x97m\x14s\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x01\x01 \x00\xe1\xf5\x05\x00\x00\x00\x00\x17\xa9\x14\xaf\xde\t\'\xf3\xbd\xf5\xa9\xc3\xdbH;\xb8L\x93\xa5$\x96\x7f>\x87"\x02\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03G0D\x02 \x1f\xa0f\x1ct\xd6\xb9S\xbd\xc4"\x0cY\x19\xe0\xe4p\xdc\xe8qR\xc8$\xf4Hf\xa6\x07\x8e\xda\x16b\x02 W;\xfb\xc0\xbaWo]/\xcc\xd8\xdb\xe8\xc85\xee\x9bx\x1c\xea\xba\xf4[vM\xac\xc2\x11\xae-G\xc7\x01\x01\x04"\x00 \xe7\xa2\x14\x15\xf9\xc7K\xd7\xe8&\x9c\xac\x05\x15\xa2\xfa\xec\xd40\xc2p\xa2R\xe6\xaam\x15-\xec\x8e\x90\xe9\x01\x05iR!\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03!\x03f rK\xb0\x8d\xa8v\xf7\x08\x95F\x00:\xc0\\y\xd7\xee\x9a\xca\xbc\xde\x08\x846xN3\x7f\x13\xed!\x03\xa7RPg\xdbg\'\xd8#\xc2fC\x12#\xa7\x03i\x92\xb6JR\xd5\xdbJ\xd3\xea\x9a\x8c\xa1\x00\x89\xb0S\xae"\x06\x02g\xeaEbC\x93V0~xo\xaf@P70\xd8\xd9Z :\x0e4\\\xb3U\xa5\xdf\xa0?\xce\x03\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03f rK\xb0\x8d\xa8v\xf7\x08\x95F\x00:\xc0\\y\xd7\xee\x9a\xca\xbc\xde\x08\x846xN3\x7f\x13\xed\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00"\x06\x03\xa7RPg\xdbg\'\xd8#\xc2fC\x12#\xa7\x03i\x92\xb6JR\xd5\xdbJ\xd3\xea\x9a\x8c\xa1\x00\x89\xb0\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00"\x00 d\x1c\x13\xabNQ\x92\x9a\x8a\xbf\xa1U\xe8\xb4#\xb8\xcd;B\xfd?m\x87\xd6U\xcfMQ\x03\x85\xbf\x04\x01\x01iR!\x027\xda5Ru8\x1e\xbb\xbf\x98d\xaa\xd6~\x03\x99\xd8\x9f\xcbW~\x9c\xe6\xb0h\x02\x94\xf3\x86\xb3e\x0c!\x02\xfa\x11*\x9bu\xe6F\xdf:\xd8\x01E{"{\xa7Y\xbc\x03\xe5{s8\xfa9\xa8\xd46\x00\x9f\x83\x81!\x03\xf3\x14U\xfcF\x87\x897>\x8d\xcb\x07\xc0\xa61\x1b/ w\x064\xed\x1e\x95H\x04M\xa2\x13d\r\xd4S\xae"\x02\x027\xda5Ru8\x1e\xbb\xbf\x98d\xaa\xd6~\x03\x99\xd8\x9f\xcbW~\x9c\xe6\xb0h\x02\x94\xf3\x86\xb3e\x0c\x1c\x02\x08\xcbw0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x02\xfa\x11*\x9bu\xe6F\xdf:\xd8\x01E{"{\xa7Y\xbc\x03\xe5{s8\xfa9\xa8\xd46\x00\x9f\x83\x81\x1c&\xbb\x83\xc40\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00"\x02\x03\xf3\x14U\xfcF\x87\x897>\x8d\xcb\x07\xc0\xa61\x1b/ w\x064\xed\x1e\x95H\x04M\xa2\x13d\r\xd4\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x01\x00\x00\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    MISSING_GLOBAL_XPUBS_PSBT = "cHNidP8BAFUCAAAAASeaIyOl37UfxF8iD6WLD8E+HjNCeSqF1+Ns1jM7XLw5AAAAAAD/////AaBa6gsAAAAAGXapFP/pwAYQl8w7Y28ssEYPpPxCfStFiKwAAAAAAAEBIJVe6gsAAAAAF6kUY0UgD2jRieGtwN8cTRbqjxTA2+uHIgIDsTQcy6doO2r08SOM1ul+cWfVafrEfx5I1HVBhENVvUZGMEMCIAQktY7/qqaU4VWepck7v9SokGQiQFXN8HC2dxRpRC0HAh9cjrD+plFtYLisszrWTt5g6Hhb+zqpS5m9+GFR25qaAQEEIgAgdx/RitRZZm3Unz1WTj28QvTIR3TjYK2haBao7UiNVoEBBUdSIQOxNBzLp2g7avTxI4zW6X5xZ9Vp+sR/HkjUdUGEQ1W9RiED3lXR4drIBeP4pYwfv5uUwC89uq/hJ/78pJlfJvggg71SriIGA7E0HMunaDtq9PEjjNbpfnFn1Wn6xH8eSNR1QYRDVb1GELSmumcAAACAAAAAgAQAAIAiBgPeVdHh2sgF4/iljB+/m5TALz26r+En/vykmV8m+CCDvRC0prpnAAAAgAAAAIAFAACAAAA="

    # WSH Miniscript - wsh(or_d(pk([73c5da0a/48'/1'/0'/2']tpubDFH9dgzveyD8zTbPUFuLrGmCydNvxehyNdUXKJAQN8x4aZ4j6UZqGfnqFrD4NqyaTVGKbvEW54tsvPTK2UoSbCC1PJY8iCNiwTL3RWZEheQ/<0;1>/*),and_v(v:pkh([02e8bff2/48'/1'/0'/2']tpubDESmyzX6RMHRHvzxgLVXymd193CSYYT6C9M9wa4XK649tbAy2WeEvkPwBgoC7i76MypQxpuruUazQjqibbCogTZuENJX6YiuZ5Fy8sf7GNi/<0;1>/*),older(65535))))#466dtswe
    # tb1qrtvmveqwrzsndt8tzzkgepp2mw8de95dk7hz70kr95f5dt7axvrsgq8lcp
    MINIS_P2WSH_PSBT = b'psbt\xff\x01\x00\xa8\x02\x00\x00\x00\x01\x96Y\x17$\xc8\xc8p\x00\x1e\x981\xe1\x14\xc9\nV7\x0c\x10\xff\xc2\xf6-\xbcyP\x05h\x88q\x9c\x9d\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x03 \xa1\x07\x00\x00\x00\x00\x00\x16\x00\x14V\x911\x9a\xfbg\x8b\xbfC\xad&\x8cE\xa8\x8a\x88\xcd\x8dOk@B\x0f\x00\x00\x00\x00\x00"\x00 \x9f\xef\xdeW\x0e\x8a}\xabP\xf15\x8e\x1df\xcdz\xba\xf6\xb2\xfb\x04\x85\xffu\xda\xcd\xdb\xd3\x8f\xdc\r\xf3\xab\x8d\x07\x00\x00\x00\x00\x00"\x00 \xdffN{{P\x15\\\xc0s\xeb\xa4n[\xfd(G\xe8T\x84\x13\xa4Eb\xf2\xbc\t\xcd\xa7/\x1cj\x00\x00\x00\x00\x00\x01\x00\xa2\x02\x00\x00\x00\x00\x01\x01O#\x9f\xea\xd3\xa8\x1f4|WJn=Bt\xeaV/\xdfR\xcb\xc7\xce^\xfb:\x88\xd4\x020c&\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x01\x06y\x1e\x00\x00\x00\x00\x00"\x00 \x1a\xd9\xb6d\x0e\x18\xa16\xac\xeb\x10\xac\x8c\x84*\xdb\x8e\xdc\x96\x8d\xb7\xae/>\xc3-\x13F\xaf\xdd3\x07\x01@?\xd8Y\xef$\xc2\xc61\x90\xce\xa2\x11\xc7\xfe\xed\x16\x9a\x14}\xc9S\xe9\xc5)s\xbf\x80U\x17\xdbp\xe7\x803\xe9l\xd08\xb2\xaa\x13D\x9d\xff\xe6*5<\xb2YuF~O\xaf}\xc1\xf0,6\x1ca<\xe4\x00\x00\x00\x00\x01\x01+\x06y\x1e\x00\x00\x00\x00\x00"\x00 \x1a\xd9\xb6d\x0e\x18\xa16\xac\xeb\x10\xac\x8c\x84*\xdb\x8e\xdc\x96\x8d\xb7\xae/>\xc3-\x13F\xaf\xdd3\x07\x01\x05D!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\xacsdv\xa9\x14Pf\xd5\xb4\x9de\xad\xceB\xdd\xc8\x8f\x05\xf1D?\xec\xa9\x90\x8a\x88\xad\x03\xff\xff\x00\xb2h"\x06\x03,\xc4Rd\x176!k\xcaX\x9c\x0c\xc1\x018\xddWsSu3\x98\xb3\x12\x9c\x15\x1a\xf4\x7f\xf96\x92\x1c\x02\xe8\xbf\xf20\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00"\x02\x02q\x1f\xb6a\x95\x93\xfb\xc9\x82\xdf\x18\x9f\xd6P\xd2\x1bb\xbc\xf7#\xd3\xdd\xbdy7\xe4\t\xaej\x9b\xea\x04\x1c\x02\xe8\xbf\xf20\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x03\x00\x00\x00"\x02\x02\xb1\xa15\xd5*\x95\x1e\x01\x00\xe2\xc6L\xca\xd8\xd9\x92XM\x03Q\xb9\xda{}N\xe2\xf1\xca\xd1&\xa8\x04\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x03\x00\x00\x00\x00"\x02\x02|n:1\xc3+\xcb\x9e\xa2\x05ds")l[\xa3i6?\x13n\xf8\xeeZ\xcb!\xc8\xf9\xd5\x1eP\x1c\x02\xe8\xbf\xf20\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x01\x00\x00\x00"\x02\x02\xf6l0\xa0}\xbc\xfda\xe7\xc5\xb6\xfa\xcfNl\'\xf9G\xba\xfa\xcb\xb3\xfc\x0e\xa2\x81\xe0\x16~n\x94\x8d\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x01\x00\x00\x00\x00'
    MINIS_P2WSH_PSBT_B43 = "75W:GGD-BWMM*4TP9NAF77L:6V/PUOLESPFPQKQ57CC5ELTGF:IWI89XQDFGV.VM2.-S*0PRBXHCPG8$52N:X.MU2Z29SS11P67*86UF8VKH05CL7GB5BRT:7O*VSFVEA$5Q0NHIQ+F+W2R.9LLY26K9IM*LWSAN3797LD8RP.1NPFJO:Q9Z+7TW.74-NW95D$6M1Q+FVC9PFF:LIL59I-PJYPPG6B58LYGOY.CC9X+DDN9*W1GQ02.3YDQT4H/3E.JV+ZSFC8P0Q8HV8BY7*VLG5RI/Z+301:T2G56ODNRAN$*RX:N$9YP1::D0*V96PZX7W/L3VI8UPP4ET:::ZJ4-F84FOTK7FP25:H+Y+2:48LLR-E74EHPB435$X1P6JZ**C*84Y8UIOVP*/VL:UG9ID2Q.66G$ON70V7KJ9K15ZMFMFEY3ADI0T7NEFT81AD8/1SIT5Y$ZZ3JB*AXVCPB3/0UAX8-D8M1SWD7L.I2-+JW8QPA$5J:6BNVZW1BIU4OUFJE131SX68GV/ZE6E:E.Y.6Q-JVPP.S2GDXNEXNR2GL4L+7I6X66CW3G1KUF6XL--5$AA74+R.-DC$0E5PHHB*CDN+Y-6*N66.T79*9N$1*9EGMWJSZGMKK7PBY-QF6Y-XRPIZ$$2*MVRG5*:DACDHHU/N725G:$OPTU8Q1XJH9C*0/TTPY67P-JM-432EC+1+TK:J4JGH24:*J:QFRE3VP.YF71.KLG-.9D-H6L+UZ4J3DFJK*BXPIWUKQUTGLKEY3XVXDEV+$PI0VH+NNQ1.QQ1LDVJO-OLA9H7*072I25H99+8745AWL2AET$Z:+USI*R$W+AH54B.D1YFO5421NGLTSQZ:+ZP2-YW*72YCB$E$F37$++9*X.BU/W1-M:OT0-19EW4ILXCD+0W*9$$ZUF49HX2BETK:9RC9XZZO2IKA.HQ9KSB2SPWM/NEJ3L9K++*0AZC*EIYQ0JD9V3C8J93HPLSG795DB$D:IJBQS.C4.LG-OCY0FOSGEB8O*VK*98LQVWMAXQNR/RUQDM5YJLMKNHAZ2VW$CZ5+93WJ4C.AH-*WISRKMN:SE.L*ZU/I9N2RR+71W:B0IQU2/5R6N.6W2TF+68.ZTPBOJZUL1FL*PA-J0/1L0-O.XDAG:65BS49/S933SNXT/4.*8Q779GOHHE8.53V39WKO1VE*.ZXV$$IMZG*WT6UI+A.72MH+-.8-LVOJHRKHOP:U69IG.H2WJ7:"
    MINIS_P2WSH_PSBT_B58 = "8vsnQ1aCezSMDDvQnutdZoPfBE3jeAtaVyAaJ2MFA3okEUQwcUsgJKkSo97SQe8yns793CxoYrMB7yDs2UFGvLJP4xwFaod14K14By9ByDVkSvKhka27fTSJd5aU4arYaUugGDcYVACZR1ZdK5k2bAPtjneKhq6CU7cqV9mz3ZRHskKw4zonXfMPZkfcwPxoYoW83aj2YbNaCmLyLvKnX3oJuniExGkHnBGkxjLNYyiHMZ17eTCzwactEEjgnbgRtHFdQv8sYQf6r6jjZsZ8UeLbKYoR43TFg27nz9AGhNQvA4KSH7wAm1r5x2WQh6oae9pRVKfQFKxzRAdqoYA1DAjXtWbqDXZ5wxhqqrFxBtns8kGjGqjmgvJarjGkjrXjQ9YpQRtrU8fzkVjfD8yMRZ8m1xeznQ3G5XCYN9XDkXTJ9hmLiK1qhtvU7thTZ1rFeP9rGgJbbrV1KWdd7s6G1BZfacSzWapoMgKUBZurcTPH5GD7BmTug5VK8bmyvQzn7FDrLXGwdDzHiVcBqfbHFTHgPmemNYRgjFvHC3v6MMd2rim3TBWCTJmo38SHmR4nJuZUy1JqyLnHndN5yJo5uhTwL54r68ReUw5uj8yjXdbszWqWPm4uZ42uV3VC6pcfu87nbPubYue3VFEHcW579EMB4bQXb3PLsBRuqAkbWDKFpfUEvzfqbjSJSzPM6446BTFkDg1wqTinJSfbcuaMj5jGzNC2RRDTey6haNEM18nhPHWtpyfVyynKNAQbT6U4UVMGfK5P52V3U36VLmNVy2PCXciBPwsCYtPoiJ9LECz3K2n2o1xqttFeEkHrVXTeVBgCs2bBG1ithZeoyXPfxayuxNEKw2DpmoH4qBFYmKSSdz1SeRn1rHdiN1BQ4HijPXtbjKm6ak3QvNWtCsNdJGFbG8aUN8HHTxcLCRyfRpL1beDPUauVXQr76jZoQLUrV3Ep3LX27uf1tbLp7J4CV1KWuET4YPcV48dE1PMwCzJKqrt7o2ukNGHuXXdf8X2fp5Y56kGvddL3Bk96VKKxUXVd6serKdebyNcCnS7vUjov92ph1LvbZ8byDvYf6jAe43tdNmuhNcvAgY76CghBbJpfsC2TJbHXyTZWoML5vJNnEW1seG1Let6gQ6yLXt4ZPQodh"
    MINIS_P2WSH_PSBT_B64 = "cHNidP8BAKgCAAAAAZZZFyTIyHAAHpgx4RTJClY3DBD/wvYtvHlQBWiIcZydAAAAAAD9////AyChBwAAAAAAFgAUVpExmvtni79DrSaMRaiKiM2NT2tAQg8AAAAAACIAIJ/v3lcOin2rUPE1jh1mzXq69rL7BIX/ddrN29OP3A3zq40HAAAAAAAiACDfZk57e1AVXMBz66RuW/0oR+hUhBOkRWLyvAnNpy8cagAAAAAAAQCiAgAAAAABAU8jn+rTqB80fFdKbj1CdOpWL99Sy8fOXvs6iNQCMGMmAQAAAAD9////AQZ5HgAAAAAAIgAgGtm2ZA4YoTas6xCsjIQq247clo23ri8+wy0TRq/dMwcBQD/YWe8kwsYxkM6iEcf+7RaaFH3JU+nFKXO/gFUX23DngDPpbNA4sqoTRJ3/5io1PLJZdUZ+T699wfAsNhxhPOQAAAAAAQErBnkeAAAAAAAiACAa2bZkDhihNqzrEKyMhCrbjtyWjbeuLz7DLRNGr90zBwEFRCEDaJVy4osP7anWmBwCN9nl3tv+wW3nFD9oCgLtXRWfdYesc2R2qRRQZtW0nWWtzkLdyI8F8UQ/7KmQioitA///ALJoIgYDLMRSZBc2IWvKWJwMwQE43VdzU3UzmLMSnBUa9H/5NpIcAui/8jAAAIABAACAAAAAgAIAAIAAAAAAAQAAACIGA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHHHPF2gowAACAAQAAgAAAAIACAACAAAAAAAEAAAAAACICAnEftmGVk/vJgt8Yn9ZQ0htivPcj0929eTfkCa5qm+oEHALov/IwAACAAQAAgAAAAIACAACAAAAAAAMAAAAiAgKxoTXVKpUeAQDixkzK2NmSWE0DUbnae31O4vHK0SaoBBxzxdoKMAAAgAEAAIAAAACAAgAAgAAAAAADAAAAACICAnxuOjHDK8ueogVkcyIpbFujaTY/E2747lrLIcj51R5QHALov/IwAACAAQAAgAAAAIACAACAAQAAAAEAAAAiAgL2bDCgfbz9YefFtvrPTmwn+Ue6+suz/A6igeAWfm6UjRxzxdoKMAAAgAEAAIAAAACAAgAAgAEAAAABAAAAAA=="
    MINIS_P2WSH_PSBT_UR_PSBT = UR("crypto-psbt", PSBT(MINIS_P2WSH_PSBT).to_cbor())

    SIGNED_MINIS_P2WSH_PSBT = b'psbt\xff\x01\x00\xa8\x02\x00\x00\x00\x01\x96Y\x17$\xc8\xc8p\x00\x1e\x981\xe1\x14\xc9\nV7\x0c\x10\xff\xc2\xf6-\xbcyP\x05h\x88q\x9c\x9d\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x03 \xa1\x07\x00\x00\x00\x00\x00\x16\x00\x14V\x911\x9a\xfbg\x8b\xbfC\xad&\x8cE\xa8\x8a\x88\xcd\x8dOk@B\x0f\x00\x00\x00\x00\x00"\x00 \x9f\xef\xdeW\x0e\x8a}\xabP\xf15\x8e\x1df\xcdz\xba\xf6\xb2\xfb\x04\x85\xffu\xda\xcd\xdb\xd3\x8f\xdc\r\xf3\xab\x8d\x07\x00\x00\x00\x00\x00"\x00 \xdffN{{P\x15\\\xc0s\xeb\xa4n[\xfd(G\xe8T\x84\x13\xa4Eb\xf2\xbc\t\xcd\xa7/\x1cj\x00\x00\x00\x00\x00\x01\x00\xa2\x02\x00\x00\x00\x00\x01\x01O#\x9f\xea\xd3\xa8\x1f4|WJn=Bt\xeaV/\xdfR\xcb\xc7\xce^\xfb:\x88\xd4\x020c&\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x01\x06y\x1e\x00\x00\x00\x00\x00"\x00 \x1a\xd9\xb6d\x0e\x18\xa16\xac\xeb\x10\xac\x8c\x84*\xdb\x8e\xdc\x96\x8d\xb7\xae/>\xc3-\x13F\xaf\xdd3\x07\x01@?\xd8Y\xef$\xc2\xc61\x90\xce\xa2\x11\xc7\xfe\xed\x16\x9a\x14}\xc9S\xe9\xc5)s\xbf\x80U\x17\xdbp\xe7\x803\xe9l\xd08\xb2\xaa\x13D\x9d\xff\xe6*5<\xb2YuF~O\xaf}\xc1\xf0,6\x1ca<\xe4\x00\x00\x00\x00\x01\x01+\x06y\x1e\x00\x00\x00\x00\x00"\x00 \x1a\xd9\xb6d\x0e\x18\xa16\xac\xeb\x10\xac\x8c\x84*\xdb\x8e\xdc\x96\x8d\xb7\xae/>\xc3-\x13F\xaf\xdd3\x07"\x02\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87G0D\x02 +\xe4\x00\xa1\xcb\xf1\x87\x8b\xef\x07\x86\x89\x1aV\x99\x0b%3W\xfb\xe0v\xc2S\\\xaf\xc4T\x8ej\xe6p\x02 \x1d/\\\x9eS\x0e<\xff\xd0\x81UL\xd1\x15|\x1c}y\x8e?\xdc\xaa\xbc=6\xc1\xcc\x06ll\xca\xc9\x01\x01\x05D!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\xacsdv\xa9\x14Pf\xd5\xb4\x9de\xad\xceB\xdd\xc8\x8f\x05\xf1D?\xec\xa9\x90\x8a\x88\xad\x03\xff\xff\x00\xb2h\x00\x00\x00\x00'
    SIGNED_MINIS_P2WSH_PSBT_B43 = "1TFBDGI0U9N.JNF9JXZO5QI.R..ULE3SYFCOR2+C/2/N6GRF$UFW0$ONNTH.6JYIB/NLQX6H4IPU+P+BHLUB-40/ZB8IK$01$$CS3:5K6MD5R-1U7Z4Y$4QON+B9T:L3$V1OWNAAAK9PHL6:J:1FEHNJ1OV74-I*KNUCQ6G*JGP0/JC:N3Q-X-2-3+OF-:B$--I1TX8X7N+8606XP01.OV1CGGZ2R6R9+Z-KX9ZQXH-LXX75-P43.X6TO44.ARWD85RI1WHNLD903+IAV2FV6T5//T1EM9HNP*1EYDKUZN3*$U8L944W3K*Y2N0N7:AW-M:X0:PZURT:+4:ZBVOZ3$1BKQGHG1DDP8T8YO:NI7.NBVUVPN2-0-4:STS*GJM28W+B-J/T+IJTK4U.OV+MFEYLOC012A22J+L/37BE+E7PZ-2.7F:-UY/E$ZN1ZC2+P7V5FS4CIPRTDAGGCB-XBGZ7.3T7929P8$VPZQSAPU4V8/8BAR:PP/IE+DP.YWW1HJW/3JPDXE.Z90.BN91FW1HQSUVQDHL46*UXBX2BL9T23HT7F.TBS3:86MGX/I8M:YD*:+JMS$WKPWB65.T36WJP1.7A7H*K03GCUW0KGLU-H*5C6Z/0P*LQY2CL$-.P7XC1XG0HQPJM.FKGOC6S3+3KLZX:XW79I.-*4G.S6A05R:YE*6AU*UHA89R$RV.XJX5OQH:9UGKJ0X-JQ2EUTP2TBB/2B6933J.CNJW6M711I2GG-S9*8NTM*ONCBIBQ3BR87.HP17HKP*1P6$8*WRDVWUXRYRMDD9B-OG0+CZ7L3SKK0W64SUVH1-TRP8N$:.F1+6BQ0"
    SIGNED_MINIS_P2WSH_PSBT_B58 = "3UCmDenEJ8kw38Fft6J4JkeeDFYGE139af8mZigLkDsjrthMUBvRfHGs8vFUB8R4LP71PWpogqs6qnCbALrfbFCntEtFGPUNLR4WPrZAe1NCDVwGKHiJfBhxZidHBW2AzLStnJ5utyBZaWG1EjbiPbnhjVNymwy83FQjHjJNr6cqYf71efwP1QXqM33cT5SiFiFw2ANxSKyJxbvWkvVexKqc46fBBkbBnhnPzh5ycnjjNL8v6vx2yzigCPNpRs1xXrPWvdCKf6dFQbuDneqS4uFuUvR1eWv7DfWDVoMZaxvvttKAoUhEELibnSJFkuQoh4637PRbRaAL4EeyRnYP4mqiKEXvTbT4Dp2mYBvW28eZ1irrXkWsLhNyRyuE54NahJpd9vVfpBpa7U5EDRReN83xSaiboWNJ8dxc6UdGAkKqYmDu5RmPAxKYfmTWmA2s1o1WWpNchgaqkYPygMR1VyV8jrbNc8jnhfzGiH9Jo2Wjc8snnUPHY7mGXMmcgvtZtVQqBgMpqfgo1p5JP94LdiTrvu6fPxA9a8GpRw2hXBjeZd1BszHXcPeVWWx8LLkCAn5BiVmRG4RFh8pSfz4yQd5VDWGvrSepRnToPDQNPAYLbQCMKMgUPf3m2uRQtRRqf5t7wcwnSAdCzYVqKScZV3SRWZM2aNZD8fDnj4XKd6TJmmBTuxe51h3odc7fJWqZju2MuJQqAV4grSwE24xk478pyfXSN7Jg9f54MucGTeGFuVFYyiTkozkLjfaXY9mB6SpCBP5wo1R"
    SIGNED_MINIS_P2WSH_PSBT_B64 = "cHNidP8BAKgCAAAAAZZZFyTIyHAAHpgx4RTJClY3DBD/wvYtvHlQBWiIcZydAAAAAAD9////AyChBwAAAAAAFgAUVpExmvtni79DrSaMRaiKiM2NT2tAQg8AAAAAACIAIJ/v3lcOin2rUPE1jh1mzXq69rL7BIX/ddrN29OP3A3zq40HAAAAAAAiACDfZk57e1AVXMBz66RuW/0oR+hUhBOkRWLyvAnNpy8cagAAAAAAAQCiAgAAAAABAU8jn+rTqB80fFdKbj1CdOpWL99Sy8fOXvs6iNQCMGMmAQAAAAD9////AQZ5HgAAAAAAIgAgGtm2ZA4YoTas6xCsjIQq247clo23ri8+wy0TRq/dMwcBQD/YWe8kwsYxkM6iEcf+7RaaFH3JU+nFKXO/gFUX23DngDPpbNA4sqoTRJ3/5io1PLJZdUZ+T699wfAsNhxhPOQAAAAAAQErBnkeAAAAAAAiACAa2bZkDhihNqzrEKyMhCrbjtyWjbeuLz7DLRNGr90zByICA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHRzBEAiAr5AChy/GHi+8HhokaVpkLJTNX++B2wlNcr8RUjmrmcAIgHS9cnlMOPP/QgVVM0RV8HH15jj/cqrw9NsHMBmxsyskBAQVEIQNolXLiiw/tqdaYHAI32eXe2/7BbecUP2gKAu1dFZ91h6xzZHapFFBm1bSdZa3OQt3IjwXxRD/sqZCKiK0D//8AsmgAAAAA"
    SIGNED_MINIS_P2WSH_PSBT_UR_PSBT = UR(
        "crypto-psbt", PSBT(SIGNED_MINIS_P2WSH_PSBT).to_cbor()
    )
    SIGNED_MINIS_P2WSH_PSBT_SD = b'psbt\xff\x01\x00\xa8\x02\x00\x00\x00\x01\x96Y\x17$\xc8\xc8p\x00\x1e\x981\xe1\x14\xc9\nV7\x0c\x10\xff\xc2\xf6-\xbcyP\x05h\x88q\x9c\x9d\x00\x00\x00\x00\x00\xfd\xff\xff\xff\x03 \xa1\x07\x00\x00\x00\x00\x00\x16\x00\x14V\x911\x9a\xfbg\x8b\xbfC\xad&\x8cE\xa8\x8a\x88\xcd\x8dOk@B\x0f\x00\x00\x00\x00\x00"\x00 \x9f\xef\xdeW\x0e\x8a}\xabP\xf15\x8e\x1df\xcdz\xba\xf6\xb2\xfb\x04\x85\xffu\xda\xcd\xdb\xd3\x8f\xdc\r\xf3\xab\x8d\x07\x00\x00\x00\x00\x00"\x00 \xdffN{{P\x15\\\xc0s\xeb\xa4n[\xfd(G\xe8T\x84\x13\xa4Eb\xf2\xbc\t\xcd\xa7/\x1cj\x00\x00\x00\x00\x00\x01\x00\xa2\x02\x00\x00\x00\x00\x01\x01O#\x9f\xea\xd3\xa8\x1f4|WJn=Bt\xeaV/\xdfR\xcb\xc7\xce^\xfb:\x88\xd4\x020c&\x01\x00\x00\x00\x00\xfd\xff\xff\xff\x01\x06y\x1e\x00\x00\x00\x00\x00"\x00 \x1a\xd9\xb6d\x0e\x18\xa16\xac\xeb\x10\xac\x8c\x84*\xdb\x8e\xdc\x96\x8d\xb7\xae/>\xc3-\x13F\xaf\xdd3\x07\x01@?\xd8Y\xef$\xc2\xc61\x90\xce\xa2\x11\xc7\xfe\xed\x16\x9a\x14}\xc9S\xe9\xc5)s\xbf\x80U\x17\xdbp\xe7\x803\xe9l\xd08\xb2\xaa\x13D\x9d\xff\xe6*5<\xb2YuF~O\xaf}\xc1\xf0,6\x1ca<\xe4\x00\x00\x00\x00\x01\x01+\x06y\x1e\x00\x00\x00\x00\x00"\x00 \x1a\xd9\xb6d\x0e\x18\xa16\xac\xeb\x10\xac\x8c\x84*\xdb\x8e\xdc\x96\x8d\xb7\xae/>\xc3-\x13F\xaf\xdd3\x07"\x02\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87G0D\x02 +\xe4\x00\xa1\xcb\xf1\x87\x8b\xef\x07\x86\x89\x1aV\x99\x0b%3W\xfb\xe0v\xc2S\\\xaf\xc4T\x8ej\xe6p\x02 \x1d/\\\x9eS\x0e<\xff\xd0\x81UL\xd1\x15|\x1c}y\x8e?\xdc\xaa\xbc=6\xc1\xcc\x06ll\xca\xc9\x01\x01\x05D!\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\xacsdv\xa9\x14Pf\xd5\xb4\x9de\xad\xceB\xdd\xc8\x8f\x05\xf1D?\xec\xa9\x90\x8a\x88\xad\x03\xff\xff\x00\xb2h"\x06\x03,\xc4Rd\x176!k\xcaX\x9c\x0c\xc1\x018\xddWsSu3\x98\xb3\x12\x9c\x15\x1a\xf4\x7f\xf96\x92\x1c\x02\xe8\xbf\xf20\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00"\x06\x03h\x95r\xe2\x8b\x0f\xed\xa9\xd6\x98\x1c\x027\xd9\xe5\xde\xdb\xfe\xc1m\xe7\x14?h\n\x02\xed]\x15\x9fu\x87\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00"\x02\x02q\x1f\xb6a\x95\x93\xfb\xc9\x82\xdf\x18\x9f\xd6P\xd2\x1bb\xbc\xf7#\xd3\xdd\xbdy7\xe4\t\xaej\x9b\xea\x04\x1c\x02\xe8\xbf\xf20\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x03\x00\x00\x00"\x02\x02\xb1\xa15\xd5*\x95\x1e\x01\x00\xe2\xc6L\xca\xd8\xd9\x92XM\x03Q\xb9\xda{}N\xe2\xf1\xca\xd1&\xa8\x04\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x00\x00\x00\x00\x03\x00\x00\x00\x00"\x02\x02|n:1\xc3+\xcb\x9e\xa2\x05ds")l[\xa3i6?\x13n\xf8\xeeZ\xcb!\xc8\xf9\xd5\x1eP\x1c\x02\xe8\xbf\xf20\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x01\x00\x00\x00"\x02\x02\xf6l0\xa0}\xbc\xfda\xe7\xc5\xb6\xfa\xcfNl\'\xf9G\xba\xfa\xcb\xb3\xfc\x0e\xa2\x81\xe0\x16~n\x94\x8d\x1cs\xc5\xda\n0\x00\x00\x80\x01\x00\x00\x80\x00\x00\x00\x80\x02\x00\x00\x80\x01\x00\x00\x00\x01\x00\x00\x00\x00'
    SIGNED_MINIS_P2WSH_PSBT_B64_SD = "cHNidP8BAKgCAAAAAZZZFyTIyHAAHpgx4RTJClY3DBD/wvYtvHlQBWiIcZydAAAAAAD9////AyChBwAAAAAAFgAUVpExmvtni79DrSaMRaiKiM2NT2tAQg8AAAAAACIAIJ/v3lcOin2rUPE1jh1mzXq69rL7BIX/ddrN29OP3A3zq40HAAAAAAAiACDfZk57e1AVXMBz66RuW/0oR+hUhBOkRWLyvAnNpy8cagAAAAAAAQCiAgAAAAABAU8jn+rTqB80fFdKbj1CdOpWL99Sy8fOXvs6iNQCMGMmAQAAAAD9////AQZ5HgAAAAAAIgAgGtm2ZA4YoTas6xCsjIQq247clo23ri8+wy0TRq/dMwcBQD/YWe8kwsYxkM6iEcf+7RaaFH3JU+nFKXO/gFUX23DngDPpbNA4sqoTRJ3/5io1PLJZdUZ+T699wfAsNhxhPOQAAAAAAQErBnkeAAAAAAAiACAa2bZkDhihNqzrEKyMhCrbjtyWjbeuLz7DLRNGr90zByICA2iVcuKLD+2p1pgcAjfZ5d7b/sFt5xQ/aAoC7V0Vn3WHRzBEAiAr5AChy/GHi+8HhokaVpkLJTNX++B2wlNcr8RUjmrmcAIgHS9cnlMOPP/QgVVM0RV8HH15jj/cqrw9NsHMBmxsyskBAQVEIQNolXLiiw/tqdaYHAI32eXe2/7BbecUP2gKAu1dFZ91h6xzZHapFFBm1bSdZa3OQt3IjwXxRD/sqZCKiK0D//8AsmgiBgMsxFJkFzYha8pYnAzBATjdV3NTdTOYsxKcFRr0f/k2khwC6L/yMAAAgAEAAIAAAACAAgAAgAAAAAABAAAAIgYDaJVy4osP7anWmBwCN9nl3tv+wW3nFD9oCgLtXRWfdYccc8XaCjAAAIABAACAAAAAgAIAAIAAAAAAAQAAAAAAIgICcR+2YZWT+8mC3xif1lDSG2K89yPT3b15N+QJrmqb6gQcAui/8jAAAIABAACAAAAAgAIAAIAAAAAAAwAAACICArGhNdUqlR4BAOLGTMrY2ZJYTQNRudp7fU7i8crRJqgEHHPF2gowAACAAQAAgAAAAIACAACAAAAAAAMAAAAAIgICfG46McMry56iBWRzIilsW6NpNj8TbvjuWsshyPnVHlAcAui/8jAAAIABAACAAAAAgAIAAIABAAAAAQAAACICAvZsMKB9vP1h58W2+s9ObCf5R7r6y7P8DqKB4BZ+bpSNHHPF2gowAACAAQAAgAAAAIACAACAAQAAAAEAAAAA"

    return namedtuple(
        "TestData",
        [
            "TEST_MNEMONIC",
            "P2PKH_PSBT",
            "P2PKH_PSBT_B43",
            "P2PKH_PSBT_B58",
            "P2PKH_PSBT_B64",
            "P2PKH_PSBT_UR_PSBT",
            "SIGNED_P2PKH_PSBT",
            "SIGNED_P2PKH_PSBT_B43",
            "SIGNED_P2PKH_PSBT_B58",
            "SIGNED_P2PKH_PSBT_B64",
            "SIGNED_P2PKH_PSBT_UR_PSBT",
            "SIGNED_P2PKH_PSBT_SD",
            "SIGNED_P2PKH_PSBT_B64_SD",
            "P2WPKH_PSBT",
            "P2WPKH_PSBT_B43",
            "P2WPKH_PSBT_B58",
            "P2WPKH_PSBT_B64",
            "P2WPKH_PSBT_UR_PSBT",
            "P2WPKH_PSBT_BBQR_PSBT",
            "SIGNED_P2WPKH_PSBT",
            "SIGNED_P2WPKH_PSBT_B43",
            "SIGNED_P2WPKH_PSBT_B58",
            "SIGNED_P2WPKH_PSBT_B64",
            "SIGNED_P2WPKH_PSBT_UR_PSBT",
            "SIGNED_P2WPKH_PSBT_BBQR_PSBT",
            "SIGNED_P2WPKH_PSBT_SD",
            "SIGNED_P2WPKH_PSBT_B64_SD",
            "P2SH_P2WPKH_PSBT",
            "P2SH_P2WPKH_PSBT_B43",
            "P2SH_P2WPKH_PSBT_B58",
            "P2SH_P2WPKH_PSBT_B64",
            "P2SH_P2WPKH_PSBT_UR_PSBT",
            "SIGNED_P2SH_P2WPKH_PSBT",
            "SIGNED_P2SH_P2WPKH_PSBT_B43",
            "SIGNED_P2SH_P2WPKH_PSBT_B58",
            "SIGNED_P2SH_P2WPKH_PSBT_B64",
            "SIGNED_P2SH_P2WPKH_PSBT_UR_PSBT",
            "SIGNED_P2SH_P2WPKH_PSBT_SD",
            "SIGNED_P2SH_P2WPKH_PSBT_B64_SD",
            "P2TR_PSBT",
            "P2TR_PSBT_B43",
            "P2TR_PSBT_B58",
            "P2TR_PSBT_B64",
            "P2TR_PSBT_UR_PSBT",
            "SIGNED_P2TR_PSBT",
            "SIGNED_P2TR_PSBT_B43",
            "SIGNED_P2TR_PSBT_B58",
            "SIGNED_P2TR_PSBT_B64",
            "SIGNED_P2TR_PSBT_UR_PSBT",
            "SIGNED_P2TR_PSBT_SD",
            "SIGNED_P2TR_PSBT_B64_SD",
            "P2WSH_PSBT",
            "P2WSH_PSBT_B43",
            "P2WSH_PSBT_B58",
            "P2WSH_PSBT_B64",
            "P2WSH_PSBT_UR_PSBT",
            "SIGNED_P2WSH_PSBT",
            "SIGNED_P2WSH_PSBT_B43",
            "SIGNED_P2WSH_PSBT_B58",
            "SIGNED_P2WSH_PSBT_B64",
            "SIGNED_P2WSH_PSBT_UR_PSBT",
            "SIGNED_P2WSH_PSBT_SD",
            "P2SH_P2WSH_PSBT",
            "P2SH_P2WSH_PSBT_B43",
            "P2SH_P2WSH_PSBT_B58",
            "P2SH_P2WSH_PSBT_B64",
            "P2SH_P2WSH_PSBT_UR_PSBT",
            "SIGNED_P2SH_P2WSH_PSBT",
            "SIGNED_P2SH_P2WSH_PSBT_B43",
            "SIGNED_P2SH_P2WSH_PSBT_B58",
            "SIGNED_P2SH_P2WSH_PSBT_B64",
            "SIGNED_P2SH_P2WSH_PSBT_UR_PSBT",
            "SIGNED_P2SH_P2WSH_PSBT_SD",
            "MISSING_GLOBAL_XPUBS_PSBT",
            "MINIS_P2WSH_PSBT",
            "MINIS_P2WSH_PSBT_B43",
            "MINIS_P2WSH_PSBT_B58",
            "MINIS_P2WSH_PSBT_B64",
            "MINIS_P2WSH_PSBT_UR_PSBT",
            "SIGNED_MINIS_P2WSH_PSBT",
            "SIGNED_MINIS_P2WSH_PSBT_B43",
            "SIGNED_MINIS_P2WSH_PSBT_B58",
            "SIGNED_MINIS_P2WSH_PSBT_B64",
            "SIGNED_MINIS_P2WSH_PSBT_UR_PSBT",
            "SIGNED_MINIS_P2WSH_PSBT_SD",
            "SIGNED_MINIS_P2WSH_PSBT_B64_SD",
        ],
    )(
        TEST_MNEMONIC,
        P2PKH_PSBT,
        P2PKH_PSBT_B43,
        P2PKH_PSBT_B58,
        P2PKH_PSBT_B64,
        P2PKH_PSBT_UR_PSBT,
        SIGNED_P2PKH_PSBT,
        SIGNED_P2PKH_PSBT_B43,
        SIGNED_P2PKH_PSBT_B58,
        SIGNED_P2PKH_PSBT_B64,
        SIGNED_P2PKH_PSBT_UR_PSBT,
        SIGNED_P2PKH_PSBT_SD,
        SIGNED_P2PKH_PSBT_B64_SD,
        P2WPKH_PSBT,
        P2WPKH_PSBT_B43,
        P2WPKH_PSBT_B58,
        P2WPKH_PSBT_B64,
        P2WPKH_PSBT_UR_PSBT,
        P2WPKH_PSBT_BBQR_PSBT,
        SIGNED_P2WPKH_PSBT,
        SIGNED_P2WPKH_PSBT_B43,
        SIGNED_P2WPKH_PSBT_B58,
        SIGNED_P2WPKH_PSBT_B64,
        SIGNED_P2WPKH_PSBT_UR_PSBT,
        SIGNED_P2WPKH_PSBT_BBQR_PSBT,
        SIGNED_P2WPKH_PSBT_SD,
        SIGNED_P2WPKH_PSBT_B64_SD,
        P2SH_P2WPKH_PSBT,
        P2SH_P2WPKH_PSBT_B43,
        P2SH_P2WPKH_PSBT_B58,
        P2SH_P2WPKH_PSBT_B64,
        P2SH_P2WPKH_PSBT_UR_PSBT,
        SIGNED_P2SH_P2WPKH_PSBT,
        SIGNED_P2SH_P2WPKH_PSBT_B43,
        SIGNED_P2SH_P2WPKH_PSBT_B58,
        SIGNED_P2SH_P2WPKH_PSBT_B64,
        SIGNED_P2SH_P2WPKH_PSBT_UR_PSBT,
        SIGNED_P2SH_P2WPKH_PSBT_SD,
        SIGNED_P2SH_P2WPKH_PSBT_B64_SD,
        P2TR_PSBT,
        P2TR_PSBT_B43,
        P2TR_PSBT_B58,
        P2TR_PSBT_B64,
        P2TR_PSBT_UR_PSBT,
        SIGNED_P2TR_PSBT,
        SIGNED_P2TR_PSBT_B43,
        SIGNED_P2TR_PSBT_B58,
        SIGNED_P2TR_PSBT_B64,
        SIGNED_P2TR_PSBT_UR_PSBT,
        SIGNED_P2TR_PSBT_SD,
        SIGNED_P2TR_PSBT_B64_SD,
        P2WSH_PSBT,
        P2WSH_PSBT_B43,
        P2WSH_PSBT_B58,
        P2WSH_PSBT_B64,
        P2WSH_PSBT_UR_PSBT,
        SIGNED_P2WSH_PSBT,
        SIGNED_P2WSH_PSBT_B43,
        SIGNED_P2WSH_PSBT_B58,
        SIGNED_P2WSH_PSBT_B64,
        SIGNED_P2WSH_PSBT_UR_PSBT,
        SIGNED_P2WSH_PSBT_SD,
        P2SH_P2WSH_PSBT,
        P2SH_P2WSH_PSBT_B43,
        P2SH_P2WSH_PSBT_B58,
        P2SH_P2WSH_PSBT_B64,
        P2SH_P2WSH_PSBT_UR_PSBT,
        SIGNED_P2SH_P2WSH_PSBT,
        SIGNED_P2SH_P2WSH_PSBT_B43,
        SIGNED_P2SH_P2WSH_PSBT_B58,
        SIGNED_P2SH_P2WSH_PSBT_B64,
        SIGNED_P2SH_P2WSH_PSBT_UR_PSBT,
        SIGNED_P2SH_P2WSH_PSBT_SD,
        MISSING_GLOBAL_XPUBS_PSBT,
        MINIS_P2WSH_PSBT,
        MINIS_P2WSH_PSBT_B43,
        MINIS_P2WSH_PSBT_B58,
        MINIS_P2WSH_PSBT_B64,
        MINIS_P2WSH_PSBT_UR_PSBT,
        SIGNED_MINIS_P2WSH_PSBT,
        SIGNED_MINIS_P2WSH_PSBT_B43,
        SIGNED_MINIS_P2WSH_PSBT_B58,
        SIGNED_MINIS_P2WSH_PSBT_B64,
        SIGNED_MINIS_P2WSH_PSBT_UR_PSBT,
        SIGNED_MINIS_P2WSH_PSBT_SD,
        SIGNED_MINIS_P2WSH_PSBT_B64_SD,
    )


def test_init_singlesig(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR, FORMAT_BBQR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))
    cases = [
        (tdata.P2PKH_PSBT, FORMAT_NONE),
        (tdata.P2PKH_PSBT_B43, FORMAT_PMOFN),
        (tdata.P2PKH_PSBT_B58, FORMAT_PMOFN),
        (tdata.P2PKH_PSBT_B64, FORMAT_PMOFN),
        (tdata.P2PKH_PSBT_UR_PSBT, FORMAT_UR),
        (tdata.P2WPKH_PSBT, FORMAT_NONE),
        (tdata.P2WPKH_PSBT_B43, FORMAT_PMOFN),
        (tdata.P2WPKH_PSBT_B58, FORMAT_PMOFN),
        (tdata.P2WPKH_PSBT_B64, FORMAT_PMOFN),
        (tdata.P2WPKH_PSBT_UR_PSBT, FORMAT_UR),
        (tdata.P2WPKH_PSBT_BBQR_PSBT, FORMAT_BBQR),
        (tdata.P2SH_P2WPKH_PSBT, FORMAT_NONE),
        (tdata.P2SH_P2WPKH_PSBT_B43, FORMAT_PMOFN),
        (tdata.P2SH_P2WPKH_PSBT_B58, FORMAT_PMOFN),
        (tdata.P2SH_P2WPKH_PSBT_B64, FORMAT_PMOFN),
        (tdata.P2SH_P2WPKH_PSBT_UR_PSBT, FORMAT_UR),
        (tdata.P2TR_PSBT, FORMAT_NONE),
        (tdata.P2TR_PSBT_B43, FORMAT_PMOFN),
        (tdata.P2TR_PSBT_B58, FORMAT_PMOFN),
        (tdata.P2TR_PSBT_B64, FORMAT_PMOFN),
        (tdata.P2TR_PSBT_UR_PSBT, FORMAT_UR),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0], case[1])
        assert isinstance(signer, PSBTSigner)


def test_init_singlesig_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))
    cases = [
        (tdata.P2PKH_PSBT, FORMAT_NONE),
        (tdata.P2WPKH_PSBT, FORMAT_NONE),
        (tdata.P2SH_P2WPKH_PSBT, FORMAT_NONE),
        (tdata.P2TR_PSBT, FORMAT_NONE),
    ]

    for case in cases:
        mocker.patch("builtins.open", mock_open(MockFile(case[0])))
        signer = PSBTSigner(wallet, None, case[1], "dummy.psbt")
        assert isinstance(signer, PSBTSigner)


def test_init_empty_file_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))
    mocker.patch("builtins.open", mock_open(MockFile()))
    with pytest.raises(ValueError):
        PSBTSigner(wallet, None, FORMAT_NONE, "dummy.psbt")


def test_init_multisig(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MULTISIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MULTISIG, NETWORKS["test"]))
    cases = [
        (tdata.P2WSH_PSBT, FORMAT_NONE),
        (tdata.P2WSH_PSBT_B43, FORMAT_PMOFN),
        (tdata.P2WSH_PSBT_B58, FORMAT_PMOFN),
        (tdata.P2WSH_PSBT_B64, FORMAT_PMOFN),
        (tdata.P2WSH_PSBT_UR_PSBT, FORMAT_UR),
        (tdata.P2SH_P2WSH_PSBT, FORMAT_NONE),
        (tdata.P2SH_P2WSH_PSBT_B43, FORMAT_PMOFN),
        (tdata.P2SH_P2WSH_PSBT_B58, FORMAT_PMOFN),
        (tdata.P2SH_P2WSH_PSBT_B64, FORMAT_PMOFN),
        (tdata.P2SH_P2WSH_PSBT_UR_PSBT, FORMAT_UR),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0], case[1])
        assert isinstance(signer, PSBTSigner)


def test_init_multisig_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MULTISIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MULTISIG, NETWORKS["test"]))
    cases = [
        (tdata.P2WSH_PSBT, FORMAT_NONE),
        (tdata.P2SH_P2WSH_PSBT, FORMAT_NONE),
    ]

    for case in cases:
        mock_file = MockFile(case[0])
        mocker.patch("builtins.open", return_value=mock_file)
        signer = PSBTSigner(wallet, None, case[1], "dummy.psbt")
        assert isinstance(signer, PSBTSigner)


def test_init_miniscript(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MINISCRIPT
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MINISCRIPT, NETWORKS["test"]))
    cases = [
        (tdata.MINIS_P2WSH_PSBT, FORMAT_NONE),
        (tdata.MINIS_P2WSH_PSBT_B43, FORMAT_PMOFN),
        (tdata.MINIS_P2WSH_PSBT_B58, FORMAT_PMOFN),
        (tdata.MINIS_P2WSH_PSBT_B64, FORMAT_PMOFN),
        (tdata.MINIS_P2WSH_PSBT_UR_PSBT, FORMAT_UR),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0], case[1])
        assert isinstance(signer, PSBTSigner)


def test_init_miniscript_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MINISCRIPT
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MINISCRIPT, NETWORKS["test"]))
    cases = [
        (tdata.MINIS_P2WSH_PSBT, FORMAT_NONE),
    ]

    for case in cases:
        mock_file = MockFile(case[0])
        mocker.patch("builtins.open", return_value=mock_file)
        signer = PSBTSigner(wallet, None, FORMAT_NONE, "dummy.psbt")
        assert isinstance(signer, PSBTSigner)


def test_init_fails_on_invalid_psbt(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from ur.ur import UR
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))

    cases = [
        ("thisisnotavalidpsbt", FORMAT_NONE),
        (UR("unknown-type", bytearray("thisisnotavalidpsbt".encode())), FORMAT_UR),
    ]
    for case in cases:
        with pytest.raises(ValueError):
            PSBTSigner(wallet, case[0], case[1])


def test_init_fails_on_invalid_psbt_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from ur.ur import UR
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))

    mock_file = MockFile("thisisnotavalidpsbt")
    mocker.patch("builtins.open", return_value=mock_file)
    with pytest.raises(ValueError):
        PSBTSigner(wallet, None, FORMAT_NONE, "dummy.psbt")


def test_sign_singlesig(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR, FORMAT_BBQR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))
    cases = [
        (tdata.P2PKH_PSBT, FORMAT_NONE, tdata.SIGNED_P2PKH_PSBT),
        (tdata.P2PKH_PSBT_B43, FORMAT_PMOFN, tdata.SIGNED_P2PKH_PSBT_B43),
        (tdata.P2PKH_PSBT_B58, FORMAT_PMOFN, tdata.SIGNED_P2PKH_PSBT_B58),
        (tdata.P2PKH_PSBT_B64, FORMAT_PMOFN, tdata.SIGNED_P2PKH_PSBT_B64),
        (tdata.P2PKH_PSBT_UR_PSBT, FORMAT_UR, tdata.SIGNED_P2PKH_PSBT_UR_PSBT),
        (tdata.P2WPKH_PSBT, FORMAT_NONE, tdata.SIGNED_P2WPKH_PSBT),
        (tdata.P2WPKH_PSBT_B43, FORMAT_PMOFN, tdata.SIGNED_P2WPKH_PSBT_B43),
        (tdata.P2WPKH_PSBT_B58, FORMAT_PMOFN, tdata.SIGNED_P2WPKH_PSBT_B58),
        (tdata.P2WPKH_PSBT_B64, FORMAT_PMOFN, tdata.SIGNED_P2WPKH_PSBT_B64),
        (tdata.P2WPKH_PSBT_UR_PSBT, FORMAT_UR, tdata.SIGNED_P2WPKH_PSBT_UR_PSBT),
        (tdata.P2WPKH_PSBT_BBQR_PSBT, FORMAT_BBQR, tdata.SIGNED_P2WPKH_PSBT_BBQR_PSBT),
        (tdata.P2SH_P2WPKH_PSBT, FORMAT_NONE, tdata.SIGNED_P2SH_P2WPKH_PSBT),
        (tdata.P2SH_P2WPKH_PSBT_B43, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WPKH_PSBT_B43),
        (tdata.P2SH_P2WPKH_PSBT_B58, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WPKH_PSBT_B58),
        (tdata.P2SH_P2WPKH_PSBT_B64, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WPKH_PSBT_B64),
        (
            tdata.P2SH_P2WPKH_PSBT_UR_PSBT,
            FORMAT_UR,
            tdata.SIGNED_P2SH_P2WPKH_PSBT_UR_PSBT,
        ),
        (tdata.P2TR_PSBT, FORMAT_NONE, tdata.SIGNED_P2TR_PSBT),
        (tdata.P2TR_PSBT_B43, FORMAT_PMOFN, tdata.SIGNED_P2TR_PSBT_B43),
        (tdata.P2TR_PSBT_B58, FORMAT_PMOFN, tdata.SIGNED_P2TR_PSBT_B58),
        (tdata.P2TR_PSBT_B64, FORMAT_PMOFN, tdata.SIGNED_P2TR_PSBT_B64),
        (tdata.P2TR_PSBT_UR_PSBT, FORMAT_UR, tdata.SIGNED_P2TR_PSBT_UR_PSBT),
        (tdata.P2WPKH_PSBT, FORMAT_PMOFN, tdata.SIGNED_P2WPKH_PSBT_B64),
        (tdata.P2SH_P2WPKH_PSBT, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WPKH_PSBT_B64),
    ]

    num = 0
    for case in cases:
        print("test_sign_singlesig case: ", num)
        num += 1
        signer = PSBTSigner(wallet, case[0], case[1])
        signer.sign()
        if case[1] == FORMAT_BBQR:
            psbt_qr = signer.psbt_qr()
            assert psbt_qr[0].payload == case[2].payload
            assert psbt_qr[1] == case[1]
        else:
            assert signer.psbt_qr() == (case[2], case[1])


def test_sign_singlesig_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))
    cases = [
        (tdata.P2PKH_PSBT, FORMAT_NONE, tdata.SIGNED_P2PKH_PSBT_SD),
        (tdata.P2PKH_PSBT_B64, FORMAT_NONE, tdata.SIGNED_P2PKH_PSBT_B64_SD),
        (tdata.P2WPKH_PSBT, FORMAT_NONE, tdata.SIGNED_P2WPKH_PSBT_SD),
        (tdata.P2WPKH_PSBT_B64, FORMAT_NONE, tdata.SIGNED_P2WPKH_PSBT_B64_SD),
        (tdata.P2SH_P2WPKH_PSBT, FORMAT_NONE, tdata.SIGNED_P2SH_P2WPKH_PSBT_SD),
        (tdata.P2SH_P2WPKH_PSBT_B64, FORMAT_NONE, tdata.SIGNED_P2SH_P2WPKH_PSBT_B64_SD),
        (tdata.P2TR_PSBT, FORMAT_NONE, tdata.SIGNED_P2TR_PSBT_SD),
        (tdata.P2TR_PSBT_B64, FORMAT_NONE, tdata.SIGNED_P2TR_PSBT_B64_SD),
    ]

    num = 0
    for case in cases:
        print("test_sign_singlesig_from_sdcard case: ", num)
        mock_file = MockFile(case[0])
        mocker.patch("builtins.open", mock_open(mock_file))
        signer = PSBTSigner(wallet, None, case[1], "dummy.psbt")
        signer.sign(trim=False)
        if num % 2 == 1:
            # If test case num is odd, check if detected as base64
            assert signer.is_b64_file
            signed_psbt, _ = signer.psbt_qr()
            with open("/sd/" + "dummy-signed.psbt", "w") as f:
                f.write(signed_psbt)
        else:
            with open("/sd/" + "dummy-signed.psbt", "wb") as f:
                signer.psbt.write_to(f)
        assert mock_file.write_data == case[2]
        num += 1


def test_sign_multisig(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MULTISIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MULTISIG, NETWORKS["test"]))
    cases = [
        (tdata.P2WSH_PSBT, FORMAT_NONE, tdata.SIGNED_P2WSH_PSBT),
        (tdata.P2WSH_PSBT_B43, FORMAT_PMOFN, tdata.SIGNED_P2WSH_PSBT_B43),
        (tdata.P2WSH_PSBT_B58, FORMAT_PMOFN, tdata.SIGNED_P2WSH_PSBT_B58),
        (tdata.P2WSH_PSBT_B64, FORMAT_PMOFN, tdata.SIGNED_P2WSH_PSBT_B64),
        (tdata.P2WSH_PSBT_UR_PSBT, FORMAT_UR, tdata.SIGNED_P2WSH_PSBT_UR_PSBT),
        (tdata.P2SH_P2WSH_PSBT, FORMAT_NONE, tdata.SIGNED_P2SH_P2WSH_PSBT),
        (tdata.P2SH_P2WSH_PSBT_B43, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WSH_PSBT_B43),
        (tdata.P2SH_P2WSH_PSBT_B58, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WSH_PSBT_B58),
        (tdata.P2SH_P2WSH_PSBT_B64, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WSH_PSBT_B64),
        (
            tdata.P2SH_P2WSH_PSBT_UR_PSBT,
            FORMAT_UR,
            tdata.SIGNED_P2SH_P2WSH_PSBT_UR_PSBT,
        ),
        (tdata.P2WSH_PSBT, FORMAT_PMOFN, tdata.SIGNED_P2WSH_PSBT_B64),
        (tdata.P2SH_P2WSH_PSBT, FORMAT_PMOFN, tdata.SIGNED_P2SH_P2WSH_PSBT_B64),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0], case[1])
        signer.sign()
        assert signer.psbt_qr() == (case[2], case[1])


def test_sign_multisig_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MULTISIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MULTISIG, NETWORKS["test"]))
    cases = [
        (tdata.P2WSH_PSBT, FORMAT_NONE, tdata.SIGNED_P2WSH_PSBT_SD),
        (tdata.P2SH_P2WSH_PSBT, FORMAT_NONE, tdata.SIGNED_P2SH_P2WSH_PSBT_SD),
    ]

    for case in cases:
        mock_file = MockFile(case[0])
        mocker.patch("builtins.open", return_value=mock_file)
        signer = PSBTSigner(wallet, None, case[1], "dummy.psbt")
        signer.sign(trim=False)
        with open("dummy-signed.psbt", "wb") as f:
            signer.psbt.write_to(f)
        assert mock_file.write_data == case[2]


def test_sign_miniscript(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MINISCRIPT
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MINISCRIPT, NETWORKS["test"]))
    cases = [
        (tdata.MINIS_P2WSH_PSBT, FORMAT_NONE, tdata.SIGNED_MINIS_P2WSH_PSBT),
        (tdata.MINIS_P2WSH_PSBT_B43, FORMAT_PMOFN, tdata.SIGNED_MINIS_P2WSH_PSBT_B43),
        (tdata.MINIS_P2WSH_PSBT_B58, FORMAT_PMOFN, tdata.SIGNED_MINIS_P2WSH_PSBT_B58),
        (tdata.MINIS_P2WSH_PSBT_B64, FORMAT_PMOFN, tdata.SIGNED_MINIS_P2WSH_PSBT_B64),
        (
            tdata.MINIS_P2WSH_PSBT_UR_PSBT,
            FORMAT_UR,
            tdata.SIGNED_MINIS_P2WSH_PSBT_UR_PSBT,
        ),
    ]

    for case in cases:
        signer = PSBTSigner(wallet, case[0], case[1])
        signer.sign()
        assert signer.psbt_qr() == (case[2], case[1])


def test_sign_miniscript_from_sdcard(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MINISCRIPT
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE, FORMAT_PMOFN, FORMAT_UR

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MINISCRIPT, NETWORKS["test"]))
    cases = [
        (tdata.MINIS_P2WSH_PSBT, FORMAT_NONE, tdata.SIGNED_MINIS_P2WSH_PSBT_SD),
        (tdata.MINIS_P2WSH_PSBT_B64, FORMAT_NONE, tdata.SIGNED_MINIS_P2WSH_PSBT_B64_SD),
    ]

    for i, case in enumerate(cases):
        mock_file = MockFile(case[0])
        mocker.patch("builtins.open", mock_open(mock_file))
        signer = PSBTSigner(wallet, None, case[1], "dummy.psbt")
        signer.sign(trim=False)
        if i == 1:
            assert signer.is_b64_file
            signed_psbt, _ = signer.psbt_qr()
            with open("/sd/" + "dummy-signed.psbt", "w") as f:
                f.write(signed_psbt)
        else:
            with open("/sd/" + "dummy-signed.psbt", "wb") as f:
                signer.psbt.write_to(f)
        assert mock_file.write_data == case[2]


def test_sign_fails_with_0_sigs_added(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MULTISIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MULTISIG, NETWORKS["test"]))
    signer = PSBTSigner(wallet, tdata.P2WSH_PSBT, FORMAT_NONE)
    mocker.patch.object(signer.psbt, "sign_with", mocker.MagicMock(return_value=0))

    with pytest.raises(ValueError):
        signer.sign()
    signer.psbt.sign_with.assert_called_with(wallet.key.root)


def test_outputs_singlesig(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG, P2PKH, P2WPKH, P2SH_P2WPKH, P2TR
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    cases = [
        (
            tdata.P2PKH_PSBT,
            [
                "Inputs (3): ₿ 0.00 001 856\n\nSpend (1): ₿ 0.00 001 000\n\nFee: ₿ 0.00 000 856 (85.6%) ~1.8 sat/vB",
                "1. Spend: \n\ntb1q4mx3ahp7laj65gyaqg27w0tsjpwuz6rvaxx3tl\n\n₿ 0.00 001 000",
            ],
            Wallet(
                Key(
                    tdata.TEST_MNEMONIC,
                    TYPE_SINGLESIG,
                    NETWORKS["test"],
                    script_type=P2PKH,
                )
            ),
        ),
        (
            tdata.P2WPKH_PSBT,
            [
                "Inputs (1): ₿ 1.00 000 000\n\nSpend (1): ₿ 0.10 000 000\n\nSelf-transfer or Change (1): ₿ 0.89 997 180\n\nFee: ₿ 0.00 002 820 (0.1%) ~20.0 sat/vB",
                "1. Spend: \n\ntb1que40al7rsw88ru9z0vr78vqwme4w3ctqj694kx\n\n₿ 0.10 000 000",
                "1. Change: \n\ntb1q9u62588spffmq4dzjxsr5l297znf3z6j5p2688\n\n₿ 0.89 997 180",
            ],
            Wallet(
                Key(
                    tdata.TEST_MNEMONIC,
                    TYPE_SINGLESIG,
                    NETWORKS["test"],
                    script_type=P2WPKH,
                )
            ),
        ),
        (
            tdata.P2SH_P2WPKH_PSBT,
            [
                "Inputs (1): ₿ 1.00 000 000\n\nSpend (1): ₿ 0.10 000 000\n\nSelf-transfer or Change (1): ₿ 0.89 996 700\n\nFee: ₿ 0.00 003 300 (0.1%) ~20.0 sat/vB",
                "1. Spend: \n\ntb1que40al7rsw88ru9z0vr78vqwme4w3ctqj694kx\n\n₿ 0.10 000 000",
                "1. Change: \n\n2MvdUi5o3f2tnEFh9yGvta6FzptTZtkPJC8\n\n₿ 0.89 996 700",
            ],
            Wallet(
                Key(
                    tdata.TEST_MNEMONIC,
                    TYPE_SINGLESIG,
                    NETWORKS["test"],
                    script_type=P2SH_P2WPKH,
                )
            ),
        ),
        (
            tdata.P2TR_PSBT,
            [
                "Inputs (1): ₿ 0.00 010 111\n\nSpend (1): ₿ 0.00 001 000\n\nSelf-transfer or Change (2): ₿ 0.00 008 738\n\nFee: ₿ 0.00 000 373 (3.9%) ~2.0 sat/vB",
                "1. Spend: \n\ntb1q4mx3ahp7laj65gyaqg27w0tsjpwuz6rvaxx3tl\n\n₿ 0.00 001 000",
                "1. Self-transfer: \n\ntb1pn5kekm0xpnwd6kg8c8qfvv2fr0w5xnhw42927wem7xwk84f7gzvsvctkhp\n\n₿ 0.00 001 000",
                "1. Change: \n\ntb1pwhn9lzpaukrjwvwe365x7hcgvtcfywwsaxcq7j04jgrfcxzdq23qhzr7wt\n\n₿ 0.00 007 738",
            ],
            Wallet(
                Key(
                    tdata.TEST_MNEMONIC,
                    TYPE_SINGLESIG,
                    NETWORKS["test"],
                    script_type=P2TR,
                )
            ),
        ),
    ]
    case_num = 0
    for case in cases:
        print("test_outputs_singlesig case: ", case_num)
        signer = PSBTSigner(case[2], case[0], FORMAT_NONE)
        outputs, _ = signer.outputs()
        assert outputs == case[1]
        case_num += 1


def test_outputs_multisig(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MULTISIG, P2WSH, P2SH_P2WSH
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    cases = [
        (
            tdata.P2WSH_PSBT,
            [
                "Inputs (2): ₿\u20090.20 000 000\n\nSpend (2): ₿\u20090.19 993 880\n\nFee: ₿\u20090.00 006 120 (0.1%) ~20.1 sat/vB",
                "1. Spend: \n\ntb1q4xgr8suxvgenukgf4c7r6qaawxxmy9zelh24q8hg5pfxzn2ekn3qfw808t\n\n₿\u20090.01 000 000",
                "2. Spend: \n\ntb1q35pg2rdt3p0v27dmdh9st43q8vzl29cps6kt3yradnqmg55eahfqfgn83n\n\n₿\u20090.18 993 880",
            ],
            Wallet(
                Key(
                    tdata.TEST_MNEMONIC,
                    TYPE_MULTISIG,
                    NETWORKS["test"],
                    script_type=P2WSH,
                )
            ),
        ),
        (
            tdata.P2SH_P2WSH_PSBT,
            [
                "Inputs (1): ₿\u20091.00 000 000\n\nSpend (2): ₿\u20090.99 995 740\n\nFee: ₿\u20090.00 004 260 (0.1%) ~20.0 sat/vB",
                "1. Spend: \n\n2N3vYfcg14Axr4NN33ADUorE2kEGEchFJpC\n\n₿\u20090.89 995 740",
                "2. Spend: \n\ntb1que40al7rsw88ru9z0vr78vqwme4w3ctqj694kx\n\n₿\u20090.10 000 000",
            ],
            Wallet(
                Key(
                    tdata.TEST_MNEMONIC,
                    TYPE_MULTISIG,
                    NETWORKS["test"],
                    script_type=P2SH_P2WSH,
                )
            ),
            # TODO: Add multisigs with descriptor so change can be deteted
        ),
    ]

    for case in cases:
        signer = PSBTSigner(case[2], case[0], FORMAT_NONE)
        outputs, _ = signer.outputs()
        assert outputs == case[1]


def test_xpubs_fails_with_no_xpubs(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_MULTISIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    wallet = Wallet(Key(tdata.TEST_MNEMONIC, TYPE_MULTISIG, NETWORKS["test"]))

    with pytest.raises(ValueError, match="missing xpubs"):
        signer = PSBTSigner(wallet, tdata.MISSING_GLOBAL_XPUBS_PSBT, FORMAT_NONE)
        signer.xpubs()


def test_sign_single_1_input_1_output_no_change(m5stickv):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_PMOFN

    MNEMONIC = "action action action action action action action action action action action action"
    PSBT_B64 = "cHNidP8BAFMCAAAAAcfPlS2RvKvXxP/UxRmlAzMZcpLPKTOsBNbFM1JpT5Q7BwAAAAD9////AXAXAAAAAAAAF6kUK7ey9d8Pcw7ufsChrS3L5Ays13SHEgQlAE8BBDWHzwNOAaDGgAAAAA6sE2xHBRocbxB2m7sG3JvBy6PH2P+6FU8Xz26TLNf+Ax8/bmYn6gHZ6KY5opTh2Ajf+3sKBpZ40s59aYtcEnY+EODFlcVUAACAAQAAgAAAAIAAAQD9fQECAAAAAwZh04JGb3rJ3RJGINf/5lNG3RFk9DQyfqaKJK336OcaAQAAAAD9////pZE7Tecrp3E9O5JGSLma4D5TCG5N3uD4deLODBvkt4EAAAAAAP3///+lkTtN5yuncT07kkZIuZrgPlMIbk3e4Ph14s4MG+S3gQEAAAAA/f///wgsAQAAAAAAABYAFARbVWJaVJuYh2b3/HFtU3tQ9eoCLAEAAAAAAAAWABT4gSb5k7/g3ZrEXLyHFlP/C11NFCwBAAAAAAAAFgAU04NlSannloiWwZHvG1uf9aL0NPosAQAAAAAAABYAFNDJ5cj/6H72UNT95nAOLylXp/S5LAEAAAAAAAAWABTj8DqdkD3qZujRRRl4HlpWaADUBywBAAAAAAAAFgAUmPKKcthXsgBlI5AZbJtdEUrFe6gsAQAAAAAAABYAFF1lFcZm2E/gjALNKEfBtzGMsrsqmRgAAAAAAAAWABRk/PxLrogzR/Meytzu0v72RMgGh878JAABAR+ZGAAAAAAAABYAFGT8/EuuiDNH8x7K3O7S/vZEyAaHAQMEAQAAACIGAloQH2tjbm2ayZtJb2Gb0juSNIH9MIoEfX2UW0zE3l/SGODFlcVUAACAAQAAgAAAAIAAAAAAYwAAAAAA"
    OUTPUT = [
        "Inputs (1): ₿ 0.00 006 297\n\nSpend (1): ₿ 0.00 006 000\n\nFee: ₿ 0.00 000 297 (5.0%) ~2.7 sat/vB",
        "1. Spend: \n\n2MwEP7AfPt8NC65ACmcUhUtDZgGSxYiWUy4\n\n₿ 0.00 006 000",
    ]

    wallet = Wallet(Key(MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))
    signer = PSBTSigner(wallet, PSBT_B64, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert outputs == OUTPUT


def test_path_mismatch(mocker, m5stickv, tdata):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, P2WPKH, P2SH_P2WPKH, P2TR, TYPE_SINGLESIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_NONE

    cases = [
        (
            # Legacy wallet vs Legacy PSBT
            P2WPKH,
            tdata.P2WPKH_PSBT,
            "",
        ),
        (
            # Legacy wallet vs Taproot PSBT
            P2WPKH,
            tdata.P2TR_PSBT,
            "m/86'/1'/0'",
        ),
        (
            # Nested Segwit wallet vs Legacy PSBT
            P2SH_P2WPKH,
            tdata.P2PKH_PSBT,
            "m/44'/1'/0'",
        ),
        (
            # Nested Segwit wallet vs Nested Segwit PSBT
            P2SH_P2WPKH,
            tdata.P2SH_P2WPKH_PSBT,
            "",
        ),
        (
            # Native Segwit wallet vs Taproot PSBT
            P2WPKH,
            tdata.P2TR_PSBT,
            "m/86'/1'/0'",
        ),
        (
            # Native Segwit wallet vs Native Segwit PSBT
            P2WPKH,
            tdata.P2WPKH_PSBT,
            "",
        ),
        (
            # Taproot wallet vs Native Segwit PSBT
            P2TR,
            tdata.P2WPKH_PSBT,
            "m/84'/1'/0'",
        ),
        (
            # Taproot wallet vs Taproot PSBT
            P2TR,
            tdata.P2TR_PSBT,
            "",
        ),
        (
            # Native Segwit mainnet wallet vs Native Segwit testnet PSBT
            P2WPKH,
            tdata.P2WPKH_PSBT,
            "m/84'/1'/0'",
            NETWORKS["main"],
        ),
    ]

    for case in cases:
        if len(case) > 3:
            wallet = Wallet(
                Key(tdata.TEST_MNEMONIC, TYPE_SINGLESIG, case[3], script_type=case[0])
            )
        else:
            wallet = Wallet(
                Key(
                    tdata.TEST_MNEMONIC,
                    TYPE_SINGLESIG,
                    NETWORKS["test"],
                    script_type=case[0],
                )
            )
        signer = PSBTSigner(wallet, case[1], FORMAT_NONE)
        path_mismatch = signer.path_mismatch()
        assert path_mismatch == case[2]


def test_sign_sats_vB(m5stickv):
    from embit.networks import NETWORKS
    from krux.psbt import PSBTSigner
    from krux.key import Key, TYPE_SINGLESIG, TYPE_MULTISIG
    from krux.wallet import Wallet
    from krux.qr import FORMAT_PMOFN

    MNEMONIC = "action action action action action action action action action action action action"
    wallet = Wallet(Key(MNEMONIC, TYPE_SINGLESIG, NETWORKS["test"]))

    PSBT_satvB_1_31 = "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"
    signer = PSBTSigner(wallet, PSBT_satvB_1_31, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (5): ₿ 0.00 001 500\n\nSpend (1): ₿ 0.00 001 000\n\nFee: ₿ 0.00 000 500 (50.0%) ~1.3 sat/vB"
    )

    PSBT_satvB_28_04 = "cHNidP8BAH4CAAAAAcfPlS2RvKvXxP/UxRmlAzMZcpLPKTOsBNbFM1JpT5Q7BwAAAAD9////AugDAAAAAAAAIgAguKIqvP6jJ6Lj5PVWAoa1nazfyQ8DzfgI34hQnNxYStPoAwAAAAAAABepFGJYgmsnwywOzlosjYc84fGiiGPTh7r5KgBPAQQ1h88DTgGgxoAAAAAOrBNsRwUaHG8Qdpu7Btybwcujx9j/uhVPF89ukyzX/gMfP25mJ+oB2eimOaKU4dgI3/t7CgaWeNLOfWmLXBJ2PhDgxZXFVAAAgAEAAIAAAACAAAEA/X0BAgAAAAMGYdOCRm96yd0SRiDX/+ZTRt0RZPQ0Mn6miiSt9+jnGgEAAAAA/f///6WRO03nK6dxPTuSRki5muA+UwhuTd7g+HXizgwb5LeBAAAAAAD9////pZE7Tecrp3E9O5JGSLma4D5TCG5N3uD4deLODBvkt4EBAAAAAP3///8ILAEAAAAAAAAWABQEW1ViWlSbmIdm9/xxbVN7UPXqAiwBAAAAAAAAFgAU+IEm+ZO/4N2axFy8hxZT/wtdTRQsAQAAAAAAABYAFNODZUmp55aIlsGR7xtbn/Wi9DT6LAEAAAAAAAAWABTQyeXI/+h+9lDU/eZwDi8pV6f0uSwBAAAAAAAAFgAU4/A6nZA96mbo0UUZeB5aVmgA1AcsAQAAAAAAABYAFJjyinLYV7IAZSOQGWybXRFKxXuoLAEAAAAAAAAWABRdZRXGZthP4IwCzShHwbcxjLK7KpkYAAAAAAAAFgAUZPz8S66IM0fzHsrc7tL+9kTIBofO/CQAAQEfmRgAAAAAAAAWABRk/PxLrogzR/Meytzu0v72RMgGhwEDBAEAAAAiBgJaEB9rY25tmsmbSW9hm9I7kjSB/TCKBH19lFtMxN5f0hjgxZXFVAAAgAEAAIAAAACAAAAAAGMAAAAAAAA="
    signer = PSBTSigner(wallet, PSBT_satvB_28_04, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (1): ₿ 0.00 006 297\n\nSpend (2): ₿ 0.00 002 000\n\nFee: ₿ 0.00 004 297 (214.9%) ~27.9 sat/vB"
    )

    PSBT_satvB_12_03 = "cHNidP8BAP0WAQIAAAABx8+VLZG8q9fE/9TFGaUDMxlyks8pM6wE1sUzUmlPlDsHAAAAAP3///8GTAEAAAAAAAAiACC4oiq8/qMnouPk9VYChrWdrN/JDwPN+AjfiFCc3FhK0xwCAAAAAAAAF6kUYliCayfDLA7OWiyNhzzh8aKIY9OHTAEAAAAAAAAiACDwabzM44F/2f9evGkQqXxhFwjzErVHgJfc2IE2I91E/U0BAAAAAAAAIlEgJeBfcLU573hJOaYb6XQGR/eOKVSvBR9TW3+FoxRQEWIkAgAAAAAAABl2qRRrgQv3nFAPaNKPYAXmsjT7Ru6DJoisHAIAAAAAAAAXqRSDAQVKg8ZQzf3pc5CIXtSjjvybt4e/+SoATwEENYfPA04BoMaAAAAADqwTbEcFGhxvEHabuwbcm8HLo8fY/7oVTxfPbpMs1/4DHz9uZifqAdnopjmilOHYCN/7ewoGlnjSzn1pi1wSdj4Q4MWVxVQAAIABAACAAAAAgAABAP19AQIAAAADBmHTgkZvesndEkYg1//mU0bdEWT0NDJ+pookrffo5xoBAAAAAP3///+lkTtN5yuncT07kkZIuZrgPlMIbk3e4Ph14s4MG+S3gQAAAAAA/f///6WRO03nK6dxPTuSRki5muA+UwhuTd7g+HXizgwb5LeBAQAAAAD9////CCwBAAAAAAAAFgAUBFtVYlpUm5iHZvf8cW1Te1D16gIsAQAAAAAAABYAFPiBJvmTv+DdmsRcvIcWU/8LXU0ULAEAAAAAAAAWABTTg2VJqeeWiJbBke8bW5/1ovQ0+iwBAAAAAAAAFgAU0MnlyP/ofvZQ1P3mcA4vKVen9LksAQAAAAAAABYAFOPwOp2QPepm6NFFGXgeWlZoANQHLAEAAAAAAAAWABSY8opy2FeyAGUjkBlsm10RSsV7qCwBAAAAAAAAFgAUXWUVxmbYT+CMAs0oR8G3MYyyuyqZGAAAAAAAABYAFGT8/EuuiDNH8x7K3O7S/vZEyAaHzvwkAAEBH5kYAAAAAAAAFgAUZPz8S66IM0fzHsrc7tL+9kTIBocBAwQBAAAAIgYCWhAfa2NubZrJm0lvYZvSO5I0gf0wigR9fZRbTMTeX9IY4MWVxVQAAIABAACAAAAAgAAAAABjAAAAAAAAAAAAAA=="
    signer = PSBTSigner(wallet, PSBT_satvB_12_03, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (1): ₿ 0.00 006 297\n\nSpend (6): ₿ 0.00 002 625\n\nFee: ₿ 0.00 003 672 (139.9%) ~12.0 sat/vB"
    )

    PSBT_satvB_8_75 = "cHNidP8BAP0WAQIAAAABx8+VLZG8q9fE/9TFGaUDMxlyks8pM6wE1sUzUmlPlDsHAAAAAP3///8GJAIAAAAAAAAZdqkUa4EL95xQD2jSj2AF5rI0+0bugyaIrDUFAAAAAAAAIlEgJeBfcLU573hJOaYb6XQGR/eOKVSvBR9TW3+FoxRQEWIcAgAAAAAAABepFIMBBUqDxlDN/elzkIhe1KOO/Ju3hxwCAAAAAAAAF6kUYliCayfDLA7OWiyNhzzh8aKIY9OHTAEAAAAAAAAiACC4oiq8/qMnouPk9VYChrWdrN/JDwPN+AjfiFCc3FhK00wBAAAAAAAAIgAg8Gm8zOOBf9n/XrxpEKl8YRcI8xK1R4CX3NiBNiPdRP2/+SoATwEENYfPA04BoMaAAAAADqwTbEcFGhxvEHabuwbcm8HLo8fY/7oVTxfPbpMs1/4DHz9uZifqAdnopjmilOHYCN/7ewoGlnjSzn1pi1wSdj4Q4MWVxVQAAIABAACAAAAAgAABAP19AQIAAAADBmHTgkZvesndEkYg1//mU0bdEWT0NDJ+pookrffo5xoBAAAAAP3///+lkTtN5yuncT07kkZIuZrgPlMIbk3e4Ph14s4MG+S3gQAAAAAA/f///6WRO03nK6dxPTuSRki5muA+UwhuTd7g+HXizgwb5LeBAQAAAAD9////CCwBAAAAAAAAFgAUBFtVYlpUm5iHZvf8cW1Te1D16gIsAQAAAAAAABYAFPiBJvmTv+DdmsRcvIcWU/8LXU0ULAEAAAAAAAAWABTTg2VJqeeWiJbBke8bW5/1ovQ0+iwBAAAAAAAAFgAU0MnlyP/ofvZQ1P3mcA4vKVen9LksAQAAAAAAABYAFOPwOp2QPepm6NFFGXgeWlZoANQHLAEAAAAAAAAWABSY8opy2FeyAGUjkBlsm10RSsV7qCwBAAAAAAAAFgAUXWUVxmbYT+CMAs0oR8G3MYyyuyqZGAAAAAAAABYAFGT8/EuuiDNH8x7K3O7S/vZEyAaHzvwkAAEBH5kYAAAAAAAAFgAUZPz8S66IM0fzHsrc7tL+9kTIBocBAwQBAAAAIgYCWhAfa2NubZrJm0lvYZvSO5I0gf0wigR9fZRbTMTeX9IY4MWVxVQAAIABAACAAAAAgAAAAABjAAAAAAAAAAAAAA=="
    signer = PSBTSigner(wallet, PSBT_satvB_8_75, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (1): ₿ 0.00 006 297\n\nSpend (6): ₿ 0.00 003 625\n\nFee: ₿ 0.00 002 672 (73.8%) ~8.7 sat/vB"
    )

    PSBT_satvB_5_48 = "cHNidP8BAP0WAQIAAAABx8+VLZG8q9fE/9TFGaUDMxlyks8pM6wE1sUzUmlPlDsHAAAAAP3///8GJAIAAAAAAAAZdqkUa4EL95xQD2jSj2AF5rI0+0bugyaIrBwCAAAAAAAAF6kUYliCayfDLA7OWiyNhzzh8aKIY9OHHAIAAAAAAAAXqRSDAQVKg8ZQzf3pc5CIXtSjjvybt4dMAQAAAAAAACIAIPBpvMzjgX/Z/168aRCpfGEXCPMStUeAl9zYgTYj3UT9TAEAAAAAAAAiACC4oiq8/qMnouPk9VYChrWdrN/JDwPN+AjfiFCc3FhK0x0JAAAAAAAAIlEgJeBfcLU573hJOaYb6XQGR/eOKVSvBR9TW3+FoxRQEWK/+SoATwEENYfPA04BoMaAAAAADqwTbEcFGhxvEHabuwbcm8HLo8fY/7oVTxfPbpMs1/4DHz9uZifqAdnopjmilOHYCN/7ewoGlnjSzn1pi1wSdj4Q4MWVxVQAAIABAACAAAAAgAABAP19AQIAAAADBmHTgkZvesndEkYg1//mU0bdEWT0NDJ+pookrffo5xoBAAAAAP3///+lkTtN5yuncT07kkZIuZrgPlMIbk3e4Ph14s4MG+S3gQAAAAAA/f///6WRO03nK6dxPTuSRki5muA+UwhuTd7g+HXizgwb5LeBAQAAAAD9////CCwBAAAAAAAAFgAUBFtVYlpUm5iHZvf8cW1Te1D16gIsAQAAAAAAABYAFPiBJvmTv+DdmsRcvIcWU/8LXU0ULAEAAAAAAAAWABTTg2VJqeeWiJbBke8bW5/1ovQ0+iwBAAAAAAAAFgAU0MnlyP/ofvZQ1P3mcA4vKVen9LksAQAAAAAAABYAFOPwOp2QPepm6NFFGXgeWlZoANQHLAEAAAAAAAAWABSY8opy2FeyAGUjkBlsm10RSsV7qCwBAAAAAAAAFgAUXWUVxmbYT+CMAs0oR8G3MYyyuyqZGAAAAAAAABYAFGT8/EuuiDNH8x7K3O7S/vZEyAaHzvwkAAEBH5kYAAAAAAAAFgAUZPz8S66IM0fzHsrc7tL+9kTIBocBAwQBAAAAIgYCWhAfa2NubZrJm0lvYZvSO5I0gf0wigR9fZRbTMTeX9IY4MWVxVQAAIABAACAAAAAgAAAAABjAAAAAAAAAAAAAA=="
    signer = PSBTSigner(wallet, PSBT_satvB_5_48, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (1): ₿ 0.00 006 297\n\nSpend (6): ₿ 0.00 004 625\n\nFee: ₿ 0.00 001 672 (36.2%) ~5.5 sat/vB"
    )

    PSBT_satvB_2_2 = "cHNidP8BAP0WAQIAAAABx8+VLZG8q9fE/9TFGaUDMxlyks8pM6wE1sUzUmlPlDsHAAAAAP3///8GJAIAAAAAAAAZdqkUa4EL95xQD2jSj2AF5rI0+0bugyaIrAUNAAAAAAAAIlEgJeBfcLU573hJOaYb6XQGR/eOKVSvBR9TW3+FoxRQEWJMAQAAAAAAACIAILiiKrz+oyei4+T1VgKGtZ2s38kPA834CN+IUJzcWErTHAIAAAAAAAAXqRSDAQVKg8ZQzf3pc5CIXtSjjvybt4dMAQAAAAAAACIAIPBpvMzjgX/Z/168aRCpfGEXCPMStUeAl9zYgTYj3UT9HAIAAAAAAAAXqRRiWIJrJ8MsDs5aLI2HPOHxoohj04e/+SoATwEENYfPA04BoMaAAAAADqwTbEcFGhxvEHabuwbcm8HLo8fY/7oVTxfPbpMs1/4DHz9uZifqAdnopjmilOHYCN/7ewoGlnjSzn1pi1wSdj4Q4MWVxVQAAIABAACAAAAAgAABAP19AQIAAAADBmHTgkZvesndEkYg1//mU0bdEWT0NDJ+pookrffo5xoBAAAAAP3///+lkTtN5yuncT07kkZIuZrgPlMIbk3e4Ph14s4MG+S3gQAAAAAA/f///6WRO03nK6dxPTuSRki5muA+UwhuTd7g+HXizgwb5LeBAQAAAAD9////CCwBAAAAAAAAFgAUBFtVYlpUm5iHZvf8cW1Te1D16gIsAQAAAAAAABYAFPiBJvmTv+DdmsRcvIcWU/8LXU0ULAEAAAAAAAAWABTTg2VJqeeWiJbBke8bW5/1ovQ0+iwBAAAAAAAAFgAU0MnlyP/ofvZQ1P3mcA4vKVen9LksAQAAAAAAABYAFOPwOp2QPepm6NFFGXgeWlZoANQHLAEAAAAAAAAWABSY8opy2FeyAGUjkBlsm10RSsV7qCwBAAAAAAAAFgAUXWUVxmbYT+CMAs0oR8G3MYyyuyqZGAAAAAAAABYAFGT8/EuuiDNH8x7K3O7S/vZEyAaHzvwkAAEBH5kYAAAAAAAAFgAUZPz8S66IM0fzHsrc7tL+9kTIBocBAwQBAAAAIgYCWhAfa2NubZrJm0lvYZvSO5I0gf0wigR9fZRbTMTeX9IY4MWVxVQAAIABAACAAAAAgAAAAABjAAAAAAAAAAAAAA=="
    signer = PSBTSigner(wallet, PSBT_satvB_2_2, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (1): ₿ 0.00 006 297\n\nSpend (6): ₿ 0.00 005 625\n\nFee: ₿ 0.00 000 672 (12.0%) ~2.2 sat/vB"
    )

    PSBT_satvB_1_8 = "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"
    signer = PSBTSigner(wallet, PSBT_satvB_1_8, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (7): ₿ 0.00 002 100\n\nSpend (3): ₿ 0.00 000 997\n\nFee: ₿ 0.00 001 103 (110.7%) ~1.8 sat/vB"
    )

    wallet = Wallet(Key(MNEMONIC, TYPE_MULTISIG, NETWORKS["test"]))
    PSBT_satvB_164_83 = "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"
    signer = PSBTSigner(wallet, PSBT_satvB_164_83, FORMAT_PMOFN)
    outputs, _ = signer.outputs()
    assert (
        outputs[0]
        == "Inputs (2): ₿\u20090.00 130 622\n\nSpend (9): ₿\u20090.00 028 343\n\nFee: ₿\u20090.00 102 279 (360.9%) ~165.2 sat/vB"
    )

    # TODO: Add a multisig with descriptor so change can be deteted
