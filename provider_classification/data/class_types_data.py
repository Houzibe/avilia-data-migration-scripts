import numpy as np

class_types = np.array([
    {
        "name": "Available services",
        "descr": "Types of services that are rendered by the provider.",
        "allow_multiple": 1
    },
    {
        "name": "Providers by band",
        "descr": "Classification of providers by their band(A+,A,B,C).",
        "allow_multiple": 1
    }
])