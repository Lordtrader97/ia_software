from flask import Flask
import requests
app=Flask(__name__)

@app.route("/credit/predict")
def predict():
	response=requests.post("http://127.0.0.1:5000/servicioai",json={"age":23,"housing":"rent","amount":1000})
	print("ia_responde",response.json())
	return response.json()

if __name__=='__main__':
	app.run(host='0.0.0.0',port=8080)

