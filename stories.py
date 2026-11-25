# stories.py -- the 40 dated stories of Tuesday 24 November 2026.
# Every story was verified against its original source on 25 Nov 2026.
# Tag CONFIRMED: the source confirms the event happened on 24 Nov 2026.
# Tag REPORTED: the story was first reported on 24 Nov 2026.
# Headlines are ASCII-only so the 5x7 bitmap renderer can draw them.

TITLE = (
    "Tuesday 24 November 2026 -- The World in One Day: "
    "40 dated stories, 7 regions: Riyadh tower hit again, "
    "BepiColombo reaches Mercury, Zaporizhzhia struck"
)

REGIONS = [
    "NORTH AMERICA",
    "LATIN AMERICA",
    "EUROPE",
    "MIDDLE EAST",
    "AFRICA",
    "ASIA-PACIFIC",
    "SCIENCE & CULTURE",
]

# Each story: (region index, headline, source, tag)
STORIES = [
    # ---- NORTH AMERICA (8) ----
    (0, "Trump orders DOJ to speed up federal death sentences",
     "Just Security", "REPORTED"),
    (0, "Jensen Huang reinstated as Nvidia CEO after Trump lobbying",
     "BBC", "REPORTED"),
    (0, "Oregon and Virginia sue SpaceX over Grok sex deepfakes",
     "NPR", "REPORTED"),
    (0, "Pentagon: Canada falling short as North America defence partner",
     "AP", "REPORTED"),
    (0, "Commanders stun Bengals 22-20 on walk-off field goal",
     "AP", "REPORTED"),
    (0, "Rep. Jimmy Gomez to quit Congress after ethics findings",
     "NYT", "REPORTED"),
    (0, "Ex-Hegseth aide Kaspar: defence chief should resign",
     "Politico", "REPORTED"),
    (0, "Trump to meet NATO chief Rutte in Florida on Wednesday",
     "Hindu BusinessLine", "REPORTED"),
    # ---- LATIN AMERICA (5) ----
    (1, "Mexico captures 'El Chapo Isidro' in deadly Sinaloa raid",
     "ENNW", "CONFIRMED"),
    (1, "Lula backs second fiscal package to curb spending",
     "Reuters", "CONFIRMED"),
    (1, "Ecuador town declares flood emergency as El Nino rains hit",
     "Rio Times", "CONFIRMED"),
    (1, "Dengue deaths reach 45 in Peru's Lambayeque region",
     "Rio Times", "CONFIRMED"),
    (1, "Chile mourns actress Delfina Guzman, dead at 98",
     "Rio Times", "CONFIRMED"),
    # ---- EUROPE (6) ----
    (2, "Russian strike on Zaporizhzhia kills 2, wounds 40",
     "Reuters", "CONFIRMED"),
    (2, "Germany first to access Ukraine's Delta battle system",
     "Kyiv Independent", "CONFIRMED"),
    (2, "NATO vows to defend space after Russian nuclear satellite reports",
     "BBC", "REPORTED"),
    (2, "Russian drone briefly enters Polish airspace",
     "h.ua", "CONFIRMED"),
    (2, "Zelensky: seek more US help if peace deal fails",
     "h.ua", "CONFIRMED"),
    (2, "Ukraine and Norway expand joint DESNA air defence",
     "h.ua", "CONFIRMED"),
]

STORIES += [
    # ---- MIDDLE EAST (5) ----
    (3, "Houthi strike hits Riyadh's tallest tower again, 11 hurt",
     "AFP", "CONFIRMED"),
    (3, "Three tankers catch fire after hitting mines in Hormuz",
     "Pakistan TV", "CONFIRMED"),
    (3, "Israeli strike kills Hamas security chief in Gaza",
     "Reuters", "CONFIRMED"),
    (3, "US Treasury sanctions Iran shadow banking network",
     "Geopolitiki", "CONFIRMED"),
    (3, "Iran vows 'all means' against US naval blockade",
     "Reuters", "CONFIRMED"),
    # ---- AFRICA (5) ----
    (4, "Fighting traps Ebola responders in DR Congo's Ituri",
     "UN News", "CONFIRMED"),
    (4, "Amnesty: Tigray strikes may be war crimes",
     "Reuters", "CONFIRMED"),
    (4, "Nigeria opposition boycotts police security meeting",
     "Rio Times", "CONFIRMED"),
    (4, "Somalia and Uganda step up fight against al-Shabaab",
     "IQMIA", "CONFIRMED"),
    (4, "CAS hands Senegal back Africa Cup title",
     "Rio Times", "CONFIRMED"),
    # ---- ASIA-PACIFIC (6) ----
    (5, "Russian jets enter South Korea air defence zone",
     "AP", "CONFIRMED"),
    (5, "MSCI: no decision yet on Indonesia market downgrade",
     "Reuters", "CONFIRMED"),
    (5, "Indonesia factory fire toll rises to 26",
     "AP", "REPORTED"),
    (5, "Japan to pay full 2027 ICC bill early",
     "Reuters", "CONFIRMED"),
    (5, "Seoul offers $375,000 to catch AI exam cheats",
     "WSJ", "CONFIRMED"),
    (5, "Hasina plans return to Bangladesh on Dec 16",
     "Reuters", "CONFIRMED"),
    # ---- SCIENCE & CULTURE (5) ----
    (6, "BepiColombo safe in Mercury orbit after glitch",
     "The Register", "REPORTED"),
    (6, "FIFA: four nations to host 2031 Women's World Cup",
     "Ungated", "REPORTED"),
    (6, "Mexico launches Atlas of Textile Art",
     "ENNW", "CONFIRMED"),
    (6, "London show tells capital's story from Romans to street art",
     "La Mediterranee", "CONFIRMED"),
    (6, "WHO offers Cuba $2m in vaccines as health crisis bites",
     "Rio Times", "CONFIRMED"),
]

# Four illustrated lead cards: (image file, kicker, headline, caption)
LEADS = [
    ("thumb-riyadh.png", "MIDDLE EAST",
     "Riyadh tower hit again",
     "Houthi strike on the PIF Tower injures 11; second hit in days."),
    ("thumb-mercury.png", "SCIENCE",
     "BepiColombo reaches Mercury",
     "Probe safe in orbit after a glitch cut its braking burn short."),
    ("thumb-zaporizhzhia.png", "EUROPE",
     "Zaporizhzhia struck overnight",
     "Russian attack kills 2 and wounds 40, including four children."),
    ("thumb-mnf.png", "SPORT / USA",
     "Commanders win at the gun",
     "Walk-off field goal stuns the Bengals 22-20 on Monday night."),
]
