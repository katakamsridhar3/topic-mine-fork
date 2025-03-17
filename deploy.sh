#!/bin/bash
# Copyright 2022 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#    https://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

echo "Setting variable values..."
PROJECT_ID=$(cat config.json | jq -r '.project_id')
PROJECT_REGION=$(cat config.json | jq -r '.project_region // "us-central1"')
CLOUD_RUN_SERVICE_NAME=$(cat config.json | jq -r '.cloud_run_service // "topic-mine"')
SERVICE_ACCOUNT_NAME=$(cat config.json | jq -r '.service_account_name // "topic-mine-service-account"')
FRONTENT_BUILD_OUTPUT_DIR="dist/topic_mine"
FRONTEND_BUCKET=$(cat config.json | jq -r '.bucket_name // "topic-mine-bucket"')
FIRESTORE_DATABASE_ID=$(cat config.json | jq -r '.bucket_name // "topic-mine-settings-database"')

echo "Setting Google Cloud project..."
gcloud config set project "$PROJECT_ID"

echo "Enabling required API services..."
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services enable googleads.googleapis.com
gcloud services enable sheets.googleapis.com

echo "Creating Service Account..."
gcloud iam service-accounts create $SERVICE_ACCOUNT_NAME --display-name "Topic Mine Service Account"
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com \
    --role roles/bigquery.admin
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:$SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com \
    --role roles/run.invoker

echo "Creating Firestore database..."
gcloud firestore databases create --database=$FIRESTORE_DATABASE_ID --location=$PROJECT_REGION --project=$PROJECT_ID

echo "Deploying Cloud Run..."
gcloud run deploy $CLOUD_RUN_SERVICE_NAME --region=$PROJECT_REGION --source="." --allow-unauthenticated

echo "Obtaining backend base URL..."
BACKEND_URL=$(gcloud run services describe $CLOUD_RUN_SERVICE_NAME --region=$PROJECT_REGION --format="value(status.url)")

echo "Setting up frontend pointing to URL $BACKEND_URL..."
echo "{ \"url\": \"$BACKEND_URL\" }" > frontend/src/assets/config.json


echo "Building frontend..."
cd frontend
npm install
ng build --configuration=production --output-path="$FRONTENT_BUILD_OUTPUT_DIR"

echo "Deploying frontend to Google Cloud Storage..."
gsutil mb -l "$PROJECT_REGION" "gs://$FRONTEND_BUCKET"
gsutil -m rm -rf "gs://$FRONTEND_BUCKET/**" #remove existing files
gsutil -m cp -r "$FRONTENT_BUILD_OUTPUT_DIR"/* "gs://$FRONTEND_BUCKET"

# Make files publicly accessible (if needed)
# echo "Making files publicly accessible..."
# gsutil -m acl ch -u AllUsers:R "gs://$FRONTEND_BUCKET/**"

echo "Deployment complete. Your Angular app is available at: https://storage.googleapis.com/$FRONTEND_BUCKET/index.html"
