#!/usr/bin/env python3
"""
Working Vercel handler for Maya Cosmic Blueprint Platform
"""

def handler(request):
    """Main request handler"""
    
    # Get request method and path
    method = getattr(request, 'method', 'GET')
    path = getattr(request, 'url', '/')
    
    # Basic HTML response
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maya Cosmic Blueprint Platform</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; min-height: 100vh; }
        .container { max-width: 800px; margin: 0 auto; text-align: center; }
        .logo { font-size: 3em; margin-bottom: 20px; }
        .subtitle { font-size: 1.2em; margin-bottom: 40px; opacity: 0.9; }
        .feature { background: rgba(255,255,255,0.1); padding: 20px; margin: 20px 0; border-radius: 10px; }
        .btn { background: #ff6b6b; color: white; padding: 15px 30px; text-decoration: none; border-radius: 25px; display: inline-block; margin: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🌟 Maya Cosmic Blueprint</div>
        <div class="subtitle">Discover Your Sacred Cosmic Signature</div>
        
        <div class="feature">
            <h3>🔮 AI-Powered Spiritual Guidance</h3>
            <p>Connect with ancient Maya wisdom through modern AI technology</p>
        </div>
        
        <div class="feature">
            <h3>⭐ Personalized Cosmic Analysis</h3>
            <p>Receive detailed insights about your spiritual path and purpose</p>
        </div>
        
        <div class="feature">
            <h3>🎭 Sacred Soul Contracts</h3>
            <p>Discover your divine mission and cosmic connections</p>
        </div>
        
        <div class="feature">
            <h3>💫 Ix Chel AI Companion</h3>
            <p>Chat with the Maya Moon Goddess for personalized spiritual guidance</p>
        </div>
        
        <div style="margin-top: 40px;">
            <h4>Platform Status: Operational</h4>
            <p>Vercel deployment successful - Function invocation working</p>
            <p>Ready for full FastAPI integration</p>
        </div>
    </div>
</body>
</html>"""
    
    # Return proper response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html; charset=utf-8',
            'Cache-Control': 'no-cache'
        },
        'body': html_content
    }

# Export for Vercel
app = handler
