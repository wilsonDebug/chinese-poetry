# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, abort
import os
import json

app = Flask(__name__)

# 诗词JSON数据目录
DATA_DIR = os.path.join(os.path.dirname(__file__), '宋词')

# 获取所有宋词分卷文件名
def get_ci_json_files():
    files = []
    for fname in os.listdir(DATA_DIR):
        if fname.startswith('ci.song.') and fname.endswith('.json'):
            files.append(os.path.join(DATA_DIR, fname))
    return sorted(files)

# 获取所有宋词
@app.route('/api/ci', methods=['GET'])
def get_all_ci():
    result = []
    for fpath in get_ci_json_files():
        with open(fpath, encoding='utf-8') as f:
            result.extend(json.load(f))
    return jsonify(result)

# 按作者查询宋词
@app.route('/api/ci/author/<author>', methods=['GET'])
def get_ci_by_author(author):
    result = []
    for fpath in get_ci_json_files():
        with open(fpath, encoding='utf-8') as f:
            for ci in json.load(f):
                if ci['author'] == author:
                    result.append(ci)
    return jsonify(result)

# 按词牌名查询宋词
@app.route('/api/ci/rhythmic/<rhythmic>', methods=['GET'])
def get_ci_by_rhythmic(rhythmic):
    result = []
    for fpath in get_ci_json_files():
        with open(fpath, encoding='utf-8') as f:
            for ci in json.load(f):
                if ci['rhythmic'] == rhythmic:
                    result.append(ci)
    return jsonify(result)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': '中国古代诗词 RESTful API',
        'endpoints': [
            '/api/ci',
            '/api/ci/author/<author>',
            '/api/ci/rhythmic/<rhythmic>'
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)