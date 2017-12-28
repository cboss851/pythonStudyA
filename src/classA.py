class Order:
    orderNo = ""
    def getOrderNo(self):
      return self.orderNo
    def setOrderNo(self,orderTemp):
        self.orderNo = orderTemp

orderA = Order();
print(orderA.getOrderNo())
orderA.setOrderNo("201739418234203")
print(orderA.getOrderNo())
print(orderA.orderNo)


