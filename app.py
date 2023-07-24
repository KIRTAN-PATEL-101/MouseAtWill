from flask import Flask, render_template, request, Response

app = Flask(__name__)

def ifmobile():
    mobile = False
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        mobile = True
    elif "android" in user_agent:
        mobile = True
    return mobile
    
def ifiphone():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return True
    else:
        return False

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        return render_template('room.html')

@app.route('/room', methods=["GET", "POST"])
def room():
    if request.method == "GET":
        return render_template('room.html')
    else:
        if request.form.get('Mobile') == 'Press here on Mobile':
            if (ifmobile() == False):
                return render_template('wrong_device.html')
            else:
                return render_template('tmp.html')
        elif request.form.get('PC') == 'Press here on PC':
            if (ifmobile() == True):
                return render_template('wrong_device.html')
            else:
                return render_template('tmp.html')
            pass


    
