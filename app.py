from flask import Flask, request, jsonify
from flask.logging import create_logger
import numpy as np
import logging
import mlib

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


@app.route("/")
def home():
    html = r"""<h3>Diabetes prediction API.</h3>
    Input for the /predict route looks like: (testing deploy - part 02)<br>
    {{<br>
    'preg':1,<br>
    'plas':93,<br>
    'pres':70,<br>
    'skin':31,<br>
    'test':0,<br>
    'mass':30.4,<br>
    'pedi':0.315,<br>
    'age':23<br>
    }}<br><br>
    Results for the /predict route looks like:<br>
    result: {{<br>
    "prediction": {{<br>
    "has_diabetes_class": 0,<br>
    "has_diabetes_human_readable": "no"<br>
    }}<br>
    }}"""
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """Predicts whether a patient has diabetes."""

    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    din = np.array(
        [
            json_payload["preg"],
            json_payload["plas"],
            json_payload["pres"],
            json_payload["skin"],
            json_payload["test"],
            json_payload["mass"],
            json_payload["pedi"],
            json_payload["age"],
        ]
    )
    prediction = mlib.predict(din)
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
