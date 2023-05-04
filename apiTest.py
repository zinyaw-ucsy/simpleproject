import requests
import json
# Replace YOUR_API_KEY with your actual API key from AbuseIPDB
API_KEY = 'ab994408de8ea406ceeb3d3202b8d931777b3e49a9dfec7c63c03b922a03b1799d6537d7e7a5e96f'
# Prompt the user for the IP address they want to query
#IP_ADDRESS = input("Enter the IP address : ")
IP_ADDRESS = "107.170.235.12"
url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={IP_ADDRESS}&maxAgeInDays=90'
headers = {
    'Key': API_KEY,
    'Accept': 'application/json'
}
response = requests.request(method='GET',url=url, headers=headers )
print(response.json())
if response.status_code == 200:
    #data = response.json()
    data = json.loads(response.text)
    print(data)
    print(json.dumps(data, sort_keys=True, indent=4))
    if data['data']['abuseConfidenceScore'] > 0:
        print(f"IP address {IP_ADDRESS} has been reported {data['data']['totalReports']} times with an abuse confidence score of {data['data']['abuseConfidenceScore']} and Country Name is {data['data']['countryCode']} with {data['data']['isp']}")
        if 'reports' in data['data']:
            for report in data['data']['reports']:
                print(f"Reported on {report['reportedAt']} by {report['reporter']} with a confidence score of {report['abuseConfidenceScore']} and a category of {report['category']}.")
    else:
        print(f"No abuse reports found for IP address {IP_ADDRESS}.")
else:
    print(f"Error {response.status_code}: {response.text}")







