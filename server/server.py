from flask import Flask,request,jsonify
from werkzeug.wrappers import response
import utils
app=Flask(__name__)
@app.route('/get_locations',methods=['GET'])
def get_location():
    response=jsonify({'locations':utils.get_locations()})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response 
@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    response=jsonify({
        "price":utils.get_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__=='__main__':
    print('Flask Server is running...')
    utils.load_saved_location()
    app.run()