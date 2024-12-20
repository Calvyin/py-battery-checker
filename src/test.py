import pystray
from PIL import Image, ImageDraw

def create_high_res_cat_icon():
    # Define the size of the icon
    width, height = 128, 128

    # Create a blank image
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Define the pixelated cat design (16x16 grid for higher resolution)
    # Each tuple represents a row in the grid; 0 = background, 1 = cat
    cat_design = [
        (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0),
        (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
        (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
        (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
        (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
    ]

    # Set pixel size for scaling the grid into the icon size
    pixel_size = width // 16

    # Draw the cat design
    for row_index, row in enumerate(cat_design):
        for col_index, cell in enumerate(row):
            if cell == 1:  # Draw a filled square for the cat
                x0 = col_index * pixel_size
                y0 = row_index * pixel_size
                x1 = x0 + pixel_size
                y1 = y0 + pixel_size
                draw.rectangle([x0, y0, x1, y1], fill='black')

    return image

# Create the tray icon using the higher resolution cat image
icon = pystray.Icon(
    'High Res Pixel Cat',
    icon=create_high_res_cat_icon(),
    title='High-Resolution Pixel Cat'
)

# Run the icon in the system tray
icon.run()
