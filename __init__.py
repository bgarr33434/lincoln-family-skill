from mycroft import MycroftSkill, intent_file_handler


class LincolnFamily(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('family.lincoln.intent')
    def handle_family_lincoln(self, message):
        self.speak_dialog('family.lincoln')


def create_skill():
    return LincolnFamily()

