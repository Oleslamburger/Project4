// Creating the map object
let myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 4
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

// Load the GeoJSON data.
let geoData = 'http://127.0.0.1:5000/api/v1.0/state_geojson';

let geojson;

// Get the data with d3.
d3.json(geoData).then(function(data) {

  // Create a new choropleth layer.
  geojson = L.choropleth(data, {

    // Define which property in the features to use.
    valueProperty: "price",

    // Set the color scale.
    scale: ["white", "blue"],

    // The number of breaks in the step range
    steps: 12,

    // q for quartile, e for equidistant, k for k-means
    mode: "e",
    style: {
      // Border color
      color: "#fff",
      weight: 2,
      fillOpacity: 0.7
    },

    // Binding a popup to each layer
    onEachFeature: function(feature, layer) {
      layer.bindPopup("<strong>" + "State: "+ feature.properties.name + "</strong><hr>The Average Price Of Sold Houses: $" +d3.format('.2f') (feature.properties.price));
    }
  }).addTo(myMap);

  // Set up the legend.
  let legend = L.control({ position: "bottomright" });
  legend.onAdd = function() {
    let div = L.DomUtil.create("div", "info legend");
    let limits = geojson.options.limits;
    let colors = geojson.options.colors;
    let labels = [];

    // Add the minimum and maximum.
    let legendInfo = "<h1>Avg Price For Each State</h1>" +
      "<div class=\"labels\">" +
        "<div class=\"min\">"  +d3.format('.2f')(limits[0]) + "</div>" +
        "<div class=\"max\">"  +d3.format('.2f')(limits[limits.length - 1]) + "</div>" +
      "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function(limit, index) {
      labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;
  };

  // Adding the legend to the map
  legend.addTo(myMap);

});
