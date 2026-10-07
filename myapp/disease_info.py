"""Prevention and management guidance keyed to PlantVillage class names."""

DEFAULT_GUIDE = {
    "prevention": [
        "Use certified, disease-free planting material.",
        "Keep fields clean of crop debris and weeds that harbor pests.",
        "Avoid overhead watering late in the day so leaves can dry quickly.",
        "Rotate crops and maintain balanced nutrition for plant vigor.",
    ],
    "management": [
        "Remove and destroy severely infected plant parts.",
        "Improve air flow through pruning or wider spacing.",
        "Apply a labeled crop-specific product only after confirming the disease.",
        "Monitor the field again after 5–7 days and adjust treatment if needed.",
    ],
}

HEALTHY_GUIDE = {
    "prevention": [
        "Continue using healthy seed or transplants and inspect new plants before introducing them.",
        "Water at the base of plants and keep foliage as dry as possible.",
        "Maintain recommended spacing, prune crowded growth, and control weeds.",
        "Scout weekly so any new spots, wilting, or insects are caught early.",
    ],
    "management": [
        "No disease treatment is required based on this diagnosis.",
        "Keep soil moisture even and follow a balanced fertilizer schedule.",
        "Remove damaged or old leaves so they do not invite secondary infection.",
        "Re-check the crop after weather changes (rain, humidity, or heat stress).",
    ],
}

