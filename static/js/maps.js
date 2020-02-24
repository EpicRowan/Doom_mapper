"use strict";


// We use a function declaration for initMap because we actually *do* need
// to rely on value-hoisting in this circumstance.

var map;
      function initMap() {
        map = new google.maps.Map
        (document.querySelector('#map'), {
          center: {lat: 37.773972, lng: -122.431297},
           styles:  [
            {elementType: 'geometry', stylers: [{color: "#212121"}]},
            {elementType: 'labels.text.stroke', stylers: [{color: "#212121"}]},
            {elementType: 'labels.text.fill', stylers: [{color: "#757575"}]},
            {elementType: 'labels.icon', stylers: [{"visibility": "off"}]},
            {
              featureType: 'administrative.locality',
              elementType: 'labels.text.fill',
              stylers: [{color: "#9e9e9e"}]
            },
            {
              featureType: 'poi',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'geometry',
              stylers: [{color: '#212121'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'labels.text.fill',
              stylers: [{color: '#6b9a76'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry',
              stylers: [{color: "#2c2c2c"}]
            },
            {
              featureType: 'road',
              elementType: 'geometry.stroke',
              stylers: [{color: '#212a37'}]
            },
            {
              featureType: 'road',
              elementType: 'labels.text.fill',
              stylers: [{color: '#9ca5b3'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry',
              stylers: [{color: '#746855'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry.stroke',
              stylers: [{color: '#1f2835'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'labels.text.fill',
              stylers: [{color: '#f3d19c'}]
            },
            {
              featureType: 'transit',
              elementType: 'geometry',
              stylers: [{color: '#2f3948'}]
            },
            {
              featureType: 'transit.station',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'water',
              elementType: 'geometry',
              stylers: [{color: '#c3d0e4'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.fill',
              stylers: [{color: '#515c6d'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.stroke',
              stylers: [{color: '#17263c'}]
            }
          ]
        });
        var overlay = new google.maps.KmlLayer({ 
    url: 'https://data.sfgov.org/api/geospatial/7ahv-68ap?method=export&format=KML', 
    preserveViewport: false,
    map: map 
  }); 

google.maps.event.addListenerOnce(map, 'zoom_changed', function() {
    // set the zoom level to 13
    map.setZoom(13);
});
     
var markerGroups = {
    "tall": [],
        "monumentos": [],
        "restaurantes": [],
        "hotel": []
};

  $.get("/api/tallbuildings", (tallbuildings) => {
    
    for (const tall of tallbuildings) {
  
      
      const tallMarker = new google.maps.Marker({
        position: {
          lat: parseFloat(tall.latitude),
          lng: parseFloat(tall.longitude)
        },
        title: `${tall.name}`,
        type: "tall",
        // url: 'http://localhost:5000/search',
        icon: {
          url: 'https://upload.wikimedia.org/wikipedia/commons/7/7b/WhiteDot.svg',
          scaledSize: new google.maps.Size(10, 10)
        },
        map: map,
      });

      markerGroups["tall"].push(tallMarker);


      google.maps.event.addListener(tallMarker, 'click', function() {
      window.location.href = this.url;
    });


    }
  })

  console.log(markerGroups["tall"])

    $.get("/api/softbuildings", (softbuildings) => {
      // console.log(softbuildings)
    for (const soft of softbuildings) {

      const softMarker = new google.maps.Marker({
        position: {
          lat: parseFloat(soft.latitude),
          lng: parseFloat(soft.longitude)
        },
        title: `${soft.address}`,
       icon: {
          url: 'https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg',
          scaledSize: new google.maps.Size(10, 10)
        },
        map: map,
      });

    }
  })



 function toggleGroup(type) {
    for (const marker of markerGroups[type]) {
        if (!marker.getVisible()) {
            marker.setVisible(true);
        } else {
            marker.setVisible(false);
        }
    }
}

    if (!markerGroups[type]) markerGroups[type] = [];
    markerGroups[type].push(marker);


// function check() {
//   $('input[type="checkbox"]').prop("checked", true).change();
// }

// function uncheck() {
//   $('input[type="checkbox"]').prop("checked", false).change();
// }



 // $('#show_ss').change(function() {       
 //     softMarker.setVisible($(this).is(":checked"));               
 // });



  }
    
  
  