# -*- coding: utf-8 -*-
# @Time    : 25.06.21 13:28
# @Author  : Tek Raj Chhetri
# @Email   : tekraj.chhetri@sti2.at
# @File    : user.py
# @Software: PyCharm


from flask_restful import Resource, request
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, ValidationError
from flask_apispec import marshal_with, doc, use_kwargs
from core.storage.JWTUser import JWTUser


class UserSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    confirm_password = fields.Str()
    organizational_identifier = fields.Str()


class ReturnSchemaJWT(Schema):
    act_status_code = fields.Integer(required=True)
    decision = fields.String(required=True)
    decision_token = fields.String(required=True)
    message = fields.String(optional=True)
    timestamp = fields.String(required=True)


class LoginSchema(Schema):
    username = fields.Str()
    password = fields.Str()


class LoginReturnSchema(Schema):
    access_token = fields.Str()


class JWTUserRegister(MethodResource, Resource):
    @doc(description="User.", tags=["USER"])
    @use_kwargs(UserSchema)
    @marshal_with(ReturnSchemaJWT)
    def post(self, **kwargs):
        schema_serializer = UserSchema()
        data = request.get_json(force=True)
        try:
            validated_data = schema_serializer.load(data)
        except ValidationError as e:
            return {"error": str(e)}, 400

        jwt_user_inst = JWTUser()
        response = jwt_user_inst.register_user(
            username=validated_data["username"],
            password=validated_data["password"],
            confirm_password=validated_data["confirm_password"],
            organization=validated_data["organizational_identifier"],
        )
        return response


class JWTUserLogin(MethodResource, Resource):
    @doc(description="User.", tags=["USER"])
    @use_kwargs(LoginSchema)
    @marshal_with(LoginReturnSchema)
    def post(self, **kwargs):
        schema_serializer = LoginSchema()
        data = request.get_json(force=True)
        try:
            validated_data = schema_serializer.load(data)
        except ValidationError as e:
            return {"error": str(e)}, 400

        jwt_user_inst = JWTUser()
        response = jwt_user_inst.login_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        return response
