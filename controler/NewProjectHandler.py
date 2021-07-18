from Exeption.Error import ProjectNameRepititive
from model.Project import Project


class NewProjectHandler:

    def __init__(self):
        self.processor = None

    def set_processor(self, processor):
        self.processor = processor

    def new_project(self, value):
        try:
            project = Project(value[0], value[1])
            print(project.name+"/"+project.description)
            self.processor.db.save_new_project(project)
        except Exception as e:
            raise ProjectNameRepititive
        return self.processor.start()
