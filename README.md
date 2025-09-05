# Biblioteca de Cărți - Flask App

A simple web application for managing a book library, built with Flask and SQLite.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/andreipirone/books_database.git
   cd books_database
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Access the application**
   Open your web browser and go to `http://localhost:5000`

3. **Manage your library**
   - View all books on the main page
   - Click "Add Book" to create new entries
   - Use the edit/delete buttons to modify existing books

## API Endpoints

- `GET /` - Display all books
- `GET /create` - Show book creation form
- `POST /generate` - Create a new book
- `GET /edit/<id>` - Show book editing form
- `POST /change` - Update a book
- `GET /delete/<id>` - Delete a book

## Dependencies

- **Flask** - Web framework
- **SQLite3** - Database engine (included with Python)

## License

This project is open source and available under the MIT License.
