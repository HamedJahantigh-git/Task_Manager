class User(object):

    def __init__(self, username, projectsList):
        self.username = username
        self.projectsList = projectsList

    def projects_list_name(self):
        ans = []
        for i in self.projectsList:
            ans.append(i.name)
        return ans

    def get_project(self, value):
        for i in self.projectsList:
            if i.name == value:
                return i
        return None

    def project_entity(self, name):
        for i in self.projectsList:
            if i.name is name:
                i.entitiy
                break
