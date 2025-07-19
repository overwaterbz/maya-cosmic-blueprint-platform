#!/usr/bin/env python3
"""
Maya Cosmic Blueprint Platform - Vercel Entry Point
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Maya Cosmic Blueprint Platform")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def homepage():
    """Maya platform homepage"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maya Cosmic Blueprint Platform</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Arial', sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            color: white; 
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container { max-width: 1200px; padding: 40px 20px; text-align: center; }
        .logo { font-size: 4rem; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .subtitle { font-size: 1.5rem; margin-bottom: 40px; opacity: 0.9; }
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin: 40px 0; }
        .feature { 
            background: rgba(255,255,255,0.1); 
            padding: 30px; 
            border-radius: 15px; 
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease;
        }
        .feature:hover { transform: translateY(-5px); }
        .feature h3 { font-size: 1.5rem; margin-bottom: 15px; }
        .cta { 
            background: linear-gradient(45deg, #ff6b6b, #feca57); 
            color: white; 
            padding: 20px 40px; 
            border: none; 
            border-radius: 30px; 
            font-size: 1.2rem; 
            cursor: pointer; 
            margin: 20px 10px;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
        }
        .cta:hover { transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
        .status { 
            background: rgba(0,255,0,0.2); 
            padding: 20px; 
            border-radius: 10px; 
            margin-top: 40px; 
            border: 1px solid rgba(0,255,0,0.3);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🌟 Maya Cosmic Blueprint</div>
        <div class="subtitle">Discover Your Sacred Cosmic Signature Through Ancient Maya Wisdom</div>
        
        <div class="features">
            <div class="feature">
                <h3>🔮 AI-Powered Spiritual Guidance</h3>
                <p>Connect with Ix Chel, the Maya Moon Goddess, for personalized spiritual insights and cosmic guidance tailored to your unique spiritual signature.</p>
            </div>
            
            <div class="feature">
                <h3>⭐ Cosmic Blueprint Analysis</h3>
                <p>Receive detailed analysis of your Maya day sign, galactic tone, and cosmic elements that reveal your soul's purpose and spiritual path.</p>
            </div>
            
            <div class="feature">
                <h3>🎭 Sacred Soul Contracts</h3>
                <p>Discover your divine mission, soul gifts, and cosmic connections through comprehensive soul contract readings based on Maya calendar wisdom.</p>
            </div>
            
            <div class="feature">
                <h3>💫 Spiritual Tools Marketplace</h3>
                <p>Access Maya Oracle Cards, Dream Interpretation, Sacred Rituals, and other spiritual tools designed for your cosmic blueprint.</p>
            </div>
        </div>
        
        <div>
            <a href="/register" class="cta">Get Your Cosmic Blueprint</a>
            <a href="/login" class="cta">Access Your Dashboard</a>
        </div>
        
        <div class="status">
            <h4>✅ Platform Status: Operational</h4>
            <p>Vercel deployment successful - Maya Cosmic Blueprint Platform is live at magic.mayanbelize.com</p>
            <p>Ready for user registration and cosmic blueprint generation</p>
        </div>
    </div>
</body>
</html>"""

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "platform": "Maya Cosmic Blueprint", "version": "1.0.0"}

@app.get("/api/status")
async def api_status():
    """API status endpoint"""
    return {
        "status": "operational",
        "platform": "Maya Cosmic Blueprint Platform",
        "features": [
            "Cosmic Blueprint Analysis",
            "AI Spiritual Guidance", 
            "Soul Contract Generation",
            "Spiritual Tools Marketplace"
        ],
        "deployment": "Vercel",
        "domain": "magic.mayanbelize.com"
    }

# For Vercel deployment
handler = app
