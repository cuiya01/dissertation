##################################################
#  @Author: Ya Cui
#  @Date: 17/08/2022
#  @Description: Calculate mean of RSSI and SNR
##################################################
import json
import pandas as pd


def get_data_from_json(filename):
    # get all data from json file
    with open(filename, 'r', encoding='utf-8') as file:
        json_file = json.load(file)

    # only extract data from receiving signal, get payload, rssi and snr
    list_addr = []
    list_rssi = []
    list_snr = []

    for i in json_file:
        if i.get("name") == 'as.up.data.forward':
            print('time:', q)
            print(i.get("data").get("uplink_message").get("frm_payload"))
            for j in i.get("data").get("uplink_message").get("rx_metadata"):
                list_addr.append(i.get("data").get("uplink_message").get("frm_payload"))
                list_rssi.append(j["rssi"])
                print(j["rssi"])
                print('\n')
                if 'snr' in j.keys():
                    list_snr.append(j["snr"])
                else:
                    list_snr.append(None)

    return list_addr, list_rssi, list_snr


address, rssi, snr = get_data_from_json('1214_live_data_1660684606787.json')
print(address)
print(rssi)
print(snr)

# write data into excel
combination = {'Payload':address, 'rssi': rssi, 'snr': snr}
df = pd.DataFrame(combination)
print(df)
df.to_excel('data.xlsx', sheet_name='Sheet1', index=False)
