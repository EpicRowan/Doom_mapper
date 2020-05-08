"use strict";

// Initialize the map from the Google Maps API

var map;
      function initMap() {
        map = new google.maps.Map
        (document.querySelector('#map'), {
          center: {lat: 37.773972, lng: -122.431297},
          zoom: 13,
           styles:  MAPSTYLES,
        });

// Add the liquefaction layer KML file on top of the initialized map

        let overlay = new google.maps.KmlLayer({ 

    url: 'https://docs.google.com/uc?id=1eOG4xoRL7ZP9D52QWZ3jgDCozbKhHhTz&amp;export=kml', 
    preserveViewport: true,
    clickable: false,
    map: map,

  });  



// The KML layer resets the default zoom, so set the zoom again to 13 

google.maps.event.addListenerOnce(map, 'zoom_changed', function() {
    map.setZoom(13);
  
});

// Set the categories of the different Marker types and KML layer     

var markerGroups = {
    "tall": [],
        "soft": [],
        "liq": [],
        
};


// Create the tall building markers and populate the map with the markers

  $.get("/api/tallbuildings", (tallbuildings) => {
    
    for (const tall of tallbuildings) {
      console.log(tall.id)
      const tallMarker = new google.maps.Marker({
        position: {
          lat: parseFloat(tall.latitude),
          lng: parseFloat(tall.longitude)
        },
        title: `${tall.name}`,
        url: '/buildings/' + tall.id,
        icon: {
          url: 'https://upload.wikimedia.org/wikipedia/commons/4/48/Bluedot.svg',
          scaledSize: new google.maps.Size(7, 7)
        },
        map: map,
      });

      markerGroups["tall"].push(tallMarker);

// Create the event listener that will connect with the information page for tall buildings

      google.maps.event.addListener(tallMarker, 'click', function() {
      window.location.href = this.url;

    });

    }
  })


  // Create the soft story building markers and populate the map with the markers


    $.get("/api/softbuildings", (softbuildings) => {
      // console.log(softbuildings)
    for (const soft of softbuildings) {

      const softMarker = new google.maps.Marker({
        position: {
          lat: parseFloat(soft.latitude),
          lng: parseFloat(soft.longitude)
        },
        title: `${soft.address}`,
        url: '/buildings/' + soft.id,
       icon: {
          url: 'https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg',
          scaledSize: new google.maps.Size(10, 10)
        },
        map: map,

        // Attempt to log soft story markers in local storage 
        localStorage.setItem(softMarker);
      });


       markerGroups["soft"].push(softMarker);


      google.maps.event.addListener(softMarker, 'click', function() {
      window.location.href = this.url;

    });

    }
  })


  // Toggle the markers on and off depending on if the checkbox is checked or unchecked

 function toggleGroup(type) {
    for (const marker of markerGroups[type]) {
        if (!marker.getVisible()) {
            marker.setVisible(true);
        } else {
            marker.setVisible(false);
        }
    }
}  
function toggleKML() {
        if (!document.getElementById('liq').checked) {

          overlay.setMap(null); 
                
        } else {overlay.setMap(map);
        }

  // Main function for turning on or off markers and liquefaction zone    
                
}
let dataLayerChoice = document.getElementById('datacheckbox');
dataLayerChoice.addEventListener("click", function (evt) {
  let elem = evt.target;
  if (elem.id === "tall" || elem.id === "soft") {
    toggleGroup(elem.id);
}  else if (elem.id === "liq") {
    toggleKML()  
  }
          
     

});

}
    
 