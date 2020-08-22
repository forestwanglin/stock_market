import http.client

conn = http.client.HTTPConnection("stock.xueqiu.com")

headers = {
    'Cookie': "xq_a_token=9c75d6bfbd0112c72b385fd95305e36563da53fb; xq_a_token.sig=-6-bcHntQlhRjsyrvsY2IGwh-B4; xq_r_token=9ad364aac7522791166c59720025e1f8f11bf9eb; xq_r_token.sig=usx1_hrblByw-9h0cXk1yLIUlL4; u=321537085819834; Hm_lvt_1db88642e346389874251b5a1eded6e3=1537085820; _ga=GA1.2.1936212577.1537085820; _gid=GA1.2.1872475394.1537085820; device_id=36d2ef5cafd4ba1153dc2b8b63314bd6; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1537085885",
    'Cache-Control': "no-cache",
    'Postman-Token': "89360678-2b49-495c-ae37-161ed2ce4f39"
    }

conn.request("GET", "https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH601318&begin=1537086492245&period=day&type=before&count=-142&indicator=kline,ma,macd,kdj,boll,rsi,wr,bias,cci,psy", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))