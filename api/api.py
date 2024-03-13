from flask import Flask, request, jsonify
from flask_cors import CORS
from regression import apply_regression
from extract_data import extract_data

app = Flask(__name__)
CORS(app)

@app.route('/predict_sales_quantity', methods=['POST'])
def predict_sales_quantity():
    data = request.get_json()
    from_date = data.get('from_date')
    to_date = data.get('to_date')
    material_code = data.get('material_code')
    sales_office_id = data.get('sales_office_id')
    sales_quantity = apply_regression(from_date, to_date, material_code, sales_office_id)
    print (sales_quantity)
    return sales_quantity

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
