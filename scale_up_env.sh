echo "welcome to my first shell script"
start=`date +%s`
echo "current time is ${start}"
STATUS=`gcloud compute instances describe --project "saas-non-prod-infra-220605" --zone "us-central1-a" "petco-perftest-cassandra-01" | grep status | tr -s ' ' | awk '{print $2}'`

echo $STATUS
