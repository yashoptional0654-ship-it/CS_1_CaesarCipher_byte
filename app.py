"""
Caesar Cipher - Web App
Task 1 | CyberSecurity Track | AVIP 2026

Same encrypt/decrypt logic as caesar_cipher.py (CLI version), wrapped in a
small Flask web app so it can be deployed live (e.g. on Render.com).
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# ---- Same core logic as caesar_cipher.py ----

def shift_char(ch: str, shift: int) -> str:
    """Shift a single character by `shift` positions, wrapping A-Z / a-z.
    Non-alphabet characters (numbers, spaces, punctuation) are returned unchanged."""
    if ch.isupper():
        return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    if ch.islower():
        return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    return ch


def caesar_encrypt(text: str, shift: int) -> str:
    shift = shift % 26
    return ''.join(shift_char(c, shift) for c in text)


def caesar_decrypt(text: str, shift: int) -> str:
    shift = shift % 26
    return ''.join(shift_char(c, -shift) for c in text)


# ---- Routes ----

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/process", methods=["POST"])
def process():
    data = request.get_json(force=True, silent=True) or {}
    text = data.get("text", "")
    mode = data.get("mode", "encrypt")
    shift_raw = data.get("shift", 0)

    try:
        shift = int(shift_raw)
    except (TypeError, ValueError):
        return jsonify({"error": "Shift must be an integer."}), 400

    if not isinstance(text, str):
        return jsonify({"error": "Text must be a string."}), 400

    if mode == "encrypt":
        result = caesar_encrypt(text, shift)
    elif mode == "decrypt":
        result = caesar_decrypt(text, shift)
    else:
        return jsonify({"error": "Mode must be 'encrypt' or 'decrypt'."}), 400

    return jsonify({"result": result})


@app.route("/healthz")
def healthz():
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True)
