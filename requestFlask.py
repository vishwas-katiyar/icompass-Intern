import requests
import json , requests , pytest
url='http://127.0.0.1:5000/v1/sanitized/input/'

def do_req(payload):
    return requests.post(url,payload)
    
   
def test_post_req_1():
    test_payload={"input":'/*'}  
    response=do_req(test_payload)
    assert response.status_code==200
    assert response.json()['Message']=='unsanitized'

def test_post_req_2():
    test_payload={"input":'sample'}  
    response=do_req(test_payload)
    assert response.status_code==200
    assert response.json()['Message']=='sanitized'


def test_post_req_3():
    test_payload={"input":'-- sample'} 
    response=do_req(test_payload)
    assert response.status_code==200
    assert response.json()['Message']=='unsanitized'

def test_post_req_4():
    test_payload={"input":'-- sample'} 
    response=do_req(test_payload)
    assert response.status_code==200
    assert response.json()['Message']=='unsanitized'


# ########## Request method ###############
def test_post_req_5():
    test_payload={"input":'-- sample'} 
    # response=do_req(test_payload)
    response=requests.get(url)
    assert response.status_code==404
    assert response.json()['Message']=='Not Post Method'
