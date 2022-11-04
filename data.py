from datetime import datetime
import sqlite3 as sq


class Trip:
    def __init__(self, km, money, liters, message, date=None):
        self.km = km
        self.money = money
        self.liters = liters
        self.message = message
        if not date:
            date = datetime.now()
            self.date = f"{date.year}-{date.month}-{date.day} {date.hour}:" \
                        f"{'0' + str(date.minute) if date.minute < 10 else date.minute }"
        else:
            self.date = date

    def save(self):
        try:
            with sq.connect('data.db') as db:
                cur = db.cursor()
                cur.execute(f"INSERT INTO trips  (tr_date, km, liters) "
                            f"VALUES ('{self.date}', '{self.km}', '{self.liters}')")
                db.commit()
            return True
        except sq.IntegrityError:
            return False


