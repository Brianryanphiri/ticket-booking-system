# 🎟️ Ticket Booking System

A **Django-based Event Ticket Booking System** where users can browse events, book tickets, make payments, and manage their accounts.  
The project is structured into modular apps for **events, tickets, users, and payments**, making it easy to scale and maintain.

---

## ✨ Features

### 🗓️ Events Management
- Browse upcoming events  
- View event details (title, description, date, location)  
- Admins can create, edit, or delete events  

### 🎫 Ticket Management
- Multiple ticket types (Regular, VIP, Student, etc.)  
- Check availability before booking  
- Secure booking process  

### 👤 User Management
- Custom user model (`users_app.User`)  
- User registration and login/logout  
- Profile page with user details  
- Password validation and error handling  

### 💳 Payments
- Payment model includes:
  - `user`, `ticket`, `amount`, `status`, `payment_date`
- Supports integration with:
  - Stripe  
  - PayPal  
  - Razorpay  
- Includes initiation, confirmation, and success/failure pages  

### 🔑 Admin Dashboard
- Manage users, events, tickets, and payments  
- View all bookings and transactions  

---

## 🛠️ Tech Stack

- **Backend:** Django 5  
- **Database:** SQLite (default, can be upgraded to PostgreSQL/MySQL)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Payments:** Stripe/PayPal/Razorpay ready  
- **Deployment:** Compatible with Gunicorn, Nginx, Docker  

---

## 📂 Project Structure

ticket-booking-system/
├── config/ # Project configuration
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── events_app/ # Events management
├── tickets_app/ # Ticket booking and availability
├── users_app/ # Custom user model, auth, profiles
├── payments_app/ # Payment processing
│
├── templates/ # Global templates (base.html, etc.)
│ └── registration/ # Auth templates (login.html, register.html)
│
├── static/ # Static files (CSS, JS, images)
├── db.sqlite3 # Local database (development)
├── manage.py
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ticket-booking-system.git
cd ticket-booking-system
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
bash
Copy code
python manage.py createsuperuser
6️⃣ Run Development Server
bash
Copy code
python manage.py runserver
Visit 👉 http://127.0.0.1:8000/

💳 Payments Setup (Optional)
By default, payments are mock/test only.
To integrate with real payment gateways:

Create a developer account on Stripe, PayPal, or Razorpay.

Get your API keys.

Add them in config/settings.py. Example:

python
Copy code
STRIPE_SECRET_KEY = "your-secret-key"
STRIPE_PUBLISHABLE_KEY = "your-publishable-key"
Update payments_app/views.py to handle live transactions.

🔐 Authentication Routes
/users/register/ → User Registration

/users/login/ → User Login

/users/logout/ → User Logout

/users/profile/ → Profile Page

👨‍💻 Contributing
Want to improve this project? Here’s how:

Fork the repo

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m "Add amazing feature")

Push to your branch (git push origin feature/amazing-feature)

Open a Pull Request 🎉

📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this project.

🚀 Roadmap / Future Improvements
✅ Email notifications after booking

✅ QR code for tickets

✅ Multi-currency payment support

✅ Event categories & filtering

✅ API support (REST framework integration)

🏗️ Project Status
📌 Currently under active development.
Core apps (users, events, tickets, payments) are in place.
Next phase → Payment gateway integration & UI improvements.








Ask ChatGPT
