import os
from flask import Flask, request, jsonify, render_template
import smtplib
from email.message import EmailMessage
import re

app = Flask(__name__, template_folder='templates')

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

def safe_email(email):
    return bool(email and EMAIL_RE.match(email))


@app.route("/")
def home():
    return render_template("share_location.html")


@app.route("/report", methods=["POST"])
def report():
    data = request.get_json()
    if not data:
        return "No JSON body", 400

    lat = data.get("latitude")
    lon = data.get("longitude")
    name = data.get("name", "")
    accuracy = data.get("accuracy")
    ua = data.get("userAgent", "")
    ts = data.get("timestamp", "")

    if lat is None or lon is None:
        return "Missing coordinates", 400

    # Default destination email (can be overridden with ?to=...)
    dest = os.environ.get("DEST_EMAIL", "majumakmurbumdes04@gmail.com")

    # Allow temporary override via query param, if it looks like an email
    to_override = request.args.get("to")
    if to_override and safe_email(to_override):
        dest = to_override

    if not dest:
        return "No destination email configured", 500

    # Build Google Maps link
    maps_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"

    subject = f"Lokasi dibagikan{' oleh ' + name if name else ''}"
    body = f"""
Lokasi dibagikan:

Nama: {name or '(tidak diisi)'}
Latitude: {lat}
Longitude: {lon}
Akurasi (meter): {accuracy}
Waktu (UTC ISO): {ts}
User-Agent: {ua}

🔗 Lihat di Google Maps:
{maps_link}
"""

    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = os.environ.get("SMTP_USER")
        msg["To"] = dest
        msg.set_content(body)

        smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(os.environ.get("SMTP_PORT", 587))

        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(os.environ.get("SMTP_USER"), os.environ.get("SMTP_PASS"))
            smtp.send_message(msg)

        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
