from flask import request, jsonify
from .models import db, Destino


def init_routes(app):

    # Rota Home
    @app.route("/")
    def home():
        return jsonify({"mensagem": "Bem-vindo à API de Destinos de Viagem!"})


    # GET - Listar todos os destinos
    @app.route("/destinos", methods=["GET"])
    def obter_destinos():
        destinos = Destino.query.all()
        return jsonify([destino.to_dict() for destino in destinos])


    # GET - Buscar destino por ID
    @app.route("/destinos/<int:destination_id>", methods=["GET"])
    def obter_destino(destination_id):
        destino = Destino.query.get(destination_id)

        if not destino:
            return jsonify({"erro": "Destino não encontrado"}), 404

        return jsonify(destino.to_dict())


    # POST - Criar novo destino
    @app.route("/destinos", methods=["POST"])
    def adicionar_destino():
        data = request.get_json()

        # Validação simples
        if not data or not all(k in data for k in ("destino", "pais", "nota")):
            return jsonify({"erro": "Dados inválidos"}), 400

        novo_destino = Destino(
            destino=data["destino"],
            pais=data["pais"],
            nota=data["nota"]
        )

        db.session.add(novo_destino)
        db.session.commit()

        return jsonify(novo_destino.to_dict()), 201


    # PUT - Atualizar destino
    @app.route("/destinos/<int:destination_id>", methods=["PUT"])
    def atualizar_destino(destination_id):
        destino = Destino.query.get(destination_id)

        if not destino:
            return jsonify({"erro": "Destino não encontrado"}), 404

        data = request.get_json()

        destino.destino = data.get("destino", destino.destino)
        destino.pais = data.get("pais", destino.pais)
        destino.nota = data.get("nota", destino.nota)

        db.session.commit()

        return jsonify(destino.to_dict())


    # DELETE - Remover destino
    @app.route("/destinos/<int:destination_id>", methods=["DELETE"])
    def deletar_destino(destination_id):
        destino = Destino.query.get(destination_id)

        if not destino:
            return jsonify({"erro": "Destino não encontrado"}), 404

        db.session.delete(destino)
        db.session.commit()

        return jsonify({"mensagem": "Destino deletado com sucesso"})
