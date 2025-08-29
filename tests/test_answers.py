def test_add_answer_validation_and_fetch(client):
    q = client.post("/questions/", json={"text": "Q"}).json()

    bad = client.post(f"/questions/{q['id']}/answers/", json={"user_id": "", "text": "A"})
    assert bad.status_code == 422  # пустой user_id

    ok = client.post(
        f"/questions/{q['id']}/answers/", json={"user_id": "user-123", "text": "Ответ"}
    )
    assert ok.status_code == 201
    aid = ok.json()["id"]

    got = client.get(f"/answers/{aid}")
    assert got.status_code == 200
    assert got.json()["user_id"] == "user-123"


def test_answer_to_nonexistent_question_forbidden(client):
    r = client.post("/questions/999/answers/", json={"user_id": "u", "text": "A"})
    assert r.status_code == 400
