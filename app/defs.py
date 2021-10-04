#文字列から数値に変換
def time (x):
    if x ==x:
        if x == '30分?60分':
            x = 45
        elif x == '1H?1H30':
            x = 75
        elif x == '2H?':
            x = 120
        elif x == '1H30?2H':
            x = 105
        else:
            x = int(x)
    return x

def area (x):
    if x ==x:
        if x == '2000㎡以上':
            x = 2000
        else:
            x = int(x)
    return x

def years(wareki):
    if wareki == wareki:
        if wareki == '戦前':
            wareki = '昭和20年'
        value = wareki[2:-1]
        if value == '元':
            value = 1
        else:
            value = int(value)
        if '昭和' in wareki:
            seireki = 1925+value
        elif '平成' in wareki:
            seireki = 1988+value
        elif '令和' in wareki:
            seireki = 2018+value
    else:
        seireki = wareki
    return seireki

def trade_year(shihanki):
        year = int(shihanki[:4])
        if '第4四半期' in shihanki:
            year += 1
        else:
            year = year            
        return year
    
def trade_month(shihanki):
    if '第１四半期' in shihanki:
        shihanki = 4
    elif '第２四半期' in shihanki:
        shihanki = 7
    elif '第３四半期' in shihanki:
        shihanki = 10
    elif '第４四半期' in shihanki:
        shihanki = 1

    return shihanki

#都道府県名を緯度経度に返還する

def angle (name):
    if name == name :
        if name == '北海道':
            ido = 43.06171            
            keido = 141.35062
            
        elif name == '青森県':
            ido = 40.82175            
            keido = 140.74353
            
        elif name == '岩手県':
            ido = 39.70079            
            keido=141.15601
            
        elif name == '宮城県':
            ido=38.26592            
            keido=140.87536
            
        elif name == '秋田県':
            ido=39.71581            
            keido=140.10592
            
        elif name == '山形県':
            ido=38.2376            
            keido=140.36671
            
        elif name == '福島県':
            ido=37.74698            
            keido=140.47114
            
        elif name == '茨城県':
            ido=36.33822            
            keido=140.44997
            
        elif name == '栃木県':
            ido=36.5627            
            keido=139.88687
            
        elif name == '群馬県':
            ido=36.38797            
            keido=139.06401
            
        elif name == '埼玉県':
            ido=35.85373            
            keido=139.6521
            
        elif name == '千葉県':
            ido=35.60148            
            keido=140.12657
            
        elif name == '東京都':
            ido=35.68622            
            keido=139.69487 
            
        elif name == '神奈川県':
            ido=35.44453            
            keido=139.64569
            
        elif name == '新潟県':
            ido=37.89924            
            keido=139.02686
            
        elif name == '富山県':
            ido=36.69221           
            keido=137.21443
            
        elif name == '石川県':
            ido=36.59137            
            keido=136.62855
            
        elif name == '福井県':
            ido=36.06216            
            keido=136.22487
            
        elif name == '山梨県':
            ido=35.66068            
            keido=138.57144
            
        elif name == '長野県':
            ido=36.64829            
            keido=138.18423
            
        elif name == '岐阜県':
            ido=35.38791            
            keido=136.72516
            
        elif name == '静岡県':
            ido=34.97366            
            keido=138.38612
            
        elif name == '愛知県':
            ido=34.97038            
            keido=138.38918
            
        elif name == '三重県':
            ido=34.72701            
            keido=136.51151
            
        elif name == '滋賀県':
            ido=35.00121            
            keido=135.87118
            
        elif name == '京都府':
            ido=35.01816            
            keido=135.75841
            
        elif name == '大阪府':
            ido=34.68313            
            keido=135.52281
            
        elif name == '兵庫県':
            ido=34.68814            
            keido=135.18584  
            
        elif name == '奈良県':
            ido=34.68202            
            keido=135.83562
            
        elif name == '和歌山県':
            ido=34.22281            
            keido=135.17026
            
        elif name == '鳥取県':
            ido=35.50046            
            keido=134.24107
            
        elif name == '島根県':
            ido=35.46909            
            keido=133.0532
            
        elif name == '岡山県':
            ido=34.65844            
            keido=133.93768
            
        elif name == '広島県':
            ido=34.39315           
            keido=132.46198
            
        elif name == '山口県':
            ido=34.18259            
            keido=131.47384
            
        elif name == '徳島県':
            ido=34.06252            
            keido=134.56214
            
        elif name == '香川県':
            ido=34.33701            
            keido=134.046
            
        elif name == '愛媛県':
            ido=33.83837            
            keido=132.76865
            
        elif name == '高知県':
            ido=33.55638            
            keido=133.5337
            
        elif name == '福岡県':
            ido = 33.55303            
            keido = 133.53629
            
        elif name == '佐賀県':
            ido=33.24612            
            keido=130.3012
            
        elif name == '長崎県':
            ido=32.74135            
            keido=129.87586
            
        elif name == '熊本県':
            ido=32.78634           
            keido=130.744 
            
        elif name == '大分県':
            ido=33.23471            
            keido=131.61492
            
        elif name == '宮崎県':
            ido=31.90763           
            keido=131.42623
            
        elif name == '鹿児島県':
            ido=31.55677            
            keido=130.56031
            
        elif name == '沖縄県':
            ido=26.20847            
            keido=127.68288
            
        return (ido,keido)