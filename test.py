import http.client
conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
headers = {
'x-rapidapi-key': "894bd0a94dmsh425f2518955eb22p11d6ffjsne26fb73cf88b",
'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
}
conn.request("GET", "/v2/coachs/coach/18", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
