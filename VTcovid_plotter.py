import pandas as pd
import matplotlib.pyplot as plt

def fetch_and_plot_data(start_date, end_date):
    # Fetching the data
    url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"
    data = pd.read_csv(url, parse_dates=['dateRep'], dayfirst=True)

    # Filtering data for Germany
    country_data = data[data["countriesAndTerritories"] == "Germany"]

    # Filtering data between the specified dates
    filtered_data = country_data[(country_data["dateRep"] >= start_date) & (country_data["dateRep"] <= end_date)]
    filtered_data = filtered_data.sort_values(by="dateRep")

    # Plotting the data
    plt.figure(figsize=(15,7))
    plt.plot(filtered_data["dateRep"], filtered_data["cases"], label="Daily Cases", color="blue")
    plt.plot(filtered_data["dateRep"], filtered_data["deaths"], label="Daily Deaths", color="red")
    plt.title(f"COVID Data for Germany from {start_date} to {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Number of Cases/Deaths")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Modify these dates for your desired range
start_date = "2021-01-01"
end_date = "2021-12-31"
fetch_and_plot_data(start_date, end_date)