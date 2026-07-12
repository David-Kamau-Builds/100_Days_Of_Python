# Day 66: Cafe & Wifi RESTful API with Flask

## Project Overview
A RESTful API built with Flask for managing a database of cafes, including information about wifi availability, power sockets, toilet access, and coffee prices. The API supports full CRUD operations with password-protected write endpoints and flexible search functionality.

## Key Concepts Learned
- **RESTful API Design**: Building a complete REST API with proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- **SQLAlchemy ORM**: Defining models with typed Mapped columns and DeclarativeBase
- **Serialization**: Converting SQLAlchemy model instances to dictionaries for JSON responses
- **Route Parameters**: Using URL path parameters for resource identification and authentication
- **Query Parameters**: Flexible search filtering with optional query string parameters
- **Environment Variables**: Securing API passwords using python-dotenv and .env files
- **Error Handling**: Returning appropriate HTTP status codes (400, 403, 404) with descriptive error messages

## Technical Skills
- SQLAlchemy DeclarativeBase with typed Mapped columns (Integer, String, Boolean)
- Flask route handling for CRUD operations with GET, POST, PUT, PATCH, DELETE methods
- Database session management with add, commit, delete, and query operations
- Dynamic query building with SQLAlchemy's `where()` clause chaining
- JSON serialization using `jsonify()` and custom `to_dict()` model method
- Column introspection with `__table__.columns` for automatic serialization
- Password-based route protection via URL parameters
- Random record selection using `db.func.random()`
- Form data parsing with `request.form.get()`
- Query string parsing with `request.args.get()`

## Features
- **Random Cafe**: Get a random cafe from the database
- **Get One Cafe**: Retrieve a specific cafe by its ID
- **Get All Cafes**: List all cafes in the database
- **Search Cafes**: Filter cafes by location, name, or both with personalized error messages
- **Add Cafe**: Create a new cafe entry (password-protected)
- **Update Price**: Modify a cafe's coffee price (password-protected)
- **Close Cafe**: Delete a cafe from the database (password-protected)

## Project Structure
- `main.py` - Main Flask application with routes, models, and API logic
- `requirements_3.13.txt` - Project dependencies (tested on Python 3.13.1)
- `.env` - Environment variables (MY_SECURE_PASSWORD) — not tracked in git
- `instance/cafes.db` - SQLite database file
- `templates/index.html` - API documentation home page
- `Cafe_API.postman_collection.json` - Postman collection for testing all endpoints

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/random` | Get a random cafe |
| GET | `/one/<cafe_id>` | Get a specific cafe by ID |
| GET | `/all` | Get all cafes |
| GET | `/search?location=&name=` | Search cafes by location and/or name |
| POST | `/add/<password>` | Add a new cafe |
| PUT/PATCH | `/update_price/<cafe_id>/<password>` | Update a cafe's coffee price |
| DELETE | `/close_cafe/<cafe_id>/<password>` | Delete a cafe |

## Setup
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements_3.13.txt`
3. Add your password to `.env`: `MY_SECURE_PASSWORD=your_password_here`
4. Run the app: `python main.py`
5. Import `Cafe_API.postman_collection.json` into Postman to test endpoints
