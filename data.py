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
                cur.execute(f"INSERT INTO trips  (tr_date, km, liters, money) "
                            f"VALUES ('{self.date}', '{self.km}', '{self.liters}', '{self.money}')")
                db.commit()
            return True
        except sq.IntegrityError:
            return False

    @staticmethod
    def clear_data(dialog):
        with sq.connect('data.db') as db:
            cur = db.cursor()
            cur.execute(f"DELETE FROM trips")
            db.commit()
        dialog.dismiss()

    @staticmethod
    def __get_trips():
        with sq.connect('data.db') as db:
            cur = db.cursor()
            cur.execute(f"SELECT * FROM trips")
            raw_trips = cur.fetchall()
            result_trips = []
            for trip in raw_trips:
                result_trips.append(Trip(trip[1], trip[3], trip[2], message=None, date=trip[0]))
            return result_trips

    @staticmethod
    def data_rows():
        data_in_row = []
        data_from_base = Trip.__get_trips()
        for index in range(len(data_from_base)):
            data_in_row.append((data_from_base[index].date,
                                data_from_base[index].km,
                                data_from_base[index].liters,
                                data_from_base[index].money))
        return data_in_row
