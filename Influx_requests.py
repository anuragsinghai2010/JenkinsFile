import requests


response = requests.get("http://localhost:8086/query?db=example&q=select * from cpu_load_short where time>="+sttime+" and "time<= "+endtime+")
print(response.text)
