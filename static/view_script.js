var map;
var bounds;

function loadMapScenario() {
    var top_left = new Microsoft.Maps.Location(44.984204, -93.249469);
    var bottom_right = new Microsoft.Maps.Location(44.966457, -93.215558);
    bounds = Microsoft.Maps.LocationRect.fromLocations(top_left, bottom_right);
    map = new Microsoft.Maps.Map(document.getElementById('myMap'), {maxBounds: bounds,
        credentials:"AkqvQ6FOF6sIQ8L4KcoHPmwFoGHipTvcwbpgQEJho8KJMA5_ep6OLKv2x9XakjJh"});
    let reports = document.getElementsByClassName('report');
    for (let i = 0; i < reports.length; i++) {
        const loc = new Microsoft.Maps.Location(parseFloat(reports[i].children.reportLat.innerText), parseFloat(reports[i].children.reportLong.innerText));
        let pin = new Microsoft.Maps.Pushpin(loc, {
            title: reports[i].children.reportName.innerText,
            subTitle: reports[i].children.reportDescription.innerText,
            text: reports[i].children.reportID.innerText
        });
        map.entities.push(pin);
    }
}


