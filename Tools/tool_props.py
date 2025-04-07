def ReqTool():
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
    return equivalent_resistance_tool

def trashTool():
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
    return trashcan_tool

def satTool():
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
    return isat_tool

def matrixTool():
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
    return matrix_tool

def weatherTool():
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
    return weather_tool