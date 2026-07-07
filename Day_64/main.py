from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(32).hex())
Bootstrap5(app)

## CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

## CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# Forms
class EditForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Search")

class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = FloatField("Rating")
    ranking = IntegerField("Ranking")
    review = StringField("Review")
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# Local Mock Database fallback when TMDB API Key is not configured
MOCK_MOVIES = [
    {
        "id": 101,
        "title": "The Dark Knight",
        "release_date": "2008-07-16",
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "img_url": "https://image.tmdb.org/t/p/w500/qJ2tWw2COwKXJhq5kBFYmtuuaA6.jpg"
    },
    {
        "id": 102,
        "title": "Inception",
        "release_date": "2010-07-15",
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "img_url": "https://image.tmdb.org/t/p/w500/o01vCoZ2iciR3t4i176j7f47jMA.jpg"
    },
    {
        "id": 103,
        "title": "Interstellar",
        "release_date": "2014-11-05",
        "description": "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.",
        "img_url": "https://image.tmdb.org/t/p/w500/gEU2QvHOm5tJ708vj3nuoSIYZBB.jpg"
    },
    {
        "id": 104,
        "title": "Pulp Fiction",
        "release_date": "1994-09-10",
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "img_url": "https://image.tmdb.org/t/p/w500/d5iil4FJm0VZjsYEvq59I0m1Cmc.jpg"
    },
    {
        "id": 105,
        "title": "Fight Club",
        "release_date": "1999-10-15",
        "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
        "img_url": "https://image.tmdb.org/t/p/w500/pB8BM76G6j0N7i6Z085eJDXZ4qg.jpg"
    },
    {
        "id": 106,
        "title": "The Matrix",
        "release_date": "1999-03-30",
        "description": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
        "img_url": "https://image.tmdb.org/t/p/w500/f89U3wz6j2F7R7fsR7jK1eLEwaR.jpg"
    },
    {
        "id": 107,
        "title": "The Godfather",
        "release_date": "1972-03-14",
        "description": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone, barely survives an attempt on his life, his youngest son, Michael, steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
        "img_url": "https://image.tmdb.org/t/p/w500/3bhkrj6PjOqabNmjjgk60ueXDW8.jpg"
    },
    {
        "id": 108,
        "title": "Forrest Gump",
        "release_date": "1994-06-23",
        "description": "A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. Yet, despite all the things he has attained, his one true love eludes him.",
        "img_url": "https://image.tmdb.org/t/p/w500/arw2je72tNy2546yp2HBmgj7a0M.jpg"
    },
    {
        "id": 109,
        "title": "The Shawshank Redemption",
        "release_date": "1994-09-23",
        "description": "Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden.",
        "img_url": "https://image.tmdb.org/t/p/w500/q6y0Go1tsDU2zKo2ptzSQgC7tOI.jpg"
    },
    {
        "id": 110,
        "title": "Gladiator",
        "release_date": "2000-05-01",
        "description": "In the year 180, the death of Emperor Marcus Aurelius throws the Roman Empire into chaos. Maximus is one of the Roman army's most capable and trusted generals and a key advisor to the Emperor. As Marcus' devious son Commodus ascends to the throne, Maximus is condemned to death, and his family is slaughtered.",
        "img_url": "https://image.tmdb.org/t/p/w500/ty85ILIL3h1n2lrVwtzUNhqz76L.jpg"
    },
    {
        "id": 111,
        "title": "Avatar",
        "release_date": "2009-12-10",
        "description": "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.",
        "img_url": "https://image.tmdb.org/t/p/w500/kyeE2m2Xn6n24nb7C24gfw4hy5q.jpg"
    },
    {
        "id": 112,
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "release_date": "2001-12-18",
        "description": "Young hobbit Frodo Baggins, after inheriting a mysterious ring from his uncle Bilbo, must leave his home and journey to Mount Doom to destroy it.",
        "img_url": "https://image.tmdb.org/t/p/w500/6oom5QDN2187KMW3BEiJj1wJ65c.jpg"
    }
]

