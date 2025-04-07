from Tools.calculators.electronics_calcs.r_equivalent_calc import *
from Tools.calculators.electronics_calcs.semi_cond_current_calc import *
from Tools.calculators.matrix_calcs import *
from Tools.GeoCoding.WeatherAPIs import *
from Tools.pattern_match import *
from Tools.tool_props import *
from Tools.TTS.TTS import say
from openai import OpenAI
import subprocess as sub
import time
"""
    API endpoints
"""
model_url = "http://localhost:1234/v1/models" #GET
url = "http://localhost:1234/v1"              #POST


def server_handling(task):
    match task:
        case "open":
            load = sub.run("lms server start", shell=True)
            return_code = load.returncode
            if return_code != 0:
                display("There was an error starting the model server")
                exit()
        case "close":
            close = sub.run("lms server stop", shell=True)
            return_code = close.returncode
            if return_code != 0:
                display("There was an error closing the model server")

#server status
try:
    rq.get(model_url)
except Exception as e:
    server_handling("open")


def get_weather(text):
    forecast, location, location_error = weather(text)
    if not location_error:
        display(f"The forecast for {location} is {forecast[4]}, the high will be {forecast[2]}, the low will be {forecast[3]}, the current temp is {forecast[0]}, and it feels like {forecast[1]}")
    else:
        display("There was an error retrieving the forecast")

def get_matrix():
    matrix_calc()

def get_Isat():
    isat()

def get_Req(text):
    r1 = get_pattern_match('r1 is ([0-9]*) ',text)
    r2 = get_pattern_match('r2 is ([0-9]*) ',text)
    config = get_pattern_match('config.* is ([a-z]*) ', text)
    Requivalent_0_5(r1,r2,config)

"""
ADD FUNCTIONALITY to request action from embedded trash ESP
"""
def get_trashcan():
    return 0

def display(text):
    print(text)
    say(text)


# call tool properties
weather_tool = weatherTool()
matrix_tool = matrixTool()
isat_tool = satTool()
trashcan_tool = trashTool()
equivalent_resistance_tool = ReqTool()

def chat(text):
    # Point to the local server
    client = OpenAI(base_url=url, api_key="lm-studio")

    completion = client.chat.completions.create(
        model="deepseek-r1-distill-qwen-1.5b-fully-uncensored-i1",
        messages=[
            {"role": "user", "content": text.lower()}
        ],
        tools = [weather_tool, isat_tool, equivalent_resistance_tool, matrix_tool, trashcan_tool],
    )
    response = completion.choices[0].message
    if response is not None:
        tool_handler(response.content, text)
        return response.content
    else:
        display("the model could not generate a response")

def tool_handler(response, text):
    weather = get_pattern_match('.*"(get_weather)',response)
    matrix = get_pattern_match('.*"(get_matrix)',response)
    i_sat = get_pattern_match('.*"(get_[I-i]sat)',response)
    trash = get_pattern_match('.*"(get_trashcan)',response)
    req =  get_pattern_match('.*"(get_[R-r]eq)',response)
    if weather is not None:
        display("Forecasting")
        get_weather(text)
    elif matrix is not None:
        display("Opening matrix calc")
        get_matrix()
    elif i_sat is not None:
        display("Opening saturation current calc")
        get_Isat()
    elif req is not None:
        display("Opening equivalent resistance calc")
        get_Req(text)
    elif trash is not None:
        display("Opening trash can")
        # get_trashcan()
    else:
        print(f"---------------------No tool called---------------------\n{response}")
        say(response)



def main():
    display('Who am I speaking to?')
    text = str(input(":"))
    display(f'How can I help you {text}?')
    while True:
        text = str(input("Enter your request: "))
        if text == "quit":
            break
        response = chat(text)
        time.sleep(1)
    display("Closing connection, Goodbye")
    server_handling("close")

if __name__ == "__main__":
    main()