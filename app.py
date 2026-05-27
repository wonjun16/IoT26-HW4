
import RPi.GPIO as GPIO
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Use BCM GPIO numbering
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
pins = {
    23: {
        "name": "GPIO 23",
        "state": GPIO.LOW
    },
    24: {
        "name": "GPIO 24",
        "state": GPIO.LOW
    }
}

# Set each GPIO pin as output and turn it off
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


@app.route("/")
def main():
    """
    Main page.
    Reads the current GPIO states and displays them on the web page.
    """
    for pin in pins:
        pins[pin]["state"] = GPIO.input(pin)

    template_data = {
        "pins": pins
    }

    return render_template("main.html", **template_data)


@app.route("/<int:change_pin>/<action>")
def change_pin(change_pin, action):
    """
    Controls the selected GPIO pin.
    URL example:
    /23/on
    /23/off
    """

    if change_pin not in pins:
        return "Invalid GPIO pin", 400

    if action == "on":
        GPIO.output(change_pin, GPIO.HIGH)
    elif action == "off":
        GPIO.output(change_pin, GPIO.LOW)
    else:
        return "Invalid action", 400

    return redirect(url_for("main"))


@app.route("/cleanup")
def cleanup():
    """
    Cleans up GPIO settings.
    """
    GPIO.cleanup()
    return "GPIO cleanup completed."


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=80, debug=False, use_reloader=False)
    finally:
        GPIO.cleanup()
