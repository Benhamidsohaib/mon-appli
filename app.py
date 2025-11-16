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
      <img src="https://fr.freepik.com/vecteurs-libre/voitures-usines-grande-ville-font-fumee-sale_5837846.htm#fromView=search&page=1&position=0&uuid=00fbdff7-8ae1-42c8-a93e-fcf66b79a40d&query=voiture+polluante" alt="Poubelle déposée">
      <div class="card-body">
        <h3>Photo d'une poubelle déposée</h3>
        <p class="note">Essence polluante</p>
      </div>
    </div>

    <div class="box small">
      <img src="https://fr.freepik.com/vecteurs-libre/composition-dechets-organiques_26764821.htm#fromView=search&page=1&position=3&uuid=e381b856-2515-44e1-9c83-2cb74ac469af&query=poubelle+pleine" alt="Poubelle débordante">
      <div class="card-body">
        <h3>Poubelle  (remplie)</h3>
        <p class="note">Poubelle qui déborde</p>
      </div>
    </div>
  </section>

  <!-- deux grandes vignettes en bas -->
  <section class="grid-bottom">
    <div class="box large">
      <img src="https://fr.freepik.com/vecteurs-libre/illustration-concept-abstrait-voyage-terrain-voyage-scolaire-excursion-pour-eleves-voyage-groupe-etudiants-decouverte-nature-visite-experience-culturelle-activite-processus-scolaire_12145624.htm#fromView=search&page=2&position=10&uuid=9979704c-2067-4ab4-8bdc-56bf4a87ec54&query=bus" alt="Transports en commun">
      <div class="card-body">
        <h3>Prioriser les transports en commun</h3>
        <p class="note">Mobilité durable — image libre Pixabay</p>
      </div>
    </div>

    <div class="box large">
      <img src="https://images.pexels.com/photos/2873277/pexels-photo-2873277.jpeg" alt="Pollution plastique océan">
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
            

