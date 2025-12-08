// Bookcube for Bookrobot System
// Size: 0.35m(W) x 0.33m(D) x 0.30m(H)
// Top and Front: OPEN
// Bottom: 2 circular holes at side edges (10mm diameter)

// Dimensions (in mm for OpenSCAD)
width = 350;
depth = 330;
height = 300;
bottom_thickness = 30;
wall_thickness = 10;

// Hole parameters
hole_diameter = 20;  // 20mm (2cm) diameter holes
hole_x_offset = 155; // holes at ±155mm from center (total distance 310mm = 31cm)

module bookcube() {
    difference() {
        union() {
            // Bottom plate (thick)
            translate([0, 0, bottom_thickness/2])
                cube([width, depth, bottom_thickness], center=true);

            // Left side wall
            translate([-width/2 + wall_thickness/2, 0, bottom_thickness + height/2])
                cube([wall_thickness, depth, height], center=true);

            // Right side wall
            translate([width/2 - wall_thickness/2, 0, bottom_thickness + height/2])
                cube([wall_thickness, depth, height], center=true);

            // Back wall
            translate([0, -depth/2 + wall_thickness/2, bottom_thickness + height/2])
                cube([width - 2*wall_thickness, wall_thickness, height], center=true);
        }

        // Left hole (circular, through bottom plate)
        translate([-hole_x_offset, 0, -1])
            cylinder(h=bottom_thickness + 2, d=hole_diameter, center=false, $fn=32);

        // Right hole (circular, through bottom plate)
        translate([hole_x_offset, 0, -1])
            cylinder(h=bottom_thickness + 2, d=hole_diameter, center=false, $fn=32);
    }
}

// Create the model
bookcube();
