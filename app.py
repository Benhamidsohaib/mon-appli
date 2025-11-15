from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projet Anti-Gaspi</title>

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
    <div class="subtitle">Photos libres de droits — Thème vert écologique</div>
</header>

<div class="container">

  <!-- deux petites vignettes en haut -->
  <section class="grid-top">
    <div class="box small">
      <img src="https://images.unsplash.com/photo-1602524201788-2a6b5a0a9d6d?auto=format&fit=crop&w=1200&q=80" alt="poubelle à terre">
      <div class="card-body">
        <h3>Photo d'une poubelle déposée</h3>
        <p class="note">Poubelle renversée / déchets au sol — image libre (Unsplash)</p>
      </div>
    </div>

    <div class="box small">
      <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=80" alt="poubelle remplie devant restaurant">
      <div class="card-body">
        <h3>Poubelle à côté d'un restaurant (remplie)</h3>
        <p class="note">Bac plein à l'extérieur d'un commerce — image libre (Unsplash)</p>
      </div>
    </div>
  </section>

  <!-- deux grandes vignettes en bas -->
  <section class="grid-bottom">
    <div class="box large">
      <img src="https://images.unsplash.com/photo-1511918984145-48de785d4c4b?auto=format&fit=crop&w=1400&q=80" alt="conducteur voiture">
      <div class="card-body">
        <h3>Quelqu'un qui conduit une voiture</h3>
        <p class="note">Image représentant la mobilité et le transport — image libre (Unsplash)</p>
      </div>
    </div>

    <div class="box large">
      <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1400&q=80" alt="océan plastique">
      <div class="card-body">
        <h3>Océan avec une flaque (ou accumulation) de plastique</h3>
        <p class="note">Pollution marine et déchets plastiques — image libre (Unsplash)</p>
      </div>
    </div>
  </section>

</div>

<footer>
    Fait par Sohaib — images Unsplash (libres). Si tu veux d'autres photos, dis-moi le type exact et je les remplace.
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

