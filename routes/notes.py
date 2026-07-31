from flask import Blueprint, request, session

from config import db
from models import Note

notes_bp = Blueprint("notes", __name__)


def current_user_id():
    return session.get("user_id")


@notes_bp.route("/notes", methods=["GET"])
def get_notes():
    user_id = current_user_id()

    if not user_id:
        return {"error": "Unauthorized"}, 401

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)

    pagination = (
        Note.query
        .filter_by(user_id=user_id)
        .order_by(Note.created_at.desc())
        .paginate(page=page, per_page=per_page, error_out=False)
    )

    notes = []

    for note in pagination.items:
        notes.append({
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "created_at": note.created_at.isoformat(),
        })

    return {
        "notes": notes,
        "page": pagination.page,
        "pages": pagination.pages,
        "total": pagination.total,
    }, 200


@notes_bp.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    user_id = current_user_id()

    if not user_id:
        return {"error": "Unauthorized"}, 401

    note = Note.query.filter_by(id=id, user_id=user_id).first()

    if not note:
        return {"error": "Note not found"}, 404

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "created_at": note.created_at.isoformat(),
    }, 200


@notes_bp.route("/notes", methods=["POST"])
def create_note():
    user_id = current_user_id()

    if not user_id:
        return {"error": "Unauthorized"}, 401

    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    note = Note(
        title=title,
        content=content,
        user_id=user_id,
    )

    db.session.add(note)
    db.session.commit()

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "created_at": note.created_at.isoformat(),
    }, 201


@notes_bp.route("/notes/<int:id>", methods=["PATCH"])
def update_note(id):
    user_id = current_user_id()

    if not user_id:
        return {"error": "Unauthorized"}, 401

    note = Note.query.filter_by(id=id, user_id=user_id).first()

    if not note:
        return {"error": "Note not found"}, 404

    data = request.get_json()

    if "title" in data:
        note.title = data["title"]

    if "content" in data:
        note.content = data["content"]

    db.session.commit()

    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "created_at": note.created_at.isoformat(),
    }, 200


@notes_bp.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    user_id = current_user_id()

    if not user_id:
        return {"error": "Unauthorized"}, 401

    note = Note.query.filter_by(id=id, user_id=user_id).first()

    if not note:
        return {"error": "Note not found"}, 404

    db.session.delete(note)
    db.session.commit()

    return {}, 204