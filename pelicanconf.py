AUTHOR = "Squark"
SITENAME = "Parrot avifauna"
SITESUBTITLE = "Ornithological stochasticity"
SITEURL = ""  # "https://kakapo.st"

PATH = "content"
THEME = "themes/cid"

TIMEZONE = "Pacific/Auckland"

ARTICLE_ORDER_BY = 'title'
PAGE_ORDER_BY = 'title'

DEFAULT_LANG = "EN"

BIRD_SUGGESTION_URL = "https://github.com/glasnt/kakapo.st/issues/new?template=suggestion.md"

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
