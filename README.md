# 🚗 Showroom Mobil - Django App

A web application to manage car showroom data built with Python Django. This app supports adding, viewing, servicing, and calculating financing details for cars in the showroom.

---

## 📦 Features

- Add new cars with optional bank loan info
- List and detail view for cars
- Add service records for cars
- Automatic HPP (Harga Pokok Produksi) and monthly installment calculation
- Delete cars
- Tailwind CSS for styling (via CDN)

---

## ⚙️ Requirements

- Python 3.8+
- pip
- Virtualenv (optional but recommended)

---

## 🚀 Getting Started

Follow these steps to run the app locally:

### 1. Clone the Repository

```bash
git clone git@github.com:Fadhyoung/showroom_kreasiAi.git
cd showroom
```

### 2. Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

```

### 2. Install Dependencies
```
pip install django
```

### 3. Run Migrations
```
python manage.py migrate
```

### 4. Start the Server
```
python manage.py runserver
```

## Styling

Tailwind CSS is included via CDN. You can customize styles inside templates.

## Project Structure

```
cars
├── admin.py
├── apps.py
├── forms.py
├── __init__.py
├── migrations
│   ├── 0001_initial.py
│   ├── __init__.py
│   └── __pycache__
│       ├── 0001_initial.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── models.py
├── __pycache__
│   ├── admin.cpython-312.pyc
│   ├── apps.cpython-312.pyc
│   ├── forms.cpython-312.pyc
│   ├── __init__.cpython-312.pyc
│   ├── models.cpython-312.pyc
│   ├── urls.cpython-312.pyc
│   └── views.cpython-312.pyc
├── templates
│   └── cars
│       ├── _action_button.html
│       ├── base.html
│       ├── car_detail.html
│       ├── car_form.html
│       ├── car_list.html
│       ├── _form.html
│       ├── _jumbotron.html
│       ├── _navbar.html
│       └── service_form.html
├── templatetags
│   ├── action_buttons.py
│   ├── __init__.py
│   └── __pycache__
│       ├── action_buttons.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── tests.py
├── urls.py
└── views.py
```
