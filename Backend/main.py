from flask import Flask
from flask_cors import CORS
from pyngrok import ngrok
from app.routes import main_routes
from app.models import image_model
from app.models import text_model

def create_app():
    app = Flask(__name__)
    CORS(app) #CORS支持 前端可以跨域请求后端
    app.register_blueprint(main_routes.bp)
    return app #理解为返回一个服务器

if __name__ == "__main__":
    ngrok.set_auth_token("Your Tokens")
    public_url = ngrok.connect(5000) #本地端5000映射为公网地址
    print(f"Public URL: {public_url}")

    app = create_app()
    app.run(port=5000) #在端口5000处运行