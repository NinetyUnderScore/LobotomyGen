videos = [];
videosTrimmed = [];

async function setMaskX(x) {
    path = document.getElementById("svg_1");

    trans = path.getAttribute("transform");
    transArray = trans.split(" ");

    newX = parseFloat(x);
    newX = -320 + newX * 587;

    transArray[2] = "translate(0," + newX.toString() + ")";
    trans = transArray.join(" ");
    path.setAttribute("transform", trans);

    return
}

function setMaskY(y) {
    path = document.getElementById("svg_1");

    trans = path.getAttribute("transform");
    transArray = trans.split(" ");
    transArray[1] = "translate(" + y.toString() + ",0)";
    trans = transArray.join(" ");
    path.setAttribute("transform", trans);

    return
}

function sanitizeString(str){
    str = str.replace(/[^a-z0-9áéíóúñü \.,_-]/gim,"");
    return str.trim();
}

async function quickFetch(cmd, p1, p2, p3) {
    const response = await fetch('http://127.0.0.1:9900/', {
        method: 'POST',
        headers:{
        'Content-Type': 'application/x-www-form-urlencoded'
        },    
        body: new URLSearchParams({
            'command': cmd,
            'param1': p1,
            'param2': p2,
            'param3': p3
        })
    });
 
    return response;
}

// simple no input no return functions

async function updateProgress() {
    response = await quickFetch('getProgress', 0, 0, 0);

    jso = await response.json();

    console.log(jso["message"]);

    setMaskX(jso["message"]);
}

async function clearTrimmed() {
    response = await quickFetch('clearTrimmed', 0, 0, 0);

    videosTrimmed.length = 0;
    console.log("cleared videosTrimmed");
}

async function clearResults() {
    response = await quickFetch('clearResults', 0, 0, 0);

    videos.length = 0;
    console.log("cleared videos");
}

async function search() {
    query = document.getElementById("searchQuery").value;
    amnt = sanitizeString(document.getElementById("searchAmount").value);

    console.log("searching: " + query + ", " + amnt);

    response = await quickFetch('search', query, amnt, 0);

    console.log("search completed");
}

async function trim() {
    response = await quickFetch('trim', 0, 0, 0);

    console.log("trimmed");
}

async function combine() {
    response = await quickFetch('combine', 0, 0, 0)

    console.log("combined");
}

// REFRESH_INTERVAL = 0.5;

// setInterval(() => {
//     updateProgress();
//  }, REFRESH_INTERVAL * 1000)