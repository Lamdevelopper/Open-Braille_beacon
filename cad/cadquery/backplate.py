"""
Open Braille Beacon - wall tag backplate.

Parametric CadQuery model for the base plate. Units are millimeters.
Run from this directory with:

    python backplate.py

Requires CadQuery. The script exports STEP/STL when CadQuery is available.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BackplateParams:
    length: float = 40.0
    width: float = 35.0
    thickness: float = 2.5
    corner_radius: float = 6.0
    rim_height: float = 1.5
    rim_thickness: float = 1.0
    print_clearance: float = 0.3
    screw_hole_diameter: float = 3.2
    boss_outer_diameter: float = 5.5
    boss_height: float = 5.6
    screw_spacing_x: float = 25.0
    screw_spacing_y: float = 30.0
    pcb_length: float = 32.0
    pcb_width: float = 26.0
    pcb_thickness: float = 1.6
    battery_diameter: float = 20.0
    battery_cavity_diameter: float = 21.0
    battery_holder_length: float = 24.0
    battery_holder_width: float = 22.0
    battery_holder_height: float = 5.0
    reed_pocket_length: float = 12.0
    reed_pocket_width: float = 3.0
    reed_pocket_height: float = 3.0
    reed_x: float = 15.0
    reed_y: float = 0.0
    vhb_length: float = 30.0
    vhb_width: float = 25.0
    vhb_recess_depth: float = 0.3
    antenna_keepout_length: float = 12.0
    antenna_keepout_width: float = 8.0
    antenna_y: float = 11.5


P = BackplateParams()


def rounded_box(cq, length, width, height, corner_radius):
    return (
        cq.Workplane("XY")
        .box(length, width, height, centered=(True, True, False))
        .edges("|Z")
        .fillet(corner_radius)
    )


def build_backplate(params=P):
    import cadquery as cq

    p = params
    part = rounded_box(cq, p.length, p.width, p.thickness, p.corner_radius)

    vhb_cut = (
        cq.Workplane("XY")
        .box(p.vhb_length, p.vhb_width, p.vhb_recess_depth + 0.05, centered=(True, True, False))
        .translate((0, 0, -0.02))
    )
    part = part.cut(vhb_cut)

    rim_outer_length = p.length - 2 * p.print_clearance
    rim_outer_width = p.width - 2 * p.print_clearance
    rim_inner_length = rim_outer_length - 2 * p.rim_thickness
    rim_inner_width = rim_outer_width - 2 * p.rim_thickness
    rim_outer = (
        cq.Workplane("XY")
        .box(rim_outer_length, rim_outer_width, p.rim_height, centered=(True, True, False))
        .translate((0, 0, p.thickness))
    )
    rim_inner = (
        cq.Workplane("XY")
        .box(rim_inner_length, rim_inner_width, p.rim_height + 0.2, centered=(True, True, False))
        .translate((0, 0, p.thickness - 0.1))
    )
    part = part.union(rim_outer.cut(rim_inner))

    screw_positions = [
        (-p.screw_spacing_x / 2, -p.screw_spacing_y / 2),
        (p.screw_spacing_x / 2, -p.screw_spacing_y / 2),
        (-p.screw_spacing_x / 2, p.screw_spacing_y / 2),
        (p.screw_spacing_x / 2, p.screw_spacing_y / 2),
    ]
    for x, y in screw_positions:
        boss = (
            cq.Workplane("XY")
            .circle(p.boss_outer_diameter / 2)
            .extrude(p.boss_height)
            .translate((x, y, p.thickness))
        )
        hole = (
            cq.Workplane("XY")
            .circle(p.screw_hole_diameter / 2)
            .extrude(p.boss_height + p.thickness + 0.4)
            .translate((x, y, -0.2))
        )
        part = part.union(boss).cut(hole)

    battery_ring_outer = (
        cq.Workplane("XY")
        .circle(p.battery_cavity_diameter / 2)
        .extrude(1.0)
        .translate((0, 0, p.thickness))
    )
    battery_ring_inner = (
        cq.Workplane("XY")
        .circle(p.battery_diameter / 2)
        .extrude(1.2)
        .translate((0, 0, p.thickness - 0.1))
    )
    part = part.union(battery_ring_outer.cut(battery_ring_inner))

    reed_pocket = (
        cq.Workplane("XY")
        .box(p.reed_pocket_width, p.reed_pocket_length, p.reed_pocket_height, centered=(True, True, False))
        .translate((p.reed_x, p.reed_y, p.thickness))
    )
    part = part.union(reed_pocket)

    antenna_keepout = (
        cq.Workplane("XY")
        .box(p.antenna_keepout_length, p.antenna_keepout_width, 0.25, centered=(True, True, False))
        .translate((0, p.antenna_y, p.thickness + 0.05))
    )
    part = part.union(antenna_keepout)

    pcb_posts = [
        (-p.pcb_length / 2 + 3, -p.pcb_width / 2 + 3),
        (p.pcb_length / 2 - 3, -p.pcb_width / 2 + 3),
        (-p.pcb_length / 2 + 3, p.pcb_width / 2 - 3),
        (p.pcb_length / 2 - 3, p.pcb_width / 2 - 3),
    ]
    for x, y in pcb_posts:
        post = (
            cq.Workplane("XY")
            .box(2.2, 2.2, 1.8, centered=(True, True, False))
            .translate((x, y, p.thickness))
        )
        part = part.union(post)

    return part


def export_model():
    import cadquery as cq

    model = build_backplate(P)
    root = Path(__file__).resolve().parents[1]
    step_path = root / "exports" / "step" / "backplate.step"
    stl_path = root / "exports" / "stl" / "backplate.stl"
    step_path.parent.mkdir(parents=True, exist_ok=True)
    stl_path.parent.mkdir(parents=True, exist_ok=True)
    cq.exporters.export(model, str(step_path))
    cq.exporters.export(model, str(stl_path), tolerance=0.05, angularTolerance=0.15)

    bb = model.val().BoundingBox()
    print("backplate exported")
    print(f"STEP: {step_path}")
    print(f"STL:  {stl_path}")
    print(f"Bounding box: {bb.xlen:.2f} x {bb.ylen:.2f} x {bb.zlen:.2f} mm")
    print(f"Screw centers: {P.screw_spacing_x:.2f} x {P.screw_spacing_y:.2f} mm")
    print(f"VHB recess: {P.vhb_length:.2f} x {P.vhb_width:.2f} x {P.vhb_recess_depth:.2f} mm")
    print(f"Antenna keep-out marker center: x=0.00, y={P.antenna_y:.2f} mm")


if __name__ == "__main__":
    export_model()
