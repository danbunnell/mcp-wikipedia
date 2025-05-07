from flask import Flask, request, jsonify
import wikipedia
import json

app = Flask(__name__)

@app.route('/mcp', methods=['POST'])
def handle_mcp_request():
    try:
        # Parse the MCP request
        data = request.get_json()
        if not data or 'topic' not in data:
            return jsonify({
                'error': 'Missing topic parameter'
            }), 400

        topic = data['topic']
        
        # Get the Wikipedia page content
        page = wikipedia.page(topic)
        
        # Return the response in MCP format
        return jsonify({
            'status': 'success',
            'data': {
                'title': page.title,
                'content': page.content,
                'url': page.url
            }
        })

    except wikipedia.exceptions.DisambiguationError as e:
        return jsonify({
            'status': 'error',
            'error': 'Disambiguation page',
            'options': e.options
        }), 400
    except wikipedia.exceptions.PageError:
        return jsonify({
            'status': 'error',
            'error': 'Page not found'
        }), 404
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 