
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif']= 'STIXGeneral'
mpl.rcParams['mathtext.fontset']= 'stix'
mpl.rcParams['font.size']= 28
mpl.rcParams["figure.dpi"] = 300
from matplotlib import font_manager

font_dirs = ["/usr/share/fonts/truetype/lato/"]  # The path to the custom font file.
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)
palette = [
    "#ca0020",
    "#f4a582",
    "#92c5de",
    '#0571b0'
]

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'lato'
palette = list(map(mpl.colors.hex2color, palette, ))