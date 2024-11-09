# Weather Alert SMS Notification 🌦️📲

This project is a Python script that checks the weather forecast and sends an SMS alert if it's going to rain. It uses the OpenWeather API for weather data and Twilio API for sending SMS messages.

## Table of Contents
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Example Output](#example-output)
- [License](#license)

---

## Getting Started 🚀

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/weather-alert.git
   cd weather-alert
    ```
2. Install dependencies using pip:
```bash
pip install -r requirements.txt
```
---
## Environment Variables 🔐
The project requires the following environment variables to be set for accessing the APIs and phone numbers.

Create a .env file in the root of your project and add:
```bash
OWM_ENDPOINT=https://api.openweathermap.org/data/2.5/forecast
API_KEY=YOUR_OPENWEATHER_API_KEY
ACCOUNT_SID=YOUR_TWILIO_ACCOUNT_SID
AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN
FROM_PHONE=YOUR_TWILIO_PHONE_NUMBER
TO_PHONE=RECEIVER_PHONE_NUMBER
```
Replace YOUR_OPENWEATHER_API_KEY, YOUR_TWILIO_ACCOUNT_SID, etc., with your actual credentials.
---
## Dependencies 📦
- **requests**: To make HTTP requests to the OpenWeather API.
- **twilio**: For sending SMS alerts.
- **dotenv**: For loading environment variables from the .env file.
```bash
pip install requests twilio python-dotenv
```
---
## Usage ▶️
Run the script with the following command:
```bash
python main.py
```
The script checks the weather for the given location. If rain is forecasted, an SMS alert is sent to the specified number.
---
## Example Output 📝
If rain is forecasted, the Twilio API will send an SMS. You can check the delivery status in the terminal output:
```bash
queued
```
---
## License 📄
This project is open-source and available under the MIT License.
