import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

from db import describe_database_target, init_db
from routes import bp

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
    )
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")

    # Local default: SQLite file. For production set a Postgres DATABASE_URL.
    app.config["DATABASE_URL"] = os.environ.get(
        "DATABASE_URL",
        "sqlite:///feedback.db",
    )

    init_db(app)
    app.register_blueprint(bp)

    @app.get("/health")
    def health():
        return {
            "ok": True,
            "database": describe_database_target(app.config["DATABASE_URL"]),
        }

    return app


app = create_app()


if __name__ == "__main__":
    print(f"Database: {describe_database_target(app.config['DATABASE_URL'])}")
    app.run(debug=True, port=int(os.environ.get("PORT", "5000")))
