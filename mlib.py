import joblib
import logging
import warnings
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO)
warnings.filterwarnings("ignore", category=UserWarning)


def load_model(model="model.joblib"):
    """Loads model from disk"""

    clf = joblib.load(model)
    return clf


def data():
    """Loads data from disk"""

    df = pd.read_csv("data/pima.train")
    return df


def retrain(
    tsize=0.2,
    model_name="model.joblib",
    n_estimators=100,
    criterion="gini",
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features="sqrt",
):
    """Retrains the model"""
    df = data()

    array = df.values
    X = array[:, 0:8]
    y = array[:, 8]
    y = y.reshape(-1, 1)

    scaler = StandardScaler()
    X_scaler = scaler.fit(X)
    X = X_scaler.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=tsize, random_state=10
    )

    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        criterion=criterion,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features=max_features,
    )
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)

    logging.debug(f"Model accuracy: {accuracy}")
    joblib.dump(clf, model_name)

    return accuracy


def scale_input(din):
    """Scales input to training feature values"""
    din = din.reshape(1, -1)

    df = data()
    array = df.values
    features = array[:, 0:8]

    input_scaler = StandardScaler().fit(features)
    scaled_input = input_scaler.transform(din)

    return scaled_input


def human_readable_payload(predict_value):
    """Takes the predicted value and returns back human readable dictionary"""

    result = {
        "has_diabetes_class": predict_value,
        "has_diabetes_human_readable": "yes" if predict_value == 1 else "no",
    }
    return result


def predict(din):
    """Takes data from a new patient and predicts whether he/she has diabetes"""
    clf = load_model()
    scaled_input_result = scale_input(din)
    diabetes_prediction = int(clf.predict(scaled_input_result))
    payload = human_readable_payload(diabetes_prediction)
    predict_log_data = {
        "new_patient_data": din,
        "scaled_input_result": scaled_input_result,
        "diabetes_prediction": diabetes_prediction,
        "human_readable_payload": payload,
    }
    logging.debug(f"Prediction: {predict_log_data}")
    return payload
