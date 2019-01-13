from StratMap.app_data.database import DataBase




def create_hosp_codes():
    c = DataBase()
    c.connect()
    values_list = [{'hosp_code': '01103', 'name': 'ביה"ח אסף הרופה', 'type': '1'},
                   {'hosp_code': '01108', 'name': 'ביה"ח ברזילי', 'type': '1'},
                   {'hosp_code': '01204', 'name': 'ביה"ח בני ציון', 'type': '1'},
                   {'hosp_code': '01107', 'name': 'ביה"ח נהריה', 'type': '1'},
                   {'hosp_code': '01106', 'name': 'ביה"ח הלל יפה', 'type': '1'},
                   {'hosp_code': '01109', 'name': 'ביה"ח פוריה', 'type': '1'},
                   {'hosp_code': '01102', 'name': 'ביה"ח רמבם', 'type': '1'},
                   {'hosp_code': '01201', 'name': 'ביה"ח איכילוב', 'type': '1'},
                   {'hosp_code': '01104', 'name': 'ביה"ח וולפסון', 'type': '1'},
                   {'hosp_code': '01105', 'name': 'ביה"ח זיו', 'type': '1'},
                   {'hosp_code': '01101', 'name': 'ביה"ח שיבה', 'type': '1'},
                   {'hosp_code': '11101', 'name': 'ביה"ח שער המנשה', 'type': '3'},
                   {'hosp_code': '11102', 'name': 'ביה"ח יהודה אברבנאל', 'type': '3'},
                   {'hosp_code': '11103', 'name': 'ביה"ח ע"ש פליגלמן מזור', 'type': '3'},
                   {'hosp_code': '11104', 'name': 'המרכז לבריאות הנפש בער יעקב', 'type': '3'},
                   {'hosp_code': '11105', 'name': 'המרכז הרפואי לברה''נ לב השרון', 'type': '3'},
                   {'hosp_code': '11106', 'name': 'ביה"ח מעלה הכרמל', 'type': '3'},
                   {'hosp_code': '11107', 'name': 'המרכז לבריאות הנפש בער שבה', 'type': '3'},
                   {'hosp_code': '11109', 'name': 'מרכז רפואי לבריאות הנפש ירושלים', 'type': '3'},
                   {'hosp_code': '21101', 'name': 'מרכז רפואי גריאטרי שמואל הרופא', 'type': '2'},
                   {'hosp_code': '21102', 'name': 'מרכז גריאטרי שיקומי ע''ש פלימן', 'type': '2'},
                   {'hosp_code': '22101', 'name': 'מרכז הגריאטרי המשולב ע"ש שוהם', 'type': '2'},
                   {'hosp_code': '22102', 'name': 'מרכז גריאטרי דורות נתניה', 'type': '2'},
                   {'hosp_code': '22103', 'name': 'מרכז גריאטרי ראשל"צ', 'type': '2'},
                   {'hosp_code': '31101', 'name': 'מרכז קהילתי לבריאות הנפש', 'type': '2'},
                   {'hosp_code': '1', 'name': 'חטיבה', 'type': '0'}]
    data = {'name': 'hospital_codes', 'values_list': values_list}
    c.post('app_data_decryptiontables', data)


