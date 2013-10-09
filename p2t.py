# -*- coding: utf-8 -*-
from parse import Parse
from pivotal import Pivotal
from trello import Trello

organization = '51i37940cwbrccd3a1749d39000113'

bugs_board = '525yu166bf12dc90e1b10c001acf'
planning_board = '5690f1439576fee44f982b0009ec'
current_dev_board = '51tgs4393427a6320f450000d4d'

bugs_inbox_id = '5166bf12dc90e1b10c001ad0'
planning_nextup_id = '34sdw9576fee44f982b0009ed'
current_nextup_id = '34sdw5eae09f8c03200048e'
current_inprogress_id = '34sdw427a6320f450000d4e'
current_qa_id = '34sdw427a6320f450000d4f'
current_live_id = '34sdw8e4571979847000d64'


# Bugs Board Lists
# {u'pos': 16384, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd9576fee44f982b0009ed', u'closed': False, u'name': u'Next Up'}
# {u'pos': 32768, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd9576fee44f982b0009ee', u'closed': False, u'name': u'Spec'}
# {u'pos': 49152, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd9576fee44f982b0009ef', u'closed': False, u'name': u'Design'}
# {u'pos': 115712, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd95be04bf835957000b42', u'closed': False, u'name': u'Ready'}


# Planning Board Lists
# {u'pos': 16384, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd9576fee44f982b0009ed', u'closed': False, u'name': u'Next Up'}
# {u'pos': 32768, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd9576fee44f982b0009ee', u'closed': False, u'name': u'Spec'}
# {u'pos': 49152, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd9576fee44f982b0009ef', u'closed': False, u'name': u'Design'}
# {u'pos': 115712, u'idBoard': u'34sdw9576fee44f982b0009ec', u'id': u'34sd95be04bf835957000b42', u'closed': False, u'name': u'Ready'}

# Current development Board Lists
# {u'pos': 9216, u'idBoard': u'34sdw427a6320f450000d4d', u'id': u'34sdw935eae09f8c03200048e', u'closed': False, u'name': u'Next Up'}
# {u'pos': 16384, u'idBoard': u'34sdw427a6320f450000d4d', u'id': u'34sdw93427a6320f450000d4e', u'closed': False, u'name': u'In Progress'}
# {u'pos': 32768, u'idBoard': u'34sdw427a6320f450000d4d', u'id': u'34sdw93427a6320f450000d4f', u'closed': False, u'name': u'QA'}
# {u'pos': 49152, u'idBoard': u'34sdw427a6320f450000d4d', u'id': u'34sdw93427a6320f450000d50', u'closed': False, u'name': u'Launchpad'}
# {u'pos': 115712, u'idBoard': u'34sdw427a6320f450000d4d', u'id': u'34sdw938e4571979847000d64', u'closed': False, u'name': u'Live'}

pivotal = Pivotal()
trello = Trello()

# unscheduled 32162031

movements = {
    'icebox_bugs': {'target': bugs_inbox_id, 'filters': {'filter': 'type:bug state:unscheduled'}},
    'icebox_features': {'target': planning_nextup_id, 'filters': {'filter': 'type:feature,chore state:unscheduled', 'limit': '10', 'offset': '76'}},
    'current_nextup': {'target': current_nextup_id, 'filters': {'filter': 'state:unstarted', 'limit': '30', 'offset': '10'}},
    'current_inprogress': {'target': current_inprogress_id, 'filters': {'filter': 'state:started'}},
    'current_qa': {'target': current_qa_id, 'filters': {'filter': 'state:finished'}},
    'current_live': {'target': current_live_id, 'filters': {'filter': 'state:delivered', 'limit': '30', 'offset': '7'}},
    'current_inprogress2': {'target': current_inprogress_id, 'filters': {'filter': 'state:rejected'}},
    # 'icebox_features': {'target': planning_nextup_id, 'filters': {'filter': 'id:43068683,41430591,33693103,33691827,32161881,37317209'}}
    # 'icebox_bugs': {'target': bugs_inbox_id, 'filters': {'filter': 'id:41753701,38746909'}}
}


print '############################'

movement = movements['current_inprogress2']

stories = pivotal.getStories(movement['filters'])
# print stories['stories']['story']

target_list = trello.getList(movement['target'])
print target_list.getListInformation()

parse = Parse()
i = 1
for story in stories:
    print '========================================== %d' % i
    try:
        data = parse.parseData(story)
        print data
        card = trello.addCard(target_list, data)
        print card.getCardInformation()
        i += 1
    except Exception, e:
        print story['id']['#text']
        raise e

# cards = planning_nextup_list.getCards()
# for card in cards:
#     print card.getCardInformation()
#     print '------------'
#     for checklist in card.getChecklists():
#         print checklist.getChecklistInformation()
#         for item in checklist.getItems():
#             print '...........'
#             print item

# org = trello.getOrganization(organization)
# for board in org.getBoards():
#     print '..............................'
#     print board.getBoardInformation()

# planning = trello.getBoard(bugs_board)
# print '---------------------'
# lists = planning.getLists()

# for blist in lists:
#     print blist.getListInformation()

# print '---------------------'
