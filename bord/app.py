from flask import Flask,Blueprint,render_template,request
import random
app=Flask(__name__)
products = [
    {"name": "Laptop", "price": 999.99, "description": "A high-performance laptop for all your computing needs."},
    {"name": "Smartphone", "price": 699.99, "description": "A powerful smartphone with the latest features."},
    {"name": "Headphones", "price": 199.99, "description": "Noise-cancelling headphones for immersive audio."},
    {"name": "Smartwatch", "price": 249.99, "description": "A smartwatch to keep you connected on the go."},
    {"name": "Gaming Console", "price": 499.99, "description": "Experience the best of gaming with this console."},
    {"name": "Tablet", "price": 329.99, "description": "A versatile tablet for work and play."},
    {"name": "Camera", "price": 849.99, "description": "A DSLR camera to capture your best moments."},
    {"name": "Wireless Charger", "price": 49.99, "description": "A fast wireless charger for your devices."},
    {"name": "Bluetooth Speaker", "price": 129.99, "description": "A portable speaker with powerful sound."},
    {"name": "External Hard Drive", "price": 89.99, "description": "1TB external hard drive for your data needs."},
    {"name": "Office Chair", "price": 149.99, "description": "Ergonomic office chair for maximum comfort."},
    {"name": "Electric Kettle", "price": 39.99, "description": "Boil water quickly with this electric kettle."},
    {"name": "Smart TV", "price": 1199.99, "description": "Enjoy movies and shows on this 4K Smart TV."},
    {"name": "Air Purifier", "price": 299.99, "description": "Keep your air clean and fresh."},
    {"name": "Coffee Machine", "price": 249.99, "description": "Brew your favorite coffee with ease."},
    {"name": "Fitness Tracker", "price": 99.99, "description": "Track your fitness and health goals."},
    {"name": "Gaming Mouse", "price": 59.99, "description": "Precision gaming mouse with customizable buttons."},
    {"name": "Wireless Keyboard", "price": 79.99, "description": "Slim wireless keyboard for your workstation."},
    {"name": "Drone", "price": 499.99, "description": "Capture stunning aerial footage with this drone."},
    {"name": "Smart Light Bulbs", "price": 24.99, "description": "Control your home lighting with these smart bulbs."},
    {"name": "Soundbar", "price": 179.99, "description": "Enhance your TV's audio with this soundbar."},
    {"name": "Electric Scooter", "price": 799.99, "description": "Travel in style with this electric scooter."},
    {"name": "Instant Pot", "price": 99.99, "description": "Cook meals quickly with this multi-use cooker."},
    {"name": "Vacuum Cleaner", "price": 199.99, "description": "Keep your home clean with this powerful vacuum."},
    {"name": "Projector", "price": 399.99, "description": "Create a home theater with this projector."},
    {"name": "Monitor", "price": 299.99, "description": "27-inch 4K monitor for work or gaming."},
    {"name": "Smart Doorbell", "price": 149.99, "description": "See and speak to visitors with this smart doorbell."},
    {"name": "Graphic Tablet", "price": 349.99, "description": "Draw and design with this professional graphic tablet."},
    {"name": "Electric Guitar", "price": 549.99, "description": "Make music with this high-quality electric guitar."},
]
About_Us = "Welcome to online shopping, your one-stop online shopping destination. We are committed to offering a variety of high-quality products at affordable prices. Whether you're looking for the latest gadgets, stylish clothing, home essentials, or unique gifts, we have something for everyone. Our goal is to make shopping online a convenient, fun, and hassle-free experience for our customers."
Our_Mission='Our mission is simple: to provide our customers with an easy-to-navigate platform where they can shop for their favorite products with confidence. We aim to deliver top-notch customer service, excellent product quality, and fast, reliable shipping. Every product in our catalog is carefully selected to meet the needs and preferences of our diverse customer base.'
@app.route('/')
def home():
    num1 = random.randint(0, 28)
    num2 = random.randint(0, 28)
    num3 = random.randint(0, 28)
    num4 = random.randint(0, 28)
    num5 = random.randint(0, 28)
    return render_template("home.html",products=products,num1=num1,num2=num2,num3=num3,num4=num4,num5=num5)
@app.route('/about')
def about():
    return render_template("about.html",discription=About_Us,Our_Mission=Our_Mission)
@app.route('/product')
def product():
    return render_template("product.html",products=products)
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('par', '').lower()
    filtered_products = [product for product in products if query in product['name'].lower()]
    return render_template('search.html', products=filtered_products, query=query)

if __name__ =="__main__":
    app.run(debug=True)