from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projet 0 déchets</title>

    <style>
        body {
            margin: 0;
            font-family: "Poppins", Arial, sans-serif;
            background-color: #eaf6ea;
            color: #214d2e;
            text-align: center;
        }

        header {
            padding: 20px;
            background-color: #2f8a44;
            color: white;
        }

        .subtitle {
            font-size: 14px;
            color: #e6f6e8;
            margin-top: 6px;
            font-weight: 300;
        }

        .container {
            width: 94%;
            max-width: 1100px;
            margin: 18px auto;
            padding: 0 10px 30px;
        }

        .grid-top {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 18px;
        }

        .grid-bottom {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }

        .box {
            background: white;
            padding: 10px;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(20, 60, 30, 0.06);
            text-align: left;
            overflow: hidden;
        }

        .box img {
            width: 100%;
            height: 190px;
            object-fit: cover;
            border-radius: 8px;
            display: block;
        }

        .small img { height: 150px; }
        .large img { height: 270px; }

        .card-body {
            padding: 10px 6px 12px;
        }
        h3 { margin: 0 0 6px; color:#1f4a2a; font-size:16px; }
        p.note { margin:0; color:#6b756d; font-size:13px; }

        footer {
            margin-top: 22px;
            padding: 12px;
            color: #4a604f;
            font-size: 13px;
        }

        @media (max-width:800px){
            .grid-top, .grid-bottom { grid-template-columns: 1fr; }
            .box img { height: 220px; }
        }
    </style>
</head>

<body>

<header>
    <div style="font-size:22px; font-weight:600">Projet Anti-Gaspi</div>
    <div class="subtitle">Photos libres de droits — Pexels & Pixabay</div>
</header>

<div class="container">

  <!-- deux petites vignettes en haut -->
  <section class="grid-top">
    <div class="box small">
      <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fz%2Fcar-emitting-carbon-dioxide-co-environmental-pollution-problem-vector-illustration-isolated-white-background-124259733.jpg&f=1&nofb=1&ipt=d91c33fa5278a4c60968589c59d3d39a9dcd2c658f499fa4c1fb55cf10544446" alt="voiture pollution">
      <div class="card-body">
        <h3>Photo d'une poubelle déposée</h3>
        <p class="note">Essence polluante</p>
      </div>
    </div>

    <div class="box small">
      <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.freepik.com%2Fvecteurs-libre%2Fpoubelle-debordante-ordures-menageres-restes_376504-6.jpg%3Fsize%3D626%26ext%3Djpg&f=1&nofb=1&ipt=884b10f01d118cd843823cdf5436a0339de66c17b9d7eac5ffe0f904b9c6133e">
      <div class="card-body">
        <h3>Poubelle  (remplie)</h3>
        <p class="note">Poubelle qui déborde</p>
      </div>
    </div>
  </section>

  <!-- deux grandes vignettes en bas -->
  <section class="grid-bottom">
    <div class="box large">
      <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.freepik.com%2Fvecteurs-premium%2Fdessin-bus-descendant-route-montagnes-arriere-plan_1157866-1253.jpg&f=1&nofb=1&ipt=4bd3ce37bc5db28f05b7de62489e08eb389db3f5953928f5a3764ce51faf4863" alt="Transports en commun">
      <div class="card-body">
        <h3>Prioriser les transports en commun</h3>
        <p class="note">Mobilité durable — image libre Pixabay</p>
      </div>
    </div>

    <div class="box large">
      <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Fd%25C3%25A9chets-plastiques-de-dans-l-eau-mer-oc%25C3%25A9an-illustration-vecteur-plastique-la-avec-des-dessin-d-environnement-pollu%25C3%25A9-202922331.jpg&f=1&nofb=1&ipt=5ed8f954c12b8842c62d930525109a20e4ec6056c08f7b2a822b3abff1f47283" alt="Pollution plastique océan">
      <div class="card-body">
        <h3>Océan avec accumulation de plastique</h3>
        <p class="note">Pollution marine — image libre Pexels</p>
      </div>
    </div>
  </section>

</div>

<footer>
    Fait par Sohaib ait bella — images libres de droits (Pexels / Pixabay)
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
            

