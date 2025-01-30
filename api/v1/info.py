#!/usr/bin/env python3
"""
module app:
Flask public API
"""
from api.v1 import app_bp
from datetime import datetime
from flask import jsonify


@app_bp.route('/info')
def info():
    """ Retrieves basic information:
    Registered email address; Current date and time; Github URL
    """
    email = 'twkamanja@gmail.com'
    current_dt = datetime.now()
    github_url = 'https://github.com/Toteya/hng-stage_0.git'
    
    information = {
        "email": email,
        "current_datetime": current_dt.isoformat(timespec='seconds'),
        "github_url": github_url
    }

    return jsonify(information), 200
