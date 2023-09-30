import pyttsx3
import subprocess
import time
from twilio.rest import Client

# Define the Wi-Fi network name you want to trigger the message on.
target_wifi_ssid = "YourWiFiSSID"

# Define the message you want to send.
message = "You are connected to the target Wi-Fi network."

# Twilio Account SID and Auth Token
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"

# Twilio phone number (Sender)
twilio_phone_number = "your_twilio_phone_number"

# Destination phone number (Recipient)
phone_number = "+1234567890"

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def get_current_wifi_ssid():
    try:
        result = subprocess.run(["/usr/sbin/networksetup", "-getairportnetwork", "en0"], capture_output=True, text=True)
        output = result.stdout.strip()
        return output.split(":")[1].strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

def send_message():
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=phone_number
        )
        print(f"Message sent with SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

while True:
    current_wifi_ssid = get_current_wifi_ssid()
    if current_wifi_ssid == target_wifi_ssid:
        send_message()
    time.sleep(60)  # Check every 60 seconds
