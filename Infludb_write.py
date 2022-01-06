import argparse

from influxdb import InfluxDBClient
import datetime
import time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d'+"T"+'%H:%M:%S'+"Z")
print(st)


def main(host, port):
    """Instantiate a connection to the InfluxDB."""
    user = 'root'
    password = 'root1234'
    dbname = 'local_monitoring1'
    dbuser = 'smly'
    dbuser_password = 'my_secret_password'
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": st,
            "fields": {
                "Float_value": 0.90,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    client = InfluxDBClient(host, port, user, password, dbname)

   # print("Create database: " + dbname)
   # client.create_database(dbname1)

  #  print("Create a retention policy")
  #  client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    print("Switch user: " + dbuser)
    client.switch_user(dbuser, dbuser_password)

    print("Write points: {0}".format(json_body))
    client.write_points(json_body)



def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=True,

                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=True,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
