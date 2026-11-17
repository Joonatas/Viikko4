from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="salasana123",
        database="exampledb"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT hits FROM counter WHERE id = 1")
    row = cursor.fetchone()

    hits = row[0]

    cursor.close()
    conn.close()

    return f"""
    <html>
    <head>
        <title>Viikko 4 - Replica Server</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                max-width: 1000px;
                margin: auto;
                padding: 30px;
                line-height: 1.6;
            }}

            .card {{
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: #005fb8;
            }}

            h2 {{
                color: #333;
            }}

            .counter {{
                font-size: 3em;
                color: #008000;
                font-weight: bold;
            }}
        </style>
    </head>