# Helper to automatically update rankings based on rating
def update_rankings():
    # Sort all rated movies by rating descending
    rated_movies = db.session.execute(
        db.select(Movie).where(Movie.rating != None).order_by(Movie.rating.desc())
    ).scalars().all()
    
    for i, movie in enumerate(rated_movies):
        movie.ranking = i + 1
        
    # Unrated movies go to the bottom
    unrated_movies = db.session.execute(
        db.select(Movie).where(Movie.rating == None)
    ).scalars().all()
    
    for movie in unrated_movies:
        movie.ranking = len(rated_movies) + 1
        
    db.session.commit()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = db.get_or_404(Movie, id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        update_rankings()
        return redirect(url_for('home'))
    
    # Pre-fill
    form.rating.data = movie.rating
    form.review.data = movie.review
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete/<int:id>")
def delete(id):
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    update_rankings()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        return redirect(url_for('select', title=movie_title))
    return render_template("add.html", form=form)

@app.route("/select")
def select():
    title = request.args.get("title", "")
    tmdb_key = os.environ.get("TMDB_API_KEY")
    results = []
    
    if tmdb_key:
        # Search TMDB
        try:
            url = f"https://api.themoviedb.org/3/search/movie"
            response = requests.get(url, params={"api_key": tmdb_key, "query": title})
            if response.status_code == 200:
                data = response.json().get("results", [])
                for item in data:
                    release_date = item.get("release_date", "N/A")
                    poster_path = item.get("poster_path")
                    img_url = f"https://image.tmdb.org/t/p/w780{poster_path}" if poster_path else ""
                    results.append({
                        "id": item["id"],
                        "title": item["title"],
                        "release_date": release_date,
                        "description": item.get("overview", ""),
                        "img_url": img_url
                    })
        except Exception as e:
            pass
            
    # If no TMDB search was run or if it returned no results, search mock movies
    if not results:
        results = [
            m for m in MOCK_MOVIES if title.lower() in m["title"].lower()
        ]
        
    return render_template("select.html", movies=results)

@app.route("/find")
def find():
    movie_id = request.args.get("id")
    title = request.args.get("title")
    year = request.args.get("year", "2020")
    description = request.args.get("description", "")
    img_url = request.args.get("img_url", "")
    
    # Check if TMDB key exists and ID is numeric
    tmdb_key = os.environ.get("TMDB_API_KEY")
    movie_data = None
    
    if tmdb_key and movie_id and movie_id.isdigit():
        try:
            url = f"https://api.themoviedb.org/3/movie/{movie_id}"
            response = requests.get(url, params={"api_key": tmdb_key})
            if response.status_code == 200:
                data = response.json()
                poster_path = data.get("poster_path")
                movie_data = {
                    "title": data.get("title"),
                    "year": int(data.get("release_date", "2020-01-01").split("-")[0]),
                    "description": data.get("overview", ""),
                    "img_url": f"https://image.tmdb.org/t/p/w780{poster_path}" if poster_path else ""
                }
        except Exception:
            pass
            
    if not movie_data:
        # Check mock database
        mock_item = next((m for m in MOCK_MOVIES if str(m["id"]) == str(movie_id)), None)
        if mock_item:
            movie_data = {
                "title": mock_item["title"],
                "year": int(mock_item["release_date"].split("-")[0]),
                "description": mock_item["description"],
                "img_url": mock_item["img_url"]
            }
        else:
            # Manual fallback from params
            movie_data = {
                "title": title or "Unknown",
                "year": int(year.split("-")[0]) if year else 2020,
                "description": description or "No description available.",
                "img_url": img_url or "/static/images/placeholder.jpg"
            }
            
    # Add to DB
    # Check if already exists in DB to prevent unique constraint error
    existing = db.session.execute(db.select(Movie).where(Movie.title == movie_data["title"])).scalar()
    if existing:
        return redirect(url_for('edit', id=existing.id))
        
    new_movie = Movie(
        title=movie_data["title"],
        year=movie_data["year"],
        description=movie_data["description"],
        img_url=movie_data["img_url"]
    )
    db.session.add(new_movie)
    db.session.commit()
    update_rankings()
    
    # Retrieve the added movie to get its ID
    added_movie = db.session.execute(db.select(Movie).where(Movie.title == movie_data["title"])).scalar()
    return redirect(url_for('edit', id=added_movie.id))

@app.route("/add-manual", methods=["GET", "POST"])
def add_manual():
    form = AddForm()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            year=form.year.data,
            description=form.description.data,
            rating=form.rating.data,
            ranking=form.ranking.data,
            review=form.review.data,
            img_url=form.img_url.data or "/static/images/placeholder.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()
        update_rankings()
        return redirect(url_for('home'))
    return render_template("add.html", form=form, manual=True)

if __name__ == '__main__':
    app.run(debug=True)