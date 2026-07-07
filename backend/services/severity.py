def get_severity(label):

    if label == "normal":
        return "Low"

    elif label in [
        "neptune",
        "smurf",
        "back",
        "teardrop"
    ]:
        return "High"

    elif label in [
        "ipsweep",
        "nmap",
        "portsweep",
        "satan"
    ]:
        return "Medium"

    else:
        return "Critical"