import boto3
from boto3.dynamodb.conditions import Attr

from config import *


class DynamoDB(object):
    client = boto3.client(
        "dynamodb",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION,
    )

    resource = boto3.resource(
        "dynamodb",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION,
    )

    def __init__(self):
        super().__init__()

    def create_table(self, name, pk, pk_type, read_cap_units, write_cap_units):
        """Create table"""
        table = self.resource.create_table(
            TableName=name,
            KeySchema=[{"AttributeName": pk, "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": pk, "AttributeType": pk_type}],
            ProvisionedThroughput={
                "ReadCapacityUnits": read_cap_units,
                "WriteCapacityUnits": write_cap_units,
            },
        )
        return table

    def list_tables(self):
        """List all tables"""
        return list(self.resource.tables.all())

    def create_item(self, table, item: dict):
        """Create an item"""
        tbl = self.resource.Table(table)
        return tbl.put_item(Item=item)

    def create_multiple_items(self, table, items_arr: list):
        """Add multiple items to a table"""
        tbl = self.resource.Table(table)
        with tbl.batch_writer() as batch:
            for item in items_arr:
                batch.put_item(Item=item)

    def read_item(self, table, key: dict):
        """Read single item from table"""
        tbl = self.resource.Table(table)
        return tbl.get_item(Key=key)["Item"]

    def read_all_items(self, table):
        """Read all items from table"""
        tbl = self.resource.Table(table)
        return tbl.scan()["Items"]

    def delete_item(self, table, key):
        """Delete single item from table"""
        tbl = self.resource.Table(table)
        return tbl.delete_item(Key=key)

    def update_item(
        self,
        table,
        Key,
        ExpressionAttributeNames,
        ExpressionAttributeValues,
        UpdateExpression,
        **kwargs
    ):
        """Update item in table"""
        return self.client.update_item(
            TableName=table,
            Key=Key,
            ExpressionAttributeNames=ExpressionAttributeNames,
            ExpressionAttributeValues=ExpressionAttributeValues,
            UpdateExpression=UpdateExpression,
            **kwargs
        )

    def filter_items(self, table, filter_expression):
        """Returns from table the items that matches the filter expression"""
        tbl = self.resource.Table(table)
        return tbl.scan(FilterExpression=filter_expression)["Items"]


def main():
    table_name = TABLE_NAME
    db = DynamoDB()

    # db.create_table(table_name, "id", "N", 1, 1)  # uncomment to create table

    print("List of all tables: ", end="\t")
    print(db.list_tables())

    db.create_item(table_name, {"id": 2, "name": "suraj"})
    db.create_item(table_name, {"id": 4, "name": "ram"})
    db.create_item(table_name, {"id": 3, "name": "hari"})
    db.create_item(table_name, {"id": 5, "name": "shyam", "phone": 12})

    db.create_multiple_items(table_name, [{"id": 10, "name": "joey"}, {"id": 11, "name": "jane"}])

    print(db.read_item(table_name, key={"id": 4}))

    print(db.filter_items(table_name, filter_expression=Attr("name").eq("suraj")))
    print(db.filter_items(table_name, filter_expression=Attr("id").eq(2)))
    print(db.filter_items(table_name, filter_expression=Attr("id").gte(3)))
    print(db.filter_items(table_name, filter_expression=Attr("id").between(2, 4)))
    print(db.filter_items(table_name, filter_expression=Attr("name").begins_with("s")))
    print(
        db.filter_items(
            table_name, filter_expression=Attr("id").gte(5) & Attr("name").is_in(["ram", "shyam"])
        )
    )
    print(db.filter_items(table_name, filter_expression=Attr("phone").exists()))

    print(db.read_all_items(table_name))

    db.update_item(
        table_name,
        Key={"id": {"N": "2"}},
        ExpressionAttributeNames={"#add": "address", "#n": "name"},
        UpdateExpression="set #add=:city, #n=:fname",
        ExpressionAttributeValues={":city": {"S": "kathmandu"}, ":fname": {"S": "jim"}},
    )

    db.delete_item(table_name, key={"id": 3})


if __name__ == "__main__":
    main()
