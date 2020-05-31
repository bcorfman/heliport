from dataclasses import dataclass, field
from typing import List


@dataclass
class RoofSegment:
    units: int
    direction: str


@dataclass
class CandidateEdges:
    top: List[float]
    bottom: List[float]
    left: List[float]
    right: List[float]


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Rect:
    left: float
    top: float
    right: float
    bottom: float


@dataclass
class Circle:
    center: Point
    radius: float


@dataclass
class Roof:
    upper_right_segments: List[RoofSegment] = field(default_factory=list)
    upper_right_points: List[Point] = field(default_factory=list)
    bottom_left_segments: List[RoofSegment] = field(default_factory=list)
    bottom_left_points: List[Point] = field(default_factory=list)

