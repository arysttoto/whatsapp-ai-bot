"""
Main Application Entry Point

This module serves as the main entry point for the WhatsApp AI bot application.
It creates the Flask application instance and runs the development server.

This file is typically used for development and testing. For production
deployment, consider using a WSGI server like Gunicorn or uWSGI.

Example:
    python app/main.py  # Run development server
    gunicorn app.main:app  # Run with production WSGI server
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) 
