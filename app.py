from flask import Flask, render_template, url_for, request, redirect
from caption import *
import warnings
warnings.filterwarnings("ignore")
from sound import*

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
	return render_template('aboutus.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']
		# print(img)
		# print(img.filename)

		img.save("static/"+img.filename)
		caption = caption_this_image("static/"+img.filename)
		snd=play(caption)	

	result_dic = {
			'image' : "static/" + img.filename,
			'description' : caption,
			'sound':snd
		}
	return render_template('index.html', results = result_dic)

if __name__ == '__main__':
	app.run(debug = True)

