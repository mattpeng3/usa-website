
var District = L.tileLayer(
  'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + 'pk.eyJ1Ijoic2hlZXBpbmF2IiwiYSI6ImNqZHA2bnFrMjBjYnoycm80M3BiaW1lc3EifQ.3MflXoZep5Hlr1ryAomj9A', {
   id: 'mapbox.light',
});

// TOPOJSON IMPLEMENTATION STARTS
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

var map = L.map('map', {zoomSnap: 0.1,
                        zoomControl: true,
                        renderer: L.canvas(),
						layers: [District]});
map.zoomControl.setPosition('topright');

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
var costWeight = 0.25;
var safetyWeight = 0.25;
var travelWeight = 0.25;
var schoolWeight = 0.25;
function addTopoData(topoData) {
	topoLayer.addData(topoData);
	topoLayer.addTo(map);
	topoLayer.eachLayer(handleLayer);
}

function handleLayer(layer) {
	// TODO: Fix colors
	//console.log("SCORES ");
	// console.log("cost: " + layer.feature.properties.cost + "\nsafety: " + layer.feature.properties.safety + "\n travel: " + layer.feature.properties.travel + "\nschool: " + 	layer.properties.feature.school_system);
	const colorValue = 	costWeight*layer.feature.properties.cost +
						safetyWeight*layer.feature.properties.safety +
						travelWeight*layer.feature.properties.travel +
						schoolWeight*layer.feature.properties.school_system;
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
		document.getElementById("countyContent").innerHTML = countyName;
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
		map.flyToBounds(e.target.getBounds(),{padding:[100,100]});
		error(); // Jank but necessary workaround
	}

	function showinfo(e) {
		info.update(e.target.feature.properties);
		if (!leftVisible)
			toggleSidebar();
	}

	var info = L.control();

	// kk: I wanted to delete this function but leaflet errors without it...
	info.onAdd = function (map) {
		this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
		return this._div;
	};

	info.update = function (props) {
		if (props) {
			for (var i = 0; i < parameters.length; i++) {
        if (i != 1 && !props[parameters[i]['val']]) {
          document.getElementById(parameters[i]['id']).innerHTML = "N/A";
        } else if (i == 5) {
          document.getElementById(parameters[i]['id']).innerHTML = props[parameters[i]['val']].toFixed(1);
        } else if (i == 4) { //rounding for school district score
					document.getElementById(parameters[i]['id']).innerHTML = (props[parameters[i]['val']]* 10).toFixed(1);
				} else if (i == 2 || i == 3) {
          document.getElementById(parameters[i]['id']).innerHTML = "$" + props[parameters[i]['val']];
        } else if (i == 1) {
          document.getElementById(parameters[i]['id']).innerHTML = colorValue.toFixed(1);
        } else {
					document.getElementById(parameters[i]['id']).innerHTML = props[parameters[i]['val']];
				}
			}
		}
	};

  info.addTo(map);
}; //end handleLayer

//END TopoJSON

//adding reset button
ResetButton = L.easyButton( {
  position:'topright',
  states:[{
    icon: '<strong>Reset Map</strong>',
    onClick: function(){
      reset();
    }
  }]
}).addTo(map);
ResetButton.button.style.width = '100px';

