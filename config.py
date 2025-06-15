from database import Users, Movies

TOKEN = ""
WEBHOOK_URL = ""

# part database
DB_NAME = "database/database.db"

users = Users()
movies = Movies()

CHANNEL_ID = {
    "short_video": ,
    "full_video": ,
    "ads": {
        1: {
            "type": "channel",
            "id": ,
            "link": ""
        },
        2: {
            "type": "channel",
            "id": ,
            "link": ""
        },
        3: {
            "type": "channel",
            "id": ,
            "link": ""
        },
        4: {
            "type": "channel",
            "id": ,
            "link": ""
        },
        5: {
            "type": "channel",
            "id": ,
            "link": ""
        },
        6: {
            "type": "channel",
            "id": ,
            "link": ""
        }
    }
}
    

class Steps:
    main_menu = 0
    add_movie = 1
    add_movie_title = 2
    