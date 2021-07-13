from model.Project import Project


class NewProjectHandler:

    def __init__(self):
        self.processor = None

    def set_processor(self, processor):
        self.processor = processor

    def new_project(self, value):
        project = Project(value[0], value[1], [])
        self.processor.user.projectsList.append(project)
        return self.processor.start()
