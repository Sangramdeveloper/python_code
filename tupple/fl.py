import bpy
import math

# Function to create a rose
def create_rose(num_petals=8):
    petals = []
    for i in range(num_petals):
        angle = 2 * math.pi * i / num_petals
        bpy.ops.mesh.primitive_circle_add(
            radius=1,
            fill_type='NOTHING',
            location=(0, 0, 0),
            vertices=32
        )
        petal = bpy.context.object
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_TRANSLATE=value=(0, 0, 0.2))
        bpy.ops.object.mode_set(mode='OBJECT')
        petal.rotation_euler[2] = angle
        petal.location.x = 2 * math.cos(angle)
        petal.location.y = 2 * math.sin(angle)
        petals.append(petal)
    
    bpy.ops.object.select_all(action='DESELECT')
    for petal in petals:
        petal.select_set(True)
    bpy.context.view_layer.objects.active = petals[0]
    bpy.ops.object.join()
    rose = bpy.context.object
    rose.name = "Rose"
    
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.1,
        depth=5,
        location=(0, 0, -2.5)
    )
    stem = bpy.context.object
    stem.name = "Stem"
    
    rose.location.z += 2.5
    bpy.ops.object.shade_smooth()

# Function to create a daisy
def create_daisy(num_petals=12):
    petals = []
    for i in range(num_petals):
        angle = 2 * math.pi * i / num_petals
        bpy.ops.mesh.primitive_cylinder_add(
            radius=0.2,
            depth=0.1,
            location=(0, 0, 0),
            vertices=6
        )
        petal = bpy.context.object
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_TRANSLATE=value=(0, 0, 0.2))
        bpy.ops.object.mode_set(mode='OBJECT')
        petal.rotation_euler[2] = angle
        petal.location.x = 1 * math.cos(angle)
        petal.location.y = 1 * math.sin(angle)
        petals.append(petal)
    
    bpy.ops.object.select_all(action='DESELECT')
    for petal in petals:
        petal.select_set(True)
    bpy.context.view_layer.objects.active = petals[0]
    bpy.ops.object.join()
    daisy = bpy.context.object
    daisy.name = "Daisy"
    
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=0.2,
        location=(0, 0, 0.2)
    )
    center = bpy.context.object
    center.name = "Center"
    
    daisy.location.z += 0.5
    bpy.ops.object.shade_smooth()

# Function to create a tulip
def create_tulip():
    bpy.ops.mesh.primitive_cone_add(
        vertices=6,
        radius1=1,
        depth=2,
        location=(0, 0, 0)
    )
    tulip = bpy.context.object
    tulip.name = "Tulip"
    tulip.rotation_euler[0] = math.radians(90)
    
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.1,
        depth=3,
        location=(0, 0, -1)
    )
    stem = bpy.context.object
    stem.name = "TulipStem"
    
    tulip.location.z += 1
    bpy.ops.object.shade_smooth()

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create flowers
create_rose(num_petals=8)
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Rose'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['Rose']
bpy.ops.transform.translate(value=(0, 0, 0))

create_daisy(num_petals=12)
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Daisy'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['Daisy']
bpy.ops.transform.translate(value=(3, 0, 0))

create_tulip()
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Tulip'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['Tulip']
bpy.ops.transform.translate(value=(-3, 0, 0))

# Set render settings
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.filepath = "/tmp/flowers_combined.png"

# Render image
bpy.ops.render.render(write_still=True)
