# Django Healthcare Backend

A backend system for a healthcare application using Django, Django REST Framework (DRF), JWT authentication, and PostgreSQL (Supabase).

## Features
- User registration and JWT login
- Patient and doctor management (CRUD)
- Patient-doctor mapping (assign, list, remove)
- Secure endpoints (JWT authentication)
- PostgreSQL via Supabase

## Setup Instructions

1. **Clone the repository and navigate to the project directory.**
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create a `.env` file** in the project root with your DB and secret settings:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=5432
   ```
5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Start the server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Register:** `POST /api/auth/register/`
- **Login:** `POST /api/token/`
- **Patients:** `/api/patients/`
- **Doctors:** `/api/doctors/`
- **Mappings:** `/api/mappings/`

> All endpoints (except registration and login) require JWT authentication. Use the `Authorization: Bearer <access_token>` header.

## Testing

- Use Postman or any API client to test endpoints.
- See assignment instructions for sample requests.

## Notes
- Do **not** commit your `.env` file.
- All sensitive settings are managed via environment variables. 