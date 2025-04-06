from Tools.calculators.electronics_calcs.r_equivalent_calc import *
from Tools.calculators.electronics_calcs.semi_cond_current_calc import *
from Tools.calculators.matrix_calcs import *
from Tools.GeoCoding.WeatherAPIs import *
from Tools.pattern_match import *
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
                print("There was an error starting the model server")
                exit()
        case "close":
            close = sub.run("lms server stop", shell=True)
            return_code = close.returncode
            if return_code != 0:
                print("There was an error closing the model server")

#server status
try:
    rq.get(model_url)
except Exception as e:
    server_handling("open")


def get_weather(text):
    forecast, location, location_error = weather(text)
    if not location_error:
        print(f"The forecast for {location} is {forecast[4]}, the high will be {forecast[2]}, the low will be {forecast[3]}, the current temp is {forecast[0]}, and it feels like {forecast[1]}")
    else:
        print("There was an error retrieving the forecast")

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

weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": (
            "returns a weather forecast by making a request to an api endpoint."
            "Always pick this tool when the user is asking for something with weather forecasting and they supply a comma seperated city and state"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "the name of city the weather forecast is being requested for",
                },
                "state": {
                    "type": "string",
                    "description": "the name of the state the weather forecast is being requested for",
                },
            },
            "required": ["city"],
        },
    },
}

matrix_tool = {
    "type": "function",
    "function": {
        "name": "get_matrix",
        "description": (
            "find the determinant cofactors and minors of a given 3x3 matrix"
            "Always use when matrices are mentioned"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "matrix": {
                    "type": "boolean",
                    "description": "matrices explicitly mentioned",
                },
            },
            "required": ["matrix"],
        },
    },
}

isat_tool = {
    "type": "function",
    "function": {
        "name": "get_Isat",
        "description": (
            "calculate the the saturation current of a transistor"
            "Always use this if the user is asking for something with saturation current"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "saturation": {
                    "type": "boolean",
                    "description": "saturation current explicitly mentioned",
                },
            },
            "required": ["saturation"],
        },
    },
}

trashcan_tool = {
    "type": "function",
    "function": {
        "name": "get_trashcan",
        "description": (
            "opens auto trashcan"
            "Always use this if the user is asking for something with a trash can"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "open": {
                    "type": "boolean",
                    "description": "open the trash",
                },
            },
            "required": ["open"],
        },
    },
}

equivalent_resistance_tool = {
    "type": "function",
    "function": {
        "name": "get_Requivalent_0_5",
        "description": (
            "Computes the equivalent resistance of two resistors based on their configuration"
            "Always use this if the user gives resistor values for r1 and r2 and a configuration"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "configuration": {
                    "type": "string",
                    "description": "how r1 and r2 are connected either series or parallel",
                },
                "R1": {
                    "type": "float",
                    "description": "r1 value in ohms",
                },
                "R2": {
                    "type": "float",
                    "description": "r2 value in ohms",
                },
            },
            "required": ["configuration"],
        },
    },
}

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
        print("the model could not generate a response")

def tool_handler(response, text):
    weather = get_pattern_match('.*"(get_weather)',response)
    matrix = get_pattern_match('.*"(get_matrix)',response)
    i_sat = get_pattern_match('.*"(get_[I-i]sat)',response)
    trash = get_pattern_match('.*"(get_trashcan)',response)
    req =  get_pattern_match('.*"(get_[R-r]eq)',response)
    if weather is not None:
        get_weather(text)
    elif matrix is not None:
        get_matrix()
    elif i_sat is not None:
        get_Isat()
    elif req is not None:
        print(req)
        get_Req(text)
    elif trash is not None:
        print(trash)
        # get_trashcan()
    else:
        print(f"---------------------No tool called---------------------\n{response}")



def main():
    while True:
        text = str(input("Enter a request: "))
        if text == "quit":
            break
        response = chat(text)
        time.sleep(1)
    server_handling("close")

if __name__ == "__main__":
    main()