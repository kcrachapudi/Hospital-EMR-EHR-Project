import database
import models

models.Base.metadata.create_all(bind=database.engine)