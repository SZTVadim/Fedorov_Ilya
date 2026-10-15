
from .base_api import BaseAPI


class NotesAPI(BaseAPI):

    def get_notes(self, token=None):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return self.get("/api/notes", headers=headers)


    def create_note(self, token, title, content):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        data = {
            "title": title,
            "content": content
        }

        return self.post("/api/notes", data=data, headers=headers)


    def delete_note(self, token, note_id):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return self.delete(
            f"/api/notes/{note_id}",
            headers=headers
        )
