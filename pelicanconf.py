AUTHOR = "Squark"
SITENAME = "Parrot avifauna"
SITESUBTITLE = "Ornithological stochasticity"
SITEURL = ""  # "https://kakapo.st"

PATH = "content"
THEME = "themes/cid"

TIMEZONE = "Pacific/Auckland"

DEFAULT_LANG = "EN"

# Blogroll
LINKS = [
    ("Emojipedia", "https://emojipedia.org/parrot"),
    ("eBird", "https://ebird.org/species/kakapo2"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

CATEGORY_META = {
    "Aratinga solstitialis": { 
        "wiki_slug": "Sun_conure",
        "ebird": "sunpar1",
    },
    "Ara ararauna": {
        "wiki_slug": "Blue-and-yellow_macaw",
        "ebird": "baymac"
    },
    "Ara macao": { 
        "wiki_slug": "Scarlet_macaw", 
        "ebird": "scamac1",
    },
    "Eclectus roratus": { 
        "description": "Male Moluccan eclectus", 
        "wiki_slug": "Moluccan_eclectus",
        "ebird": "eclpar1",
    },
    "Amazona viridigenalis": {
        "ebird": "recpar",
        "wiki_slug": "Red-crowned_amazon",
    },
    "unknown": {
        "description": "Unknown / Yet to be identified",
        "wiki_slug": "Jizz_(birding)",
    }
}
