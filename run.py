from app import create_app

spotifun = create_app()

if __name__ == "__main__":
    spotifun.run(debug=True)

