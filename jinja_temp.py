from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    t_name = "Test User"
    name= "sayali"
    return render_template('index.html',test_name=t_name,html_name=name)


@app.route('/list')
def list_data():
    list_elements = ['AAAP', 'TESL', 'MSE' , 'MICRO', 'TCS']
    return render_template('list.html', ticker=list_elements)

@app.route('/user')
def user_list():
    users = [
        {'name': 'Sayali'  , 'age': '24', 'Trainer': 'DSA'},
        {'name': 'Shyamli' , 'age': '27', 'Trainer': 'React'},
        {'name': 'Achal'   , 'age': '29', 'Trainer': 'Java/Python'},
        {'name': 'Ritiksha', 'age': '30', 'Trainer': 'Full Stack'}
    ]
    return render_template('user.html',test_user = users)

@app.route('/dict')
def user_dict():
    user = {
        1:{'name': 'Sayali'  , 'age': '24', 'Trainer': 'DSA'},
        2:{'name': 'Shyamli' , 'age': '27', 'Trainer': 'React'},
        3:{'name': 'Achal'   , 'age': '29', 'Trainer': 'Java/Python'},
        4:{'name': 'Ritiksha', 'age': '30', 'Trainer': 'Full Stack'}
    }
    return render_template('dict.html',dict_user=user)


def combine_data():
    name = "Test User"

    list_elements = ['AAAP', 'TESL', 'MSE' , 'MICRO', 'TCS']

    users = [
        {'name': 'Sayali'  , 'age': '24', 'Trainer': 'DSA'},
        {'name': 'Shyamli' , 'age': '27', 'Trainer': 'React'},
        {'name': 'Achal'   , 'age': '29', 'Trainer': 'Java/Python'},
        {'name': 'Ritiksha', 'age': '30', 'Trainer': 'Full Stack'}
    ]

    user = {
        1:{'name': 'Sayali'  , 'age': '24', 'Trainer': 'DSA'},
        2:{'name': 'Shyamli' , 'age': '27', 'Trainer': 'React'},
        3:{'name': 'Achal'   , 'age': '29', 'Trainer': 'Java/Python'},
        4:{'name': 'Ritiksha', 'age': '30', 'Trainer': 'Full Stack'}
    }

    return render_template('combo.html',name=name,)

#app.run(debug=True)

if __name__=='__main__':
    app.run(port=9001)