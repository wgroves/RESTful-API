from sqlalchemy_declaration import Base, Parent, Child
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBController:

    def __init__(self):
        self.engine = create_engine('sqlite:///parent_child.db')
        Base.metadata.bind = self.engine
        DBSession = sessionmaker()
        DBSession.bind = self.engine
        self.session = DBSession()

    def addParent(self, parent_name):
        parent = Parent(name=parent_name)
        self.session.add(parent)
        self.session.commit()

    def addChild(self, child_name, p_id):
        child = Child(name=child_name, parent_id = p_id)
        self.session.add(child)
        self.session.commit()

    def getChild(self, id):
        child = self.session.query(Child).filter(Child.id == id).one()
        parent = self.session.query(Parent).filter(Parent.id == child.parent_id).one()
        parentDict = {
            "id": parent.id,
            "name": parent.name
        }
        childDict = {
            "name": child.name,
            "id": child.id,
            "parent": parentDict
        }
        return childDict

    def getParent(self, id):
        parent = self.session.query(Parent).filter(Parent.id == id).one()
        children = self.session.query(Child).filter(Child.parent_id == parent.id).all()
        child_list = []
        for child in children:
            childDict = {
                "id": child.id,
                "name": child.name
            }
            child_list.append(childDict)

        parentDict = {
            "name": parent.name,
            "id": parent.id,
            "children": child_list
        }

        return parentDict

