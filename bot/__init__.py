from web.plat import is_docker

if is_docker():
    pass
else:
    from dotenv import load_dotenv

    print(f'Dotenv loaded: {load_dotenv()}')