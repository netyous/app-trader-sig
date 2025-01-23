from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
sample_news = [
    {"title": "Bloomberg: US GDP Growth Slows", "impact": "High", "asset": "USD", "color": "red"},
    {"title": "Reuters: ECB Rate Decision Announced", "impact": "Medium", "asset": "EUR", "color": "orange"},
    {"title": "Investing.com: NFP Data Released", "impact": "High", "asset": "USD", "color": "red"},
]

sample_events = [
    {"title": "US Federal Reserve Rate Decision", "date": "2023-10-04", "impact": "High", "asset": "USD", "color": "red"},
    {"title": "Eurozone Inflation Data", "date": "2023-10-05", "impact": "Medium", "asset": "EUR", "color": "orange"},
    {"title": "Non-Farm Payrolls (NFP)", "date": "2023-10-06", "impact": "High", "asset": "USD", "color": "red"},
]

sample_signals = [
    {"asset": "EUR/USD", "signal": "Strong", "entry": 1.10, "stopLoss": 1.08, "takeProfit": 1.12, "color": "green"},
    {"asset": "XAU/USD", "signal": "Moderate", "entry": 1900, "stopLoss": 1880, "takeProfit": 1920, "color": "light-green"},
    {"asset": "USD/JPY", "signal": "Neutral", "entry": 110.50, "stopLoss": 110.00, "takeProfit": 111.00, "color": "yellow"},
    {"asset": "GBP/USD", "signal": "Moderate", "entry": 1.25, "stopLoss": 1.23, "takeProfit": 1.27, "color": "orange"},
    {"asset": "USD/CAD", "signal": "Strong", "entry": 1.35, "stopLoss": 1.33, "takeProfit": 1.37, "color": "red"},
]

@app.route('/api/news', methods=['GET'])
def get_news():
    return jsonify(sample_news)

@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(sample_events)

@app.route('/api/signals', methods=['GET'])
def get_signals():
    return jsonify(sample_signals)

if __name__ == '__main__':
    app.run(debug=True)
