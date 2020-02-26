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

console.log(markerGroups)


// Create the tall building markers and populate the map with the markers

  $.get("/api/tallbuildings", (tallbuildings) => {
    
    for (const tall of tallbuildings) {
      
      const tallMarker = new google.maps.Marker({
        position: {
          lat: parseFloat(tall.latitude),
          lng: parseFloat(tall.longitude)
        },
        title: `${tall.name}`,
        type: "tall",
        // url: '/buildings/search'
        icon: {
          url: 'https://upload.wikimedia.org/wikipedia/commons/4/48/Bluedot.svg',
          scaledSize: new google.maps.Size(5, 5)
        },
        map: map,
      });

      markerGroups["tall"].push(tallMarker);

// Create the event listener that will connect with the information page for tall buildings

      google.maps.event.addListener(tallMarker, 'click', function() {
      // window.location.href = this.url;
          
          url: '/buildings/search'

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
       icon: {
          url: 'https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg',
          scaledSize: new google.maps.Size(10, 10)
        },
        map: map,
      });

       markerGroups["soft"].push(softMarker);

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
                
}
let dataLayerChoice = document.getElementById('datacheckbox');
dataLayerChoice.addEventListener("click", function (evt) {
  let elem = evt.target;
  if (elem.id === "tall" || elem.id === "soft") {
    toggleGroup(elem.id);
}  else if (elem.id === "liq") {
    toggleKML()  
  }
    

               
// else
//     overlay.setMap(map); 

// }  else if (elem.id === "liq") {
//      overlay.setMap(null);
//   }
         
     

});

}
    
 


//   function toggleKml() {
// let kml = document.getElementById('datacheckbox');
// kml.addEventListener("click", function (evt) {
//   let elem = evt.target;
//         if (!document.getElementById('liq').checked)
//                 overlay.setMap(null);
//         else
//                 overlay.setMap(map);





// SIDELINES OF CODE

  // overlay.setMap(map);
  

         // overlay.addListener('click', function(event)

      // document.getElementById('liq').checked = true;

       // markerGroups["liq"].push(overlay);

// Add the liquefaction layer KML file on top of the initialized map

  //       let overlay = new google.maps.KmlLayer({ 
  //   url: 'https://data.sfgov.org/api/geospatial/7ahv-68ap?method=export&format=KML', 
  //   preserveViewport: false,
  //   map: map,

  // }); 
