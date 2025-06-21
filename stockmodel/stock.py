import streamlit as st
import yfinance as yf
import pandas as pd

st.sidebar.markdown("# :orange[Stock Price Analysis and Sales Prediction Using Machine Learning]")
a = ["APPLE", "MICROSOFT", "GOOGLE", "NETFLIX","AMAZON","FACEBOOK","TESLA"]
q = st.sidebar.selectbox(" 📈 Select Stock", options=a,)

if q == "APPLE":
    st.markdown(f"# :orange[APPLE STOCK PRICE ANALYSIS]")
    x = st.number_input("Enter the number of years for analysis", min_value=1, max_value=30, value=1, step=1)
    if st.button("Submit"):
        ticker_symbol = "AAPL" 
        ticker = yf.Ticker(ticker_symbol)
        dataset = ticker.history(period=f"{x}y")
        
        st.markdown("### :blue[Historical Data:]")
        data = dataset.iloc[:, :5]  # Open, High, Low, Close, Volume columns usually first 5
        st.write(data)
        st.write(f"Data shape: {data.shape}")

        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown("#### :orange[Stock Price (High & Low)]")
        st.line_chart(data[["High", "Low"]], use_container_width=True,color=["#00FFFF",	"#FF00FF"])
        
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :orange[{q} Stock Price Open and Close]")
        st.bar_chart(data[["Open", "Close"]], use_container_width=True,color=["#00FFFF","#000080"])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} TOTAL SALE IN DOLLAR($) ]")
        st.line_chart(dataset["Volume"],y_label="SALE IN DOLLAR",color="#00FFFF")
        
        st.markdown("### :blue[----------------------------------------------------------]")
        dataset["change"]=dataset["Volume"].pct_change()
        
        st.markdown("### :blue[COMPANY GROWTH AND DOWNFALL IN PERCENTAGE]")

        st.line_chart(dataset["change"],y_label="IN PERCENTAGE",color="#00FFFF")
        st.markdown("### :blue[----------------------------------------------------------]")

        st.markdown("### :blue[MACHINR LEARNING ALGORITHM  LINEAR REGRESSION USE TO PREDICTION]")
        st.markdown("### :blue[                                                     ]")


        # MACHINE LAEARNING MODEL
        
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression

       # Drop missing values
        dataset.dropna(inplace=True)

       # Feature and target selection
        x = dataset[['Open', 'High', 'Low', 'Close', 'change']]
        y = dataset[['Volume']]

       # Split data into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

       # Linear Regression model training
        lg = LinearRegression()
        lg.fit(x_train, y_train)

       # Predict volume and convert to integer type
        dataset["predict"] = lg.predict(x).astype(int)

        # Display line chart in Streamlit
        st.line_chart(dataset[["Volume", "predict"]], use_container_width=True, color=["#00FFFF","#CD5C5C"])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.write(dataset[["Volume","predict"]])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[ {q} COMPANY  PER DAY SALE USING MACHINE LAEARING PREDICTION MODEL]")
        st.markdown(f"###### :orange[1-input variable is {q} company open stock ,close stock,day hight stock and low stock and day wise growth  ]")
        st.markdown(f"###### :orange[ 2- output is volumn means total sale in day]")
        st.markdown(f"### :blue[                                   ]")
        a= st.number_input("OPEN STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        b= st.number_input("CLOSE STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        c= st.number_input("HIGH STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        d= st.number_input("LOW STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        e = st.number_input("STOCK PRICE CHANGE",min_value=-100.0,max_value=100.0,value=0.5,step=0.1,format="%.2f")
        
        if st.success("submit") :
         v=lg.predict([[a,b,c,d,e]])
         s=int(v[0])
         f=f"{q} TOTAL DAY SALE IS :-  {s} $"
         st.info(f)
         st.subheader("TOTAL SALE IN RUPEES")
         p=s*81
         k=f"{q} TOTAL DAY SALE IS :-  {p} ₹"
         st.success(k)
         
elif q == "MICROSOFT":
   st.markdown(f"# :blue[MICROSOFT STOCK PRICE ANALYSIS]")
   x = st.number_input("Enter the number of years for analysis", min_value=1, max_value=30, value=1, step=1)
   if st.button("Submit"):
        ticker_symbol = "MSFT"
        ticker = yf.Ticker(ticker_symbol)
        dataset = ticker.history(period=f"{x}y")
        
        st.markdown("### :blue[Historical Data:]")
        data = dataset.iloc[:, :5]  # Open, High, Low, Close, Volume columns usually first 5
        st.write(data)
        st.write(f"Data shape: {data.shape}")

        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown("### :blue[Stock Price (High & Low)]")
        st.line_chart(data[["High", "Low"]], use_container_width=True,color=["#CD5C5C","#00FFFF"])
        
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} Stock Price Open and Close]")
        st.bar_chart(data[["Open", "Close"]], use_container_width=True,color=["#CD5C5C","#00FFFF"])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} TOTAL SALE IN DOLLAR($) ]")
        st.line_chart(dataset["Volume"],y_label="SALE IN DOLLAR",color="#CD5C5C")
        dataset["change"]=dataset["Volume"].pct_change()
        
        st.markdown("### :blue[COMPANY GROWTH AND DOWNFALL IN PERCENTAGE]")

        st.line_chart(dataset["change"],y_label="IN PERCENTAGE",color="#00FFFF")
        st.markdown("### :blue[----------------------------------------------------------]")

        st.markdown("### :blue[MACHINR LEARNING ALGORITHM  RIDGE REGRESSION USE TO PREDICTION]")
        st.markdown("### :blue[                                                     ]")


        # MACHINE LAEARNING MODEL
        
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import Ridge

       # Drop missing values
        dataset.dropna(inplace=True)

       # Feature and target selection
        x = dataset[['Open', 'High', 'Low', 'Close', 'change']]
        y = dataset[['Volume']]

       # Split data into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

       # Linear Regression model training
        lg = Ridge()
        lg.fit(x_train, y_train)

       # Predict volume and convert to integer type
        dataset["predict"] = lg.predict(x).astype(int)

        # Display line chart in Streamlit
        st.line_chart(dataset[["Volume", "predict"]], use_container_width=True, color=["#00FFFF","#CD5C5C"])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.write(dataset[["Volume","predict"]])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[ {q} COMPANY  PER DAY SALE USING MACHINE LAEARING PREDICTION MODEL]")
        st.markdown(f"###### :orange[1-input variable is {q} company open stock ,close stock,day hight stock and low stock and day wise growth  ]")
        st.markdown(f"###### :orange[ 2- output is volumn means total sale in day]")
        st.markdown(f"### :blue[                                   ]")
        a= st.number_input("OPEN STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        b= st.number_input("CLOSE STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        c= st.number_input("HIGH STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        d= st.number_input("LOW STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        e = st.number_input("STOCK PRICE CHANGE",min_value=-100.0,max_value=100.0,value=0.5,step=0.1,format="%.2f")
        if st.success("submit") :
         v=lg.predict([[a,b,c,d,e]])
         s=int(v[0])
         f=f"{q} TOTAL DAY SALE IS :-  {s} $"
         st.info(f)
         st.subheader("TOTAL SALE IN RUPEES")
         p=s*81
         k=f"{q} TOTAL DAY SALE IS :-  {p} ₹"
         st.success(k)

        
        

elif q == "GOOGLE":
   st.markdown(f"# :blue[GOOGLE STOCK PRICE ANALYSIS]")
   x = st.number_input("Enter the number of years for analysis", min_value=1, max_value=30, value=1, step=1)
   if st.button("Submit"):
        ticker_symbol = "GOOGL"
        ticker = yf.Ticker(ticker_symbol)
        dataset = ticker.history(period=f"{x}y")
        
        st.markdown("### :blue[Historical Data:]")
        data = dataset.iloc[:, :5]  # Open, High, Low, Close, Volume columns usually first 5
        st.write(data)
        st.write(f"Data shape: {data.shape}")

        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown("### :blue[Stock Price (High & Low)]")
        st.line_chart(data[["High", "Low"]], use_container_width=True)
        
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### blue[{q} Stock Price Open and Close]")
        st.bar_chart(data[["Open", "Close"]], use_container_width=True)
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} TOTAL SALE IN DOLLAR($) ]")
        st.line_chart(dataset["Volume"],y_label="SALE IN DOLLAR",color="#00FFFF")
        dataset["change"]=dataset["Volume"].pct_change()
        
        st.markdown("### :blue[COMPANY GROWTH AND DOWNFALL IN PERCENTAGE]")

        st.line_chart(dataset["change"],y_label="IN PERCENTAGE",color="#00FFFF")
        st.markdown("### :blue[----------------------------------------------------------]")

        st.markdown("### :orange[MACHINR LEARNING ALGORITHM  LASSO REGRESSION USE TO PREDICTION]")
        st.markdown("### :blue[                                                     ]")


        # MACHINE LAEARNING MODEL
        
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import Lasso

       # Drop missing values
        dataset.dropna(inplace=True)

       # Feature and target selection
        x = dataset[['Open', 'High', 'Low', 'Close', 'change']]
        y = dataset[['Volume']]

       # Split data into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

       # Linear Regression model training
        lg = Lasso()
        lg.fit(x_train, y_train)

       # Predict volume and convert to integer type
        dataset["predict"] = lg.predict(x).astype(int)

        # Display line chart in Streamlit
        st.line_chart(dataset[["Volume", "predict"]], use_container_width=True, color=["#00FFFF","#CD5C5C"])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.write(dataset[["Volume","predict"]])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[ {q} COMPANY  PER DAY SALE  PREDICTION USING MACHINE LAEARING PREDICTION MODEL]")
        st.markdown(f"###### :orange[1-input variable is {q} company open stock ,close stock,day hight stock and low stock and day wise growth  ]")
        st.markdown(f"###### :orange[ 2- output is volumn means total sale in day]")
        st.markdown(f"## :blue[                                   ]")
        a= st.number_input("OPEN STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        b= st.number_input("CLOSE STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        c= st.number_input("HIGH STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        d= st.number_input("LOW STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        e = st.number_input("STOCK PRICE CHANGE",min_value=-100.0,max_value=100.0,value=0.5,step=0.1,format="%.2f")
        if st.success("submit") :
         v=lg.predict([[a,b,c,d,e]])
         s=int(v[0])
         f=f"{q} TOTAL DAY SALE IS :-  {s} $"
         st.info(f)
         st.subheader("TOTAL SALE IN RUPEES")
         p=s*81
         k=f"{q} TOTAL DAY SALE IS :-  {p} ₹"
         st.success(k)
       

        
        
elif q == "NETFLIX":
   st.markdown(f"# :blue[NETFLIX STOCK PRICE ANALYSIS]")
   x = st.number_input("Enter the number of years for analysis", min_value=1, max_value=30, value=1, step=1)
   if st.button("Submit"):
        ticker_symbol = "NFLX"
        ticker = yf.Ticker(ticker_symbol)
        dataset = ticker.history(period=f"{x}y")
        
        st.markdown("### :blue[Historical Data:]")
        data = dataset.iloc[:, :5]  # Open, High, Low, Close, Volume columns usually first 5
        st.write(data)
        st.write(f"Data shape: {data.shape}")

        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown("### :blue[Stock Price (High & Low)]")
        st.line_chart(data[["High", "Low"]], use_container_width=True)
        
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} Stock Price Open and Close]")
        st.bar_chart(data[["Open", "Close"]], use_container_width=True)
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} TOTAL SALE IN DOLLAR($) ]")
        st.line_chart(dataset["Volume"],y_label="SALE IN DOLLAR",color="#00FFFF")
        dataset["change"]=dataset["Volume"].pct_change()
        
        st.markdown("### :blue[COMPANY GROWTH AND DOWNFALL IN PERCENTAGE]")

        st.line_chart(dataset["change"],y_label="IN PERCENTAGE",color="#00FFFF")
        st.markdown("### :blue[----------------------------------------------------------]")

        st.markdown("### :blue[MACHINR LEARNING ALGORITHM  LINEAR REGRESSION USE TO PREDICTION]")
        st.markdown("### :blue[                                                     ]")


        # MACHINE LAEARNING MODEL
        
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression

       # Drop missing values
        dataset.dropna(inplace=True)

       # Feature and target selection
        x = dataset[['Open', 'High', 'Low', 'Close', 'change']]
        y = dataset[['Volume']]

       # Split data into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

       # Linear Regression model training
        lg = LinearRegression()
        lg.fit(x_train, y_train)

       # Predict volume and convert to integer type
        dataset["predict"] = lg.predict(x).astype(int)

        # Display line chart in Streamlit
        st.line_chart(dataset[["Volume", "predict"]], use_container_width=True, color=["#00FFFF","#CD5C5C"])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.write(dataset[["Volume","predict"]])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[ {q} COMPANY  PER DAY SALE USING MACHINE LAEARING PREDICTION MODEL]")
        st.markdown(f"###### :orange[1-input variable is {q} company open stock ,close stock,day hight stock and low stock and day wise growth  ]")
        st.markdown(f"###### :orange[ 2- output is volumn means total sale in day]")
        st.markdown(f"### :blue[                                   ]")
        a= st.number_input("OPEN STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        b= st.number_input("CLOSE STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        c= st.number_input("HIGH STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        d= st.number_input("LOW STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        e = st.number_input("STOCK PRICE CHANGE",min_value=-100.0,max_value=100.0,value=0.5,step=0.1,format="%.2f")
        if st.success("submit") :
         v=lg.predict([[a,b,c,d,e]])
         s=int(v[0])
         f=f"{q} TOTAL DAY SALE IS :-  {s} $"
         st.info(f)
         st.subheader("TOTAL SALE IN RUPEES")
         p=s*81
         k=f"{q} TOTAL DAY SALE IS :-  {p} ₹"
         st.success(k)

        
        
elif q == "AMAZON":
   st.markdown(f"# :blue[AMAZON STOCK PRICE ANALYSIS]")
   x = st.number_input("Enter the number of years for analysis", min_value=1, max_value=30, value=1, step=1)
   if st.button("Submit"):
        ticker_symbol = "AMZN"
        ticker = yf.Ticker(ticker_symbol)
        dataset = ticker.history(period=f"{x}y")
        
        st.markdown("### :blue[Historical Data:]")
        data = dataset.iloc[:, :5]  # Open, High, Low, Close, Volume columns usually first 5
        st.write(data)
        st.write(f"Data shape: {data.shape}")

        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown("### :blue[Stock Price (High & Low)]")
        st.line_chart(data[["High", "Low"]], use_container_width=True)
        
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} Stock Price Open and Close]")
        st.bar_chart(data[["Open", "Close"]], use_container_width=True)
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} TOTAL SALE IN DOLLAR($) ]")
        st.line_chart(dataset["Volume"],y_label="SALE IN DOLLAR",color="#00FFFF")
        dataset["change"]=dataset["Volume"].pct_change()
        
        st.markdown("### :blue[COMPANY GROWTH AND DOWNFALL IN PERCENTAGE]")

        st.line_chart(dataset["change"],y_label="IN PERCENTAGE",color="#00FFFF")
        st.markdown("### :blue[----------------------------------------------------------]")

        st.markdown("### :blue[MACHINR LEARNING ALGORITHM  LASSO REGRESSION USE TO PREDICTION]")
        st.markdown("### :blue[                                                     ]")


        # MACHINE LAEARNING MODEL
        
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import Lasso

       # Drop missing values
        dataset.dropna(inplace=True)

       # Feature and target selection
        x = dataset[['Open', 'High', 'Low', 'Close', 'change']]
        y = dataset[['Volume']]

       # Split data into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

       # Linear Regression model training
        lg = Lasso()
        lg.fit(x_train, y_train)

       # Predict volume and convert to integer type
        dataset["predict"] = lg.predict(x).astype(int)

        # Display line chart in Streamlit
        st.line_chart(dataset[["Volume", "predict"]], use_container_width=True, color=["#00FFFF","#CD5C5C"])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.write(dataset[["Volume","predict"]])
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"## :blue[ {q} COMPANY  PER DAY SALE USING MACHINE LAEARING PREDICTION MODEL]")
        st.markdown(f"###### :orange[1-input variable is {q} company open stock ,close stock,day hight stock and low stock and day wise growth  ]")
        st.markdown(f"###### :orange[ 2- output is volumn means total sale in day]")
        st.markdown(f"### :blue[                                   ]")
        a= st.number_input("OPEN STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        b= st.number_input("CLOSE STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        c= st.number_input("HIGH STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        d= st.number_input("LOW STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        e = st.number_input("STOCK PRICE CHANGE",min_value=-100.0,max_value=100.0,value=0.5,step=0.1,format="%.2f")
        if st.success("submit") :
         v=lg.predict([[a,b,c,d,e]])
         s=int(v[0])
         f=f"{q} TOTAL DAY SALE IS :-  {s} $"
         st.info(f)
         st.subheader("TOTAL SALE IN RUPEES")
         p=s*81
         k=f"{q} TOTAL DAY SALE IS :-  {p} ₹"
         st.success(k)


        
        
elif q == "FACEBOOK":
   st.markdown(f"# :blue[FACEBOOK STOCK PRICE ANALYSIS]")
   x = st.number_input("Enter the number of years for analysis", min_value=1, max_value=30, value=1, step=1)
   if st.button("Submit"):
        ticker_symbol = "META"
        ticker = yf.Ticker(ticker_symbol)
        dataset = ticker.history(period=f"{x}y")
        
        st.markdown("### :blue[Historical Data:]")
        data = dataset.iloc[:, :5]  # Open, High, Low, Close, Volume columns usually first 5
        st.write(data)
        st.write(f"Data shape: {data.shape}")

        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown("### :blue[Stock Price (High & Low)]")
        st.line_chart(data[["High", "Low"]], use_container_width=True)
        
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} Stock Price Open and Close]")
        st.bar_chart(data[["Open", "Close"]], use_container_width=True)
        st.markdown("### :blue[----------------------------------------------------------]")
        st.markdown(f"### :blue[{q} TOTAL SALE IN DOLLAR($) ]")
        st.line_chart(dataset["Volume"],y_label="SALE IN DOLLAR",color="#00FFFF")
        dataset["change"]=dataset["Volume"].pct_change()
        
        st.markdown("### :blue[COMPANY GROWTH AND DOWNFALL IN PERCENTAGE]")

        st.line_chart(dataset["change"],y_label="IN PERCENTAGE",color="#00FFFF")
        st.markdown("### :blue[----------------------------------------------------------]")

        st.markdown("### :orange[MACHINR LEARNING ALGORITHM  RIDGE REGRESSION USE TO PREDICTION]")
        st.markdown("### :blue[                                                     ]")


        # MACHINE LAEARNING MODEL
        
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import Ridge

       # Drop missing values
        dataset.dropna(inplace=True)

       # Feature and target selection
        x = dataset[['Open', 'High', 'Low', 'Close', 'change']]
        y = dataset[['Volume']]

       # Split data into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

       # Linear Regression model training
        lg = Ridge()
        lg.fit(x_train, y_train)

       # Predict volume and convert to integer type
        dataset["predict"] = lg.predict(x).astype(int)

        # Display line chart in Streamlit
        st.line_chart(dataset[["Volume", "predict"]], use_container_width=True, color=["#00FFFF","#CD5C5C"])
        st.markdown("## :blue[----------------------------------------------------------]")
        st.write(dataset[["Volume","predict"]])
        st.markdown("## :blue[----------------------------------------------------------]")
        st.markdown(f"## :blue[ {q} COMPANY  PER DAY SALE USING MACHINE LAEARING PREDICTION MODEL]")
        st.markdown(f"###### :orange[1-input variable is {q} company open stock ,close stock,day hight stock and low stock and day wise growth  ]")
        st.markdown(f"###### :orange[ 2- output is volumn means total sale in day]")
        st.markdown(f"## :blue[                                   ]")
        a= st.number_input("OPEN STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        b= st.number_input("CLOSE STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        c= st.number_input("HIGH STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        d= st.number_input("LOW STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        e = st.number_input("STOCK PRICE CHANGE",min_value=-100.0,max_value=100.0,value=0.5,step=0.1,format="%.2f")
        if st.success("submit") :
         v=lg.predict([[a,b,c,d,e]])
         s=int(v[0])
         f=f"{q} TOTAL DAY SALE IS :-  {s} $"
         st.info(f)
         st.subheader("TOTAL SALE IN RUPEES")
         p=s*81
         k=f"{q} TOTAL DAY SALE IS :-  {p} ₹"
         st.success(k)

        
        
elif q == "TESLA":
   st.markdown(f"# :blue[TESLA STOCK PRICE ANALYSIS]")
   x = st.number_input("Enter the number of years for analysis", min_value=1, max_value=30, value=1, step=1)
   if st.button("Submit"):
        ticker_symbol = "TSLA"
        ticker = yf.Ticker(ticker_symbol)
        dataset = ticker.history(period=f"{x}y")
        
        st.markdown("### :blue[Historical Data:]")
        data = dataset.iloc[:, :5]  # Open, High, Low, Close, Volume columns usually first 5
        st.write(data)
        st.write(f"Data shape: {data.shape}")

        st.markdown("## :blue[----------------------------------------------------------]")
        st.markdown("### :blue[Stock Price (High & Low)]")
        st.line_chart(data[["High", "Low"]], use_container_width=True)
        
        st.markdown("## :blue[----------------------------------------------------------]")
        st.markdown(f"## :blue[{q} Stock Price Open and Close]")
        st.bar_chart(data[["Open", "Close"]], use_container_width=True)
        st.markdown("## :blue[----------------------------------------------------------]")
        st.markdown(f"## :blue[{q} TOTAL SALE IN DOLLAR($) ]")
        st.line_chart(dataset["Volume"],y_label="SALE IN DOLLAR",color="#00FFFF")
        dataset["change"]=dataset["Volume"].pct_change()
        
        st.markdown("## :blue[COMPANY GROWTH AND DOWNFALL IN PERCENTAGE]")

        st.line_chart(dataset["change"],y_label="IN PERCENTAGE",color="#00FFFF")
        st.markdown("## :blue[----------------------------------------------------------]")

        st.markdown("## :blue[MACHINR LEARNING ALGORITHM  LASSO REGRESSION USE TO PREDICTION]")
        st.markdown("## :blue[                                                     ]")


        # MACHINE LAEARNING MODEL
        
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import Lasso

       # Drop missing values
        dataset.dropna(inplace=True)

       # Feature and target selection
        x = dataset[['Open', 'High', 'Low', 'Close', 'change']]
        y = dataset[['Volume']]

       # Split data into train and test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

       # Linear Regression model training
        lg = Lasso()
        lg.fit(x_train, y_train)

       # Predict volume and convert to integer type
        dataset["predict"] = lg.predict(x).astype(int)

        # Display line chart in Streamlit
        st.line_chart(dataset[["Volume", "predict"]], use_container_width=True, color=["#00FFFF","#CD5C5C"])
        st.markdown("## :blue[----------------------------------------------------------]")
        st.write(dataset[["Volume","predict"]])
        st.markdown("## :blue[----------------------------------------------------------]")
        st.markdown(f"## :blue[ {q} COMPANY  PER DAY SALE USING MACHINE LAEARING PREDICTION MODEL]")
        st.markdown(f"###### :orange[1-input variable is {q} company open stock ,close stock,day hight stock and low stock and day wise growth  ]")
        st.markdown(f"###### :orange[ 2- output is volumn means total sale in day]")
        st.markdown(f"## :blue[                                   ]")
        a= st.number_input("OPEN STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        b= st.number_input("CLOSE STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        c= st.number_input("HIGH STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        d= st.number_input("LOW STOCK PRICE", min_value=50, max_value=1000, value=200, step=1)
        e = st.number_input("STOCK PRICE CHANGE",min_value=-100.0,max_value=100.0,value=0.5,step=0.1,format="%.2f")
        if st.success("submit") :
         v=lg.predict([[a,b,c,d,e]])
         s=int(v[0])
         f=f"{q} TOTAL DAY SALE IS :-  {s} $"
         st.info(f)
         st.subheader("TOTAL SALE IN RUPEES")
         p=s*81
         k=f"{q} TOTAL DAY SALE IS :-  {p} ₹"
         st.success(k)
         


        
        

   
   
   
   
   