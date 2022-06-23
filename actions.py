# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet
import spacy
#
#
talking_points=[]
action_items={}
owners=[]
deadline=[]
nlp = spacy.load('en_core_web_sm')
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionTalkingPoint(Action):
    def name(self) -> Text:
        return 'action_talking_point'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #talking_points.append(tracker.latest_message.get("text"))
        talking_points.append(tracker.get_slot('talking_point_text'))
        return []

class ActionActionItem(Action):
    def name(self) -> Text:
        return 'action_action_item'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=tracker.latest_message.get("text")
        ##NER
        #owners=[]
        #deadline=[]
        #modify_ents(text)------delete
        
      #if yes: owner owners.append(word)
      # else: print("Specify owner")
      #       owner.append(input_string) 
          
       #if yes: deadline deadline.append(word)
      # else: print("Specify deadliner")
      #       deadline.append(input_string) 

        #print("Owners:",owners)
       
        #print("Deadline",deadline).\venv
        #fields=(owners,deadline)
        #action_items[text]=fields
        str_a="Action Item Text : "+str(tracker.get_slot('actionitem_text'))
        str_b="Owner : "+str(tracker.get_slot('person'))
        str_c="Deadline : "+str(tracker.get_slot('time'))
        dispatcher.utter_message(str_a)
        dispatcher.utter_message(str_b)
        dispatcher.utter_message(str_c)
        action_items[tracker.get_slot('actionitem_text')]=[tracker.get_slot('person'),tracker.get_slot('time')]
        #action_items[tracker.get_slot('actionitem_text')]=[owners[0],deadline[0]]
        #dispatcher.utter_message(action_items)
        #return out
        return []

#class ValidateActionItemForm(FormValidationAction):
#    def name(self) -> Text:
#        return "validate_action_item_form"
#    async def extract_

class ActionResetSlots(Action):

     def name(self) -> Text:
            return "action_reset_slots"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("All slots have been reset")

         return [AllSlotsReset()]

class ActionGetOwner(Action):

     def name(self) -> Text:
            return "action_get_owner"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
         #text=tracker.get_slot('actionitem_text')
         #dispatcher.utter_message(str(nlp(text).ent s))
         owners=[]
         owner=tracker.latest_message.get("text")
         owners.append(owner)
         dispatcher.utter_message(str(owner))
         #SlotSet(key='person', value=owner)
         dispatcher.utter_message(str(tracker.get_slot('person')))
         #SlotSet(key="time", value="deadline")
         dispatcher.utter_message("Owner slot set")

         return [SlotSet(key='person', value=owner)]

class ActionGetDeadline(Action):

     def name(self) -> Text:
            return "action_get_deadline"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
         #text=tracker.get_slot('actionitem_text')
         #dispatcher.utter_message(str(nlp(text).ents))
         deadline=[]
         due=tracker.latest_message.get("text")
         deadline.append(due)
         dispatcher.utter_message(str(due))
         #SlotSet(key="person", value="owner")
         #SlotSet(key='time', value=due)
         dispatcher.utter_message(str(tracker.get_slot('time')))
         dispatcher.utter_message("Deadline slot set")

         return [SlotSet(key='time', value=due)]