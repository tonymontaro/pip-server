from flask import request
from app.models import User, PIPModel

from flask_restful import Resource


class PIPView(Resource):

    def get(self):
        pips = PIPModel.all()
        print(pips)
        results = []

        for pip in pips:
            res = {
                'id': pip.id,
                'fellow': pip.fellow,
                'location': pip.location,
                'manager': pip.manager,
                'status': pip.status
            }
            results.append(res)

        return results, 200

    def post(self):
        fellow = request.form.get('fellow')
        manager = 1

        pip = PIPModel(fellow=fellow, manager=manager)
        pip.save()
        res = {
            'id': pip.id,
            'fellow': pip.fellow,
            'manager': pip.manager
        }

        return res, 201
