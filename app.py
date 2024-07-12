from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
import os
from split_pcap import split_pcap
from analysis.analysis import extract_hierarchy_info

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
ANALYSIS_FOLDER = 'analysis'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ANALYSIS_FOLDER'] = ANALYSIS_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(ANALYSIS_FOLDER):
    os.makedirs(ANALYSIS_FOLDER)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and (file.filename.endswith('.pcap') or file.filename.endswith('.pcapng')):
        segments = request.form['segments']
        if not segments.isdigit() or int(segments) < 1:
            flash('Invalid number of segments')
            return redirect(request.url)
        segments = int(segments)
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        output_prefix = os.path.join(app.config['UPLOAD_FOLDER'], os.path.splitext(file.filename)[0])
        split_pcap(filename, output_prefix)
        
        # Get the list of split files
        split_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.startswith(os.path.splitext(file.filename)[0])]
        
        # Perform analysis
        hierarchy_data = extract_hierarchy_info(filename)
        
        return render_template('results.html', files=split_files, hierarchy_data=hierarchy_data)
    else:
        flash('Invalid file type. Only .pcap and .pcapng files are allowed.')
        return redirect(request.url)

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
