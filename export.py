import os
import json

from db import db_connect
import utils

BEAR_IMAGES_PATH = os.path.expanduser(
    "~/Library/Group Containers/9K33E3U3T4.net.shinyfrog.bear/Application Data/Local Files/Note Images"
)

# Configuration
with open("config.json") as json_config:
    config = json.load(json_config)

clean_output = config["cleanOutputDir"]
export_trash = config["exportTrash"]
output_dir = os.path.abspath(os.path.join(os.path.expanduser(config["outputDir"])))

# Open database and create cursor
con = db_connect()
cur = con.cursor()

# Query Bear SQLite DB and select title, text, tag and trashed
query = """SELECT
    ZSFNOTE.ZTITLE AS title,
	  ZSFNOTE.ZTEXT AS text,
	  ZSFNOTETAG.ZTITLE AS tag,
	  ZSFNOTE.ZTRASHED AS trashed
  FROM ZSFNOTE
  LEFT JOIN Z_7TAGS ON ZSFNOTE.Z_PK = Z_7TAGS.Z_7NOTES
  LEFT JOIN ZSFNOTETAG ON Z_7TAGS.Z_14TAGS = ZSFNOTETAG.Z_PK"""

cur.execute(query)
notes = cur.fetchall()

# Create output folder if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(os.path.abspath(output_dir))
else:
    # Clean files in output
    if clean_output:
        utils.clean_dir(os.path.abspath(output_dir), ".md")

# Copy images folder
utils.copy_dir(BEAR_IMAGES_PATH, os.path.join(output_dir, "images"))

# Write files to output dir
for note in notes:
    if note[3] == 0 or (note[3] == 1 and export_trash):
        file = os.path.join(output_dir, utils.get_valid_filename(f"{note[0]}.md"))
        with open(file, "w+") as f:
            f.write(note[1])
