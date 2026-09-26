# # import requests

# # response = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
# # price = response.json()["quotes"]["USD"]["price"]
# # print(price)


# import requests
# import json
# response = requests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
# data = response.json()


# formatted_data = json.dumps(data, indent = 4)
# print("Formatted data")
# print(formatted_data)


# print("\n" + "="*50 + "\n")

# market_cap_change_24h= data["quotes"] ["USD"] ["market_cap_change_24h"]
# print("Market Cap Change 24h: ", market_cap_change_24h)

# price = data["quotes"]["USD"]["price"]
# print("Price: ", price)


# import pandas as pd 
# crypto_data_list = [{"Coin_Name": data["name"],}]



# adding libraries
import requests 
import pandas as pd 

print("ETL Pipeline for Crypto Data Extraction, Transformation and Loading")

#extract function 
def extract_data():
    url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"
    response = requests.get(url)
    return response.json()


#Transform function 
def Transform_data(data):
    crypto_data_list= [{
        "Coin_Name" : data["name"],
        "Symbol" : data["symbol"],
        "Price_USD" : data["quotes"]["USD"]["price"],
        "Market_Cap_Change_24h": data["quotes"] ["USD"] [ "market_cap_change_24h"]
     }]

    df = pd.DataFrame(crypto_data_list)
    return df 


def Load_data(df, filename):
    df.to_csv(filename, index=False) 
    print(f"Data Loaded to '{filename}' successfully!")



#run ETL pipeline function
def run_etl_pipeline():
   print("1. Extracting data from API")
   raw_data = extract_data()

   print("2. Transforming data into Pandas Table")
   final_df = Transform_data(raw_data)

   print("\n" + "="*50) 
   print("--- Final ETL Output Table ---")
   print(final_df)

   #loading data to csv file
   print("\n3. Loading data to CSV file")
   Load_data(final_df, "crypto_data.csv")


run_etl_pipeline()



