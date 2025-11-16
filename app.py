from flask import Flask, render_template_string, request

app = Flask(__name__)

def get_text(lang):
    """Textes multilingues uniquement pour la page d'accueil"""
    translations = {
        "fr": {
            "title": "Projet Anti-Gaspi",
            "car": "Voiture polluante",
            "car_note": "Émission de CO2",
            "trash": "Poubelle",
            "trash_note": "Poubelle qui déborde",
            "bus": "Prioriser les transports en commun",
            "bus_note": "Mobilité durable",
            "ocean": "Pollution plastique dans l'océan",
            "ocean_note": "Déchets marins",
            "footer": "Site réalisé et développé par Sohaib Ait Bella — images libres de droits"
        },
        "en": {
            "title": "Anti-Waste Project",
            "car": "Polluting car",
            "car_note": "CO2 emission",
            "trash": "Trash bin",
            "trash_note": "Overflowing garbage",
            "bus": "Promote public transport",
            "bus_note": "Sustainable mobility",
            "ocean": "Plastic pollution in the ocean",
            "ocean_note": "Marine waste",
            "footer": "Website created by Sohaib Ait Bella — royalty-free images"
        },
        "de": {
            "title": "Anti-Verschwendung Projekt",
            "car": "Verschmutzendes Auto",
            "car_note": "CO2-Ausstoß",
            "trash": "Mülltonne",
            "trash_note": "Überquellender Abfall",
            "bus": "Öffentliche Verkehrsmittel fördern",
            "bus_note": "Nachhaltige Mobilität",
            "ocean": "Plastikverschmutzung im Ozean",
            "ocean_note": "Meeresabfälle",
            "footer": "Website erstellt von Sohaib Ait Bella — lizenzfreie Bilder"
        }
    }
    return translations.get(lang, translations["fr"])


@app.route("/")
def home():
    lang = request.args.get("lang", "fr")
    T = get_text(lang)

    HTML = f"""
    <!DOCTYPE html>
    <html lang="{lang}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{T['title']}</title>

        <style>
            body {{
                margin: 0;
                font-family: "Poppins", Arial, sans-serif;
                background-color: #eaf6ea;
                color: #214d2e;
                text-align: center;
            }}

            header {{
                padding: 20px;
                background-color: #2f8a44;
                color: white;
                position: relative;
            }}

            /* Drapeaux */
            .flags {{
                position: absolute;
                top: 10px;
                left: 10px;
                display: flex;
                gap: 8px;
            }}

            .flags img {{
                width: 26px;
                height: 18px;
                cursor: pointer;
                border: 1px solid white;
            }}

            .container {{
                width: 94%;
                max-width: 1100px;
                margin: 18px auto;
            }}

            .grid-top, .grid-bottom {{
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 16px;
            }}

            .box {{
                background: white;
                padding: 10px;
                border-radius: 12px;
                box-shadow: 0 6px 18px rgba(20, 60, 30, 0.06);
            }}

            .box img {{
                width: 100%;
                height: 200px;
                object-fit: cover;
                border-radius: 8px;
                cursor: pointer;
            }}

            @media (max-width:800px){{
                .grid-top, .grid-bottom {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>

    <body>

    <header>
        <div class="flags">
            <a href="/?lang=fr"><img src="https://flagcdn.com/w20/fr.png"></a>
            <a href="/?lang=en"><img src="https://flagcdn.com/w20/gb.png"></a>
            <a href="/?lang=de"><img src="https://flagcdn.com/w20/de.png"></a>
        </div>

        <div style="font-size:22px; font-weight:600">{T['title']}</div>
    </header>

    <div class="container">

      <section class="grid-top">

        <div class="box small">
          <a href="/voiture">
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fz%2Fcar-emitting-carbon-dioxide-co-environmental-pollution-problem-vector-illustration-isolated-white-background-124259733.jpg&f=1&nofb=1" alt="">
          </a>
          <h3>{T['car']}</h3>
          <p>{T['car_note']}</p>
        </div>

        <div class="box small">
          <a href="/poubelle">
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.freepik.com%2Fvecteurs-libre%2Fpoubelle-debordante-ordures-menageres-restes_376504-6.jpg%3Fsize%3D626%26ext%3Djpg&f=1&nofb=1" alt="">
          </a>
          <h3>{T['trash']}</h3>
          <p>{T['trash_note']}</p>
        </div>

      </section>

      <section class="grid-bottom">

        <div class="box large">
          <a href="/bus">
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.freepik.com%2Fvecteurs-premium%2Fdessin-bus-descendant-route-montagnes-arriere-plan_1157866-1253.jpg&f=1&nofb=1" alt="">
          </a>
          <h3>{T['bus']}</h3>
          <p>{T['bus_note']}</p>
        </div>

        <div class="box large">
          <a href="/ocean">
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Fd%25C3%25A9chets-plastiques-de-dans-l-eau-mer-oc%25C3%25A9an-illustration-vecteur-plastique-la-avec-des-dessin-d-environnement-pollu%25C3%25A9-202922331.jpg&f=1&nofb=1" alt="">
          </a>
          <h3>{T['ocean']}</h3>
          <p>{T['ocean_note']}</p>
        </div>

      </section>

    </div>

    <footer>
        {T['footer']}
    </footer>

    </body>
    </html>
    """
    return render_template_string(HTML)



