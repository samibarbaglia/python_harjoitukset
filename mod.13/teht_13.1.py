import json
import flask

app = flask.Flask(__name__)


@app.route('/prime/<int:num>')
def prime(num):
    result = test(num)

    answer = {
        "Number": num,
        "isPrime": result
    }

    json_data = json.dumps(answer, default=lambda o: o.__dict__, indent=4)
    return json_data


def test(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True
    elif num == 1:
        return True


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
