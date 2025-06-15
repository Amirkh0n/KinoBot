from database import Users, Movies
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# part database
DB_NAME = "database/database.db"

users = Users()
movies = Movies()

CHANNEL_ID = {
    "short_video": -1002639346604,
    "full_video": -1002639346604,
    "ads": {
        1: {
            "type": "channel",
            "id": -1002639346604,
            "link": ""
        },
        2: {
            "type": "channel",
            "id": -1002639346604,
            "link": ""
        },
        3: {
            "type": "channel",
            "id": -1002639346604,
            "link": ""
        },
        4: {
            "type": "channel",
            "id": -1002639346604,
            "link": ""
        },
        5: {
            "type": "channel",
            "id": -1002639346604,
            "link": ""
        },
        6: {
            "type": "channel",
            "id": -1002639346604,
            "link": ""
        }
    }
}
    

class Steps:
    main_menu = 0
    add_movie = 1
    add_movie_title = 2
    