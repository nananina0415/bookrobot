# lib_shelf Model

A complete library shelf unit combining a bookshelf frame with an organized array of bookcubes.

## Description

The `lib_shelf` model is a composite model that includes:
- **Bookshelf frame**: A wooden shelf structure with 6 levels
- **18 Bookcubes**: Arranged in 6 levels with 3 books per level

All components use consistent brown/wood coloring for a cohesive appearance.

## Structure

```
lib_shelf/
├── model.config    # Model metadata
└── model.sdf       # Complete model definition
```

## Usage

### In SDF World Files

To add a library shelf to your world, use the following XML:

```xml
<include>
  <uri>model://lib_shelf</uri>
  <name>lib_shelf_1</name>
  <pose>X Y Z ROLL PITCH YAW</pose>
</include>
```

**Example:**
```xml
<!-- Place shelf at position (-5, 5, 1.0) -->
<include>
  <uri>model://lib_shelf</uri>
  <name>lib_shelf_1</name>
  <pose>-5 5 1.0 0 0 0</pose>
</include>
```

### Multiple Instances

You can add multiple shelves by giving each a unique name:

```xml
<include>
  <uri>model://lib_shelf</uri>
  <name>lib_shelf_1</name>
  <pose>-5 5 1.0 0 0 0</pose>
</include>

<include>
  <uri>model://lib_shelf</uri>
  <name>lib_shelf_2</name>
  <pose>5 5 1.0 0 0 1.57</pose>
</include>
```

## Model Components

### Bookshelf Frame
- Model: `model://bookshelf`
- Static model with wood-colored shelf structure
- Scale: 1:1 (original size)
- Rotation: X=-90°, Z=-1m offset applied

### Bookcubes
- Model: `model://bookcube` 
- Book dimensions: ~0.2m × 0.15m × 0.25m (scaled from STL)
- Color: Brown wood finish matching bookshelf
- Static objects

### Level Configuration

6 levels with 0.35m vertical spacing:
- **Level 1**: Z = -0.96m
- **Level 2**: Z = -0.61m
- **Level 3**: Z = -0.26m
- **Level 4**: Z = 0.09m
- **Level 5**: Z = 0.44m
- **Level 6**: Z = 0.79m

Each level has 3 books with 0.3m horizontal (Y-axis) spacing:
- Left: Y = -0.3m
- Center: Y = 0m
- Right: Y = 0.3m

## Customization

To modify the shelf configuration, edit `/models/lib_shelf/model.sdf`:

1. **Add/remove levels**: Add or remove `<include>` blocks for bookcubes
2. **Adjust spacing**: Modify the Z coordinates (vertical) or Y coordinates (horizontal)
3. **Change book count**: Add more bookcubes per level by duplicating include blocks

## Dependencies

This model requires:
- `model://bookshelf` - The shelf frame structure
- `model://bookcube` - Individual book models

Ensure both models are available in your Gazebo model path.

## Technical Notes

- **Static model**: All components are static (non-physics)
- **Coordinate system**: Positions are relative to the shelf's origin
- **Scale factor**: Mesh uses 0.001 scale (mm to m conversion)
- **Total books**: 18 bookcubes across 6 levels
