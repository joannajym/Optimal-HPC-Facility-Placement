# Optimal HPC Facility Placement

## Project Overview
In the wake of changing office dynamics post-Covid-19, with many corporate spaces underutilized, this project aims to strategically identify the optimal location for a new High-Performance Computing (HPC) facility within a large technology company's building. Given the constraints of maintaining social distancing and minimising occupancy disruption, the challenge is to select office sections with the lowest total occupancy probability for the HPC installation, ensuring minimal impact on the existing workforce and maximising space utilisation.

## Example usage
occupancy_probability = [
    [31, 54, 94, 34, 12],
    [26, 25, 24, 16, 87],
    [39, 74, 50, 13, 82],
    [42, 20, 81, 21, 52],
    [30, 43, 19, 5, 47],
    [37, 59, 70, 28, 15],
    [ 2, 16, 14, 57, 49],
    [22, 38, 9, 19, 99]
]

total_occupancy, selected_sections = select_sections(occupancy_probability)

print("Total Occupancy:", total_occupancy)

print("Selected Sections:", selected_sections)
