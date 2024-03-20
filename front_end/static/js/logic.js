
baseUrl = "http://127.0.0.1:5000"

// Creating the map object
let myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 4
  });
  
  // Adding the tile layer
 let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  
// Create a chooseradius function:
function markerSize(price) {
    return Math.sqrt(price)*100;
}






    d3.json(baseUrl+"/api/v1.0/state").then(data => { 
        console.log(data)
        for (let i= 0; i<data.length; i++) {
       
                L.circle([data[i]['lat'], data[i]['lon']], {
                    stroke: false,
                    fillOpacity: 0.5,
                    color: 'white',
                    fillColor: 'red',
                    radius: markerSize(data[i]['price'])
                }).bindPopup(`<h2>State: ${data[i]["state"]}</h2> <hr> <h3>Price: ${data[i]['price'].toLocaleString()}</h3> `).addTo(myMap)
          
    
        } 
    
      
    }) 
    







