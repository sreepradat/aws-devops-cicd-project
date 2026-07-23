from datetime import datetime, timezone

from flask import Blueprint, jsonify, render_template

main = Blueprint("main", __name__)


@main.get("/")
def home():
    return render_template(
        "index.html",
        project_name="AWS DevOps CI/CD Project",
        environment="Local Development",
    )


@main.get("/health")
def health():
    return (
        jsonify(
            {
                "status": "healthy",
                "service": "aws-devops-cicd-project",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        ),
        200,
    )