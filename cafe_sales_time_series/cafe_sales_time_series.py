import pandas as pd

data = {
    "date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
    "sales": [
        200, 220, 215, 230, 250, 245, 260, 270, 265, 280,
        300, 295, 310, 330, 325, 340, 360, 355, 370, 390,
        410, 405, 420, 440, 435, 450, 470, 465, 480, 500
    ]
}

df = pd.DataFrame(data)
print(df)

date = df["date"]
sales = df["sales"] 
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(date, sales, marker='o')
plt.title("Cafe Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(sales, order=(1, 1, 1))
model_fit = model.fit()
print(model_fit.summary())
forecast = model_fit.forecast(steps=7)
print("Forecasted sales for the next 7 days:")
print(forecast)
plt.figure(figsize=(10, 5))
plt.plot(date, sales, marker='o', label='Actual Sales')
future_dates = pd.date_range(start=date.iloc[-1] + pd.Timedelta(days=1), periods=7, freq='D')
plt.plot(future_dates, forecast, marker='o', label='Forecasted Sales', color='red')
plt.title("Cafe Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

