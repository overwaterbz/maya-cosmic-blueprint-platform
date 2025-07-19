#!/usr/bin/env python3
"""
Vercel Entry Point - Maya Cosmic Blueprint Platform
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # Import the FastAPI app
    from app import app
    
    # Use app directly for Vercel
    handler = app
    
except ImportError as e:
    # Simple fallback
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse
    
    app = FastAPI()
    
    @app.get("/")
    def root():
        return HTMLResponse("""
        <html><body>
        <h1>Maya Cosmic Blueprint Platform</h1>
        <p>Import Error: Missing dependencies</p>
        <p>Error: """ + str(e) + """</p>
        </body></html>
        """)
    
    handler = app

except Exception as e:
    # Basic error handler
    def handler(event, context):
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html'},
            'body': f'<h1>Maya Platform Error</h1><p>{str(e)}</p>'
        }
