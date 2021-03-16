from flask import Flask, jsonify, render_template
from util import query

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes")
@app.route("/recipes/")
def recipes():
    retete = query(
        """
        select id, name
        from recipes
        where id > 7
        ;
    """
    )
    return jsonify(retete)


@app.route("/recipe/<int:id>")
@app.route("/recipes/<int:id>")
@app.route("/recipes/<int:id>/")
def getRecipe(id):
    reteta = query(
        """
            select
                recipes.name,
                users.name as author
            from
                recipes
            left join
                users
            on
                users.id = recipes.author
            where
                recipes.id = %(idulretetei)s;
        """,
        {"idulretetei": id},
    )
    
    return jsonify(reteta)


if __name__ == "__main__":
    app.run(debug=True)