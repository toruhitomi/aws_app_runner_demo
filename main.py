from fastapi import FastAPI

app = FastAPI(
    title="AWS App Runner Demo API",
    description="A demo API deployed on AWS App Runner",
    version="1.0.0",
)


@app.get("/")
def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the AWS App Runner Demo API"}


@app.get("/health")
def health_check():
    """Health check endpoint for AWS App Runner."""
    return {"status": "healthy"}
