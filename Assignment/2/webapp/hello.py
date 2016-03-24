from flask import Flask, render_template
app = Flask(__name__)
namedict = []

class binheap:
	def __init__(self):
		self.size = 0
	
	def printer(self):
		return "hey" 	


temp = binheap()
temp.size=2
#temp2 = 0

import sys

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project', methods=['GET'])
def sorting_get():
    return render_template('project.html')

@app.route('/hello/<name>', methods=['GET'])
def hello(name=None):
    #return render_template('hello.html', name=name
    if name == None:
	s = ','.join(map(str,testprint()))
	return ("testing \n" + s)
    if name in namedict:
	return globals()[name].printer()
	#return ','.join(map(str,locals().keys()))
    else:
	namedict.append(name)
	#name = name.encode('ascii')
        #global temp2
	temp2 = name 
	temp2 = globals()['binheap']()
        temp2.size = 2
    	return ','.join(map(str,globals().keys()))
	#return name.printer()	

def testprint():
    return [1,2,3,4]   


if __name__ == '__main__':
    app.run(debug=True)
