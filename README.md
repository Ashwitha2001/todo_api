# **To-Do List API**  

This is a **Django REST API** for managing a to-do list. It allows users to register, log in, and perform **CRUD** (Create, Read, Update, Delete) operations on their to-do items.  

## **Features**  
   User Registration & Login  
   Create, Read, Update, and Delete (CRUD) To-Do items  
   User authentication  
   Secure API endpoints  

## **Installation & Setup**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Ashwitha2001/todo_api
cd todo_api
```

### **2. Set Up Virtual Environment**  
```bash
python -m venv venv
venv\Scripts\activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser**  
```bash
python manage.py createsuperuser
```

### **6. Run the Server**  
```bash
python manage.py runserver
```
The API will be available at: **http://127.0.0.1:8000/**  

---

## **API Endpoints**  

### **User Authentication**  
- **Register** → `POST /register/`  
- **Login** → `POST /login/`  

### **To-Do Operations**  
- **Get All To-Dos** → `GET /todos/`  
- **Create To-Do** → `POST /todos/create/`  
- **Update To-Do** → `PUT /todos/<todo_id>/update/`  
- **Delete To-Do** → `DELETE /todos/<todo_id>/delete/`  

---

## **Database**  
- Default: **SQLite** 
- The `Todo` model stores tasks with a relationship to users.  

---

## **Testing the API**  
Use **Postman** or Django's browsable API to test the endpoints.  

---

## **Tech Stack**  
 **Django** – Backend Framework  
 **Django REST Framework** – API Development  
 **SQLite** – Default Database  
 **Postman** – API Testing  

