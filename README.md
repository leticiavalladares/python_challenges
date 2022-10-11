# Python challenges

[![CodeQL](https://github.com/leticiavalladares/python_challenges/actions/workflows/codeql.yml/badge.svg)](https://github.com/leticiavalladares/python_challenges/actions/workflows/codeql.yml)

### Exercise 1: Unit conversion in lb or kg
### Exercise 2: Boto3, check vpc and subnets and then add tag 

Deniss' Solution

```python
import boto3

client = boto3.client("ec2")
new_tag = {"Key": "Project", "Value": "Talent-Academy"}

def get_resource_ids():
    response = client.describe_vpcs()
    vpc_ids = [vpc["VpcId"] for vpc in response["Vpcs"]]
    print(f"VPCs: {vpc_ids}")
    response = client.describe_subnets()
    subnet_ids = [subnet["SubnetId"] for subnet in response["Subnets"]]
    print(f"Subnets: {subnet_ids}")
    return vpc_ids + subnet_ids

def add_tag(resource_ids):
    print(f"Adding new tag for {len(resource_ids)} resources...")
    client.create_tags(Resources=resource_ids, Tags=[new_tag], DryRun=True)

ids = get_resource_ids()
if ids:
    add_tag(ids)
else:
    print("No resources found")
```
