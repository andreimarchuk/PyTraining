from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class HelperManager:

    def __init__(self, app):
        self.app = app
        self.session = SessionHelper(self.app)
        self.group = GroupHelper(self.app)
        self.contact = ContactHelper(self.app)
