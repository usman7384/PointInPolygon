# Point-in-Polygon Checker using Ray-Casting Algorithm

This project implements a **Point-in-Polygon** checker using the **Ray-Casting Algorithm**. It determines whether a given point lies inside a polygon by counting how many times a ray extending from the point intersects with the polygon's edges.

## Features
- Uses geometric properties such as **orientation** and **line segment intersection**.
- Handles convex and concave polygons.
- Visualizes the polygon and test point using `matplotlib`.
- Implements an efficient algorithm with **O(n) complexity**, where `n` is the number of polygon vertices.

## How It Works
1. A polygon is defined as a list of `(x, y)` coordinates.
2. A horizontal ray extending infinitely to the right from the test point is created.
3. The number of times this ray intersects with the polygon's edges is counted.
4. If the count is **odd**, the point is **inside**; if **even**, the point is **outside**.


## Code Explanation
### Key Functions
- **`on_and_between(pt1, pt3, pt2) -> bool`**
  - Checks if `pt3` lies on the line segment between `pt1` and `pt2`.

- **`orientation(pt1, pt2, pt3) -> int`**
  - Determines if three points form a clockwise, counterclockwise, or collinear alignment.

- **`Intersect(pt1, pt2, pt3, pt4) -> bool`**
  - Checks if two line segments intersect using orientation logic.

- **`isInside(coords, p) -> bool`**
  - Implements the **Ray-Casting Algorithm** to determine if point `p` is inside the polygon.

### Visualization
The script plots the polygon and the test point using `matplotlib`, along with a dashed red line representing the ray.

## Example
Given the polygon:
```python
polygon = [(0, 0), (10, 0), (10, 10), (0, 10), (2, 6), (8, 6)]
```
And test point:
```python
p = (4, 2)
```
Output:
```
Outside the Polygon
```
