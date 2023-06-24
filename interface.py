from flask import Flask,jsonify,render_template,Request,request
import config

from utils import finance
app = Flask(__name__)


@app.route("/")
def get_homeApi():
    return "home Api"

@app.route("/predict",methods =["POST","GET"])
def get_predict():
    if request.method == "POST":
        print("We are using POST Method")
        data = request.form   
        print("Data1 using POST method",data)
        data = request.form
        loan_amnt             =  eval(data["loan_amnt"])
        term                  =  (data["term"])
        int_rate              =  float(data["int_rate"])
        emp_length            =  int(data["emp_length"])
        home_ownership        =  (data["home_ownership"])
        annual_inc            =  int(data["annual_inc"])
        purpose               =  (data["purpose"])
        addr_state            =  (data["addr_state"])
        dti                   =  float(data["dti"])
        delinq_2yrs           =  int(data["delinq_2yrs"])
        revol_util            =  float(data["revol_util"])
        total_acc             =  int(data["total_acc"]) 
        bad_loan              =  eval(data["bad_loan"])
        longest_credit_length =  int(data["longest_credit_length"])
        fin_pred = finance(loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,bad_loan,longest_credit_length)
        classification =fin_pred.get_prediction()
        return jsonify({"classification":f"prediction is:{classification}"})
     
    elif request.method == "GET":
        print("we are using GET method")
        data = request.form 
        print("Data2 using GET method",data)
        data = request.form
        loan_amnt             =  eval(data["loan_amnt"])
        term                  =  (data["term"])
        int_rate              =  float(data["int_rate"])
        emp_length            =  int(data["emp_length"])
        home_ownership        =  (data["home_ownership"])
        annual_inc            =  int(data["annual_inc"])
        purpose               =  (data["purpose"])
        addr_state            =  (data["addr_state"])
        dti                   =  float(data["dti"])
        delinq_2yrs           =  int(data["delinq_2yrs"])
        revol_util            =  int(data["revol_util"])
        total_acc             =  int(data["total_acc"]) 
        bad_loan              =  eval(data["bad_loan"])
        longest_credit_length =  int(data["longest_credit_length"])
        fin_pred = finance(loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,bad_loan,longest_credit_length)
        result  =fin_pred.get_prediction()
        return jsonify({"result":f"prediction is:{result}"})
        
        
if __name__ =="__main__":
    app.run(host = "0.0.0.0",port=config.PORT_NUMBER_1)