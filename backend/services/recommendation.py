def get_recommendation(label):

    if label == "normal":

        return "No malicious activity detected."

    if label in [
        "neptune",
        "smurf"
    ]:

        return "Possible DoS attack detected. Review firewall rules."

    if label in [
        "ipsweep",
        "portsweep",
        "nmap"
    ]:

        return "Network scan detected. Check IDS logs."

    if label in [
        "buffer_overflow",
        "rootkit",
        "perl"
    ]:

        return "Privilege escalation attack suspected."

    return "Investigate suspicious activity immediately."