# ------------------------------------------------
#   PAGES INDIVIDUELLES (inchangées)
# ------------------------------------------------

PAGE_VOITURE = """
<div style='background:#969b93; min-height:100vh; padding:20px; color:white;'>
<h1>Réduire la pollution automobile</h1>

<p>
La voiture individuelle est aujourd’hui l’une des plus grandes sources d’émission de CO₂.
Même les trajets courts multiplient la pollution atmosphérique et sonore.
Pourtant, de nombreux gestes simples permettent de réduire considérablement notre impact.
</p>

<h2>Pourquoi limiter la voiture ?</h2>
<ul>
  <li>Les moteurs rejettent du dioxyde de carbone, responsable du réchauffement climatique.</li>
  <li>Les embouteillages augmentent la consommation de carburant.</li>
  <li>La pollution de l’air favorise les maladies cardiaques et respiratoires.</li>
  <li>L’utilisation excessive des voitures dégrade les routes et les espaces urbains.</li>
</ul>

<h2>Des alternatives simples et efficaces</h2>
<ul>
  <li>Marcher ou utiliser le vélo pour les trajets de moins de 2 km.</li>
  <li>Faire du covoiturage entre voisins, collègues ou amis.</li>
  <li>Regrouper les courses et déplacements pour réduire les aller-retours.</li>
  <li>Favoriser les transports en commun quand c’est possible.</li>
</ul>

<p>
Chaque trajet évité, même court, représente un geste concret pour le climat.
Agir pour la planète commence avec des choix du quotidien.
</p>

<a href="/" style="color:white; font-weight:bold;">⬅ Retour</a>
</div>
"""


PAGE_POUBELLE = """
<div style='background:#095b21; min-height:100vh; padding:20px; color:white;'>
<h1>Mieux gérer ses déchets</h1>

<p>
Le débordement des poubelles est un problème fréquent en ville.
Un mauvais tri entraîne une pollution importante et complique le recyclage.
Pourtant, de simples bonnes pratiques peuvent tout changer.
</p>

<h2>Comment éviter les débordements ?</h2>
<ul>
  <li>Trier systématiquement : papier, plastique, verre, déchets alimentaires.</li>
  <li>Compresser les emballages (bouteilles, cartons) pour gagner de la place.</li>
  <li>Ne jamais jeter d’objets encombrants dans une petite poubelle.</li>
  <li>Utiliser les points de collecte pour le verre et les déchets recyclables.</li>
</ul>

<h2>Pourquoi c’est important ?</h2>
<ul>
  <li>Un tri correct facilite le recyclage et limite le gaspillage.</li>
  <li>Des poubelles propres empêchent les nuisibles et mauvaises odeurs.</li>
  <li>Les déchets non triés terminent souvent dans la nature.</li>
</ul>

<p>
Adopter de bons réflexes, c’est protéger son quartier, sa ville
et l’environnement pour les générations futures.
</p>

<a href="/" style="color:white; font-weight:bold;">⬅ Retour</a>
</div>
"""


