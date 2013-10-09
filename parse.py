# -*- coding: utf-8 -*-


class Parse:

    def __init__(self):
        pass

    def parseData(self, story):
        data = {
            'name': story['name'],
            'desc': self.__description(story),
            'idMembers': self.__get_members(story),
            'comments': self.__comments(story),
            'tasks': self.__tasks(story),
            'labels': self.__labels(story),
            # TODO: Fix to get attchments
            # 'attachments': self.__attachments(story)
        }
        return data

    def __attachments(self, story):
        attachments = []
        if('attachments' in story):
            if(isinstance(story['attachments']['attachment'], list)):
                for attachment in story['attachments']['attachment']:
                    attachments.append(attachment['url'])
            else:
                attachments.append(story['attachments']['attachment']['url'])
        return attachments

    def __comments(self, story):
        comments = []
        if('notes' in story and 'note' in story['notes']):
            if(isinstance(story['notes']['note'], list)):
                for note in story['notes']['note']:
                    comments.append(note['text']+u"\n\nBy "+self.__author(note['author']))
            else:
                comments.append(story['notes']['note']['text']+u"\n\nBy "+self.__author(story['notes']['note']['author']))
        return comments

    def __description(self, story):
        desc = ''
        if('description' in story and story['description']):
            desc = story['description']
        desc = desc+u"\n\nPivotal source: "+story['url']
        attachments = self.__attachments(story)
        if(len(attachments)):
            desc = desc+u"\n\nAttachments:\n"
            for attachment in attachments:
                desc = desc+attachment+u"\n"
        return self.__encode(desc)

    def __encode(self, x):
        x = unicode(x)
        return x.encode('utf-8', 'ignore')

    def __get_members(self, story):
        members = []
        if('requested_by' in story):
            members.append(self.__member(story['requested_by']))
        if('owned_by' in story):
            members.append(self.__member(story['owned_by']))
        # Remove duplicates
        members = sorted(set(members))
        return members

    def __labels(self, story):
        labels = []
        if(story['story_type'] == 'bug'):
            labels.append({'value': 'red'})
        return labels

    def __author(self, x):
        x = self.__encode(x)
        return {
            'Author name': 'Parsed author name',
        }.get(x, 'Parsed author name')

    def __member(self, x):
        x = self.__encode(x)
        return {
            'Member name': 'pivotal_member_id',
        }.get(x, 'pivotal_member_id')

    def __tasks(self, story):
        tasks = []
        if('tasks' in story):
            if(isinstance(story['tasks']['task'], list)):
                for task in story['tasks']['task']:
                    tasks.append({'name': task['description'], 'checked': task['complete']['#text']})
            else:
                tasks.append({'name': story['tasks']['task']['description'], 'checked': story['tasks']['task']['complete']['#text']})
        return tasks
