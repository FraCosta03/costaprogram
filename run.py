from flask import Flask, jsonify, make_response
from http import HTTPStatus
from src.app.__init__ import create_app

app = create_app('default')