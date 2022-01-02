import argparse
import json
import os

import requests

def main(host, port, sttime, endtime):
    path = "try.json"
    try:
        if os.path.exists(path):
            json_file = open(path, mode='r')
            json_obj = json.load(json_file)
            print(json_obj['query'])
            query_array = json_obj['query']
        else:
            print("This files does not exists")
    except Exception as e:
        print(e)

    for query in query_array:
        response = requests.get("http://"+host+":"+port+"/query?db=example&q=" + query + " where time>="+sttime+" and time<="+endtime+"")
        map = response.json()
        #print(map)
        fin_list = []
        try:
            list1 = map['results'][0]['series'][0]['values']
            for elem in range(len(list1)):
                fin_list.append(list1[elem][1])
        except:
            print("Please check the result output")

        print(max(fin_list))

def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=True,

                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=str, required=True,
                        help='port of InfluxDB http API')
    parser.add_argument('--sttime', type=str, required=True,
                        help='port of InfluxDB http API')
    parser.add_argument('--endtime', type=str, required=True,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port, sttime=args.sttime,  endtime=args.endtime)
