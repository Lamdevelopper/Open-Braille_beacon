# Open Braille Beacon CAD Models

Parametric CadQuery models for the wall beacon tag.

## Files

- `top_cover.py`: exterior top shell with LED window, lower alignment lip, and optional screw bosses.
- `backplate.py`: base plate with rim, screw bosses, VHB recess, CR2032 marker, reed switch pocket, PCB posts, and antenna keep-out marker.
- `assembly.py`: conceptual assembly with placeholders for PCB, CR2032, reed switch, light pipe, and adhesive pad.

## Export

Install CadQuery, then run:

```powershell
python cad\cadquery\top_cover.py
python cad\cadquery\backplate.py
python cad\cadquery\assembly.py
```

Exports are written to:

- `cad/exports/step/`
- `cad/exports/stl/`

## Design Intent

The model follows the current reference target:

- Exterior footprint: `40 x 35 mm`
- Total assembled height: about `12 mm`
- Top cover height: `8 mm`
- Backplate thickness: `2.5 mm`
- Exterior corner radius: `R6`
- Top fillet: about `R2`
- Wall thickness: `2 mm`
- 3D-print clearance: `0.3 mm`

The antenna keep-out is modeled as a small raised marker, not a physical metal feature. Keep copper, battery, screw heads, and large ground pours away from the antenna area in the real PCB.
