from flask import render_template,request, redirect,url_for
from model import OnlineOrder,OfflineOrder,TableReservation
import json
import datetime

def register_routes(app,db):

    """@app.route('/',methods = ['GET','POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            # return str(people)
            return render_template('index.html',people = people)

        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')  

            #creating the new object
            person = Person(name = name, age=age, job=job)
            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            # return str(people)
            return render_template('index.html',people = people)
        """
    @app.route('/')
    def home_page():
        return render_template('home_page.html')
    
    @app.route('/food_orderOF')
    def food_orderOF():
        return render_template('food_orderOF.html')
    
    @app.route('/food_order_online_form')
    def food_order_online_form():
        return render_template('food_order_online_form.html')
    

    
    @app.route('/submit_online_order', methods=['POST'])
    def submit_online_order():
        # fetch simple fields
        customer_name = request.form.get('customer_name')
        address = request.form.get('address')
        phone_no = request.form.get('phone')
        email = request.form.get('email')
        
        # fetch order data and convert JSON string to Python dict
        food_items_json = request.form.get('food_order_data')
        food_items = json.loads(food_items_json) if food_items_json else {}
        
        total_cost = request.form.get('total_cost')

        # create new order record
        new_order = OnlineOrder(
            customer_name=customer_name,
            address=address,
            phone_no=phone_no,
            email=email,
            order_time=datetime.datetime.now().time(),
            order_date=datetime.date.today(),
            food_items=food_items,
            total_cost=total_cost
        )

        db.session.add(new_order)
        db.session.commit()
        
        return redirect(url_for('success_page'))
 
   
           
    @app.route('/success_page')
    def success_page():
        return render_template("success_page.html")
    
    @app.route('/food_order_offline_form')
    def food_order_offline_form():
        return render_template('food_order_offline_form.html')
    
    @app.route('/submit_offline_order', methods=['POST'])
    def submit_offline_order():
        # fetch simple fields
        table_no = request.form.get('table_no')
        
        # fetch order data and convert JSON string to Python dict
        food_items_json = request.form.get('food_order_data')
        food_items = json.loads(food_items_json) if food_items_json else {}
        
        total_cost = request.form.get('total_cost')
        
        # create new onsite order record
        new_order = OfflineOrder(
            table_no=table_no,
            order_time=datetime.datetime.now().time(),
            order_date=datetime.date.today(),
            food_items=food_items,
            total_cost=total_cost
        )

        db.session.add(new_order)
        db.session.commit()
        
        return redirect(url_for('success_page'))

    
    @app.route('/view_order')
    def view_order():
        return render_template('view_order.html')
    
    @app.route('/table_reservation_form')
    def table_reservation_form():
        return render_template('table_reservation_form.html')
    
    @app.route('/submit_reservation', methods=['POST'])
    def submit_reservation():
        name = request.form.get('name')
        email = request.form.get('email')
        phone_no = request.form.get('phone_no')
        tables_booked = request.form.get('tables_booked')
        reservation_date = request.form.get('reservation_date')
        reservation_time = request.form.get('reservation_time')
        
        # create new reservation record
        new_reservation = TableReservation(
            name=name,
            email=email,
            phone_no=phone_no,
            tables_booked=tables_booked,
            reservation_date=reservation_date,
            reservation_time=reservation_time
        )

        db.session.add(new_reservation)
        db.session.commit()
        
        return redirect(url_for('success_page'))

    
    @app.route('/view_reservation')
    def view_reservation():
        return render_template('view_reservation.html')
    
    @app.route('/cooking')
    def cooking():
        return render_template('cooking.html')