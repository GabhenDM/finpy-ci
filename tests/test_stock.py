import json


def test_price(client):
    res = client.get('/stocks/price/AAPL')
    assert res.status_code == 200

def test_profile(client):
    res = client.get('/stocks/profile/AAPL')
    assert res.status_code == 200
    assert 'AAPL' == json.loads(res.get_data(as_text=True))['ticker']
    assert 'Apple Inc' == json.loads(res.get_data(as_text=True))['name']