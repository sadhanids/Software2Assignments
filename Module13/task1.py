from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime_number(number):
    prime_number = is_prime(number)

    response_data = {
        "Number": number,
        "isPrime": prime_number
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

