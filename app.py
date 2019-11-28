from flask import Flask, render_template, request
import pigpio

pi = pigpio.pi()
RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24
app = Flask(__name__)

def changeLights(aHex):
	hexCodeReal = aHex[1:7]
	slashedRGB = "/" + "/".join(str(i) for i in tuple(int(hexCodeReal[i:i + len(hexCodeReal) // 3], 16) for i in range(0, len(hexCodeReal), len(hexCodeReal) // 3)))
	slashedRGB = slashedRGB[1:len(slashedRGB)]
	rgbarray = slashedRGB.split('/')
	rgbarray = [int(x) for x in rgbarray]
	for i in range(0, 3):
		if(rgbarray[i] < 0):
			rgbarray[i] = 0
		if(rgbarray[i] > 255):
			rgbarray[i] = 255
	print(rgbarray)
	pi.set_PWM_dutycycle(RED_PIN, rgbarray[0])
	pi.set_PWM_dutycycle(GREEN_PIN, rgbarray[1])
	pi.set_PWM_dutycycle(BLUE_PIN, rgbarray[2])

@app.route('/', methods=['POST', 'GET'])
def formSubmit():
	if request.method == 'POST':
		hexCode = request.form.get('colorPick')
		print(hexCode)
		changeLights(hexCode)
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='10.0.0.69', port=9874)

