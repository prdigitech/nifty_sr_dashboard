📊 Automated Support & Resistance Detection System

A real-time financial analysis tool that **automatically detects support and resistance levels** for stocks. Built with **Streamlit**, **Yahoo Finance API**, and **Plotly**, this dashboard provides **candlestick charts** with detected **support & resistance lines**, helping traders make better decisions.

 

---

## **📌 Features**
✅ **Automated Support & Resistance Detection** using historical stock data  
✅ **Candlestick Chart Visualization** similar to TradingView  
✅ **Stock Selection** (Default: Nifty 50, but customizable)  
✅ **Data Table** displaying the latest 30-day stock history  
✅ **Interactive & Responsive UI** built with Streamlit  
✅ **Dark Mode Visualization** for easy analysis  

---

## **📂 Project Structure**
```
nifty_sr_dashboard/
│── venv/                    # Virtual environment (not included in repo)
│── app.py                    # Main Streamlit app
│── requirements.txt          # Dependencies file
│── README.md                 # Project documentation

```

---

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/prdigitech/nifty_sr_dashboard.git
cd nifty_sr_dashboard
```

### **2️⃣ Create a Virtual Environment (Windows)**
```sh
python -m venv venv
venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
OR install manually:
```sh
pip install streamlit yfinance plotly numpy pandas
```

### **4️⃣ Run the Streamlit App**
```sh
streamlit run app.py
```
📌 The app will open automatically in your browser at **http://localhost:8501/**

---

## **📜 How It Works**
1. **Select a Stock**  
   - Enter a stock ticker (e.g., `^NSEI` for **Nifty 50**)  
   - Uses **Yahoo Finance API** to fetch the last **60 days** of historical data  

2. **Candlestick Chart with Support & Resistance**  
   - **Support levels** (Green Dashed Line)  
   - **Resistance levels** (Red Dashed Line)  
   - Detected using **local minima & maxima** in price movement  

3. **Live Data Table**  
   - Displays **latest 30-day stock data** including **Open, High, Low, Close, and Volume**  

---

## **📊 Support & Resistance Algorithm**
### **🔍 How Support Levels are Identified**
- A price is considered **support** if it is **lower** than its previous and next price points.  
- The system **filters out noise** by ensuring levels are **not too close** to each other.  

### **🔍 How Resistance Levels are Identified**
- A price is considered **resistance** if it is **higher** than its previous and next price points.  
- The algorithm ensures **strong resistance levels** are clearly visible.  

### **📌 Example**
| Date       | Open   | High   | Low    | Close  |
|------------|--------|--------|--------|--------|
| 2024-02-01 | 21700  | 21950  | 21650  | 21800  |
| 2024-02-02 | 21810  | 22100  | 21780  | 22050  |
| 2024-02-03 | 22060  | 22400  | 21900  | 22300  |

If `21900` is the **lowest** price among surrounding days, it's marked as **Support**.  
If `22400` is the **highest** price among surrounding days, it's marked as **Resistance**.  

---

## **📌 Example Output**
![Support & Resistance Chart](https://your-chart-url.com) *(Optional: Add a sample chart image)*  

---

## **⚙️ Technologies Used**
- **Streamlit** → Interactive web app framework  
- **Yahoo Finance API** → Fetching real-time stock data  
- **Plotly** → Creating beautiful candlestick charts  
- **NumPy & Pandas** → Data manipulation & analysis  

---

## **📢 Next Steps**
🔹 **Add more indicators** (RSI, MACD, Bollinger Bands)  
🔹 **Enable multi-timeframe analysis** (Intraday, Daily, Weekly)  
🔹 **Live market updates** using WebSockets  

---

## **📜 License**
This project is **open-source** under the **MIT License**.  

📌 **Feel free to contribute!** 🚀  

---

## **👨‍💻 Author**
👤 **Pratik Ramdasi**  
📧 Email: 
🔗 GitHub: [prdigitech](https://github.com/prdigitech)  
