from mycroft import MycroftSkill, intent_file_handler
import pandas as pd


class LincolnFamily(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.register_entity_file('family.lincoln_name.entity')

    @intent_file_handler('family.lincoln.intent')
    def handle_family_lincoln(self, message):
        #self.speak_dialog('family.lincoln')
        self.speak('one second, my lord lincoln')
        
      df = pd.read_csv('FamilyDates&Numbers.csv',header=[0], index_col=[0])
    #def __init__(self,input_name,error_mess):
    input_name = ""
    error_mess = ""
    print("input name =" + input_name)
    new_df = df[(df.index == input_name)]
    if not new_df.empty:
        error_mess = "found on first try"
        print(new_df, error_mess)
        if new_df.empty:
                new_df = df[(df["Alt-name"]==self.input_name)]
                error_mess = "found on second try"
                print(new_df, error_mess)
                if new_df.empty:
                    error_mess = 'Sorry, the name could not be found'   


def create_skill():
    return LincolnFamily()

