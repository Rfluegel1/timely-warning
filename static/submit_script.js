
var map;
var bounds;
var lat = document.getElementById('lat');
var lon = document.getElementById('lon');
pushpin = null;


function loadMapScenario() {
  var top_left = new Microsoft.Maps.Location(44.984204, -93.249469);
  var bottom_right = new Microsoft.Maps.Location(44.966457, -93.215558);
  bounds = Microsoft.Maps.LocationRect.fromLocations(top_left, bottom_right);
  map = new Microsoft.Maps.Map(document.getElementById('myMap'), {maxBounds: bounds,
  credentials:"AkqvQ6FOF6sIQ8L4KcoHPmwFoGHipTvcwbpgQEJho8KJMA5_ep6OLKv2x9XakjJh"});
    Microsoft.Maps.Events.addHandler(map, 'click', function(e) {
      map.entities.remove(pushpin);
      var point = new Microsoft.Maps.Point(e.getX(), e.getY());
      var loc = e.target.tryPixelToLocation(point);
      var location = new Microsoft.Maps.Location(loc.latitude, loc.longitude);
      lat.value = loc.latitude;
      lon.value = loc.longitude;
      pushpin = new Microsoft.Maps.Pushpin(location, {'draggable': false});
      map.entities.push(pushpin);
    });
}