function reset() {
	map.flyTo([37.278,-119.418], 6.4);
}
var legend = L.control({ position: 'bottomright' });
legend.onAdd = function (map) {
	// KK: We can make this much simpler by portin this to the HTML
	var div = L.DomUtil.create('div', 'info legend');
	var labels = []
	/* Add min & max*/
	div.innerHTML = '<div id="legend"><h3 style="font-weight:bolder;font-size:larger; text-align:center;">Preference Scale</h3></div>\
		<div ><img src="data:image/png;base64,\
		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20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyIgeG1wOkNyZWF0ZURhdGU9IjIwMTgtMDQtMTNUMjA6NTQ6MjktMDc6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDE4LTA0LTI2VDE3OjI4OjUxLTA3OjAwIiB4bXA6TWV0YWRhdGFEYXRlPSIyMDE4LTA0LTI2VDE3OjI4OjUxLTA3OjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9IkRpc3BsYXkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6ZDk2N2FmYmEtOTMyNC00YjViLTk3ZWEtZjRlMDJiM2Y5M2Q4IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOmQ0ODQ2NmZjLTk1ODUtNDQ3My1iYjBlLWQwMDZjNjNmNGNlYyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOmQ0ODQ2NmZjLTk1ODUtNDQ3My1iYjBlLWQwMDZjNjNmNGNlYyIgZXhpZjpQaXhlbFhEaW1lbnNpb249Ijc3MCIgZXhpZjpQaXhlbFlEaW1lbnNpb249IjY4Ij4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6ZDQ4NDY2ZmMtOTU4NS00NDczLWJiMGUtZDAwNmM2M2Y0Y2VjIiBzdEV2dDp3aGVuPSIyMDE4LTA0LTEzVDIxOjAyOjQyLTA3OjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoTWFjaW50b3NoKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6ZDk2N2FmYmEtOTMyNC00YjViLTk3ZWEtZjRlMDJiM2Y5M2Q4IiBzdEV2dDp3aGVuPSIyMDE4LTA0LTI2VDE3OjI4OjUxLTA3OjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgMjAxOCAoTWFjaW50b3NoKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4I+GrwAAABP0lEQVRoge2bOW7DQAxFn4KcxDlQ7uuz6BgpbItLilk0ch0gAPFfIXATSY0+1Gnb9x0hqvDx3wsI8ZdI0KIUn9O63b4scrpHJHDEBpg3u6c8EnDvbst6ALidBb3YewpIz9F8S2OtAcJz9sxhtHvzyIvr7a4E3vpM1zNnqxmMsUDYOmJUHgARZ83s34KtoGcj07bRNgD3bR2BjZ393H8297l2O0zL9THDCTvPMG2piYQz24OvOWs8yytjHtp4AfHKfIzgYwSfGT/jDYGTQBLTDmKkYnWDsS3+lmrFgY+CHjc8LzUOOAZEv85Zx3WWLUEDElv6PO/7d7P1hRalkKBFKSRoUQoJWpRCghalkKBFKSRoUQoJWpRCghalkKBFKSRoUQoJWpRCghalkKBFKSRoUYpNv2CJSugLLUohQYtS/AJXh+1VzIjB9gAAAABJRU5ErkJggg==" alt="" style="width: 100%;"></div><div class="labels"><span class="domain-min">Low Pref</span>\
		<span class="domain-max">High Pref</span>\
    </div>'
	return div
}
legend.addTo(map);
// legend.style.width = '400px';
function recalculate() {
   var sum = parseInt($('#slideCost').val()) + parseInt($('#slideSafety').val()) + parseInt($('#slideTravel').val()) + parseInt($('#slideSchool').val());
   costWeight = $('#slideCost').val() / sum;
   safetyWeight = $('#slideSafety').val() / sum;
   travelWeight = $('#slideTravel').val() / sum;
   schoolWeight = $('#slideSchool').val() / sum;
   topoLayer.eachLayer(handleLayer);
}

function initMap(x,y) {
	var geocoder = new google.maps.Geocoder();
	document.getElementById('address').addEventListener('keydown', function(event) {
			if (event.which == 13)
				geocodeAddress(geocoder, map);
		});

	document.getElementById("submit").addEventListener('click', function() {
			geocodeAddress(geocoder, map);
		});
}
//Initial Overlay Code:
function titleOverlay() {
    var geocoder = new google.maps.Geocoder();
  document.getElementById("submitTitle").addEventListener('click', function() {
    console.log(geocoder);
    geocodeTitleOverlayAddress(geocoder, map);
    document.getElementById("overlay").style.display = "none";
    toggleSidebar();
    toggleDropdown();
    });
  document.getElementById('addressTitle').addEventListener('keydown', function(event) {
    if (event.which == 13) {
      geocodeTitleOverlayAddress(geocoder, map);
			document.getElementById("overlay").style.display = "none";
      toggleSidebar();
      toggleDropdown();
		}
  });
}
function removeTitleOverlay(){
    document.getElementById('addressTitle').removeEventListener()
    document.getElementById('submitTitle').removeEventListener()
    delete google.maps.Geocoder();
}

