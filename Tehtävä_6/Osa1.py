from flask import Flask, jsonify
app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:num>', methods=['GET'])
def check_prime(num):
    prime = is_prime(num)
    return jsonify({"Number": num, "isPrime": prime})

if __name__ == '__main__':
    app.run(debug=True)