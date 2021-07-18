import os
import json

from enums.Path import Path
from model.Project import Project
from model.Task import Task
from model.User import User


class FileManager:

    def __init__(self):
        pass

    def creatNeedFolder(self):
        try:
            os.makedirs(Path.USER.value)
        except:
            pass

    def load_user(self, username):
        user = """INSERT INTO "user"(username)
                     VALUES(%s) RETURNING vendor_id;"""

    def saveUser(self, user):
        user_json_str = json.dumps(user, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_file = open(Path.USER.value + "/" + user.username + ".json", "w")
        json_file.write(user_json_str)
        json_file.close()


def class_mapper(d):
    return mapping[frozenset(d.keys())](**d)


mapping = {frozenset(('username',
                      'projectsList')): User,
           frozenset(('name',
                      'description',
                      'tasks_list')): Project,
           frozenset(('name',
                      'description',
                      'date')): Task, }
