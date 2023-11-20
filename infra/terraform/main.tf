#hint: Don't hesitate to inspire yourself from this file to fill the TO COMPLETE tags in the mongodb files and to create neo4j instances
provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
  }
}


