from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple keyword-based spam detection function
def is_spam(message):
    spam_keywords = ['free', 'win', 'winner', 'cash', 'prize', 'congratulations']
    message = message.lower()
    return any(keyword in message for keyword in spam_keywords)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('message', '')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    result = "Spam" if is_spam(message) else "Ham"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

