from main import app, db, Movie

movies = [
    Movie(title='John Wick', year=2014, description='An ex-hitman comes out of retirement to track down the gangsters that killed his dog.', rating=7.4, ranking=3, review='Thrilling action masterpiece', img_url='/static/images/john_wick.jpg'),
    Movie(title='Breaking Bad', year=2008, description='A chemistry teacher diagnosed with terminal lung cancer teams up with a former student to manufacture and sell methamphetamine.', rating=9.5, ranking=1, review='Greatest TV series ever made', img_url='/static/images/breaking_bad.jpg'),
    Movie(title='Better Call Saul', year=2015, description='The trials and tribulations of criminal lawyer Jimmy McGill in the years leading up to his fateful run-in with Walter White.', rating=9.0, ranking=2, review='A slow burn masterpiece', img_url='/static/images/better_call_saul.jpg'),
    Movie(title='The Three-Body Problem', year=2024, description="A young woman's fateful decision in 1960s China reverberates across space and time to a group of scientists in the present day.", rating=7.7, ranking=4, review='Mind-bending sci-fi', img_url='/static/images/three_body_problem.jpg'),
    Movie(title='One Piece', year=1999, description='Monkey D. Luffy sets off on an adventure with his pirate crew in hopes of finding the greatest treasure ever, known as One Piece.', rating=8.9, ranking=5, review='Epic adventure on the high seas', img_url='/static/images/one_piece.jpg'),
    Movie(title='Rick and Morty', year=2013, description='An animated series that follows the exploits of a super scientist and his not-so-bright grandson.', rating=9.1, ranking=6, review='Genius dark comedy', img_url='/static/images/rick_and_morty.jpg'),
    Movie(title='All Her Fault', year=2025, description='A mother arrives to collect her son from a playdate, only to find a stranger at the door who claims to know nothing about her child.', rating=7.5, ranking=7, review='Gripping thriller', img_url='/static/images/all_her_fault.jpeg'),
    Movie(title='Friends', year=1994, description='Follows the personal and professional lives of six twenty to thirty year-old friends living in the Manhattan area.', rating=8.9, ranking=8, review='The one that defined sitcoms', img_url='/static/images/friends.jpg'),
    Movie(title='How I Met Your Mother', year=2005, description='A father recounts to his children the events that led him to meet their mother.', rating=8.3, ranking=9, review='Legend... Wait for it... Dary!', img_url='/static/images/how_i_met_your_mother.jpg'),
    Movie(title='Peaky Blinders', year=2013, description='A gangster family epic set in 1900s England, centering on a gang who sew razor blades in the peaks of their caps.', rating=8.8, ranking=10, review='By order of the Peaky Blinders', img_url='/static/images/peaky_blinders.webp'),
    Movie(title='El Camino: A Breaking Bad Movie', year=2019, description='Fugitive Jesse Pinkman runs from his captors, the law, and his past.', rating=7.0, ranking=11, review='A fitting farewell to Jesse', img_url='/static/images/el_camino.webp'),
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for movie in movies:
        db.session.add(movie)
    db.session.commit()
    print("Database seeded successfully with local images!")
    for m in db.session.execute(db.select(Movie)).scalars():
        print(f"  {m.ranking}. {m.title} ({m.year})")