function geocodeAddress(geocoder, resultsMap) {
	var addr = document.getElementById('address').value;
	addr = addr.concat(", CA");
	geocoder.geocode({address: addr,
					  componentRestrictions: {
						country: 'USA',
					  }
					 }, function(results, status) {
						if (status === 'OK') {
							map.flyTo([results[0].geometry.location.lat(),
							results[0].geometry.location.lng()], 12);
						} else {
							alert('Geocode was not successful for the following reason: ' + status);
						}
					});
}

function geocodeTitleOverlayAddress(geocoder, resultsMap) {
	var addr = document.getElementById('addressTitle').value;
	addr = addr.concat(", CA");
	geocoder.geocode({address: addr,
					  componentRestrictions: {
						country: 'USA',
					  }
					 }, function(results, status) {
						if (status === 'OK') {
							map.flyTo([results[0].geometry.location.lat(),
							results[0].geometry.location.lng()], 12);
						} else {
							alert('Geocode was not successful for the following reason: ' + status);
						}
					});
}


//TODO clear map colors and revert to base map
function clearmap() {
	$('#slideCost').val(5);
	$("#slideCost").trigger('change');
	$('#slideTravel').val(5);
	$("#slideTravel").trigger('change');
	$('#slideSafety').val(5);
	$("#slideSafety").trigger('change');
	$('#slideSchool').val(5);
	$("#slideSchool").trigger('change');
	recalculate();
}



var leftVisible = false;
function toggleSidebar() {
	var sidebar = document.getElementById("leftsidebar");
	var button = document.getElementById("toggleSidebar");
	var dropdown = document.getElementById("dropdownWindow");
	var button2 = document.getElementById("toggleDropdown");
	if (leftVisible) {
		sidebar.style.left = "-420px";
		button.style.left = "0%";
		button.style.transform = "scale(1, 1)";

		// dropdown.style.width = "calc(100% - 20px)";
		// button2.style.width = "calc(100% - 20px)";
		// dropdown.style.left = "420px";
		// button2.style.left = "420px";
	} else {
		sidebar.style.left = "0%";
		button.style.left = "420px";
		button.style.transform = "scale(-1,1)";

		// dropdown.style.width = "80%";
		// button2.style.width = "80%";
		// dropdown.style.left = "calc(420px + 20px)";
		// button2.style.left = "calc(420px + 20px)";
	}
	leftVisible = !leftVisible;
}

var botVisible = false;
function toggleDropdown() {
	var dropdown = document.getElementById("dropdownWindow");
	var button = document.getElementById("toggleDropdown");
  var sidebar = document.getElementById("leftsidebar");
  var button2 = document.getElementById("toggleSidebar");
	if (botVisible) {
		dropdown.style.bottom = "-25%";
    dropdown.style.left = "0px";
    dropdown.style.width = "100%";
		button.style.bottom = "0%";
    button.style.left = "0px";
    button.style.width = "100%";
		button.style.transform = "scale(1, 1)";

    sidebar.style.height = "calc(100% - 20px)";
    button2.style.height = "calc(100% - 20px)";
    // sidebar.style.transform = "scale(1, 1)";
    //button2.style.transform = "scale(1, 1)";
	} else {
		dropdown.style.bottom = "0%";
    dropdown.style.left = "0px";
    dropdown.style.width = "100%";
		button.style.bottom = "25%";
    button.style.left = "0px";
    button.style.width = "100%";
		button.style.transform = "scale(1,-1)";

    sidebar.style.height = "calc(75% - 20px)";
    button2.style.height = "calc(75% - 20px)";
    // sidebar.style.transform = "scale(-1, 1)";
    //button2.style.transform = "scale(1, -1)";
	}
	botVisible = !botVisible;
}

// Easteregg
var icounter = true;
function pat() {
	if (icounter) {
		document.getElementById("pat").style = "display:visible";
	} else {
		document.getElementById("pat").style = "display:none";
	}
	icounter = !icounter;
}
