from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake login endpoint
@app.route('/SecretServer/oauth2/token', methods=['POST'])
def mock_login():
    data = request.form
    if data['username'] == 'nashe223' and data['password'] == 'password':
        return jsonify({
            "access_token": "mocked_token_1234567890"
        })
    return jsonify({"error": "invalid credentials"}), 401

# Fake password rotation
@app.route('/SecretServer/api/v1/secrets/<int:secret_id>/change-password', methods=['POST'])
def mock_rotate(secret_id):
    if request.headers.get("Authorization") == "Bearer mocked_token_1234567890":
        return '', 204
    return jsonify({"error": "Unauthorized"}), 403

if __name__ == '__main__':
    app.run(debug=True, port=5000)
