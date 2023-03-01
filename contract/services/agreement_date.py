import datetime

MONTHS = {
    1: "січня",
    2: "лютого",
    3: "березня",
    4: "квітня",
    5: "травня",
    6: "червня",
    7: "липня",
    8: "серпня",
    9: "вересня",
    10: "жовтня",
    11: "листопада",
    12: "грудня",
}


def get_agreement_date():
    current_datetime = datetime.datetime.now()
    year = current_datetime.year
    month = current_datetime.month
    day = current_datetime.day
    return f"«{day}» {MONTHS[month]} {year} року"
