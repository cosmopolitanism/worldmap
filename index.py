# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask('index')


@app.route('/', methods=['GET'])
def index():
    board = list()
    with open('pole.txt', 'r') as f:
        for line in f:
            board.append('X' * len(line.strip()))
    context = {
        'board': board,
    }
    return render_template('pole.html', **context)


if __name__ == '__main__':
    app.run()
