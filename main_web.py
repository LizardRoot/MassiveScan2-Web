from flask import Flask, render_template, request, redirect
import configparser

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
	if request.method == "POST":
		port = request.form['port']
		timeout = request.form['timeout']
		thread = request.form['thread']
		ips = request.form['ips']

		read_file=open("setting.ini","w")
		#content=read_file.read()
		config_object= configparser.ConfigParser()
		config_object.read("setting.ini")
		config_object["Setting"]={
				"port": port,
				"timeout": timeout,
				"thread": thread,
				"ips": ips
				}
		with open("setting.ini","w") as file_object:
			config_object.write(file_object)
		return redirect('/')
	else:
		return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)