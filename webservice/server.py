from flask import Flask
import joblib 
from flask import request

app= Flask(__name__)
preprocess=joblib.load('models/procesamiento.joblib')
model= joblib.load('models/modelo.joblib')


@app.route('/servicioai',methods=['post'])

def servicio_ai():
	global preprocess
	global model
	content=request.json
	
	age=content['age']
	housing=content['housing']
	amount=content['amount']
	

	
	y= model.predict_proba(preprocess.transform([[age,housing,amount]]))
	print(y)
	return {"prediction":{"bad_score_proba":y[0,0],"good_score_proba":y[0,1]}}



if __name__=='__main__':
	app.run('0.0.0.0')
