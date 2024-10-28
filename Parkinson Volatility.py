#import the liberary 
import pandas as pd 
import numpy as np 
import yfinance as yf 
import datetime as dt 

#Stocks symbol whose volatility we want to know 
stocks = ['ABB.NS','ADANIENSOL.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ADANIPOWER.NS','ATGL.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANKBARODA.NS','BEL.NS','BHEL.NS','BPCL.NS','BHARTIARTL.NS','BOSCHLTD.NS','BRITANNIA.NS','CANBK.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','GAIL.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','IRFC.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWENERGY.NS','JSWSTEEL.NS','JINDALSTEL.NS','JIOFIN.NS','KOTAKBANK.NS','LTIM.NS','LT.NS','LICI.NS','LODHA.NS','M&M.NS','MARUTI.NS','NHPC.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PIDILITIND.NS','PFC.NS','POWERGRID.NS','PNB.NS','RECLTD.NS','RELIANCE.NS','SBILIFE.NS','MOTHERSON.NS','SHREECEM.NS','SHRIRAMFIN.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TVSMOTOR.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','TRENT.NS','ULTRACEMCO.NS','UNIONBANK.NS','UNITDSPR.NS','VBL.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS','ZYDUSLIFE.NS']

#Time Period 
end_date = dt.date.today()
start_date = end_date - dt.timedelta(20)

#Storing the Volatility of each stock 
stocks_volatility = []
for i in stocks :
    #importing the data from the yahoo finance
    data = yf.download(i, start=start_date , end=end_date)
    
    # For some time specfic interval like 5 min or 1 hour  
    #data = yf.download(stocks, start=start_date , end=end_date, interval = "5m")
    
    #Parkinson Volatility Formula 
    # = sqrt((1/4Nin(2))*sumlog(high/Low)**2)
    
    log_ratio = np.log(data["High"]/data["Low"])
    
    variance = (log_ratio**2).mean()/(4*np.log(2))
    
    Parkinson_Volatility = np.sqrt(variance)

    #After each calucaltion storing the volalility of each stock 
    stocks_volatility.append((i,Parkinson_Volatility))
    
# Storing the value of volatility and stock symbols     
Volatility = pd.DataFrame(stocks_volatility, columns= ["Stocks", "Volatility"])

#Arranging the Volatility from largest to smallest 
Volatility = Volatility.sort_values(by = "Volatility", ascending=False)

# Top 5 Stocks which are most volatile 
print("\n", Volatility.head(5))


