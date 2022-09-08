
# importing Flask and other modules
from flask import Flask, request, render_template
from logging import FileHandler,WARNING
# Flask constructor
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)
app = Flask(__name__, template_folder="CHATBOX", static_folder="static")  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)
if __name__=="__main__":
    app.run(debug=True)
