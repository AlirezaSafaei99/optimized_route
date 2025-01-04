# Route Optimization with Shortest Path 🚗🗺️

This project calculates and visualizes the shortest driving route between two locations using the OpenStreetMap data. The project leverages `osmnx` and `networkx` libraries to compute the shortest path based on road lengths and visualizes the path on an interactive map using `ipyleaflet`.

## 🚀 Features

- **Shortest Path Calculation:**
  - Determines the shortest route between two locations based on road length.
  - Origin and destination locations are automatically snapped to the nearest nodes in the road network.

- **Interactive Map Visualization:**
  - Displays the shortest route between two points on a dynamically generated map.
  - Adds markers to indicate the origin and destination locations.

- **Customizable Locations:**
  - Allows users to define their own origin and destination coordinates.

- **Optimized for Driving:**
  - Uses a "drive" network type for accurate route calculations based on drivable roads.
