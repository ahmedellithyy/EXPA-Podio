from pypodio2 import api

podio_client_id = 'ecb-egypt'
podio_client_secret = 'Htul5Z5AgfKKu6HsV0fGaNp4XakwOSyIwFgkPs92t2GrpslZfN1iTYZr1kBdgBD1'
podio_login_id = 'adel.mohamed@aiesec.net'
podio_login_pw = 'MCEgypt2020!'
podio = api.OAuthClient(podio_client_id, podio_client_secret, podio_login_id, podio_login_pw)


def podioUpdateAPDs(data, appID):
    if len(data) != 0:
        for i in range(len(data)):
            form_item = {
                "fields": [
                    {"external_id": "title", "values": [{"value": data[i][0]}]},
                    {"external_id": "ep-name", "values": [{"value": data[i][1]}]},
                    {"external_id": "ep-profile-link", "values": [{"url": data[i][2]}]},
                    {"external_id": "email", "values": [{"value": data[i][3]}]},
                    {"external_id": "product-4", "values": [{"value": data[i][4]}]},
                    {"external_id": "sending-lc", "values": [{"value": data[i][5]}]},
                    {"external_id": "sending-mc", "values": [{"value": data[i][6]}]},
                    {"external_id": "hosting-lc", "values": [{"value": data[i][7]}]},
                    {"external_id": "hosting-mc", "values": [{"value": data[i][8]}]},
                    {"external_id": "opportunity-link", "values": [{"url": data[i][9]}]},
                    {"external_id": "approval-date", "values": [{"start": data[i][10] + " 00:00:00"}]},
                    {"external_id": "opp-earliest-start-latest-end-date", "values": [{"start": data[i][11] + " 00:00:00"}]},
                    {"external_id": "opp-latest-end-date", "values": [{"start": data[i][12] + " 00:00:00"}]},
                ]
            }
            podio.Item.create(appID, form_item)


def podioUpdateREs(data, appID):
    if len(data) != 0:
        for i in range(len(data)):
            form_item = {
                "fields": [
                    {"external_id": "title", "values": [{"value": data[i][0]}]},
                    {"external_id": "ep-name", "values": [{"value": data[i][1]}]},
                    {"external_id": "ep-profile-link", "values": [{"url": data[i][2]}]},
                    {"external_id": "email", "values": [{"value": data[i][3]}]},
                    {"external_id": "product-4", "values": [{"value": data[i][4]}]},
                    {"external_id": "sending-lc", "values": [{"value": data[i][5]}]},
                    {"external_id": "sending-mc", "values": [{"value": data[i][6]}]},
                    {"external_id": "hosting-lc", "values": [{"value": data[i][7]}]},
                    {"external_id": "hosting-mc", "values": [{"value": data[i][8]}]},
                    {"external_id": "opportunity-link", "values": [{"url": data[i][9]}]},
                    {"external_id": "approval-date", "values": [{"start": data[i][10] + " 00:00:00"}]},
                    {"external_id": "opp-earliest-start-latest-end-date","values": [{"start": data[i][11] + " 00:00:00"}]},
                    {"external_id": "opp-latest-end-date", "values": [{"start": data[i][12] + " 00:00:00"}]},
                    {"external_id": "realization-experience-end-dates","values": [{"start": data[i][13] + " 00:00:00"}]}
                    ]
                }
            podio.Item.create(appID, form_item)


def podioUpdateFIs(data, appID):
    if len(data) != 0:
        for i in range(len(data)):
            form_item = {
                "fields": [
                    {"external_id": "title", "values": [{"value": data[i][0]}]},
                    {"external_id": "ep-name", "values": [{"value": data[i][1]}]},
                    {"external_id": "ep-profile-link", "values": [{"url": data[i][2]}]},
                    {"external_id": "email", "values": [{"value": data[i][3]}]},
                    {"external_id": "product-4", "values": [{"value": data[i][4]}]},
                    {"external_id": "sending-lc", "values": [{"value": data[i][5]}]},
                    {"external_id": "sending-mc", "values": [{"value": data[i][6]}]},
                    {"external_id": "hosting-lc", "values": [{"value": data[i][7]}]},
                    {"external_id": "hosting-mc", "values": [{"value": data[i][8]}]},
                    {"external_id": "opportunity-link", "values": [{"url": data[i][9]}]},
                    {"external_id": "approval-date", "values": [{"start": data[i][10] + " 00:00:00"}]},
                    {"external_id": "opp-earliest-start-latest-end-date", "values": [{"start": data[i][11] + " 00:00:00"}]},
                    {"external_id": "opp-latest-end-date", "values": [{"start": data[i][12] + " 00:00:00"}]},
                    {"external_id": "realization-experience-end-dates", "values": [{"start": data[i][13] + " 00:00:00"}]},
                    {"external_id": "experience-end-dates", "values": [{"start": data[i][14] + " 00:00:00"}]}
                    ]
                }
            podio.Item.create(appID, form_item)



# def checkDuplications(appItems, data):
#     duplicatedItemIDs = {}
#     notDuplicatedItems = []
#     for item in data:
#         if isDuplicated(appItems, item[0]) is not None:
#             duplicatedItemIDs[isDuplicated(appItems, item[0])] = item[13]
#         else:
#             notDuplicatedItems.append(item)
#     return duplicatedItemIDs, notDuplicatedItems
#
#
# def isDuplicated(appItems, referenceID):
#     for item in appItems['items']:
#         if item['fields'][0]['values'][0]['value'] == referenceID:
#             return item['item_id']
