import heapq
from collections import defaultdict

class AlertData:
    def __init__(self, user_id: int, price: int):
        self.user_id = user_id
        self.price = price

    def __lt__(self, other):  # for min-heap
        return self.price < other.price

    def __repr__(self):
        return f"AlertData(user={self.user_id}, price={self.price})"


class StockAlertSystem:
    def __init__(self):
        # 未觸發的 alerts：min-heap（最便宜的閾值先觸發）
        self.alerts = defaultdict(list)
        # 已觸發的 alerts：max-heap（最高閾值優先還原）
        self.triggered = defaultdict(list)

    def setAlert(self, user_id: int, ticker: str, price: int):
        """設定警報閾值"""
        heapq.heappush(self.alerts[ticker], AlertData(user_id, price))

    def sendAlert(self, user_id: int, ticker: str, price: int):
        """模擬發送警報"""
        print(f"🚨 Alert! User {user_id}'s {ticker} reached price {price}")

    def updatePrice(self, ticker: str, price: int):
        """更新股票價格"""
        alerts_heap = self.alerts[ticker]
        triggered_heap = self.triggered[ticker]

        # 價格上漲 → 觸發警報
        while alerts_heap and alerts_heap[0].price <= price:
            alert = heapq.heappop(alerts_heap)
            self.sendAlert(alert.user_id, ticker, price)
            heapq.heappush(triggered_heap, (-alert.price, alert))  # max-heap by -price

        # 價格下跌 → 還原警報
        while triggered_heap and -triggered_heap[0][0] > price:
            _, alert = heapq.heappop(triggered_heap)
            heapq.heappush(alerts_heap, alert)


# ======= 測試範例 =======
system = StockAlertSystem()

system.setAlert(1, "AAPL", 150)
system.setAlert(2, "AAPL", 155)
system.setAlert(3, "AAPL", 160)

print("\n--- 股票價格上漲 ---")
system.updatePrice("AAPL", 152)  # 應觸發 user 1
system.updatePrice("AAPL", 158)  # 應觸發 user 2
system.updatePrice("AAPL", 162)  # 應觸發 user 3

print("\n--- 股票價格下跌 ---")
system.updatePrice("AAPL", 154)  # 應還原 user 2, 3
system.updatePrice("AAPL", 149)  # 應還原全部 (1, 2, 3)

print("\n--- 再次上漲 ---")
system.updatePrice("AAPL", 161)  # 再次觸發全部
