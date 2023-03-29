import sys
sys.path.append("flask_app")

from models import *

db.drop_all()
db.create_all()
# exit()


unit_titles_file = open("units/unit_titles.txt")
unit_titles = unit_titles_file.read().split("\n")[:-1]
unit_titles_file.close()

for title in unit_titles:
    unit = Unit(title=title)
    db.session.add(unit)


for unit_no in range(1, 16):
    unit_dir = f"units/unit_{unit_no}"
    topic_file = open(f"{unit_dir}/topic_titles.txt")
    quiz_file = open(f"{unit_dir}/quiz_titles.txt")


    topic_titles = topic_file.read().split("\n")[:-1]
    quiz_title = quiz_file.read().split("\n")[:-1][0]

    topic_file.close()
    quiz_file.close()

    for title in topic_titles:
        section = Section(unit_id=unit_no, title=title, type="topic")
        db.session.add(section)

    # Only one quiz
    section = Section(unit_id=unit_no, title=quiz_title, type="quiz")
    db.session.add(section)

db.session.commit()
