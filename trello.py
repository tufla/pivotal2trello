# -*- coding: utf-8 -*-
from trolly.client import Client
from trolly.organisation import Organisation
from trolly.board import Board
from trolly.list import List
from trolly.card import Card
from trolly.checklist import Checklist
from trolly.member import Member
from trolly import ResourceUnavailable


class Trello:

    def __init__(self):
        API_KEY = 'my_trello_key'
        AUTH_TOKEN = 'my_trello_token'
        self.client = Client(API_KEY, AUTH_TOKEN)

    def getBoard(self, board_id):
        return Board(self.client, board_id)

    def getCard(self, card_id):
        return Card(self.client, card_id)

    def getList(self, list_id):
        return List(self.client, list_id)

    def getOrganization(self, organization_id):
        return Organisation(self.client, organization_id)

    def addCard(self, target_list, data):
        new_card = target_list.addCard(data)
        for member in data['idMembers']:
            new_card.addMember(member)
        for comment in data['comments']:
            new_card.addComments(comment)
        if(len(data['tasks']) > 0):
            checklist = new_card.addChecklists({'name': 'Tasks'})
            for task in data['tasks']:
                checklist.addItem(task)
        for label in data['labels']:
            new_card.addLabels(label)

        return new_card
