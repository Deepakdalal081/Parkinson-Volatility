# Parkinson-Volatility
import pandas as pd 
import numpy as np 
import yfinance as yf 
import datetime as dt 

stocks = ['ABB.NS','ADANIENSOL.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ADANIPOWER.NS','ATGL.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANKBARODA.NS','BEL.NS','BHEL.NS','BPCL.NS','BHARTIARTL.NS','BOSCHLTD.NS','BRITANNIA.NS','CANBK.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','GAIL.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','IRFC.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWENERGY.NS','JSWSTEEL.NS','JINDALSTEL.NS','JIOFIN.NS','KOTAKBANK.NS','LTIM.NS','LT.NS','LICI.NS','LODHA.NS','M&M.NS','MARUTI.NS','NHPC.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PIDILITIND.NS','PFC.NS','POWERGRID.NS','PNB.NS','RECLTD.NS','RELIANCE.NS','SBILIFE.NS','MOTHERSON.NS','SHREECEM.NS','SHRIRAMFIN.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TVSMOTOR.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','TRENT.NS','ULTRACEMCO.NS','UNIONBANK.NS','UNITDSPR.NS','VBL.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS','ZYDUSLIFE.NS']

end_date = dt.date.today()
start_date = end_date - dt.timedelta(100)

stocks_volatility = []
for i in stocks :
    data = yf.download(i, start=start_date , end=end_date)
    #data = yf.download(stocks, start=start_date , end=end_date, interval = "5m")
    
    #Parkinson Volatility 
    # = sqrt((1/4Nin(2))*sumlog(high/Low)**2)
    
    log_ratio = np.log(data["High"]/data["Low"])
    
    variance = (log_ratio**2).mean()/(4*np.log(2))
    
    Parkinson_Volatility = np.sqrt(variance)
    stocks_volatility.append((i,Parkinson_Volatility))
    
    
v = pd.DataFrame(stocks_volatility, columns= ["Stocks", "Volatility"])
v = v.sort_values(by = "Volatility", ascending=False)
print("\n", v.head(7))

#print(f"\n{i} Stocks have maximum {Parkinson_Volatility.max()}")
    
    
    
    

    
        


