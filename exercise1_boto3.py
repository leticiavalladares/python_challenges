import boto3
import json
from rich import print

## Exercise

# Write a boto3 script that prints out all VPC and subnets
# in your lab account
# Then for each resource found, attach new AWS tag
# "Project: Talent-Academy" where tag key "Project" and tag value 
# "Talent-Academy"

client = boto3.client('ec2')

response_vpc = client.describe_vpcs()
response_subnet = client.describe_subnets()

vpc_qty = len(response_vpc['Vpcs'])
vpc_name = response_vpc['Vpcs'][0]['Tags'][0]['Value']
subnet_qty = len(response_subnet['Subnets'])

print(f"\nN° of vpcs: {vpc_qty}")
print("--------------------------------------------------------------")
print(f"Name of vpc: {vpc_name}")
print("--------------------------------------------------------------")
print("VPCs attributes: ")
print(json.dumps(response_vpc['Vpcs'], sort_keys=True, indent=4))
print("============================================================\n")
print(f"N° of subnets: {subnet_qty}")
print("-------------------------------------------------------------\n")


subnets = response_subnet['Subnets']
i = 0
for subnet in subnets:
    for tag in subnet['Tags']:
        if tag['Key'] == 'Name':
            i += 1

            print(f"{i}. {tag['Value']}, id: {subnet['SubnetId']}")


print("============================================================\n")

i = 0
test_vpc = True if response_vpc['Vpcs'][0]['Tags'][0]['Key'] == 'Project' and response_vpc['Vpcs'][0]['Tags'][0]['Value'] == 'Talent-Academy' else False

print("Does the tag Project: Talent-Academy exist in every resource?")

print("-------------------------------------------------------------")

print(f"VPC   {response_vpc['Vpcs'][0]['VpcId']}: {test_vpc}" )
for subnet in subnets:
    for tag in subnet['Tags']:
        test = True if tag['Key'] == 'Project' and tag['Value'] == 'Talent-Academy' else False
        if tag['Key'] == 'Project':
            i += 1
            print(f"{i}. {subnet['SubnetId']}: {test}")

print("-------------------------------------------------------------")


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
