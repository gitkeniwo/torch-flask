from app.app import create_app

# Create the application instance
app = create_app()

if __name__ == '__main__':
    # Run the application

    app.run(host="0.0.0.0" , debug=True, port=5000)