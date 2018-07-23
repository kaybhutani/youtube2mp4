#importing files
from flask import Flask,render_template,request,redirect,url_for,send_from_directory
import os
from pytube import YouTube
import shutil

#app name
app=Flask(__name__)


#app route for main page
@app.route('/', methods=['GET', 'POST'])
def home():
	#deleting all file in the folder
	folder = 'static/temp/'
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
		except Exception as e:
			print(e)
	if request.method == 'GET':
		return render_template("index.html")
	elif request.method == 'POST':
		link=request.form.get('link')
		try:
			#object creation using YouTube which was imported in the beginning
			yt = YouTube(link)
		except:
			print("Connection Error")

			#to handle exception
		stream = yt.streams.first()
		ext=stream.mime_type[6:]
		try:
			#downloading the video
			stream.download(output_path='static/temp/', filename='video')
			
		except:
			print("Some Error!")
		print(stream)
		return render_template('thanks.html',ext=ext)
	return render_template("index.html")


if(__name__=='__main__'):
	app.run(debug=True,use_reloader=True)