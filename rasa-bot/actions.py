from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals



from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import Action
from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk.events import SlotSet
from decimal import Decimal




class ActionWeather(Action):
    def name(self):
        return 'action_get_weather'
    
    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = 'f5d0a214ccf44880ace61427180103' #your apixu key
        client = ApixuClient(api_key)
        
        loc = tracker.get_slot('GPE')
        current = client.current(q=loc)
        
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']
        
        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
        
        dispatcher.utter_message(response)
        return [SlotSet('GPE',loc)]



class ActionIelts1(Action):
    def name(self):
        return 'action_ielts_1'
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('number')
        float_loc = float(loc)
        modulo = Decimal(float_loc) % Decimal('0.5')
        if (modulo == 0):
            if (float_loc < 0.0):
                dispatcher.utter_message("I'm sorry, but I don't think Ielts score can be lower than 0")
            elif (float_loc > 9.0):
                dispatcher.utter_message("Sorry, but I think the maximum score of Ielts is 9.0.")
            elif (float_loc >= 6.0):
                dispatcher.utter_message("Congratulation, your Ielts score is very impressive, you can skip pre-university and start studying the main subjects.")
            else:
                dispatcher.utter_message("We have a pre-university program to help you improve your English before you start the main subjects.")
        else:
            dispatcher.utter_message("Sorry, but Ielts score cannot be " + str(float_loc))
        return



class ActionToefl1(Action):
    def name(self):
        return 'action_toefl_1'
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('number')
        float_loc = float(loc)
        modulo = Decimal(float_loc) % Decimal('1')
        if (modulo == 0):
            if (float_loc > 120):
                dispatcher.utter_message("I'm sorry, but Toefl score can not be higher than 120.")
            elif (float_loc < 0):
                dispatcher.utter_message("Sorry, but I don't think your score can be negative.")
            elif(float_loc >= 79):
                dispatcher.utter_message("Congrats, your Toefl score is already higher than our requirement, you can skip pre-university program and start studying the main subjects.")
            else:
                dispatcher.utter_message("We have a pre-university to help better your English before you start your main subjects.")
        else:
            dispatcher.utter_message("Sorry , but Toefl score cannot be "+ str(float_loc))
        return
