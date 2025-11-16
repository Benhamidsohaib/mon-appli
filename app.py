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
<body style="background:#969b93; font-family:Poppins; padding:30px; color:#000;">
    <h1>Réduire la pollution automobile</h1>
    <p>Pour protéger l’environnement, il est essentiel de privilégier :</p>
    <ul>
      <li>la marche à pied</li>
      <li>le vélo</li>
      <li>les déplacements courts sans voiture</li>
    </ul>
    <p>Chaque trajet évité réduit les émissions de CO₂.</p>
    <a href="/" style="color:black; font-weight:bold;">⬅ Retour</a>
</body>
"""

PAGE_POUBELLE = """
<body style="background:#095b21; font-family:Poppins; padding:30px; color:white;">
    <h1>Mieux gérer ses déchets</h1>
    <p>Pour éviter que les poubelles débordent :</p>
    <ul>
      <li>trier correctement ses déchets</li>
      <li>utiliser la bonne poubelle</li>
      <li>réduire ses déchets inutiles</li>
    </ul>
    <a href="/" style="color:white; font-weight:bold;">⬅ Retour</a>
</body>
"""

PAGE_BUS = """
<body style="background:#fff7b3; font-family:Poppins; padding:30px;">
    <h1>Favoriser les transports en commun</h1>
    <p>Le bus, le tram ou le métro permettent de :</p>
    <ul>
      <li>réduire la pollution</li>
      <li>limiter les embouteillages</li>
      <li>économiser du carburant</li>
    </ul>
    <a href="/">⬅ Retour</a>
</body>
"""

PAGE_OCEAN = """
<body style="background:#b3e9f9; font-family:Poppins; padding:30px;">
    <h1>Sensibilisation à la pollution plastique</h1>
    <p>Jeter ses déchets au sol finit souvent dans :</p>
    <ul>
      <li>les rivières</li>
      <li>les égouts</li>
      <li>l’océan</li>
    </ul>
    <p>Chaque geste compte : gardons la planète propre.</p>
    <a href="/">⬅ Retour</a>
</body>
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

            

