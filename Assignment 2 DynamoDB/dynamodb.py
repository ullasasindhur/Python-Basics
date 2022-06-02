from urllib import response
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Music')


def create_table():
    try:
        table = dynamodb.create_table(
            TableName="Music",
            KeySchema=[
                {
                    'AttributeName': "Artist",
                    'KeyType': "HASH"
                },
                {
                    'AttributeName': 'SongTitle',
                    'KeyType': "RANGE"
                }
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "Artist",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "SongTitle",
                    "AttributeType": "S"
                }
            ],
            BillingMode="PROVISIONED",
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5
            },
            Tags=[
                {
                    'Key': 'emp_id',
                    'Value': 'GS-3103'
                },
                {
                    'Key': 'project_manager',
                    'Value': 'Pankaj Khamkar',
                },
                {
                    'Key': 'duration',
                    'Value': '31-May-2022',
                },
                {
                    'Key': 'purpose',
                    'Value': 'testing'
                }
            ]
        )
    except Exception:
        return "Cannot create table, may be it already present"
    else:
        table.wait_until_exists()
    return table


def add_song(artist, songTitle):
    try:
        output = table.put_item(
            Item={
                'Artist': artist,
                'SongTitle': songTitle
            }
        )
    except Exception as e:
        return "Error Occured in add song"
    return output


def query_table(artist):
    return table.query(
        KeyConditionExpression=Key('Artist').eq(artist),
    )


def query_artist(artist):
    try:
        response = query_table(artist)
        items = response['Items']
        if len(items):
            return sorted(items, key=lambda item: item['SongTitle'], reverse=True)
        else:
            return "Nothing Found with the Artist Name"
    except Exception as e:
        return "Error Occured in query artist"


def delete_table():
    try:
        table.delete()
    except Exception:
        return "Error Occured in delete artist"
    return "Successfully Deleted the Table"


if __name__ == "__main__":
    print(create_table())
    songTitle = input('Enter song title:\t')
    artistName = input('Enter artist name:\t')
    print(add_song(artistName, songTitle))
    artistSearch = input('Enter artist name for searching:\t')
    print(query_artist(artistSearch))
    # add_song('Sid Sriram', 'A')
    # add_song('Sid Sriram', 'B')
    # add_song('Sid Sriram', 'C')
    # add_song('Sid Sriram', 'D')
    # add_song('Sid Sriram', 'a')
    # add_song('Sid Sriram', 'b')
    # add_song('Sid Sriram', 'c')
    # add_song('P', 'd')
    # add_song('A', 'e')
    # add_song('B', 'F')
    # add_song('BA', 'Nuvv')
    # add_song('BD', 'Nuvvun')
    # add_song('Bp', 'Nu')
    # add_song('S', 'Nuvvunt')
    # add_song('Sam', 'N')
    # add_song('Ram', 'Np')
    # print(query_artist('Sid Sriram'))
    print(delete_table())
