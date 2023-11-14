from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_airport_info(icao):
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()
    cur.execute("SELECT name, location FROM airports WHERE icao = %s", (icao,))
    airport = cur.fetchone()
    cur.close()
    conn.close()
    if airport:
        return {"ICAO": icao, "Name": airport[0], "Location": airport[1]}
    else:
        return {"ICAO": icao, "Name": "Airport not found", "Location": "N/A"}

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport(icao):
    airport_info = get_airport_info(icao)
    return jsonify(airport_info)

if __name__ == '__main__':
    app.run(debug=True)