from flask import Flask
from flask_graphql import GraphQLView
from schemas import schema

import sentry_sdk
sentry_sdk.init("https://007e055e5fe64e35b55b36140bf6b18d@o371271.ingest.sentry.io/5363923")

app = Flask(__name__)

app.add_url_rule(
    "/", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)
if __name__ == "__main__": 
    app.run(debug=True)

