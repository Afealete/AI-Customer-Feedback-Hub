import boto3
import json
import uuid
from datetime import datetime

comprehend = boto3.client('comprehend')
dynamo = boto3.resource('dynamodb')
table = dynamo.Table('cloudwithshad-feedback')

CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS"
}

def lambda_handler(event, context):

    # Handle CORS preflight
    if event.get("httpMethod") == "OPTIONS":
        return {"statusCode": 200, "headers": CORS, "body": ""}

    try:
        # Parse request body safely
        body = json.loads(event.get("body", "{}"))

        name = body.get("name")
        email = body.get("email")
        message = body.get("message", "")[:5000]

        # Validate input
        if not name or not email or not message:
            return {
                "statusCode": 400,
                "headers": CORS,
                "body": json.dumps({"error": "Missing name, email, or message"})
            }

        # AI analysis
        sentiment = comprehend.detect_sentiment(
            Text=message,
            LanguageCode="en"
        )

        entities = comprehend.detect_entities(
            Text=message,
            LanguageCode="en"
        )

        formatted_entities = [
            {"text": e["Text"], "type": e["Type"]}
            for e in entities.get("Entities", [])[:10]
        ]

        # Save
        feedback_id = str(uuid.uuid4())

        table.put_item(Item={
            "feedback_id": feedback_id,
            "name": name,
            "email": email,
            "message": message,
            "sentiment": sentiment["Sentiment"],
            "sentiment_score": str(sentiment["SentimentScore"]),
            "entities": formatted_entities,
            "submitted_at": datetime.utcnow().isoformat()
        })

        return {
            "statusCode": 200,
            "headers": CORS,
            "body": json.dumps({
                "success": True,
                "id": feedback_id,
                "sentiment": sentiment["Sentiment"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": CORS,
            "body": json.dumps({"error": str(e)})
        }