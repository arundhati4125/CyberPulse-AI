const scanButton = document.getElementById("scanBtn");

scanButton.addEventListener("click", analyzeTraffic);

async function analyzeTraffic() {

    scanButton.disabled = true;
    scanButton.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

    // --------------------------
    // Read Form Values
    // --------------------------

    const protocol = document.getElementById("protocol").value;
    const service = document.getElementById("service").value;
    const flag = document.getElementById("flag").value;

    const srcBytes =
        Number(document.getElementById("srcBytes").value) || 0;

    const dstBytes =
        Number(document.getElementById("dstBytes").value) || 0;

    const loggedIn =
        Number(document.getElementById("loggedIn").value);

    const count =
        Number(document.getElementById("count").value) || 0;

    const srvCount =
        Number(document.getElementById("srvCount").value) || 0;

    const sameRate =
        Number(document.getElementById("sameRate").value) || 0;

    const hostCount =
        Number(document.getElementById("hostCount").value) || 0;

    // --------------------------
    // Encode Categorical Values
    // --------------------------

    let protocolValue = 0;

    if (protocol === "udp") protocolValue = 1;
    if (protocol === "icmp") protocolValue = 2;

    let serviceValue = 1;

    if (service === "ftp") serviceValue = 2;
    if (service === "smtp") serviceValue = 3;
    if (service === "domain_u") serviceValue = 4;

    let flagValue = 2;

    if (flag === "S0") flagValue = 0;
    if (flag === "REJ") flagValue = 1;

    // --------------------------
    // Build Feature Array
    // 41 Features
    // --------------------------

    const features = [

        0,                  // duration

        protocolValue,

        serviceValue,

        flagValue,

        srcBytes,

        dstBytes,

        0,

        0,

        0,

        0,

        0,

        loggedIn,

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        0,

        count,

        srvCount,

        0,

        0,

        0,

        0,

        sameRate,

        0,

        0,

        hostCount,

        hostCount,

        sameRate,

        0,

        sameRate,

        0,

        0,

        0,

        0,

        0

    ];

    // --------------------------
    // Call Flask API
    // --------------------------

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

    protocol,

    service,

    flag,

    srcBytes,

    dstBytes,

    loggedIn,

    count,

    srvCount,

    sameRate,

    hostCount

})

            }

        );

        const result = await response.json();

        document.getElementById("status").innerHTML =
            result.status;

        document.getElementById("attack").innerHTML =
            result.attack;

        document.getElementById("confidence").innerHTML =
            result.confidence + "%";

        document.getElementById("severity").innerHTML =
            result.severity;

        document.getElementById("recommendation").innerHTML =
            result.recommendation;

    }

    catch (error) {

        alert("Cannot connect to Flask Backend");

        console.log(error);

    }

    scanButton.disabled = false;

    scanButton.innerHTML =
        '<i class="fa-solid fa-magnifying-glass"></i> Analyze Traffic';

}