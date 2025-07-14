from app import db

"""class Person(db.Model):
    __tablename__ = 'person'
    pid = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    age =  db.Column(db.Integer)
    job =  db.Column(db.String(255))

    def __repr__(self):
        return f'Person with name {self.name} and age {self.age}'"""

class TableReservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    tables_booked = db.Column(db.Integer)  # each table seats 4
    phone_no = db.Column(db.String(20))
    email = db.Column(db.String(100))
    reservation_date = db.Column(db.Date)
    reservation_time = db.Column(db.Time)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tables_booked": self.tables_booked,
            "phone_no": self.phone_no,
            "email": self.email,
            "reservation_date": self.reservation_date.isoformat(),
            "reservation_time": self.reservation_time.isoformat()
        }
    
class OnlineOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    address = db.Column(db.Text)
    phone_no = db.Column(db.String(20))
    email = db.Column(db.String(100))
    order_time = db.Column(db.Time)
    order_date = db.Column(db.Date)
    food_items = db.Column(db.JSON)  # stores dict of items with cost
    total_cost = db.Column(db.Numeric(10, 2))

    def to_dict(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "address": self.address,
            "phone_no": self.phone_no,
            "email": self.email,
            "order_time": self.order_time.isoformat(),
            "order_date": self.order_date.isoformat(),
            "food_items": self.food_items,
            "total_cost": float(self.total_cost)
        }

class OfflineOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_no = db.Column(db.Integer)
    order_time = db.Column(db.Time)
    order_date = db.Column(db.Date)
    food_items = db.Column(db.JSON)  # stores dict of items with cost
    total_cost = db.Column(db.Numeric(10, 2))

    def to_dict(self):
        return {
            "id": self.id,
            "table_no": self.table_no,
            "order_time": self.order_time.isoformat(),
            "order_date": self.order_date.isoformat(),
            "food_items": self.food_items,
            "total_cost": float(self.total_cost)
        }
