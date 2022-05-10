from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
import model
import orm
import repository
import services

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)


@app.route("/allocate", methods=["POST"])
def allocate_endpoint():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    line = model.OrderLine(
        request.json["orderid"],
        request.json["sku"],
        request.json["qty"],
    )

    try:
        batchref = services.allocate(line, repo, session)
    except (model.OutOfStock, services.InvalidSku) as e:
        return {"message": str(e)}, 400

    session.commit()
    return {"batchref": batchref}, 201


@app.route("/deallocate", methods=["POST"])
def deallocate_endpoint():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    orderid = request.json["orderid"]
    sku = request.json["sku"]

    try:
        services.deallocate(orderid, sku, repo, session)
    except services.InvalidSku as e:
        return {"message": str(e)}, 400
    except services.NotFound:
        return {"message": str(e)}, 404
    except Exception as e:
        return {"message": str(e)}, 500

    return {"message": "success"}, 200
