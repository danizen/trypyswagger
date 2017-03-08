from .fixtures import app, client


def test_list_pets_by_status(app, client):
    req, resp = app.op['findPetsByStatus'](status=['sold'])
    req.produce('application/json')
    r = client.request((req, resp))
    assert r.status == 200


