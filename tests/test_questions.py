def test_create_and_get_question(client):
    # create
    r = client.post("/questions/", json={"text": "Что такое FastAPI?"})
    assert r.status_code == 201
    q = r.json()
    assert q["id"] > 0

    # list
    r2 = client.get("/questions/")
    assert r2.status_code == 200
    assert len(r2.json()) == 1

    # get with answers
    r3 = client.get(f"/questions/{q['id']}")
    assert r3.status_code == 200
    assert r3.json()["answers"] == []


def test_delete_question_cascades_answers(client):
    q = client.post("/questions/", json={"text": "Q1"}).json()
    a = client.post(f"/questions/{q['id']}/answers/", json={"user_id": "u1", "text": "A1"}).json()
    assert a["question_id"] == q["id"]

    del_resp = client.delete(f"/questions/{q['id']}")
    assert del_resp.status_code == 204

    get_ans = client.get(f"/answers/{a['id']}")
    assert get_ans.status_code == 404
