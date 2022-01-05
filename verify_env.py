import subprocess
import json


cluster = "zonal-commits-perf"


# cluster_prop = subprocess.getoutput('gcloud container clusters get-credentials ' + cluster + ' --zone us-central1-a --project saas-non-prod-infra-220605')
# if "kubeconfig entry generated for "+cluster in cluster_prop:
#     print("Succesfully Fetched Cluster properties for cluster", cluster)
# else:
#     print("Please check the command")
#
# output = subprocess.getoutput('kubectl scale statefulsets influxdb --namespace commits-perf --replicas=0')
# print (output)
#
# if "scaled" in output:
#     print("Great")
# else:
#     print("There is some issue")

counter = 0

output = subprocess.getoutput("kubectl get pods -n monitoring -o=json")
json_obj = json.loads(output)

for i in range(len(json_obj["items"])):

    pod_name = json_obj["items"][i]['metadata']['name']
    state = (json_obj["items"][i]['status']['containerStatuses'][0]['state'])
    if 'running' in state.keys():
        #print("Pod "+pod_name+" is in running state")
    else:
        issue = json.dumps(state)
        #print("Pod "+pod_name+" have issues "+issue)
        counter = counter +1
print(counter)
