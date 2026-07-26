from __future__ import annotations

from flask import Blueprint, flash, redirect, render_template, request, url_for

from db import insert_feedback

bp = Blueprint("main", __name__)

APP_SECTIONS = (
    "Общее",
    "Сущности",
    "Матрицы",
    "Прогнозы",
    "Результаты отпвляемые 1С",
)

COMMENT_MAX_LENGTH = 5000
POSITION_MAX_LENGTH = 200


@bp.get("/")
def index():
    return render_template(
        "index.html",
        sections=APP_SECTIONS,
        submitted=False,
        form={"section": "", "comment": "", "position": ""},
    )


@bp.post("/")
def submit():
    section = (request.form.get("section") or "").strip()
    comment = (request.form.get("comment") or "").strip()
    position_raw = (request.form.get("position") or "").strip()
    position = position_raw[:POSITION_MAX_LENGTH] if position_raw else None

    errors: list[str] = []

    if section not in APP_SECTIONS:
        errors.append("Please select an application section.")
    if not comment:
        errors.append("Comment is required.")
    elif len(comment) > COMMENT_MAX_LENGTH:
        errors.append(f"Comment must be at most {COMMENT_MAX_LENGTH} characters.")

    form = {
        "section": section,
        "comment": comment,
        "position": position_raw,
    }

    if errors:
        for message in errors:
            flash(message, "error")
        return render_template(
            "index.html",
            sections=APP_SECTIONS,
            submitted=False,
            form=form,
        ), 400

    try:
        insert_feedback(section=section, comment=comment, position=position)
    except Exception:
        flash("Could not save feedback. Please try again.", "error")
        return render_template(
            "index.html",
            sections=APP_SECTIONS,
            submitted=False,
            form=form,
        ), 500

    return render_template(
        "index.html",
        sections=APP_SECTIONS,
        submitted=True,
        form=form,
    )


@bp.get("/again")
def write_again():
    return redirect(url_for("main.index"))
