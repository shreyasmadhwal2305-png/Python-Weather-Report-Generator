# 🌦️ Python Weather Report Generator

A Python-based Weather Report Generator that fetches real-time weather information for cities around the world using the **Open-Meteo API**.

## 🚀 Features

- 🌍 Search for weather information by city name.
- 🌡️ Retrieve current temperature and weather conditions.
- 💨 Display relevant weather information in a readable format.
- 🔄 Integrate with real-world APIs using Python Requests.
- ⚠️ Handle API errors, connection failures and invalid city names.
- 📄 Generate and save weather reports to a text file.
- 🕒 Include the date and time of report generation.

## 🛠️ Technologies Used

- **Python 3**
- **Requests** – API communication.
- **Open-Meteo API** – Weather and geolocation data.
- **Datetime** – Date and time formatting.
- **JSON** – Processing API responses.

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/shreyasmadhwal2305-png/Python-Weather-Report-Generator.git   ```

2. Navigate into the project directory:

   ```bash
   cd python-weather-report-generator
   ```

3. Install the required dependency:

   ```bash
   pip install requests
   ```

## ▶️ How to Run

Execute the following command:

```bash
python day30_weather_automation.py
```

Enter a city name when prompted to generate its weather report.

The generated report is saved as `weather_report.txt`.

## 🌐 API Information

This project uses the free [Open-Meteo API](https://open-meteo.com/), which provides weather forecasts and geographical location data without requiring an API key.

## 📚 What I Learned

Through this project, I practised:

- Working with external REST APIs.
- Sending HTTP GET requests.
- Processing JSON responses.
- Handling exceptions and API failures.
- Working with date and time.
- Automating report generation.
- Saving information to local files.

## 🔮 Future Improvements

- Interactive weather dashboard.
- Multi-day weather forecasts.
- Weather comparisons between cities.
- Graphical weather visualizations.
