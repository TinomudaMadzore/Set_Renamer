from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
from pathlib import Path

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/list-directory', methods=['POST'])
def list_directory():
    """List all files in a directory"""
    data = request.json
    directory = data.get('directory', '')
    
    if not directory:
        # Return user's home directory by default
        directory = str(Path.home())
    
    try:
        files = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                # Only include image files
                if item.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff')):
                    files.append({
                        'name': item,
                        'path': item_path
                    })
        
        return jsonify({
            'success': True,
            'directory': directory,
            'files': files
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/get-file', methods=['POST'])
def get_file():
    """Get file as base64 for thumbnail"""
    data = request.json
    file_path = data.get('path', '')
    
    try:
        import base64
        with open(file_path, 'rb') as f:
            file_data = base64.b64encode(f.read()).decode('utf-8')
        
        # Detect mime type
        ext = os.path.splitext(file_path)[1].lower()
        mime_types = {
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.webp': 'image/webp',
            '.tiff': 'image/tiff'
        }
        mime_type = mime_types.get(ext, 'image/jpeg')
        
        return jsonify({
            'success': True,
            'data': f'data:{mime_type};base64,{file_data}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/rename-files', methods=['POST'])
def rename_files():
    """Rename files according to the rules"""
    data = request.json
    rename_operations = data.get('operations', [])
    
    results = []
    errors = []
    
    for op in rename_operations:
        old_path = op.get('oldPath')
        new_name = op.get('newName')
        
        try:
            # Get directory and create new path
            directory = os.path.dirname(old_path)
            old_ext = os.path.splitext(old_path)[1]
            new_path = os.path.join(directory, new_name + old_ext)
            
            # Check if target already exists
            if os.path.exists(new_path):
                errors.append(f"File already exists: {new_name}{old_ext}")
                continue
            
            # Rename the file
            os.rename(old_path, new_path)
            results.append({
                'old': os.path.basename(old_path),
                'new': new_name + old_ext,
                'success': True
            })
        except Exception as e:
            errors.append(f"Failed to rename {os.path.basename(old_path)}: {str(e)}")
    
    return jsonify({
        'success': len(errors) == 0,
        'results': results,
        'errors': errors
    })

if __name__ == '__main__':
    print("=" * 50)
    print("File Renaming Tool - Server Starting")
    print("=" * 50)
    print("Open your browser and go to: http://localhost:5000")
    print("Press CTRL+C to stop the server")
    print("=" * 50)
    app.run(debug=True, port=5000)