DISEASE_GUIDES = {
    "Apple___Apple_scab": {
        "prevention": [
            "Plant scab-resistant apple varieties where they are available.",
            "Rake and destroy fallen leaves in autumn to reduce overwintering fungus.",
            "Prune the canopy so sunlight and air reach inner branches.",
            "Apply preventive fungicides from green tip through rainy spring weather.",
        ],
        "management": [
            "Start a labeled captan, myclobutanil, or similar apple scab program at tight cluster.",
            "Remove heavily spotted leaves and fallen debris around the tree.",
            "Do not use the same fungicide class repeatedly; rotate modes of action.",
            "Keep trees watered and fertilized so new growth can outgrow mild infection.",
        ],
    },
    "Apple___Black_rot": {
        "prevention": [
            "Prune out cankers and mummified fruit during dormancy and burn or bag them.",
            "Sanitize pruning tools between cuts on infected wood.",
            "Avoid wounding trunks and branches during harvest or mowing.",
            "Thin fruit and improve canopy airflow to reduce humidity.",
        ],
        "management": [
            "Cut infected twigs 15–20 cm below visible cankers during dry weather.",
            "Remove rotting fruit from the tree and orchard floor immediately.",
            "Apply labeled fungicides at petal fall and cover sprays if pressure is high.",
            "Strengthen trees with balanced nutrition; stressed trees suffer more black rot.",
        ],
    },
    "Apple___Cedar_apple_rust": {
        "prevention": [
            "Avoid planting apples next to juniper or cedar, which is the alternate host.",
            "Choose rust-resistant apple cultivars when replacing trees.",
            "Remove nearby juniper galls in winter if local regulations allow.",
            "Use protective fungicides from pink bud through early summer spore flights.",
        ],
        "management": [
            "Apply myclobutanil or other labeled rust fungicides at pink and petal fall.",
            "Pick off heavily infected leaves to reduce spread on young trees.",
            "Do not wait until orange spots appear; sprays work best as prevention.",
            "Keep records of wet spring periods to time the next season’s first spray.",
        ],
    },
    "Apple___healthy": HEALTHY_GUIDE,
    "Blueberry___healthy": HEALTHY_GUIDE,
    "Cherry_(including_sour)___Powdery_mildew": {
        "prevention": [
            "Prune for an open canopy so leaves dry quickly after dew or rain.",
            "Avoid excess nitrogen that produces dense, mildew-prone shoots.",
            "Plant in full sun with good air movement between rows.",
            "Begin sulfur or potassium bicarbonate sprays at first shoot growth if mildew is chronic.",
        ],
        "management": [
            "Apply a labeled powdery mildew fungicide at the first white film on leaves.",
            "Remove the most infected shoot tips and destroy them.",
            "Rotate FRAC groups so the fungus does not become resistant.",
            "Reduce irrigation that wets foliage; drip irrigation is preferred.",
        ],
    },
    "Cherry_(including_sour)___healthy": HEALTHY_GUIDE,
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "prevention": [
            "Rotate out of maize for at least one season to break the residue cycle.",
            "Bury or shred infected stalks after harvest.",
            "Plant hybrids with known gray leaf spot resistance.",
            "Avoid overly dense stands that stay humid in the lower canopy.",
        ],
        "management": [
            "Scout from tasseling onward; treat if lesions are moving up the plant before grain fill.",
            "Use a labeled strobilurin or triazole fungicide according to growth stage.",
            "Do not rely on one chemistry every year; rotate fungicide groups.",
            "After harvest, manage residue to lower next season’s inoculum.",
        ],
    },
    "Corn_(maize)___Common_rust_": {
        "prevention": [
            "Choose rust-tolerant maize hybrids for your region.",
            "Plant at the recommended time so plants are not at a susceptible stage during peak spore flights.",
            "Maintain adequate potassium and overall crop vigor.",
            "Scout lower leaves after humid nights for cinnamon-colored pustules.",
        ],
        "management": [
            "Treat only if rust is spreading rapidly before tasseling on a susceptible hybrid.",
            "Apply a labeled foliar fungicide; common rust often slows in hot, dry weather.",
            "Avoid unnecessary sprays on resistant hybrids with low disease.",
            "Keep notes on hybrid performance to guide next year’s seed choice.",
        ],
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "prevention": [
            "Select hybrids with Ht resistance or strong partial resistance to northern leaf blight.",
            "Rotate crops and reduce maize residue on the soil surface.",
            "Use balanced fertility; nitrogen-heavy canopies stay wet longer.",
            "Space rows to improve airflow in humid production areas.",
        ],
        "management": [
            "Scout for cigar-shaped gray-green lesions from V8 to tasseling.",
            "Apply a labeled fungicide if blight reaches the ear leaf before grain fill.",
            "Rotate fungicide modes of action across seasons.",
            "Chop and incorporate residue after harvest to cut overwintering fungus.",
        ],
    },
    "Corn_(maize)___healthy": HEALTHY_GUIDE,
    "Grape___Black_rot": {
        "prevention": [
            "Remove mummified berries and infected canes during winter pruning.",
            "Train vines for an open canopy and leaf-pull around clusters.",
            "Start a protective spray program at 3–5 cm shoot growth in wet springs.",
            "Avoid leaving fruit on the ground after harvest.",
        ],
        "management": [
            "Apply labeled captan, mancozeb, or strobilurin sprays from bloom through bunch close.",
            "Cut out infected clusters as soon as brown rotting berries appear.",
            "Improve spray coverage inside the canopy; black rot infects during rain.",
            "Sanitize harvest bins and pruning shears so spores are not carried between vines.",
        ],
    },
    "Grape___Esca_(Black_Measles)": {
        "prevention": [
            "Prune in dry weather and protect large cuts with a wound sealant or pruning paint.",
            "Avoid severe water stress, which worsens foliar measles symptoms.",
            "Plant certified vines and do not use wood from symptomatic blocks for cuttings.",
            "Delay pruning in high-risk vineyards until the risk of rain on fresh cuts is lower.",
        ],
        "management": [
            "Remove and destroy vines with severe dieback; the fungus lives in wood.",
            "Retrain a healthy sucker if the trunk is infected but roots are still viable.",
            "There is no reliable curative spray; focus on sanitation and vine stress reduction.",
            "Mark symptomatic vines at harvest so they can be removed in the dormant season.",
        ],
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "prevention": [
            "Keep the canopy open with timely shoot thinning and leaf removal.",
            "Avoid overhead irrigation that keeps leaves wet for long periods.",
            "Rake or mulch fallen infected leaves after harvest.",
            "Use preventive copper or other labeled grape fungicides in humid weather.",
        ],
        "management": [
            "Apply a labeled fungicide at the first angular leaf spots.",
            "Remove badly blighted leaves to lower spore load.",
            "Ensure clusters still have enough leaf cover for ripening after defoliation.",
            "Repeat sprays after heavy rain according to the product label.",
        ],
    },
    "Grape___healthy": HEALTHY_GUIDE,
    "Orange___Haunglongbing_(Citrus_greening)": {
        "prevention": [
            "Plant certified greening-free nursery trees only.",
            "Control Asian citrus psyllid with an area-wide spray and monitoring program.",
            "Remove volunteer citrus and ornamental hosts near the orchard.",
            "Inspect new flush regularly for blotchy mottle and lopsided fruit.",
        ],
        "management": [
            "Have a suspected tree confirmed by a plant clinic or agriculture office.",
            "Remove confirmed infected trees promptly to protect neighboring trees.",
            "Maintain intensive psyllid control; antibiotics do not cure HLB in the field.",
            "Support remaining trees with irrigation and nutrition while planning replanting with clean stock.",
        ],
    },
    "Peach___Bacterial_spot": {
        "prevention": [
            "Plant bacterial spot–resistant peach cultivars in humid regions.",
            "Avoid working trees when foliage is wet.",
            "Apply dormant copper sprays before bud swell where recommended.",
            "Reduce nitrogen late in the season so succulent growth is limited.",
        ],
        "management": [
            "Use labeled copper or oxytetracycline programs from petal fall through cover sprays if legal in your area.",
            "Prune out severely spotted shoots during dry weather.",
            "Do not apply copper in hot weather at rates that cause russeting; follow the label.",
            "Improve orchard air flow and avoid overhead irrigation.",
        ],
    },
    "Peach___healthy": HEALTHY_GUIDE,
    "Pepper,_bell___Bacterial_spot": {
        "prevention": [
            "Use certified seed and hot-water or chlorine seed treatment when advised.",
            "Transplant only healthy seedlings; discard spotted trays.",
            "Avoid working plants when they are wet and drip-irrigate instead of sprinkling.",
            "Rotate away from pepper, tomato, and other solanaceous crops for 2–3 years.",
        ],
        "management": [
            "Remove infected plants from seedbeds so the whole tray is not lost.",
            "Apply labeled copper plus mancozeb sprays during warm, wet weather.",
            "Do not save seed from diseased fruit.",
            "Disinfect stakes, scissors, and transplant trays between batches.",
        ],
    },
    "Pepper,_bell___healthy": HEALTHY_GUIDE,
    "Potato___Early_blight": {
        "prevention": [
            "Plant certified seed tubers and resistant or tolerant varieties.",
            "Hill soil well and avoid nitrogen deficiency, which increases early blight.",
            "Rotate out of potato and tomato for at least two years.",
            "Start protective fungicides at row closure in humid climates.",
        ],
        "management": [
            "Apply chlorothalonil, mancozeb, or other labeled products on a 7–10 day schedule in wet weather.",
            "Remove volunteer potatoes and heavily blighted lower leaves.",
            "Keep irrigation even; drought-stressed plants get more early blight.",
            "Allow skins to set before harvest and avoid digging into wet, infected foliage.",
        ],
    },
    "Potato___Late_blight": {
        "prevention": [
            "Plant only certified seed and destroy cull piles and volunteer plants.",
            "Choose late blight–resistant varieties when they fit the market.",
            "Avoid overhead irrigation in cool, wet weather.",
            "Follow regional late blight forecasts to time the first spray.",
        ],
        "management": [
            "Treat immediately with a labeled late-blight fungicide; this disease can destroy a crop in days.",
            "Kill vines before harvest if blight is active so tubers are not infected.",
            "Do not store blighted tubers; they rot and infect healthy potatoes.",
            "Report severe outbreaks to local extension so neighbors can protect nearby fields.",
        ],
    },
    "Potato___healthy": HEALTHY_GUIDE,
    "Raspberry___healthy": HEALTHY_GUIDE,
    "Soybean___healthy": HEALTHY_GUIDE,
    "Squash___Powdery_mildew": {
        "prevention": [
            "Plant mildew-resistant squash or pumpkin varieties.",
            "Space plants for airflow and avoid dense, shaded plantings.",
            "Water the soil, not the leaves, and irrigate in the morning.",
            "Begin potassium bicarbonate or sulfur programs at the first sign in humid areas.",
        ],
        "management": [
            "Spray a labeled mildew fungicide at the first white patches on older leaves.",
            "Remove the worst-affected leaves if the plant still has enough canopy.",
            "Rotate chemistries; powdery mildew develops resistance quickly.",
            "Keep fruit off wet soil with mulch to reduce secondary rotting.",
        ],
    },
    "Strawberry___Leaf_scorch": {
        "prevention": [
            "Plant certified disease-free runners.",
            "Renovate beds after harvest: mow, narrow rows, and remove old leaves.",
            "Avoid excess nitrogen that produces a dense, wet canopy.",
            "Use drip irrigation and keep fruiting beds weed-free.",
        ],
        "management": [
            "Apply labeled captan or other strawberry leaf-spot fungicides after renovation and in wet springs.",
            "Remove and destroy highly scorched leaves.",
            "Improve airflow by thinning crowded crowns.",
            "Replace old plantings every 3–4 years; scorch builds up in aging beds.",
        ],
    },
    "Strawberry___healthy": HEALTHY_GUIDE,
    "Tomato___Bacterial_spot": {
        "prevention": [
            "Use hot-water treated or certified seed and clean transplants.",
            "Stake or cage plants and drip-irrigate to keep leaves dry.",
            "Rotate away from tomato, pepper, and related crops.",
            "Do not handle wet plants or use tobacco products around seedlings.",
        ],
        "management": [
            "Apply copper-based sprays at the first leaf specks, mixed with mancozeb if labeled.",
            "Remove badly spotted lower leaves and destroy them; do not compost.",
            "Disinfect cages, stakes, and tools between seasons.",
            "Avoid saving seed from spotted fruit.",
        ],
    },
    "Tomato___Early_blight": {
        "prevention": [
            "Mulch to stop soil splash onto lower leaves.",
            "Stake plants and prune suckers for airflow.",
            "Rotate crops and start with clean seed or transplants.",
            "Begin protective sprays after fruit set in humid weather.",
        ],
        "management": [
            "Remove concentric-ring spotted lower leaves as soon as they appear.",
            "Apply chlorothalonil, mancozeb, or copper on a regular schedule during rain.",
            "Keep plants evenly watered; stress increases early blight.",
            "Destroy vines after harvest so spores do not overwinter nearby.",
        ],
    },
    "Tomato___Late_blight": {
        "prevention": [
            "Buy certified transplants; late blight can arrive on infected seedlings.",
            "Avoid overhead watering and crowded, unventilated greenhouses.",
            "Destroy volunteer tomato and potato plants.",
            "Watch local blight alerts during cool, wet spells.",
        ],
        "management": [
            "Remove and bag entire infected plants immediately; do not leave them in the field.",
            "Spray remaining plants with a labeled late-blight fungicide the same day.",
            "Do not compost infected material.",
            "Harvest healthy fruit and destroy the rest of the planting if the outbreak is severe.",
        ],
    },
    "Tomato___Leaf_Mold": {
        "prevention": [
            "Ventilate greenhouses; leaf mold is worst in high humidity.",
            "Water at the base and keep night humidity down.",
            "Choose resistant (Cf gene) varieties for protected culture.",
            "Space plants and prune for air movement.",
        ],
        "management": [
            "Lower humidity first; sprays fail if the greenhouse stays wet.",
            "Apply a labeled fungicide at the first olive-green mold on leaf undersides.",
            "Remove infected leaves and take them out of the house.",
            "Sanitize strings, clips, and greenhouse surfaces between crops.",
        ],
    },
    "Tomato___Septoria_leaf_spot": {
        "prevention": [
            "Mulch and use drip irrigation to reduce soil splash.",
            "Stake plants and keep lower leaves off the ground.",
            "Rotate for 2–3 years away from tomato family crops.",
            "Start protective fungicides after first fruit set in wet seasons.",
        ],
        "management": [
            "Pinch off lower leaves with small dark spots and yellowing.",
            "Spray chlorothalonil, copper, or mancozeb according to the label.",
            "Avoid working plants when wet so spores are not spread by hands.",
            "Clean up all vines at season’s end.",
        ],
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "prevention": [
            "Avoid dusty, drought-stressed plants; mites explode on dry foliage.",
            "Inspect the undersides of leaves when introducing new plants.",
            "Encourage predators by limiting broad-spectrum insecticides.",
            "Keep weeds down around the plot; many weeds host mites.",
        ],
        "management": [
            "Spray leaf undersides with a strong water jet to knock mites down.",
            "Use insecticidal soap, horticultural oil, or a labeled miticide; rotate products.",
            "Treat nearby infested weeds and the whole plant, not just the top side of leaves.",
            "Re-check in 5–7 days; eggs will have hatched and a second treatment is often needed.",
        ],
    },
    "Tomato___Target_Spot": {
        "prevention": [
            "Use drip irrigation and mulch to keep leaves dry.",
            "Space and prune plants for airflow.",
            "Start with clean transplants and rotate out of solanaceous crops.",
            "Avoid excess nitrogen that produces a dense canopy.",
        ],
        "management": [
            "Apply labeled strobilurin or chlorothalonil sprays at the first target-like lesions.",
            "Remove badly spotted leaves and destroy crop debris.",
            "Improve greenhouse or field ventilation during humid nights.",
            "Do not save seed from symptomatic fruit.",
        ],
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "prevention": [
            "Use virus-resistant tomato varieties and whitefly-proof nursery netting.",
            "Control silverleaf whitefly with yellow sticky traps and approved insecticides.",
            "Remove weeds that host whiteflies around the field.",
            "Do not plant new tomatoes next to an old, infected crop.",
        ],
        "management": [
            "Rogue (pull and destroy) plants with upward curling, yellowing leaves as soon as they appear.",
            "There is no spray that cures the virus; focus on whitefly control to stop spread.",
            "Reflective mulch can reduce whitefly landing on young plants.",
            "After a severe outbreak, take a host-free period before replanting tomato.",
        ],
    },
    "Tomato___Tomato_mosaic_virus": {
        "prevention": [
            "Use certified virus-free seed and resistant varieties.",
            "Wash hands and tools; the virus spreads by sap on fingers and clothing.",
            "Do not smoke or handle tobacco near tomato seedlings.",
            "Control chewing insects that can move sap between plants.",
        ],
        "management": [
            "Remove mosaic-symptomatic plants as soon as they are found.",
            "No chemical cure exists; sanitation is the main control.",
            "Disinfect knives and stakes with a 10% household bleach solution or equivalent.",
            "Do not save seed from mottled fruit.",
        ],
    },
    "Tomato___healthy": HEALTHY_GUIDE,
}


def _class_key(label: str) -> str:
    return label.replace(" - ", "___").strip()


def get_disease_guide(predicted_label: str) -> dict:
    key = _class_key(predicted_label)
    guide = DISEASE_GUIDES.get(key, DEFAULT_GUIDE)
    is_healthy = "healthy" in key.lower()
    return {
        "prevention": list(guide["prevention"]),
        "management": list(guide["management"]),
        "is_healthy": is_healthy,
    }
