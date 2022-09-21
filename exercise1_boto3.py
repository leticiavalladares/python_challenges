import boto3
import json

## Exercise

# Write a boto3 script that prints out all VPC and subnets
# in your lab account
# Then for each resource found, attach new AWS tag
# "Project: Talent-Academy" where tag key "Project" and tag value 
# "Talent-Academy"

client = boto3.client('ec2')

response_vpc = client.describe_vpcs()
response_subnet = client.describe_subnets()

print("\nN° of vpcs: " + str(len(response_vpc["Vpcs"])))
print("--------------------------------------------------------------")
print("Name of vpc: " + str(response_vpc["Vpcs"][0]["Tags"][0]["Value"]))
print("--------------------------------------------------------------")
print("VPCs attributes: ")
print(json.dumps(response_vpc["Vpcs"], sort_keys=True, indent=4))
print("============================================================\n")
print("N° of subnets: " + str(len(response_subnet["Subnets"])))
print("-------------------------------------------------------------")
print("")

subnets = response_subnet["Subnets"]
i = 0
for subnet in subnets:
    for tag in subnet['Tags']:
        if tag['Key'] == 'Name':
            i += 1
            print(str(i) + ". " + str(tag['Value']) + ", id: " + str(subnet['SubnetId']))


print("============================================================\n")

i = 0
test_vpc = str(True if response_vpc["Vpcs"][0]["Tags"][0]["Key"] == 'Project' and response_vpc["Vpcs"][0]["Tags"][0]["Value"] == 'Talent-Academy' else False)

print("Does the tag Project: Talent-Academy exist in every resource?")

print("-------------------------------------------------------------")

test_vpc = str(True if response_vpc["Vpcs"][0]["Tags"][0]["Key"] == 'Project' and response_vpc["Vpcs"][0]["Tags"][0]["Value"] == 'Talent-Academy' else False)

print("VPC   " + str(response_vpc["Vpcs"][0]["VpcId"]) + ": " + test_vpc )
for subnet in subnets:
    for tag in subnet['Tags']:
        test = str(True if tag['Key'] == 'Project' and tag['Value'] == 'Talent-Academy' else False)
        if tag['Key'] == 'Project':
            i += 1
            print(str(i) + ". " + str(subnet['SubnetId']) + ": " + test)


""" response_tag = client.create_tags(
    Resources = [
        'vpc-0394**********', 'subnet-098087048********',
        'subnet-0b1d91b04*******', 'subnet-005d3b07e0*******',
        'subnet-0963ee175e*******', 'subnet-014dfee14*******',
        'subnet-0dd2bf6232*******',
    ],
    Tags= [
        {
        "Key": "Project",
        "Value": "Talent-Academy"
        },
    ],
)

print(response_tag) """