def create_business_topic():
    d = DataBase()
    d.connect()
    values_list = [
            {'code': '1', 'name': 'תקן איוש ונלוות', 'sub_topic': [
                {'code': '11','name': 'תקן מוך איוש'},
                {'code': '12','name': 'כמויות נלוות'},
                {'code': '13','name': 'כמויות נלוות - מתוקן לאיוש'}
                ]
             },
            {'code': '2', 'name': 'פעילות', 'sub_topic': [
                {'code': '21','name': 'כלל מחלקות האשפוז'},
                {'code': '22','name': 'אגף פנימי'},
                {'code': '23','name': 'מלר''ד'},
                {'code': '24', 'name': 'טיפול נמרץ בילוד, טיפול מיוחד בילוד'},
                {'code': '25', 'name': 'יולדות'},
                {'code': '26', 'name': 'ניתוחים'},
                {'code': '27', 'name': 'ניתוחים לפי קוד שירות'},
                {'code': '28', 'name': 'מכונים ומרפאות'}
                ]
             },
            {'code': '3', 'name': 'חווית המטופל', 'sub_topic': [
                {'code': '31','name': 'מלר''ד'},
                {'code': '32','name': 'זימון וניהול תור'},
                {'code': '33','name': 'ביצוע סקרי שביעות רצון'},
                {'code': '34', 'name': 'אשפוז באגף הפנימי'}
                ]
             },
            {'code': '4', 'name': 'הון אנושי', 'sub_topic': [
                {'code': '41','name': 'אקרדיטציה'},
                {'code': '42','name': 'הכשרות צוותים'},
                {'code': '43','name': 'הערכות עובדים'},
                {'code': '44', 'name': 'שוויון מגדרי'},
                {'code': '45', 'name': 'מתמחים ותורנים'},
                {'code': '46', 'name': 'אלימות נגד צוותים'},
                {'code': '47', 'name': 'חיסוני צוותים'}
                ]
             },
            {'code': '5', 'name': 'איכות ובטיחות', 'sub_topic': [
                {'code': '51','name': 'מניעת זיהומים'},
                {'code': '52','name': 'אומדן כאב'},
                {'code': '53','name': 'בטיחות הטיפול'}
                ]
             },
            {'code': '6', 'name': 'תשתית כלכלית ופזית', 'sub_topic': [
                {'code': '61','name': 'ניצולת חדרי ניתוח'},
                {'code': '62','name': 'ניהול היבטי שכר'},
                {'code': '63','name': 'צריכת חשמל ומים'},
                {'code': '64', 'name': 'תחזוקת שבר מול מונעת'},
                {'code': '65', 'name': 'היבטים תקציביים ופיננסיים'}
                 ]
             },
            {'code': '7', 'name': 'ניצולת חדרי ניתוח', 'sub_topic': [
                {'code': '71','name': 'ניצולת חדרי ניתוח ( בוקר )'},
                {'code': '72','name': 'פעילות חדרי ניתוח ( דחוף ותאגיד)'}
                ]
             },
            {'code': '8', 'name': 'תשתית טכנולוגית', 'sub_topic': [
                {'code': '81','name': 'איכות הקידוד הרפואי'},
                {'code': '82','name': 'שדרוג תשתית טכנולוגית'},
                {'code': '83','name': 'היקף ההשקעה במחשוב'}
                ]
            }
        ]
    data = {'name': 'business_topic', 'values_list': values_list}
    d.post('app_data_decryptiontables', data)


def create_frequency():
    b = DataBase()
    b.connect()
    values_list = [
            {'code': '1', 'type': 'יומי'},
            {'code': '2', 'type': 'חודשי'},
            {'code': '3', 'type': 'רבעוני'},
            {'code': '4', 'type': 'חציוני'},
            {'code': '5', 'type': 'שנתי'}
        ]
    data = {'name': 'frequency', 'values_list': values_list}
    b.post('app_data_decryptiontables', data)


def create_hosp_types():
    a = DataBase()
    a.connect()
    values_list = [
        {'code': '1', 'type': 'כללים'},
        {'code': '2', 'type': 'גריאטריים'},
        {'code': '3', 'type': 'פסיכיאטריים'}
    ]
    data = {'name': 'hospital_types', 'values_list': values_list}
    a.post('app_data_decryptiontables', data)


def create_version_types():
    a = DataBase()
    a.connect()
    values_list = [
        {'code': '1', 'type': 'חצי שנתי'},
        {'code': '2', 'type': 'שנתי'}
    ]
    data = {'name': 'version_types', 'values_list': values_list}
    a.post('app_data_decryptiontables', data)


def create_measure_types():
    a = DataBase()
    a.connect()
    values_list = [
        {'code': '1', 'type': 'ON TARGET'},
        {'code': '2', 'type': 'LOW IS BETTER'},
        {'code': '3', 'type': 'HIGH IS BETTER'}
    ]
    data = {'name': 'measure_types', 'values_list': values_list}
    a.post('app_data_decryptiontables', data)
