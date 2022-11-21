from flask import Flask, Response
import json
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='lentopeli',
         user='root',
         password="p4r!i3",
         autocommit=True
         )


app = Flask(__name__)


@app.route('/port/<code>')
def port(code):
    try:
        sql = "select name, municipality from airport where ident = '" + code + "' "
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        airport = (result[0][0])
        city = (result[0][1])
        status = 200
        answer = {
            "ICAO": code,
            "Name": airport,
            "City": city
        }

    except ValueError:
        status = 400
        answer = {
            "status": status,
            "teksti": "ERROR: Wrong input"
        }

    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=status, mimetype="application/json")


@app.errorhandler(404)
def page_not_found():
    answer = {
        "status": "404",
        "teksti": "ERROR: Wrong end"
    }
    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
