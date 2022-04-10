# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello, welcome to Sparta Snacks. Where people with no lives code and eat. How can I help you today? You can say things like \"What's the temperature\" amongst other things"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

##################################################################################################################

#Template. No longer needed in final
class FromLaptopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FromLaptopIntent")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "FromLaptopIntentHandler worked successfully"
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )
        
        
        
    
class TemperatureThresholdIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TemperatureThresholdIntent")(handler_input)

    def handle(self, handler_input):
        fp,upperBound,lowerBound,data_list = open("Data.txt"), 60.0, 10.0,[] #Slots can be utilized to make maximum, minimum, and mean values.
        for line in fp: #Optimize so lines in files are globals?
            line = line.split()
            if line: data_list.append(line[3]) 
        cwd = float(data_list[-1])
        if lowerBound < cwd < upperBound: #Within range
            speak_output = "The current temperature, {:.2f} degrees celsius is between the threshold of {:.2f} and {:.2f}."\
            .format(cwd,lowerBound,upperBound)
            ask = "Anything else?"
        elif cwd < lowerBound:
            speak_output = "The current temperature, {:.2f} degrees celsius is below the minimum threshold of {:.2f}."\
                .format(cwd, lowerBound)
            ask = "Would you like me to turn on heating systems?"
        elif cwd > upperBound:
            speak_output = "The current temperature, {:.2f} degrees celsius is above the maximum threshold of {:.2f}."\
                .format(cwd, upperBound)
            ask = "Would you like me to turn off the cooling systems?"
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(ask)
            .response
        )


class HumidityThresholdIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("HumidityThresholdIntent")(handler_input)

    def handle(self, handler_input):
        fp,upperBound,lowerBound,data_list = open("Data.txt"), 50.0, 10.0,[]
        for line in fp:
            line = line.split()
            if line: data_list.append(line[7]) 
        cwd = float(data_list[-1])
        if lowerBound < cwd < upperBound: #Within range
            speak_output = "The current Humidity, {:.2%} is between the threshold of {:.2%} and {:.2%}."\
            .format(cwd/100,lowerBound/100,upperBound/100)
        elif cwd < lowerBound:
            speak_output = "The current humidity, {:.2%} is below the minimum threshold of {:.2%}."\
                .format(cwd/100, lowerBound/100)
        elif cwd > upperBound:
            speak_output = "The current humidity, {:.2%} is above the maximum threshold of {:.2%}."\
                .format(cwd/100, upperBound/100)
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask("Anything else?")
            .response
        )
    
class LightThresholdIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("LightThresholdIntent")(handler_input)

    def handle(self, handler_input):
        fp,lowerBound,data_list = open("Data.txt"),250,[]
        for line in fp:
            line = line.split()
            if line: data_list.append(line[-1]) 
        cwd = int(data_list[-1])
        if cwd > lowerBound:
            speak_output = "The light level, {:d} lumens, is sufficient and above the lower threshold of {:d}"\
                .format(cwd,lowerBound)
        if cwd < lowerBound:
            speak_output = "Insufficient levels. The current lighting, {:d} lumens is below the minimum threshold of {:d}. "\
                .format(cwd, lowerBound)
        
        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask("Anything else?")
            .response
        )
    ################  MY STUFF

#################################################################################################################
class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello! What would you like to know about the data from the Arduino?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say things like \"What's the temperature.\" Or \"Humidty levels\" for example."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Alright!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "I did not understand. You can ask, what is the temperature, humidity levels, and light levels."
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.
        speak_output = "Leaving Sparta Snack"
        return handler_input.response_builder.speak(speak_output).response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "The intent: " + intent_name + " Failed horribly. Pleas fix."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TemperatureThresholdIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HumidityThresholdIntentHandler())
sb.add_request_handler(LightThresholdIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())
lambda_handler = sb.lambda_handler()
