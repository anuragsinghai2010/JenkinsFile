import argparse

from influxdb import InfluxDBClient
### This is to read influxdb

def main(host, port,sttime,endtime):
    """Instantiate a connection to the InfluxDB."""
    print("this is sttime variable")
    
    user = 'root'
    password = 'root'
    dbname = 'example'
    dbuser = 'smly'
    dbuser_password = 'my_secret_password'
    query = 'select Float_value from cpu_load_short where time>='+sttime+ ' and time<='+endtime;
    query_where = 'select Int_value from cpu_load_short where host=$host;'
    bind_params = {'host': 'server01'}
    client = InfluxDBClient(host, port, user, password, dbname)


    print("Switch user: " + dbuser)
    client.switch_user(dbuser, dbuser_password)


    print("Querying data: " + query)
    result = client.query(query)

    print("Result: {0}".format(result))

    print("Querying data: " + query_where)
    result1 = client.query(query_where, bind_params=bind_params)

    print("Result1: {0}".format(result1))


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=True,

                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=True,
                        help='port of InfluxDB http API')
    parser.add_argument('--sttime', type=str, required=True,
                        help='port of InfluxDB http API')
    parser.add_argument('--endtime', type=str, required=True,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port, sttime=args.sttime,  endtime=args.endtime)
