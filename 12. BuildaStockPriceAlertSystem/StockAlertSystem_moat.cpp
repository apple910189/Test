class AlertData{
    int userId;
    int price;
    public:
    AlertData(int userId, int price){
        this->userId = userId;
        this->price = price;
    }
    bool operator<(AlertData data){
      return price<data.price; 
    }
    bool operator>(AlertData data){
      return price>data.price; 
    }
    int getPrice() const { 
      return price; 
    }
    int getUserId() const { 
      return userId; 
    }
};
class StockData{
    string timeStamp;
    string ticker;
    int price;
    
};
class StockAlertSystem{
    unordered_map<string,priority_queue<AlertData> > tickersAlertStream;
    unordered_map<string,priority_queue<AlertData,vector<AlertData>,greater<AlertData> > > alertedDatas;
    public:
    void init(){
        tickersAlertStream.clear();
    } 
    void setAlert(int userId, string ticker, int price){
               tickersAlertStream[ticker].push(AlertData(userId, price));
    }
    void updateTickerPrice(StockData stockData){
        auto &tickerPriorityQueue = tickersAlertStream[stockData.getTicker()];
        while(!tickerPriorityQueue.empty() && tickerPriorityQueue.top().getPrice() <= stockData.getPrice()){
            AlertData alertData = tickerPriorityQueue.top();
            sendAlert(alertData.getUserId(), stockData);
            tickerPriorityQueue.pop();
            alertedDatas[stockData.getTicker()].push(alertData);
        }
        auto &alertDataPriorityQueue = alertedDatas[stockData.getTicker()];
        while(!alertDataPriorityQueue.empty() && alertDataPriorityQueue.top().getPrice() > stockData.getPrice()){
            AlertData alertData = alertDataPriorityQueue.top();
            tickerPriorityQueue.push(alertData);
            alertDataPriorityQueue.pop();
        }
    } 
};