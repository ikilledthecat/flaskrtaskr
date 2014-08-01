from app.views import db
# from app.models.tasks import FTasks
#from datetime import date

#create the database and the db table
db.create_all()

# db.session.add(FTasks("Finish this tutorial", date(2014, 3, 13), 10, 1))
# db.session.add(FTasks("Finish Real Python", date(2014, 3, 13), 10, 1))

# # commit the changes
db.session.commit()