PAGE_BUS = """
<div style='background:#fff4a3; min-height:100vh; padding:20px; color:#5a5000;'>
<h1>Favoriser les transports en commun</h1>

<p>
Prendre le bus, le tramway ou le métro est l’un des moyens les plus efficaces
de réduire la pollution en ville. Un seul bus peut remplacer jusqu’à 40 voitures !
</p>

<h2>Les avantages des transports en commun</h2>
<ul>
  <li>Ils réduisent considérablement les émissions de CO₂ par passager.</li>
  <li>Ils permettent de limiter les embouteillages et la circulation excessive.</li>
  <li>Ils économisent du carburant et réduisent la dépendance au pétrole.</li>
  <li>Ils diminuent le stress lié à la conduite et au stationnement.</li>
</ul>

<h2>Un choix écologique et économique</h2>
<p>
Le coût d’un abonnement transport est souvent bien inférieur à l’ensemble
des dépenses liées à l’entretien d’un véhicule personnel : carburant,
assurance, réparation, stationnement…
</p>

<p>
Adopter les transports en commun, c’est choisir un mode de vie plus durable,
plus pratique, et plus économique.
</p>

<a href="/" style="color:#5a5000; font-weight:bold;">⬅ Retour</a>
</div>
"""


PAGE_OCEAN = """
<div style='background:#8fd6ff; min-height:100vh; padding:20px; color:#003b5c;'>
<h1>Sensibilisation à la pollution plastique</h1>

<p>
Chaque année, plus de 8 millions de tonnes de plastique finissent dans les océans.
Une grande partie provient de déchets jetés au sol ou mal triés.
Même un petit emballage peut parcourir des kilomètres jusqu’à la mer.
</p>

<h2>D’où vient ce plastique ?</h2>
<ul>
  <li>Des déchets abandonnés dans la rue et emportés par la pluie.</li>
  <li>Des poubelles débordantes dont les déchets s’envolent.</li>
  <li>Des microplastiques provenant de vêtements, pneus, objets usés.</li>
  <li>Des déchets rejetés illégalement dans la nature.</li>
</ul>

<h2>Les conséquences sur les océans</h2>
<ul>
  <li>Les animaux confondent le plastique avec de la nourriture.</li>
  <li>Les tortues, poissons et oiseaux s’y blessent ou s’y étouffent.</li>
  <li>Les microplastiques entrent dans la chaîne alimentaire humaine.</li>
  <li>Les écosystèmes marins se dégradent durablement.</li>
</ul>

<h2>Que pouvons-nous faire ?</h2>
<ul>
  <li>Jeter ses déchets uniquement dans la bonne poubelle.</li>
  <li>Ramasser un déchet que l’on voit par terre.</li>
  <li>Réduire sa consommation de plastique jetable.</li>
  <li>Éviter les sacs, bouteilles et couverts jetables.</li>
</ul>

<p>Protéger l’océan, c’est protéger la vie sur Terre.</p>

<a href="/" style="color:#003b5c; font-weight:bold;">⬅ Retour</a>
</div>
"""



@app.route("/voiture")
def voiture():
    return render_template_string(PAGE_VOITURE)

@app.route("/poubelle")
def poubelle():
    return render_template_string(PAGE_POUBELLE)

@app.route("/bus")
def bus():
    return render_template_string(PAGE_BUS)

@app.route("/ocean")
def ocean():
    return render_template_string(PAGE_OCEAN)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

