from datetime import datetime
import sqlite3 as sq


class Trip:

    data_actual = False

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
                cur.execute(f"INSERT INTO trips  (tr_date, km, liters, money) "
                            f"VALUES ('{self.date}', '{self.km}', '{self.liters}', '{self.money}')")
                db.commit()
            self.data_not_actual()
            return True
        except sq.IntegrityError:
            return False

    @classmethod
    def clear_data(cls, dialog):
        with sq.connect('data.db') as db:
            cur = db.cursor()
            cur.execute(f"DELETE FROM trips")
            db.commit()
        dialog.dismiss()
        cls.data_not_actual()

    @classmethod
    def __get_trips(cls):
        with sq.connect('data.db') as db:
            cur = db.cursor()
            cur.execute(f"SELECT * FROM trips")
            raw_trips = cur.fetchall()
            result_trips = []
            for trip in raw_trips:
                result_trips.append(cls(trip[1], trip[3], trip[2], message=None, date=trip[0]))
            return result_trips

    @classmethod
    def data_rows(cls):
        cls.data_is_actual()
        obj = Trip.__get_trips()
        return [(o.date, o.km, o.liters, o.money) for o in obj]

    @classmethod
    def data_is_actual(cls):
        cls.data_actual = True

    @classmethod
    def data_not_actual(cls):
        cls.data_actual = False
