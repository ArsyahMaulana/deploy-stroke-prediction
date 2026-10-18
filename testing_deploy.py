from flask import Flask, request, jsonify
import joblib

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Memuat model yang telah disimpan
model = joblib.load('gbc_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']                      # ambil data dari request JSON
    prediction = model.predict(data)                 # kelas prediksi (0 atau 1)
    probability = model.predict_proba(data)[:, 1]    # peluang kelas stroke

    return jsonify({
        'prediction': prediction.tolist(),
        'probability_stroke': probability.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)