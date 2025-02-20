# Flask REST API

This project is a basic REST API built with Flask. It provides a simple structure for creating and managing API endpoints.

## Project Structure

```
flask-rest-api
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── tests
│   └── test_routes.py
├── venv
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-rest-api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Flask application, use the following command:

```
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app` before running the command.

## API Endpoints

- List of available endpoints will be documented here.

## Running Tests

To run the tests, ensure the virtual environment is activated and execute:

```
pytest tests/test_routes.py
```

## License

This project is licensed under the MIT License.