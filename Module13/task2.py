import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)
app.json.sort_keys = False

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='DohaLife12*',
    autocommit=True
)

@app.route("/airport/<icao>", methods=['GET'])
def search_for_airports(icao):
    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s;"

    cursor = connection.cursor()
    cursor.execute(sql, (icao.upper(),))
    database_data = cursor.fetchone()

    ident, name, municipality = database_data

    response_data = {
        "ICAO": ident,
        "Name": name,
        "Location": municipality
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)