import psycopg2

from model.Project import Project
from model.Task import Task
from model.User import User

DB_NAME = "tvwsvrnk"
DB_USER = "tvwsvrnk"
DB_PASS = "Exv3f4oAVA7J61ajFjgdADA9C8VxtU-d"
DB_HOST = "batyr.db.elephantsql.com"
DB_PORT = "5432"


class DB:

    def __init__(self):
        self.username = None

    def initialize(self):
        self._connect()
        # self._drop_all_table()
        self._create_tables()

    def set_user(self, user):
        self.username = user.username

    def _connect(self):

        self.connection = psycopg2.connect(database=DB_NAME, user=DB_USER,
                                           password=DB_PASS, host=DB_HOST, port=DB_PORT)
        self.cur = self.connection.cursor()
        self.connection.autocommit = True

    def _create_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = ("""
            CREATE TABLE "user"(
                    username TEXT PRIMARY KEY,
                    user_info TEXT
                )
                """,
                    """
                    CREATE TABLE project (
                            username TEXT REFERENCES "user" (username),
                            project_name TEXT NOT NULL,
                            project_description TEXT,
                            PRIMARY KEY (username, project_name)
                    )
                    """,
                    """
                    CREATE TABLE task (
                            username TEXT NOT NULL,
                            project_name TEXT NOT NULL,
                            task_name TEXT NOT NULL,
                            task_description TEXT,
                            task_date TEXT,
                            FOREIGN KEY (username)
                                REFERENCES "user" (username)
                                ON UPDATE CASCADE ON DELETE CASCADE,
                            FOREIGN KEY (username, project_name)
                                REFERENCES project (username, project_name)
                                ON UPDATE CASCADE ON DELETE CASCADE,
                                PRIMARY KEY (username, project_name, task_name)
                    )
                    """
                    )

        try:
            # create table one by one
            for command in commands:
                self.cur.execute(command)
            # commit the changes

        except Exception as e:
            pass
            # print(e)

    def save_new_user(self, user):
        self.cur.execute("ROLLBACK")
        sql = """ INSERT INTO "user" (username, user_info) VALUES (%s,%s)"""
        self.cur.execute(sql, (user.username, user.user_info))

    def load_user(self, username):
        self.cur.execute("ROLLBACK")

        postgre_sql_select_query = "select * from \"user\" where username = %s"
        self.cur.execute(postgre_sql_select_query, (username,))
        user_db = self.cur.fetchmany(1)
        user = User(user_db[0][0], user_db[0][1])
        self.set_user(user)
        return user

    def save_new_project(self, project):
        self.cur.execute("ROLLBACK")

        sql = """ INSERT INTO "project" (username,project_name, project_description) VALUES (%s,%s,%s)"""
        self.cur.execute(sql, (self.username, project.name, project.description))

    def project_list_name(self):
        self.cur.execute("ROLLBACK")

        postgre_sql_select_query = "select project_name from project where username = %s"
        self.cur.execute(postgre_sql_select_query, (self.username,))
        project_list = self.cur.fetchall()
        return self._set_to_list(project_list)

    def project_entity(self, project_name):
        self.cur.execute("ROLLBACK")
        postgre_sql_select_query = "select * from project where (username, project_name) = (%s,%s)"
        self.cur.execute(postgre_sql_select_query, (self.username, project_name,))
        return self.cur.fetchmany(1)

    def save_new_task(self, project_name, task):
        self.cur.execute("ROLLBACK")

        sql = """ INSERT INTO "task" (username,project_name, 
                task_name ,task_description, task_date) VALUES (%s,%s,%s,%s,%s)"""
        self.cur.execute(sql, (self.username, project_name, task.name, task.description, task.date))

    def project_tasks_entity(self, project_name):
        self.cur.execute("ROLLBACK")
        postgre_sql_select_query = "select * from task where (username, project_name) = (%s,%s)"
        self.cur.execute(postgre_sql_select_query, (self.username, project_name,))
        return self.cur.fetchall()

    def exit(self):
        self.cur.close()
        self.connection.close()

    def drop_all_table(self):
        self.cur.execute("DROP TABLE task")
        self.cur.execute("DROP TABLE project")
        self.cur.execute("DROP TABLE \"user\"")

    def _set_to_list(self, list):
        ans = []
        for component in list:
            ans.append(component[0])
        return ans

    # def test(self, sql ,*arg):
    #     self.cur.execute("ROLLBACK")
    #
    #     self.cur.execute(sql, arg)
    #     return self.cur.fetchmany(1)


# db = DB()
# db.initialize()
# db.drop_all_table()
# db.drop_all_table()
# db.save_new_user(User("ali", "jahan"))
# db.save_new_user(User("hamed", "j"))
# db.load_user("ali")
# db.save_new_project(Project("robina", "hamed"))
# db.save_new_project(Project("nilva", "sajad"))
# db.save_new_task("robina", Task("task1","test3","3/2/1399"))
# db.save_new_task("nilva", Task("task2","test2","10/2/1399"))

# db.exit()
