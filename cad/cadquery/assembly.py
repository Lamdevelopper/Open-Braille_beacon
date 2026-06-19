"""
Open Braille Beacon - conceptual wall tag assembly.

This combines the top cover and backplate with simple placeholders for the
PCB, CR2032 cell, reed switch, LED light pipe, and adhesive pad.
"""

from pathlib import Path

from backplate import BackplateParams, build_backplate
from top_cover import TopCoverParams, build_top_cover


def build_assembly():
    import cadquery as cq

    top_p = TopCoverParams()
    base_p = BackplateParams()

    top = build_top_cover(top_p).translate((0, 0, base_p.thickness + base_p.rim_height + 0.2))
    base = build_backplate(base_p)

    pcb = (
        cq.Workplane("XY")
        .box(base_p.pcb_length, base_p.pcb_width, base_p.pcb_thickness, centered=(True, True, False))
        .translate((0, 0, base_p.thickness + 2.0))
    )
    battery = (
        cq.Workplane("XY")
        .circle(base_p.battery_diameter / 2)
        .extrude(3.2)
        .translate((0, 0, base_p.thickness + 2.2))
    )
    reed = (
        cq.Workplane("XY")
        .box(base_p.reed_pocket_width, base_p.reed_pocket_length, base_p.reed_pocket_height, centered=(True, True, False))
        .translate((base_p.reed_x, base_p.reed_y, base_p.thickness + 1.2))
    )
    light_pipe = (
        cq.Workplane("XY")
        .box(top_p.led_window_length - 0.4, top_p.led_window_width - 0.3, 0.8, centered=(True, True, False))
        .translate((0, top_p.width / 2 - top_p.led_window_from_top_edge, base_p.thickness + base_p.rim_height + top_p.height - 0.6))
    )
    adhesive = (
        cq.Workplane("XY")
        .box(base_p.vhb_length, base_p.vhb_width, 0.6, centered=(True, True, False))
        .translate((0, 0, -0.6))
    )

    return (
        cq.Assembly(name="open_braille_beacon_wall_tag_v1")
        .add(base, name="backplate_abs_asa")
        .add(top, name="top_cover_abs_asa")
        .add(pcb, name="pcb_placeholder_32x26x1p6", color=cq.Color(0.05, 0.25, 0.12, 1))
        .add(battery, name="cr2032_placeholder", color=cq.Color(0.55, 0.55, 0.55, 1))
        .add(reed, name="reed_switch_placeholder", color=cq.Color(0.1, 0.1, 0.1, 1))
        .add(light_pipe, name="led_light_pipe_placeholder", color=cq.Color(0.4, 1.0, 0.75, 0.8))
        .add(adhesive, name="3m_vhb_pad_placeholder", color=cq.Color(0.8, 0.05, 0.05, 1))
    )


def export_model():
    import cadquery as cq

    assembly = build_assembly()
    root = Path(__file__).resolve().parents[1]
    step_path = root / "exports" / "step" / "wall_tag_assembly.step"
    step_path.parent.mkdir(parents=True, exist_ok=True)
    assembly.save(str(step_path), exportType="STEP")
    print("assembly exported")
    print(f"STEP: {step_path}")
    print("Nominal exterior: 40.00 x 35.00 x about 12.20 mm")


if __name__ == "__main__":
    export_model()
