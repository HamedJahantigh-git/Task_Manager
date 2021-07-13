class Project(object):

    def __init__(self, name, description, tasks_list):
        self.name = name
        self.description = description
        self.tasks_list = tasks_list

    def entity(self):
        return [self.name, self.description, self.tasks_list]

