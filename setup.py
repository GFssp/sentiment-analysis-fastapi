import setuptools

setuptools.setup(
    include_package_data=True,
    name="sentiment-analysis-api",
    version='0.0.1',
    description="Sentiment Analysis API Graphql-backend based",
    packages=setuptools.find_packages(),
    install_requires=[
        'annotated-types==0.6.0',
        'anyio==3.7.1',
        'click==8.1.7',
        'colorama==0.4.6',
        'exceptiongroup==1.1.3',
        'fastapi==0.103.2',
        'graphql-core==3.2.3',
        'greenlet==3.0.0',
        'h11==0.14.0',
        'idna==3.4',
        'install==1.3.5',
        'mysql-connector-python==8.1.0',
        'mysql-connector-python-rf==2.2.2',
        'mysqlclient==2.2.0',
        'protobuf==4.21.12',
        'pydantic==2.4.2',
        'pydantic_core==2.10.1',
        'python-dateutil==2.8.2',
        'python-dotenv==1.0.0',
        'six==1.16.0',
        'sniffio==1.3.0',
        'SQLAlchemy==2.0.22',
        'starlette==0.27.0',
        'strawberry-graphql==0.209.7',
        'typing_extensions==4.8.0',
        'uvicorn==0.23.2',
    ],
)