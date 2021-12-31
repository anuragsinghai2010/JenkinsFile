import requests
sys.path.append(os.environ['WORKSPACE'])

response = requests.get("http://localhost:8086/query?db=example&q=select * from cpu_load_short where time>= 1640991590000000000 and time<=1640991670000000000")
print(response.text)
