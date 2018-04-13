
var District = L.tileLayer(
  'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + 'pk.eyJ1Ijoic2hlZXBpbmF2IiwiYSI6ImNqZHA2bnFrMjBjYnoycm80M3BiaW1lc3EifQ.3MflXoZep5Hlr1ryAomj9A', {
   id: 'mapbox.light',
});

//TOPOJSON IMPLEMENTATION STARTS
L.TopoJSON = L.GeoJSON.extend({
   addData: function(jsonData) {
     if (jsonData.type === "Topology") {
       for (key in jsonData.objects) {
         geojson = topojson.feature(jsonData, jsonData.objects[key]);
         L.GeoJSON.prototype.addData.call(this, geojson);
       }
     } else {
       L.GeoJSON.prototype.addData.call(this, jsonData);
     }
   }
});

// Put here to avoid breaking our "bad" code in earlier lines
'use strict' // "fool-proof" mechanism to avoid bad code

var map = L.map('map', {zoomSnap: 0.1,renderer: L.canvas(),
                       layers: [District]});
var topoLayer = new L.TopoJSON();

const colorScale = chroma
  //.bezier(['yellow','green','skyblue','blue'])
  .bezier(['white','skyblue','blue','darkblue'])
  .scale().correctLightness()
  .mode('lab')
  .domain([0,9]); //need to change to max value of properties later

var baseMaps = {
  };

var overlayMaps = {
    "District": District
  };

L.control.layers(baseMaps, overlayMaps).addTo(map);

District.addTo(map);
map.setView([37.278,-119.418],6);
map.setZoom(6.4);
// CHANGE THIS BACK WHEN GIVING TO SUSA
// $.getJSON('finaltracts.topo.json').done(addTopoData);
$.getJSON('https://raw.githubusercontent.com/SUSA-org/HousingCrisisAPP/master/finalTracts.topo.json').done(addTopoData);

function addTopoData(topoData) {
  topoLayer.addData(topoData);
  topoLayer.addTo(map);
  topoLayer.eachLayer(handleLayer);
}

function handleLayer(layer) {
  // TODO: Fix colors
  console.log("SCORES ");
  // console.log("cost: " + layer.feature.properties.cost + "\nsafety: " + layer.feature.properties.safety + "\n travel: " + layer.feature.properties.travel + "\nschool: " + layer.properties.feature.school_system);
  const colorValue = 0.25*layer.feature.properties.cost + 0.25*layer.feature.properties.safety +
                     0.25*layer.feature.properties.travel + 0.25*layer.feature.properties.school_system;
  const fillColor = colorScale(colorValue).hex();
  //console.log(colorValue);
  layer.setStyle({
    fillColor : fillColor,
    fillOpacity: .7,
    color:'#555',
    weight:1,
    opacity:.4
  });

  layer.on({
    mouseover: highlightFeature,
    mouseout: resetHighlight,
    dblclick: zoomToFeature,
    click: showinfo
  });

  function highlightFeature(){
    var countyName = layer.feature.properties.County;
    // console.log(countyName);
    this.bringToFront();
    this.setStyle({
      weight:2,
      opacity: 1,
      color: '#666',
      fillOpacity: 1
    });
  }

  function resetHighlight(){
    this.bringToBack();
    this.setStyle({
      weight:1,
      opacity:.5,
      fillColor:fillColor,
      fillOpacity:.7,
      color: '#555'
    });
    // info.update_loc();
  };

  function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds(),{padding:[100,100]});
    error(); // Jank but necessary workaround
  }

  function showinfo(e) {
    info.update(e.target.feature.properties);
  }

  var info = L.control();

  // kk: I wanted to delete this function but leaflet errors without it...
  info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    // this.update();
    return this._div;
  };

  info.update = function (props) {
  if (props) {
    for (var i = 0; i < parameters.length; i++) {
      if (i == 1) { //rounding for school district score
        document.getElementById(parameters[i]['id']).innerHTML = props[parameters[i]['val']].toFixed(4);
      } else {
        document.getElementById(parameters[i]['id']).innerHTML = props[parameters[i]['val']];
      }
    }
  }
  else {}
};

  info.update_loc = function (props) {
    this._div.innerHTML = '<h4>County Name</h4>' +   (props ?'<b>' + props.County : "");
    console.log(props.County);
  };

  info.addTo(map);
}; //end handleLayer

//END TopoJSON

function recalculate(layer) {
    // console.log($('#slideCost').val(),$('#slideSafety').val(),$('#slideTravel').val(),$('#slideSchool').val());
    var sum = 1.0 * ($('#slideCost').val() + $('#slideSafety').val() + $('#slideTravel').val() + $('#slideSchool').val());
    var cost = safety = travel = school = 0.0;
    cost = $('#slideCost').val() / sum;
    safety = $('#slideSafety').val() / sum;
    travel = $('#slideTravel').val() / sum;
    school = $('#slideSchool').val() / sum;
    // console.log("cost: " + 5000*cost + "\nsafety: " + 5000*safety + "\ntravel: " + 5000*travel + "\nschool: " + 5000*school);

    // Helper function for recalculate
    function newstyle(feature) {
      var weightedColor = 5000*cost*feature.properties.cost + 5000*safety*feature.properties.safety + 5000*travel*feature.properties.travel + 5000*school*feature.properties.school_system;
      return {
        fillColor: colorScale(weightedColor).hex(),
        weight: 2,
        opacity: 0.5,
        color: '#555',
        // dashArray: '3',
        fillOpacity: 0.7
      };
    }
  topoLayer.setStyle(newstyle);
}

function initMap() {
  var geocoder = new google.maps.Geocoder();

  document.getElementById('address').addEventListener('keydown', function(event) {
    if (event.which == 13)
      geocodeAddress(geocoder, map);
  });

  document.getElementById("submit").addEventListener('click', function() {
    geocodeAddress(geocoder, map);
  });
}

function geocodeAddress(geocoder, resultsMap) {
  var addr = document.getElementById('address').value;
  addr = addr.concat(", CA");
  geocoder.geocode({address: addr,
            componentRestrictions: {
            country: 'USA',
            }
           },
           function(results, status) {
            if (status === 'OK') {
              map.flyTo([results[0].geometry.location.lat(),
                   results[0].geometry.location.lng()], 12);
            } else {
              alert('Geocode was not successful for the following reason: ' + status);
            }
           });
}

function reset() {
  map.setView([37.278,-119.418], 6.4);
}

//TODO clear map colors and revert to base map
function clearmap(layer) {
  $('#slideCost').val(5);
  $("#slideCost").trigger('change');
  $('#slideTravel').val(5);
  $("#slideTravel").trigger('change');
  $('#slideSafety').val(5);
  $("#slideSafety").trigger('change');
  $('#slideSchool').val(5);
  $("#slideSchool").trigger('change');
  map.remove();
  handleLayer(layer);
}

// Easteregg
var icounter = true;
function pat() {
  if(icounter) {
    document.getElementById("pat").style = "display:visible";
  } else {
    document.getElementById("pat").style = "display:none";
  }
  icounter = !icounter;
}
