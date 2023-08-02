from flask import Flask, render_template, request, Response
import random
import string

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
    
def pairing_code():
    ran = "".join(random.choices(string.ascii_uppercase + string.digits,k=10))
    return ran

@app.route("/", methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/room', methods=["GET", "POST"])
def room():
    if request.method == "GET":
        return render_template('index.html')
    else:
        if (ifmobile() == True):
            passcode = pairing_code()
            return render_template('mobile.html', passcode = passcode)
        else:
            return render_template('pc.html')
        
@app.route('/mouse-mobile', methods=['GET', 'POST'])
def mouse_mobile():
    return render_template('mouse.html')


    
