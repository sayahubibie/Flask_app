from flask import Flask ,jsonify,render_template,request

app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello Flask App"

@app.route('/<name>/<int:age>')
def test(name,age):
    return f""" The name is {name} and \n my age is {age}
                this is my testing app 
                this"""
 

@app.route('/handle',methods=['GET'])
def handle_args_kwargs(*args,**kwargs):

    args = request.args.getlist('args')
    kwargs = {key:value for key,value in request.args.items() if key !='args'}

    args_list= list(args)
    kwargs_dict = dict(kwargs)
    
    result = {
        'args' : args,
        'kwargs' : kwargs_dict
    }

    return jsonify(result)
#http://127.0.0.1:5000/handle?args=apple&args=banana&color=red&size=large

@app.route('/example')
def example():
    key = request.args.get('key')
    values = request.args.get('values')

    result = {
        # 'key' : key,
        # 'values' :values,
        key : values
    }
    return result

@app.route('/json_example')
def json_example():
    print("request.args : ",request.args)
    print("request.form : ",request.form)
    print("request.values",request.values)
    print('jsonify(request.values) : ',jsonify(request.values))
    
    data = dict(request.args)

    # request.args
    #return request.form
    return jsonify(request.values)

@app.route("/web")
def webpage():
    return render_template('home.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')
    

if __name__ == '__main__':
    app.run()


#app.run(debug=True)
