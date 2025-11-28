import os
import sys

# Add project root to Python path so we can import app.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
