import requests
import json
import pytest
import datetime


def test_gateway_api_status_200():
    response = requests.get("https://omrest.charter.orbiwise.com/omc/gateways/geo", auth=('charter_admin', 'Charter123@'))
    global response_body
    response_body = response.json()
    assert response.status_code == 200

def test_gateway_online():
    for gateway in response_body:  # All gateways in json

        if gateway['uuid'] in gateways_all:
            status_value = gateway['alarmCounters']
            # print(status_value)
            data_for_file = gateway['uuid'] + ' => ' + status_value['omServerConnStatus']
            write_to_file(data_for_file)
            assert status_value['omServerConnStatus'] == 'CONNECTED'

    print(len(response_body))

@pytest.mark.skip()
def test_mega_online(): #Mega gateway located on castle rock
    for gateway in response_body:
        if gateway['uuid'] == r'647fdafffe005bfc':
            status_value = gateway['alarmCounters']
            # print(status_value)
            data_for_file = gateway['uuid'] + ' => ' + status_value['omServerConnStatus']
            write_to_file(data_for_file)
            assert status_value['omServerConnStatus'] == 'CONNECTED'

@pytest.mark.office
def test_browan_online(): #Browan gateway located in various floors
    for gateway in response_body:
        if gateway['uuid'] in gateways_office:
            status_value = gateway['alarmCounters']
            # print(status_value)
            data_for_file = gateway['uuid'] + ' => ' + status_value['omServerConnStatus']
            write_to_file(data_for_file)
            assert status_value['omServerConnStatus'] == 'CONNECTED'

def write_to_file(data_str):
    with open('C:/Users/MJK/PycharmProjects/WiFi_List/gateway_status.txt', 'a') as fp:
        fp.write(str(datetime.datetime.now())+'\t')
        fp.write(data_str)
        fp.write('\n')

gateways_all = ['647fdafffe00b50f', '80029cfffe61b7e2', '80029cfffe61b722']#, '647fdafffe005bfc']
gateways_office = ['80029cfffe61b57b', '80029cfffe61b7ac']
if __name__=="__main__":

    r = test_gateway_api_status_200()
    r1 = test_gateway_online()
