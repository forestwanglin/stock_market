import http.client
import time


def get_data(url, data = None):

    headers = {
        'Cookie': "xq_a_token=9c75d6bfbd0112c72b385fd95305e36563da53fb; xq_a_token.sig=-6-bcHntQlhRjsyrvsY2IGwh-B4; xq_r_token=9ad364aac7522791166c59720025e1f8f11bf9eb; xq_r_token.sig=usx1_hrblByw-9h0cXk1yLIUlL4; u=321537085819834; Hm_lvt_1db88642e346389874251b5a1eded6e3=1537085820; _ga=GA1.2.1936212577.1537085820; _gid=GA1.2.1872475394.1537085820; device_id=36d2ef5cafd4ba1153dc2b8b63314bd6; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1537085885",
        'Cache-Control': "no-cache",
        'Postman-Token': "89360678-2b49-495c-ae37-161ed2ce4f39"
    }

    conn = http.client.HTTPConnection("stock.xueqiu.com")
    conn.request("GET",
                 url,
                 headers = headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def crawl_stock(symbol):
    day = 365
    today = time.time().no
    url = 'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=' \
          + symbol \
          + '&begin=' \
          + today \
          + '&period=day&type=before&count=-' \
          + day \
          + '&indicator=kline,ma,macd,kdj,boll,rsi,wr,bias,cci,psy'
    data = get_data(url)
    print(data)

def write_data(data, name):
    file_name = name
 #   with open(file_name, 'a', errors='ignore', newline='') as f:
            #f_csv = csv.writer(f)
            #f_csv.writerows(data)


if __name__ == '__main__':
    crawl_stock('SH601318')
