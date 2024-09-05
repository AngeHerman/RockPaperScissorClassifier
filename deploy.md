## Déploiement
Après avoir créer le Dockerfile et le .dockerignore:
### 1. Créer un dépôt dans Google Artifact Registry

Pour commencer, assurez-vous d'avoir un dépôt Artifact Registry configuré dans votre projet Google Cloud.

### 2. Définir les variables

Remplacez les valeurs ci-dessous par les informations spécifiques à votre projet GCP :

```bash
PROJECT_ID="your-project-id"         # Remplacez par l'ID de votre projet GCP
REGION="europe-west9"                # Remplacez par votre région GCP
REPO_NAME="your-repo-name"           # Remplacez par le nom de votre dépôt dans Artifact Registry
IMAGE_NAME="your-image-name"         # Remplacez par le nom de votre image Docker
IMAGE_TAG="your-tag"                 # Remplacez par le tag de l'image (ex: v1.0)
```

### Construire et soumettre l'image à Google Artifact Registry
```bash
gcloud builds submit --tag ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG} .
```

```bash
gcloud builds submit --tag europe-west9-docker.pkg.dev/rcp-classifier/rcp-classifier-depot/image-classifier:v1.0 .
```

En cas d'erreur de rôle:
- acceder à la page IAM https://console.cloud.google.com/iam-admin/iam?hl=fr&_ga=2.158418553.2125674075.1725527545-389536328.1725465882
- Choisir le compte service et attribuer les rôles Storage Admin et Storage Object Admin


### Déployer l'image sur Google Cloud Run
```bash
gcloud run deploy --image ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG} --platform managed --region ${REGION}
```


```bash
gcloud run deploy --image europe-west9-docker.pkg.dev/rcp-classifier/rcp-classifier-depot/image-classifier:v1.0 --platform managed --region europe-west9
```

### Redeployer après des modifications
```bash
gcloud builds submit --tag europe-west9-docker.pkg.dev/rcp-classifier/rcp-classifier-depot/image-classifier:v1.1 .
```

```bash
gcloud run deploy <SERVICE_NAME> --image europe-west9-docker.pkg.dev/rcp-classifier/rcp-classifier-depot/image-classifier:v1.1
```

<SERVICE_NAME> est le nom de l'ancine service existant. On peux le trouver avec 
gcloud run services list

```bash
gcloud run deploy image-classifier --image europe-west9-docker.pkg.dev/rcp-classifier/rcp-classifier-depot/image-classifier:v1.1
```