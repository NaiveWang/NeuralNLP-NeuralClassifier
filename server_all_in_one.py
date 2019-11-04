from flask import Flask, request, render_template
import json
import ast
import time
import predictor

pdt = predictor.Predictor('conf/2.json')


def _infer(jtext):
    print('infering', end='')
    jtext=jtext.split('\n')
    tag=False
    if len(jtext) == 1:
        jtext = [jtext[0], jtext[0]]
        tag=True
    p=pdt.predict_batch(jtext)
    if tag:
        p = [p[0]]
    print('finished', time.time())
    return p.__str__()






app = Flask(__name__)
@app.route('/headless', methods=['POST'])
def infer_json():
    s=''
    #print("+++", request.json, "+++")
    for post in request.json['posts']:
        s+=json.dumps({
            "doc_label": [],
            'doc_token': list(post.replace('\n', '')),
            'doc_keyword': [],
            'doc_topic': []
            }, ensure_ascii=False)
        s+='\n'

    return json.dumps({"predict":ast.literal_eval(_infer(s[:-1]))})
@app.route('/', methods=['GET'])
def root():
    # show the main page
    return render_template('root.html', results=[], text='')

@app.route('/', methods=['POST'])
def infer():
    # return a result list
    if 'squash' in request.form:
        raw=request.form['raw'].replace('\n', '').replace('\r', '')
        return render_template('root.html', results=[], text=raw)

    elif 'infer' in request.form:
        raw = request.form['raw']
        rawl=raw.split('\n')
        jtext=''
        for line in rawl:
            jtext+=json.dumps({
                    "doc_label": [],
                    'doc_token': list(line),
                    'doc_keyword': [],
                    'doc_topic': []
            }, ensure_ascii=False)
            jtext+='\n'
        #print(jtext)
        results = _infer(jtext[:-1])
        #print(results)
        return render_template('root.html', results=ast.literal_eval(results), text=raw)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=55555, debug=False) 
