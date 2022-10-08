import json

from create_app import create_app, db

from flask import current_app as app, request

from models import User

@app.route("/users", methods=['Get', 'POST'])
def work_user():
    if request.method == 'GET':
        result = []
        for user in db.session.query(User).all():
            result.append(
                user.return_data()
            )

        return app.response_class(
            json.dumps(result),
            mimetype="application/json",
            status=200
        )

        if request.method == 'POST':

            data = request.json

            db.session.add(
                User(
                    **data
                )
            )
            return app.response_class(
                json.dumps("OK"),
                mimetype="application/json",
                status=200
            )

if __name__ == "__main__":
    app.run()