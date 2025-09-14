
# 🍽️ Restaurant Management System — Full-Stack on AWS 🚀

<img width="1869" height="980" alt="Screenshot 2025-07-03 223041" src="https://github.com/user-attachments/assets/10909021-7940-45e4-b5ce-12801982f6e9" />


![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20RDS-orange)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

> ⚡ **A full-stack restaurant management system built with Flask & SQL, containerized using Docker, and deployed on AWS EC2 with RDS/Aurora.**  
> Enables customers to reserve tables or place online orders, and helps restaurant staff manage operations seamlessly.

---

## 📝 Project Demonstration Link
Project Video Link:  https://youtu.be/hZUwXvWPXJw?si=51mqBC26Iaj-LDPV

---

## ✨ Features
✅ Customers can:
- Reserve tables online for in-house dining 🍽️
- Place food orders to dine on-site 🪑
- Place food orders for home delivery 🏠

✅ Staff can:
- View all reservations 📝
- Manage both offline & online orders 🍔

✅ Secure database operations via AWS RDS/Aurora 🔒

---

## 🖼️ Screenshots

- 🖥️ Homepage
  <img width="1869" height="980" alt="Screenshot 2025-07-03 223041" src="https://github.com/user-attachments/assets/33e2b81f-7285-4a16-a131-7e3067d450c7" />

- 📅 Reservation Page
  <img width="1912" height="966" alt="Screenshot 2025-07-03 162849" src="https://github.com/user-attachments/assets/d94ce8dc-0243-4c44-9706-b4c94db96b71" />

  
- 🥗 Order Management
  <img width="1879" height="962" alt="Screenshot 2025-07-03 161748" src="https://github.com/user-attachments/assets/a16b65f7-07df-436c-95e6-de0ecdf0cf94" />


---

## 🚀 Tech Stack
| Layer               | Tech Used                          |
|----------------------|----------------------------------|
| **Frontend**         | HTML, CSS, JavaScript (vanilla)  |
| **Backend**          | Python Flask                     |
| **Database**         | AWS RDS / Aurora (MySQL)         |
| **Containerization** | Docker                           |
| **Hosting**          | AWS EC2                          |

---

## 🧩 System Design

### ⚙️ Architecture Overview
```
[ Client Browser ]
⬇
[ Flask App on EC2 ]
⬇
[ Docker Container running Flask ]
⬇
[ AWS RDS / Aurora (Database) ]
```

- The Flask application is packaged as a Docker image and deployed on an EC2 instance.
- The EC2 instance securely connects to an RDS/Aurora database to handle all data operations.
- The application exposes the service on EC2’s public IP, making it accessible over the internet.

---

## 🔧 Steps to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/priyamjain1105/restaurant-management-system.git
cd restaurant-management-system
```

### 2️⃣ Create a virtual environment & install dependencies
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3️⃣ Run the app
```
python dbapplication/run.py
```

## ☁️ Deployment on AWS
### 🚀 Dockerize the App
```
docker build -t restaurant-app .
docker run -d -p 5000:5000 restaurant-app

```

### 🚀 On EC2
- Launch an EC2 instance with Docker installed.
- Copy your Docker image or pull from Docker Hub.
- Run the container and expose the port.
- Access via http://<EC2 Public IP>:5000


