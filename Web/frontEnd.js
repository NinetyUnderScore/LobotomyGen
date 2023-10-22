videos = [];
videosTrimmed = [];

async function clearTrimmed() {
    const responce = await fetch('http://127.0.0.1:9900/', {
        method: 'POST',
        headers:{
        'Content-Type': 'application/x-www-form-urlencoded'
        },    
        body: new URLSearchParams({
            'command': 'clearTrimmed'
        })
    });

    videosTrimmed.length = 0
    console.log("cleared videosTrimmed")
}