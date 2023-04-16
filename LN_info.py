from datetime import *

shelf_life = [{"Italian Basil":6, "Flat Coriander":6, "Thyme":10, "Green Mint":6, "Rosemary":10, "Chervil":6, "Tarragon":6, "Watercress":6, "Melissa":6, "Oregano":6, "Flat Parsley":6, "Pea Shoots":6},{"Italian Basil":6, "Flat Coriander":10, "Thyme":10, "Green Mint":9, "Rosemary":10, "Dill":10, "Tarragon":6, "Sage":8, "Curly Parsley":10, "Flat Parsley":10},{"Italian Basil":6, "Flat Coriander":10, "Thyme":10, "Green Mint":9, "Rosemary":10, "Curly Parsley":10, "Tarragon":6, "Flat Parsley":10, "Sage":8, "Dill":10}]#[pots,ts,fp]

ln_letters = {"1":"A","2":"B","3":"C","4":"D","5":"E","6":"F","7":"G"}

def info(dd,mm,yyyy,ref_number,process,variety):

    processes = {"pots":0,"ts":1,"fp":2}

    today = date(yyyy, mm, dd)
    PCK_day = today.weekday() + 1

    if PCK_day < 6:
        shipment_date = today + timedelta(days=1)
    else:
        shipment_date = today + timedelta(days=2)

    DC_day = shipment_date.weekday() + 1

    if DC_day < 6:
        factor = 0
    else:
        factor = 1

    delta = factor + shelf_life[processes[process]][variety]

    best_before = shipment_date + timedelta(days=delta)

    week_number = best_before.isocalendar().week

    if len(str(week_number))<2:
        week_n = "0"+str(week_number)
    else:
        week_n = str(week_number)

    sd_day = best_before.weekday() + 1

    lot_number = "L" + week_n + ln_letters[str(sd_day)]

    day = str(best_before)[8:10]
    month = str(best_before)[5:7]
    year = str(best_before)[0:4]

    return day, month, year, lot_number